FROM python3

ADD src /src

CMD ["python", "./src/CalculatorTest.py"]
