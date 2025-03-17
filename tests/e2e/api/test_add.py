
import pytest
import requests
import subprocess
import time
import os

@pytest.fixture(scope="module")
def server():
    # Ruta absoluta desde la raíz del proyecto
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
    app_path = os.path.join(project_root, 'src/app.py')
    process = subprocess.Popen(['python', app_path])
    time.sleep(5)
    yield
    process.terminate()

def test_add_functionality(server):
    response = requests.post('http://localhost:5000/add', json={'a': 1, 'b': 2})
    assert response.status_code == 200
    assert response.json() == {'result': 3}
# Inicia el servidor, envía una solicitud POST y verifica el resultado.
# Usamos requests por simplicidad, pero en una app con UI, Playwright interactuaría con la interfaz.