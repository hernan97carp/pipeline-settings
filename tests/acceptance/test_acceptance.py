# tests/acceptance/test_acceptance.py
import pytest
import requests
import subprocess
import time

@pytest.fixture(scope="module")
def server():
    process = subprocess.Popen(['python', 'app.py'])
    time.sleep(2)  # Espera a que el servidor arranque
    yield
    process.terminate()

def test_add_functionality(server):
    response = requests.post('http://localhost:5000/add', json={'a': 1, 'b': 2})
    assert response.status_code == 200
    assert response.json() == {'result': 3}
# Inicia el servidor, envía una solicitud POST y verifica el resultado.
# Usamos requests por simplicidad, pero en una app con UI, Playwright interactuaría con la interfaz.