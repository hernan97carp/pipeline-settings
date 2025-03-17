import pytest
import requests
import subprocess
import time
import os

@pytest.fixture(scope="module")
def server():
    # Obtener la ruta absoluta del directorio del archivo de prueba
    test_dir = os.path.dirname(__file__)
    # Retroceder hasta la raíz del proyecto (dos niveles desde tests/e2e/ui)
    project_root = os.path.abspath(os.path.join(test_dir, '../../../'))
    app_path = os.path.join(project_root, 'src', 'app.py')
    print(f"Project root: {project_root}")
    print(f"Intentando iniciar servidor en: {app_path}")
    if not os.path.exists(app_path):
        raise FileNotFoundError(f"El archivo {app_path} no existe. Asegúrate de que src/app.py esté en la raíz del proyecto.")
    process = subprocess.Popen(['python', app_path])
    # Esperar hasta que el servidor esté listo
    max_attempts = 20
    for _ in range(max_attempts):
        try:
            requests.get('http://localhost:5000')
            break
        except requests.ConnectionError:
            time.sleep(0.5)
    else:
        process.terminate()
        raise RuntimeError("El servidor no se inició en el tiempo esperado")
    yield
    process.terminate()
    time.sleep(1)
    if process.poll() is None:
        process.kill()

def test_add_functionality(server):
    response = requests.post('http://localhost:5000/add', json={'a': 1, 'b': 2})
    assert response.status_code == 200
    assert response.json() == {'result': 3}
# Inicia el servidor, envía una solicitud POST y verifica el resultado.
# Usamos requests por simplicidad, pero en una app con UI, Playwright interactuaría con la interfaz.