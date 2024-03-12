FROM python

WORKDIR /app

RUN pip install pydantic
RUN pip install fastapi
RUN pip install uvicorn
RUN mkdir storage
RUN touch lol.txt

VOLUME storage
COPY test.py test.py

EXPOSE 80

# Execute the script at container startup
CMD ["sh", "-c", "uvicorn test:app --host 0.0.0.0 --port 80"]
