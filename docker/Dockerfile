FROM python

WORKDIR /app

RUN pip install pydantic
RUN pip install fastapi
RUN pip install uvicorn

COPY test.py test.py

EXPOSE 8000

# Execute the script at container startup
CMD ["uvicorn", "test:app", "--host", "0.0.0.0", "--port", "8000"]
