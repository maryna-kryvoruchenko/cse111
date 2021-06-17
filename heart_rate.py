user_input = int(input("Please enter your age: "))

max_rate = 220 - user_input
lower_range = max_rate * 0.65 
higher_range = max_rate * 0.85 

print(f"When you exercise to strengthen your heart, you should keep your heart rate between {lower_range:.0f} and {higher_range:.0f} per minute")