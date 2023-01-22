FROM python:3.10.9-slim as app_builder

WORKDIR /src
COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y gcc g++ python3-dev
RUN pip install --no-cache-dir -r requirements.txt


FROM app_builder as app

ENV PYTHONPATH=/src/app

EXPOSE 80
CMD ["python", "-m", "uvicorn", "app.asgi:app", "--host", "0.0.0.0", "--port", "80"]
