#!/bin/bash

# Folders to process
FOLDERS=(
  "red-team/ctfs"
  "red-team/rooms"
  "blue-team/ctfs"
  "blue-team/rooms"
)

for folder in "${FOLDERS[@]}"; do
  index_file="$folder/README.md"
  echo "# $(basename $(dirname "$folder")) – $(basename "$folder")" > "$index_file"
  echo "" >> "$index_file"
  echo "| Room | Walkthrough |" >> "$index_file"
  echo "|------|-------------|" >> "$index_file"

  # Loop through each subdirectory
  for dir in "$folder"/*/; do
    [ -d "$dir" ] || continue
    room_name=$(basename "$dir")
    if [[ -f "$dir/walkthrough.md" ]]; then
      echo "| $room_name | [walkthrough.md]($room_name/walkthrough.md) |" >> "$index_file"
    else
      echo "| $room_name | _Missing_ |" >> "$index_file"
    fi
  done

  echo "✅ Generated index for $folder"
done

