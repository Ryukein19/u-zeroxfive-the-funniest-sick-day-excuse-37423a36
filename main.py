import os
# One-liner entry (under 200 chars): the line below is the entire submission.
# Writes the line to /output/entry.txt when run.
LINE = "Sorry, I cannot come in today. I woke up as a PDF and nobody at the office knows how to open me."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
