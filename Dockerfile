# Use python 3.6.6 container image
FROM python:3.6.6

# Set the working dir
WORKDIR /app

# Copy the current dir contents into the container at /app
COPY  . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

# Run the command to start the app
CMD ["python3", "app.py"]
