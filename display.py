def show_courses(recommendations):
    if len(recommendations) == 0:
        print("No matching courses were found.")
        print("Try entering interests such as Python, Ai, Web")
        return
    print("_"*50)#A line
    number = 1
    for score, course in recommendations:
        print(number, ".", course["name"])
        print("   Category :", course["category"])
        print("   Difficulty:", course["difficulty"])
        print("   Match Score:", score)
        print("   Topics:", ", ".join(course["tags"]))
        print("_"*  50)#A line
        number +=1