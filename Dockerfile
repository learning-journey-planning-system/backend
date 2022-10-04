# Start from the official Python base image. 
FROM python:3.9

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Set the current working directory to /backend. This is where we'll put the pipfile and the app directory.
WORKDIR /

# Copy the files with the requirements to the /backend directory.
COPY ./Pipfile /Pipfile
COPY ./Pipfile.lock /Pipfile.lock

# Install pipenv and compilation dependencies
RUN pip install pipenv && \
    apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev libssl-dev && \
    pipenv install --deploy --system && \
    apt-get remove -y gcc python3-dev libssl-dev && \
    apt-get autoremove -y && \
    pip uninstall pipenv -y

# Install application into container
COPY ./app /app

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
