#!/bin/bash

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
        # java -jar MaltEval/dist-20141005/lib/MaltEval.jar  -s "$file" -g "$combined_filename" --GroupBy Sentence:exactmatch >> "$directory"_"$gentype"_results.txt
        # java -jar MaltEval/dist-20141005/lib/MaltEval.jar  -s "$file" -g "$combined_filename" --GroupBy RelationLength:precision --Metric self >> "$directory"_"$gentype"_results.txt
        # java -jar MaltEval/dist-20141005/lib/MaltEval.jar  -s "$file" -g "$combined_filename" --GroupBy RelationLength:recall --Metric self >> "$directory"_"$gentype"_results.txt
        # java -jar MaltEval/dist-20141005/lib/MaltEval.jar  -s "$file" -g "$combined_filename" --GroupBy ArcDepth:precision --Metric self  >> "$directory"_"$gentype"_results.txt
        # java -jar MaltEval/dist-20141005/lib/MaltEval.jar  -s "$file" -g "$combined_filename" --GroupBy ArcDepth:recall --Metric self  >> "$directory"_"$gentype"_results.txt
        # java -jar MaltEval/dist-20141005/lib/MaltEval.jar  -s "$file" -g "$combined_filename" --GroupBy Deprel:precision --Metric self  >> "$directory"_"$gentype"_results.txt
        # java -jar MaltEval/dist-20141005/lib/MaltEval.jar  -s "$file" -g "$combined_filename" --GroupBy Deprel:recall --Metric self  >> "$directory"_"$gentype"_results.txt
        # java -jar MaltEval/dist-20141005/lib/MaltEval.jar  -s "$file" -g "$combined_filename" --GroupBy ArcDepth --confusion-matrix 1 --Metric self  >> "$directory"_"$gentype"_results.txt
        # java -jar MaltEval/dist-20141005/lib/MaltEval.jar  -s "$file" -g "$combined_filename" --GroupBy RelationLength:fscore --Metric self  >> "$directory"_"$gentype"_results.txt
        # java -jar MaltEval/dist-20141005/lib/MaltEval.jar  -s "$file" -g "$combined_filename" --GroupBy ArcDepth:fscore  --Metric self  >> "$directory"_"$gentype"_results.txt
        # java -jar MaltEval/dist-20141005/lib/MaltEval.jar  -s "$file" -g "$combined_filename" --GroupBy Deprel:fscore --Metric self  >> "$directory"_"$gentype"_results.txt
        # java -jar MaltEval/dist-20141005/lib/MaltEval.jar  -s "$file" -g "$combined_filename" --GroupBy SentenceLength:accuracy  >> "$directory"_"$gentype"_results.txt
        java -jar MaltEval/dist-20141005/lib/MaltEval.jar  -s "$file" -g "$combined_filename" --GroupBy ArcDepth  >> "$directory"_"$gentype"_results.txt

    fi
done