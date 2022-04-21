#!/bin/bash
# Script that send a JSON POST request to see if if valid or not
curl -s -X POST "Content-Type: application/json" -d "@$2" "$1"
