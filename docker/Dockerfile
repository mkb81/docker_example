FROM python:3.9.8-alpine3.14

RUN apk update && apk upgrade && apk add bash

# Update pip
RUN pip install --upgrade pip

# Create app folder
RUN mkdir /usr/src/app

# Set working dirctory
WORKDIR /usr/src/app

# Copy all files and imstall requirements
COPY source  /usr/src/app
COPY requirements.txt /usr/src/app
RUN pip install -r /usr/src/app/requirements.txt

# Start application
CMD ["python3", "app.py"]
