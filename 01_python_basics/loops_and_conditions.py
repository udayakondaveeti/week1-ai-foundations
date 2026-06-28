# Conditional logic and loops
scores = [78, 92, 65, 88, 54]
for score in scores:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    print(f"Score {score} -> Grade {grade}")
