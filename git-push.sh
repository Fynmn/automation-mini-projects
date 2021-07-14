#!/usr/bin/bash

git add .

git commit -m "$1"

git push

echo "$\033[0:32mGIT PUSH SUCCESSFUL\033[0m"
