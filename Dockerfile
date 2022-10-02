# Start from the official Python base image. 
FROM python:3.9

# Set the current working directory to /backend. This is where we'll put the pipfile and the app directory.
WORKDIR /backend

# Copy the file with the requirements to the /backend directory.
# Copy only the file with the requirements first, not the rest of the code.
# As this fil
e doesn't change often, Docker will detect it and use the cache for this step, enabling the cache for the next step too.
COPY ./Pipfile /backend/Pipfile
COPY ./Pipfile.lock /backend/Pipfile.lock

# start a pipenv environment

# Install the package dependencies in the pipfile file.
# The --no-cache-dir option tells pip to not save the downloaded packages locally, as that is only if pip was going to be run again to install the same packages, but that's not the case when working with containers.
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
