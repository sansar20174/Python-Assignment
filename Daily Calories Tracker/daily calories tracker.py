
        # Name: Sansar Kumar
        # Date: 06/10/2025
        # Description: A simple daily calories tracker that records meals and their calorie counts.

print("=========================================================================================================================")
print("                                 Welcome to the Daily Calories Tracker!")
print("              We will help you keep track of your meals and their calorie counts throughout the day.")
print("=========================================================================================================================")
Meals = []
Calories = []
num_meals = int(input("how many meals did you have today? "))
        
for i in range(num_meals):
    meal = input(f"Enter the name of meal {i+1}: ")
    calorie = float(input(f"Enter the calories for {meal}: "))
    Meals.append(meal)
    Calories.append(calorie)
    print(f"Recorded: {meal} with {calorie} calories.")
total_calories = sum(Calories)
average_calories = total_calories / num_meals
daily_limit = float(input("Enter your daily calorie limit: "))

print("=================================Daily Summary Report======================================")
for meal, calorie in zip(Meals, Calories):
    print(f"{meal}:\t\t {calorie}")
print(f"Total calories consumed today: {total_calories}")
print(f"Average calories per meal: {average_calories:.2f}") 
if total_calories > daily_limit:
    print("⚠️ You have exceeded your daily calorie limit. Consider healthier meal options tomorrow.")  
else:
    print("Great job! You are within your daily calorie limit. Keep it up!👍")
print("===========================================================================================")

save_choice = input("Do you want to save your daily summary to a file? (yes/no): ").strip().lower()
if save_choice in ['yes', 'y']:
    filename = input("Enter the filename to save your summary (e.g., summary.txt): ").strip()
    with open(filename, 'w') as f:
        f.write("=================================Daily Summary Report======================================\n")
        for meal, calorie in zip(Meals, Calories):
            f.write(f"{meal}:\t\t {calorie}\n")
        f.write(f"Total calories consumed today: {total_calories}\n")
        f.write(f"Average calories per meal: {average_calories:.2f}\n")
        if total_calories > daily_limit:
            f.write("⚠️ You have exceeded your daily calorie limit. Consider healthier meal options tomorrow.\n")
        else:
            f.write("Great job! You are within your daily calorie limit. Keep it up!👍\n")
        f.write("===========================================================================================\n")
    print(f"Summary saved to {filename}")
