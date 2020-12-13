#!/bin/bash
docker run -e SHUTDOWN_LOG_PATH=/tmp/shutdown.log -e SHUTDOWN_FILE_PATH=/tmp/shutdown.txt -e SHUTDOWN_ENDPOINT_URL=/secret-shutdown -p 9999:8080 -it --rm --name test-shutdown helfenkannjeder/device-shutdown:latest
