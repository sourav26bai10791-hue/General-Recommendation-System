def recommend_courses(courses, preferences):
    recommendations = []#Empty list concept
    for course in courses:
        score= 0
        for interest in preferences["interests"]:
            if interest in course["tags"]:
                score +=2
        if preferences["category"] == "any":
            score = score + 1
        elif preferences["category"] == course["category"].lower():
            score = score + 3
        if preferences["difficulty"] == "any":
            score = score + 1
        elif preferences["difficulty"] == course["difficulty"].lower():
            score = score + 2
        if score > 0:
            recommendations.append((score, course))
    for i in range(len(recommendations)):
        for j in range(i + 1, len(recommendations)):
            if recommendations[j][0] > recommendations[i][0]:
                recommendations[i], recommendations[j] = recommendations[j], recommendations[i]
    return recommendations
