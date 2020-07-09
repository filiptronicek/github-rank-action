FROM python:3.8-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["bash","/entrypoint.sh"]