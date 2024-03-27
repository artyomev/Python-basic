#Для запуска веб-приложения из контейнера docker необходимо:
#   1. Открыть терминал в папке с докер-файлом и выполнить команду "docker build . -t TAG" - вместо TAG указать любое имя
#   2. Запустить созданный образ командой "docker run -it -p 8000:8000 TAG". Можно указать любой другой свободный порт. Для докер приложения
#   порт всегда будет 8000
#   3. Перейти по адресу 0.0.0.0:8000 - вы попадете в корень приложения: на странице будет сообщение "message": "Root Page"
#   4. При переходе на 0.0.0.0:8000/ping/ - приложение возвращает объект {"message": "pong"}

FROM python:3.11.7-bookworm

WORKDIR /app


RUN pip install "poetry==1.7.1"
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

COPY fastapi_ping_app/ ./

CMD ["uvicorn",  "main:app", "--host=0.0.0.0", "--port=8000"]

EXPOSE 8000