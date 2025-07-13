FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y \
    unzip curl openjdk-17-jre-headless \
 && curl -o allure.zip -L https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.27.0/allure-commandline-2.27.0.zip \
 && unzip allure.zip -d /opt/ \
 && ln -s /opt/allure-*/bin/allure /usr/bin/allure \
 && rm allure.zip


# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Run tests and generate allure-results
CMD ["sh", "-c", "pytest --alluredir=allure-results && allure generate allure-results -o allure-report --clean"]
