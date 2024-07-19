#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: $0 <directory_path>"
    exit 1
fi

directory="$1"

if [ ! -d "$directory" ]; then
    echo "Error: '$directory' is not a directory"
    exit 1
fi

second_directory="$2"

if [ ! -d "$second_directory" ]; then
    echo "Error: '$second_directory' is not a directory"
    exit 1
fi

echo "Files in $directory:"
for file in "$directory"/*; do
    if [ -f "$file" ]; then
        gentype="$(basename "$file")"
        echo "Processing $gentype"
        combined_filename="$second_directory/$gentype"      
        java -jar MaltEval/dist-20141005/lib/MaltEval.jar  -s "$file" -g "$combined_filename" --GroupBy Sentence:exactmatch --Metric "LA" >> graph_gentypesLA.txt
    fi
done

