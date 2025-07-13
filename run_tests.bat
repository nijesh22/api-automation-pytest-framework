@REM @echo off
@REM echo ✅ Activating virtual environment...
@REM call .\venv\Scripts\activate
@REM
@REM echo Installing dependencies...
@REM pip install -r requirements.txt
@REM
@REM echo Running tests and generating Allure results...
@REM pytest --alluredir=allure-results
@REM
@REM echo Generating Allure HTML report...
@REM allure generate allure-results --clean -o allure-report
@REM
@REM echo Allure report generated at allure-report\index.html

@echo off

echo ✅ Creating virtual environment...
python -m venv venv || exit /b 1

echo ✅ Activating virtual environment...
call venv\Scripts\activate.bat || exit /b 1

echo 🔍 Python version:
python --version || exit /b 1

echo 🔄 Installing dependencies...
python -m pip install --upgrade pip || exit /b 1
python -m pip install -r requirements.txt || exit /b 1

echo 🧪 Running tests and generating Allure results...
pytest --alluredir=allure-results || exit /b 1

echo 📊 Generating Allure HTML report...
allure generate allure-results --clean -o allure-report || exit /b 1

echo ✅ Allure report generated at allure-report\index.html

