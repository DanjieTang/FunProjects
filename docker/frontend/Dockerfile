FROM python

WORKDIR /app

RUN pip install streamlit

COPY streamlit.py streamlit.py

CMD ["sh", "-c", "streamlit run streamlit.py --server.address 0.0.0.0 --server.port 80"]