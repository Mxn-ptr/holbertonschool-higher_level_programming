#!/bin/bash
# Displays the size of the body of the respo with a request to the URL passed in argument
curl -sI "$1" | awk '/Content-Length: / {print $2}'