#!/bin/bash

# Script to download any files in `README.md`.
# Expects to receive the path to the `README.md` as an argument and saves the files in the same
# directory as the `README.md`

die () {
    echo >&2 "$@"
	    exit 1
		}

[ "$#" -eq 1 ] || die "Path to README.md required as an argument, $# arguments provided. Terminating..."


readme=$1

echo "Checking for URLs to download files from '$readme'"

readme_dir=$(dirname $readme)

echo "Files will be downloaded to '$readme_dir'"

awk -F'[()]' '{print $2}'  $readme | sed '/^$/d' | while read -r url; do echo "downloading $url..."; wget $url -P $readme_dir; done