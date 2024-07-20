#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Database connection details (replace with your values)
DB_NAME="your_database"
DB_USER="your_user"
DB_PASSWORD="your_password"
DB_HOST="your_host"
DB_PORT="your_port"

echo "Starting database migrations..."

# Example: Using Flyway for database migrations
flyway -url="jdbc:postgresql://$DB_HOST:$DB_PORT/$DB_NAME" -user="$DB_USER" -password="$DB_PASSWORD" migrate

# Uncomment the following lines if using Liquibase instead
# liquibase --url="jdbc:postgresql://$DB_HOST:$DB_PORT/$DB_NAME" --username="$DB_USER" --password="$DB_PASSWORD" update

echo "Database migrations completed successfully."
