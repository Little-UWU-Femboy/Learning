#!/bin/bash

LOCAL_DIR=~/Learning/School/AdvSoftEng/Project/
REMOTE_USER=ubuntu
REMOTE_HOST=ec2-18-117-165-121.us-east-2.compute.amazonaws.com
REMOTE_DIR=/var/www/html/
SSH_KEY=~/Desktop/AdvancedSoftware.pem

scp -i "$SSH_KEY" -r "$LOCAL_DIR"* "$REMOTE_USER@$REMOTE_HOST:$REMOTE_DIR"
