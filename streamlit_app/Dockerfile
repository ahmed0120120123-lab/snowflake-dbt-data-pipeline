FROM python:3.10-slim
WORKDIR /app
RUN pip install --no-cache-dir streamlit snowflake-connector-python pandas matplotlib
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
