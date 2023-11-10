FROM python:3.10-slim

WORKDIR /app

RUN mkdir -p /app/bert

RUN apt-get update && \
    apt-get install -y gcc

COPY download_model.py ./
COPY main.py requirements.txt ./
COPY src ./src

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    python download_model.py && \
    rm /app/bert/auto-reply-categorizer-model.tar.gz

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
