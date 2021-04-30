FROM robertlgtucker/pyspark-java8:latest

WORKDIR /usr/src/app
COPY . .
RUN pip3 install pyspark==3.1.1
CMD ["python3", "solution/main.py"]