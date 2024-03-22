#!/usr/bin/env bash

# Loop through each file in the folder
for file in "tests"/*; do
  if [ -f "$file" ]; then
    echo "Running sudo python3 on $file"
    sudo python3 "$file"
  fi
done