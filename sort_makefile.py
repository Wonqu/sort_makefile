"""makefile_sort.py
Utility to easily sort targetss in Makefile.
Please take note that the targets must be formatted correctly
(exactly one empty line between block, comments directly above targets)
for this to work.
"""
import argparse
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Sort Makefile.')
    parser.add_argument('filepath', type=str, help='Path to makefile.')
    args = parser.parse_args()

    makefile_path = args.filepath

    try:
        with open(makefile_path, "r") as f:
            makefile_content = f.read()
    except IOError as e:
        print(
            """
            Please make sure that Makefile is in main project directory and
            that this script is in /scripts directory inside it.
            """
        )
        exit(-1)

    current = None
    chunks = makefile_content.split("\n\n")
    chunk_target_pairs = []

    for c in chunks:
        lines = c.split("\n")
        i = 0
        line = lines[i]
        while line.startswith("#"):
            i += 1
            line = lines[i]

        chunk_target_pairs.append((line, c))

    sorted_targets, sorted_chunks = zip(*sorted(chunk_target_pairs))
    print('\n'.join(sorted_targets))

    with open(makefile_path, "w") as f:
        f.write("\n\n".join(sorted_chunks))
        print("Sorted targets in Makefile successfully!")
