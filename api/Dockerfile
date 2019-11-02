FROM python:3.7-slim


# Installing system dependecies
RUN apt-get update -qq && apt-get install -y nodejs postgresql-client
RUN pip install --upgrade pip

# Creating API workspace
RUN mkdir api
COPY . /api
WORKDIR /api

ENV PYTHON_PATH="/api"

# Install API dependencies
RUN pip install -r requirements.txt

EXPOSE 5000

CMD python server.py