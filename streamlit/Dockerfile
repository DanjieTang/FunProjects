FROM python

WORKDIR /app

COPY temp.py temp.py

RUN pip install streamlit
RUN pip install matplotlib
RUN pip install watchdog

EXPOSE 80

CMD ["sh", "-c", "streamlit run temp.py --server.address 0.0.0.0 --server.port 80"]