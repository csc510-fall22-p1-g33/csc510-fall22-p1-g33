FROM python:3.10
EXPOSE 5000
ENV FLASK_APP=.

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN flask db init
RUN flask db migrate
RUN flask db upgrade

CMD [ "flask", "run", "--host=0.0.0.0" ]