scores = [85,90,78,92,88]

print("Scores:", scores)

print("Highest scores:", max(scores))
print("Lowest scores:", min(scores))

sum_of_scores = sum(scores)
total_members_of_scores = len(scores)
average_of_scores = sum_of_scores / total_members_of_scores
print("average_of_scores:", average_of_scores)

count = 0
for x in scores:
    if x > 85:
        count += 1

print("Scores above:", count)

scores.sort(reverse=True)
print(scores)