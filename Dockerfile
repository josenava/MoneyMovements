FROM python:3.7

WORKDIR /app/money_transactions

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .