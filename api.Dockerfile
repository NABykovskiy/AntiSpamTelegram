FROM python:3.12-slim

COPY api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY common/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY /api /api
COPY /common /api/common

WORKDIR /api

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]