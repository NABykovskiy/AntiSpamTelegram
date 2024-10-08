FROM python:3.11-slim

COPY migrations/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY /migrations /dir/migrations
COPY alembic.ini /dir

WORKDIR /dir

EXPOSE 8080

CMD ["python", "migrations/run_migration.py"]