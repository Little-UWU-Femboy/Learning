lineCount = 0
with open("tps757.csv", "r") as f:
    for _ in f:
        lineCount += 1

print(f"Total lines: {lineCount}")