#!/bin/bash
timestamp=$(date +"%Y%m%d-%H%M%S")


original_file="grades.csv"
archive_dir="archive"
archived_file="grades_${timestamp}.csv"
log_file="organizer.log"

if [ ! -f "$original_file" ]; then
    echo "Error: grades.csv does not exist."
    exit 1
fi


if [ ! -d "$archive_dir" ]; then
    mkdir -p "$archive_dir"
fi


mv "$original_file" "$archive_dir/$archived_file"

touch "$original_file"


echo "$timestamp | $original_file | $archive_dir/$archived_file" >> "$log_file"

echo "Archiving completed successfully!"
echo "Archived file: $archive_dir/$archived_file"
echo "New grades.csv created."
echo "Details recorded in $log_file."
