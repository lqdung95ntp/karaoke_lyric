#!/usr/bin/env bash

## Complete the following steps to get Docker running locally
# Step 0: Remove all created docker
docker rmi -f $(docker images -aq)

# Step 1:
docker build --tag=karaoke_proj .

# Step 2: 
docker image ls

# Step 3: 
docker run -p 8080:3001 karaoke_proj