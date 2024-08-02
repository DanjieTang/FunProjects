FROM python

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

CMD ["sh", "-c", "uvicorn backend:app --host 0.0.0.0 --port 80"]
