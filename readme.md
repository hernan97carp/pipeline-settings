# 🚀 Plantilla Python-Playwright-Pipeline
 Esta plantilla te permite integrar diferentes niveles de prueba a través de pipelines. Utiliza Python y Playwright para ejecutar tests y aprovecha el poder de la integración continua.🧑‍💻✨

# Instalar todo
pip install -r requirements.txt
playwright install

# Para correr todas las pruebas:
python -m unittest discover -s tests


# Ejecutar mis pruebas de unit test:
python -m unittest discover -s tests/unit -p "test_*.py" -v


# Ejecutar mis pruebas de integracion de Componentes:
python -m unittest tests/component/test_component.py    


# Ejecutar mis pruebas de Systemas:
python -m unittest tests/system/test_system.py

# Ejecutar mis pruebas de Integracion de Systemas:
python -m unittest tests/integration/test_integration_system.py

# Ejecutar mis pruebas de E2E:
pytest
