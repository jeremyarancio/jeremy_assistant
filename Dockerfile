FROM python:3.9

WORKDIR /app

RUN pip install --upgrade pip

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["streamlit", "run", "app.py", "--server.port=80", "--logger.level=info"]