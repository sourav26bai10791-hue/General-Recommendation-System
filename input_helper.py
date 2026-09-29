def get_user_preferences():
    print("Choose your preferences.")
    print("Available interests: Python, Programming, Web, Big Data, ai, Machine Learning, ml")
    interest_text = input("Enter your interests separated by commas!!!: ").lower()
    interests = interest_text.split(",")
    for i in range(len(interests)):
        interests[i] = interests[i].strip()
    print("Categories: programming, development, data, ai, cybersecurity, cloud, tools")
    category = input("Enter a category or type 'any': ").lower().strip()
    print("Difficulty: easy, medium, any")
    difficulty = input("Enter difficulty: ").lower().strip()
    if category == "":
        category = "any"
    if difficulty == "":
        difficulty = "any"
    return {"interests": interests,"category": category,"difficulty": difficulty}
