#!/bin/bash

# Get the current date
current_date=$(date +%Y%m%d)

# Go back 40 days
for ((i=0; i<40; i++)); do
    # Calculate the date for this iteration
    commit_date=$(date -v "-$i"d -u +%Y-%m-%d)

    # Create a new file with the commit date as its name
    touch $commit_date.txt

    # Add the file to the staging area
    git add $commit_date.txt

    # Make the commit with the commit date as the message
    git commit -m "Commit for $commit_date" --date="$commit_date"

    # Wait for 1 second to avoid committing multiple files with the same timestamp
    sleep 1
done

