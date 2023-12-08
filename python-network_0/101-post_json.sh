#!/bin/bash
# Sends a JSON POST to a URL
curl -sH "Content-Type: application/json" -d "$2" "$1"
