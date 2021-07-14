#!/usr/bin/bash

git add .

git commit -m "$1"

git push

echo -e "\033[0:32mGIT PUSH SUCCESSFUL!\033[m"
