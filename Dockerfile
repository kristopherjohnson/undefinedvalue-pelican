# Creates a Docker container with all dependencies for Pelican.
#
# User must bind-mount the application directory as "/app".

FROM python:3

COPY pip-requirements.txt .
RUN pip install -r pip-requirements.txt
WORKDIR /app
