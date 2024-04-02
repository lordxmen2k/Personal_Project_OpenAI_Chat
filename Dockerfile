# Use the official Python base image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable for OpenAI API key
ENV OPENAI_SECRET_KEYex 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

# Run app.py when the container launches
CMD ["python", "app.py"]