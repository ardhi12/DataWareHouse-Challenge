FROM python:3.8-slim

WORKDIR /usr/src/app
COPY . .
RUN pip3 install --user -r requirements.txt
CMD ["python3", "solution/main.py"]