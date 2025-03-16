# Ejecutar mis pruebas de unit test:
python -m unittest tests/unit/test_unit.py

# Para correr todas:
python -m unittest discover -s tests

# Ejecutar mis pruebas de integracion de Componentes:
python -m unittest tests/component/test_component.py    


# Ejecutar mis pruebas de Systemas:
 tests/system/test_system.py
python -m unittest tests/system/test_system.py

# Ejecutar mis pruebas de Integracion de Systemas:
python -m unittest tests/integration/test_integration_system.py

# Ejecutar mis pruebas de Aceptacion:
pytest tests/acceptance/test_acceptance.py



# Ejecutar con Playwright:


  npx playwright test
    Runs the end-to-end tests.

  npx playwright test --ui
    Starts the interactive UI mode.

  npx playwright test --project=chromium
    Runs the tests only on Desktop Chrome.

  npx playwright test example
    Runs the tests in a specific file.

  npx playwright test --debug
    Runs the tests in debug mode.

  npx playwright codegen
    Auto generate tests with Codegen.


