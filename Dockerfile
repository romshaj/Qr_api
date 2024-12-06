FROM python:3.9-slim


WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install uvicorn

EXPOSE 3200

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "3200"]
