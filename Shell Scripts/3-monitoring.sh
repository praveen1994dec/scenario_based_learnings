#!/bin/bash

# Example: Monitoring script (replace with your monitoring logic)
echo "Monitoring script started..."

# Example: Check server health using curl and grep
response=$(curl -sSf http://example.com/status | grep -q "200 OK" && echo "Server is healthy." || echo "Server is down!")

# Example: Send email alert if server is down
if [[ "$response" == *"Server is down!"* ]]; then
    echo "Sending alert email..."
    # Replace with your email sending command or integration
    # mail -s "Server Alert" your_email@example.com <<< "Server is down!"
fi

echo "Monitoring script completed."
