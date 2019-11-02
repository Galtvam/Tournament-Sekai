FROM python:3.7-slim


# Installing system dependecies
RUN pip install --upgrade pip

# Creating API workspace
RUN mkdir webapp
COPY . /webapp
WORKDIR /webapp

# Install API dependencies
RUN pip install -r requirements.txt

EXPOSE 80

CMD python server.py