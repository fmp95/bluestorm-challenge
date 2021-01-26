FROM python:3.9.1

RUN mkdir code

WORKDIR /code

copy . /code

RUN pip install -r requirements/production.txt

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
