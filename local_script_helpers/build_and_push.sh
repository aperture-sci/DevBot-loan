#!/bin/bash

# Go one directory up
cd ..

# Get the username and password from environment variables
quayIoUsername=lrochette
quayIoPassword=$dev_bot_pass

# Define the Docker image name and tag
dockerImageName="$quayIoUsername/devbot-loan"

# Get the latest release tag from GitHub
#latestRelease=$(curl -s https://api.github.com/repos/aperture-sci/DevBot-loan/releases/latest | jq -r .tag_name)
latestRelease=0.0.1

# Build the Docker image with the latest release tag
docker build -t "$dockerImageName:$latestRelease" .

# Log in to the quay.io container registry
docker login quay.io -u "$quayIoUsername" -p "$quayIoPassword"

# Tag the Docker image with the quay.io repository and latest release tag
quayIoRepository="quay.io/lrochette/devbot-loan"
docker tag "$dockerImageName:$latestRelease" "$quayIoRepository:$latestRelease"

# Push the Docker image to the quay.io container registry
docker push "$quayIoRepository:$latestRelease"

# Clean up: remove the local Docker image
docker rmi "$dockerImageName:$latestRelease"
