#!/bin/bash

# Function to get current time in seconds
get_time() {
    date +%s
}

start_time=$(get_time)

# Run for 60 minutes (3600 seconds)
end_time=$((start_time + 3600))

while [ $(get_time) -lt $end_time ]; do
    echo "Attempting to retrieve forecast..."
    
    # Use timeout to prevent hanging, pipe output to capture it
    output=$(timeout 300s nc -u -l 5455 2>&1)
    
    # Check if we received any output
    if [ -n "$output" ]; then
        echo "Received forecast:"
        echo "$output"
        exit 0
    else
        echo "No data received, will try again in 5 seconds."
    fi
    
    # Wait for 5 seconds before the next attempt
    sleep 5
done

echo "No forecast received after 60 attempts. Please check the service."
exit 1