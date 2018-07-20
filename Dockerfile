# Use an official Python runtime as a parent image
FROM python:3.6-slim

LABEL maintainer="Mikhail Lebedev <mihasichechek@gmail.com>"

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install Flask

RUN pip install requests

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]