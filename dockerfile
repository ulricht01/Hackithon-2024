FROM python:3.10-alpine

# Set the working directory in the container
WORKDIR /code

# Install system dependencies
RUN apk update && \
    apk add --no-cache mariadb-connector-c-dev build-base

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY ./code/app.py /code/

# Set environment variables for MariaDB connection
ENV DB_HOST=127.0.0.1
ENV DB_PORT=3306
ENV DB_USER=root
ENV DB_PASSWORD=123
ENV DB_NAME=hackithon_2024
ENV TZ=Europe/Prague

EXPOSE 8501

# Spusťte aplikaci Streamli

# Define the command to run the application
CMD ["python", "app.py"]
ENTRYPOINT ["streamlit", "run", "mapa.py", "--server.port=8501", "--server.address=0.0.0.0"]