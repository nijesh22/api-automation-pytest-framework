@echo off
echo ✅ Activating virtual environment...
call .\venv\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

echo Running tests and generating Allure results...
pytest --alluredir=allure-results

echo Generating Allure HTML report...
allure generate allure-results --clean -o allure-report

echo Allure report generated at allure-report\index.html
