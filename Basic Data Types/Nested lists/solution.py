#Nested Lists – Second Lowest Grade

records = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

# Extract all scores
    scores = sorted(set([score for name, score in records]))

# Find the second lowest score
    second_lowest = scores[1]

# Get names of students who have the second lowest score
    names = [name for name, score in records if score == second_lowest]

# Sort names alphabetically
    names.sort()

# Print each name on a new line
for name in names:
    print(name)
