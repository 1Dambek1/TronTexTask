FROM python


WORKDIR /app


COPY requirements.txt .
RUN   pip install -r requirements.txt
COPY . .


CMD gunicorn  src.app:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000

