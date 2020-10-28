FROM python3

ADD src /src

CMD ["python", "./src/calculatorTest.py"]
