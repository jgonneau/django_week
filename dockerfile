FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN pip install djongo
RUN pip install djangorestframework
RUN pip install markdown
RUN pip install django-filter
COPY . /code/
