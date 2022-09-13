#!/bin/bash
for file in ${1}/*.webm; do
    	echo ${file}
	ffmpeg -i "${file%.*}.webm" -vn -f wav "${file%.*}.wav"
	rm -f "${file}"
done
