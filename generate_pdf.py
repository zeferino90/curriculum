#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["pypandoc-binary"]
# ///
import sys
import pypandoc

input_file = sys.argv[1] if len(sys.argv) > 1 else "cv-ats.md"
output_file = sys.argv[2] if len(sys.argv) > 2 else "cv-Moises.pdf"

pypandoc.convert_file(
    input_file,
    "pdf",
    outputfile=output_file,
    extra_args=["--pdf-engine=xelatex", "-V", "geometry:margin=1in"],
)
print(f"Generated: {output_file}")
