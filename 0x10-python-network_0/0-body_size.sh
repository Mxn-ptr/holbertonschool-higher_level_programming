#!/bin/bash
# Script that takes in a URL and displays size of the body
curl -s "$1" | wc -c
