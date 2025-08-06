#!/bin/bash

# Folders to generate sub-indexes for
FOLDERS=(
  "red-team/ctfs"
  "red-team/rooms"
  "blue-team/ctfs"
  "blue-team/rooms"
)

# Top-level README header
TOP_INDEX="README.md"
echo "# 🧠 TryHackMe Projects" > "$TOP_INDEX"
echo "" >> "$TOP_INDEX"
echo "A structured collection of TryHackMe walkthroughs and CTF notes, organized by team type and challenge type." >> "$TOP_INDEX"
echo "" >> "$TOP_INDEX"

# Generate per-folder indexes and append to top-level index
for folder in "${FOLDERS[@]}"; do
  team=$(basename "$(dirname "$folder")")
  type=$(basename "$folder")

  # Create or overwrite subfolder README
  sub_index="$folder/README.md"
  echo "# $team – $type" > "$sub_index"
  echo "" >> "$sub_index"
  echo "| Room | Walkthrough |" >> "$sub_index"
  echo "|------|-------------|" >> "$sub_index"

  # Add section to top-level README
  echo "## ${team^} Team – ${type^}" >> "$TOP_INDEX"
  echo "" >> "$TOP_INDEX"
  echo "- 📁 [${type^}](./$folder/)" >> "$TOP_INDEX"

  for dir in "$folder"/*/; do
    [ -d "$dir" ] || continue
    room_name=$(basename "$dir")
    if [[ -f "$dir/walkthrough.md" ]]; then
      echo "| $room_name | [walkthrough.md]($room_name/walkthrough.md) |" >> "$sub_index"
      echo "  - [$room_name]($folder/$room_name/walkthrough.md)" >> "$TOP_INDEX"
    else
      echo "| $room_name | _Missing_ |" >> "$sub_index"
      echo "  - $room_name (walkthrough missing)" >> "$TOP_INDEX"
    fi
  done

  echo "" >> "$TOP_INDEX"
  echo "✅ Generated index for $folder"
done

# Add projects section to top-level
echo "## 🛠 Projects" >> "$TOP_INDEX"
echo "" >> "$TOP_INDEX"
if [[ -d "projects/" ]]; then
  for project in projects/*; do
    [ -d "$project" ] || continue
    name=$(basename "$project")
    echo "- [$name](projects/$name/)" >> "$TOP_INDEX"
  done
fi

# Footer
echo "" >> "$TOP_INDEX"
echo "> ✍️ Maintained by $(git config user.name)" >> "$TOP_INDEX"
echo "> 🗓️ Last updated: $(date '+%Y-%m-%d')" >> "$TOP_INDEX"


