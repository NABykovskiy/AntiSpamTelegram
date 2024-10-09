FROM python:3.12-slim

COPY bot/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY /bot /bot

WORKDIR /bot


CMD ["python", "main.py"]