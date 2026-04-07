FROM python:3.11-slim

WORKDIR /server

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 36363

CMD [ "python", "server.py" ]
