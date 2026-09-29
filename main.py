from input_helper import get_user_preferences
from courses import courses 
from display import show_courses
from recommender import recommend_courses
print("_" * 50)
print("        General Recommendation System")
print("_" * 50)
name =input("Enter your name: ")
preferences = get_user_preferences()
recommendations = recommend_courses(courses, preferences)
print("Hello", name + "!")
print("Here are some courses/projects based on your interests:")
show_courses(recommendations)
print("Thank you for using General Recommendation System!!!")