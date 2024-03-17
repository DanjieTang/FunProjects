FROM python

WORKDIR /app
COPY api.py api.py

RUN pip install uvicorn
RUN pip install fastapi

EXPOSE ${PORT}

CMD ["sh", "-c", "uvicorn api:app --host 0.0.0.0 --port 80"]
