# Use a slim Python 3.12 base image
FROM python:3.12.3-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /server

# Install system dependencies
RUN apt-get update
RUN apt-get install libpq-dev -y

# Install Pipenv
RUN python3 -m ensurepip --upgrade
RUN pip install pipenv

# Copy Pipenv files and lock file (if using)
COPY Pipfile Pipfile.lock ./

# Install dependencies using Pipenv
RUN pipenv install --system --dev

# Copy your application code
COPY . .

# Set the entrypoint command
EXPOSE 8000
