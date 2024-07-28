#!/bin/bash

parser="$1"

generalisation="$2"

randinit="$3"

groupby="$4"

s=output/parser/"$parser"_generalisation_sets/randinit"$randinit"/"$generalisation"_stripped.conllu

g=UD_SLOG/generalisation_sets/stripped/"$generalisation"_stripped.conllu

java -jar MaltEval/dist-20141005/lib/MaltEval.jar -s "$s" -g "$g" --GroupBy "$groupby" 