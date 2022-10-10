FROM python:3.10
EXPOSE 5000
ENV FLASK_APP=Backend

COPY Backend /app/Backend
COPY tests /app/tests

WORKDIR /app

RUN pip install -r Backend/requirements.txt
RUN flask db init
RUN flask db migrate
RUN flask db upgrade

CMD [ "flask", "run", "--host=0.0.0.0" ]

# Note: To run tests, execute the following command.
#     docker exec <CONTAINER_NAME> pytest