# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Get and install supervisor
RUN apt-get update && apt-get install -y supervisor
RUN mkdir -p /var/log/supervisor

COPY supervisord.conf /etc/supervisor/supervisord.conf


# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt 
RUN pip install --upgrade pip
RUN pip install "psycopg[binary,pool]"
RUN pip install --no-cache-dir -r ./scripts/requirements.txt


# Make port 80 available to the world outside this container (Optional, only for web apps)
# EXPOSE 80

# Add bind mount to have access to file from outside the container.
#RUN --mount=type=bind,src=./scripts,dst=/scripts/


# Define environment variable (optional)
# ENV NAME World

# Run app.py when the container launches
#CMD ["python", "./app.py"]

CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]
