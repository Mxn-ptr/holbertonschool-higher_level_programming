#!/bin/bash
# Script that send a JSON POST request to see if if valid or not
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
