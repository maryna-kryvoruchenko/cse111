import math

#Making the assignment my own: Help find the aspect ratio first

tire_width = float(input("Please enter the width of the tire in mm: "))
tire_height= float(input("Please enter the tire side wall height in mm: "))

aspect_ratio = (tire_height / tire_width) * 100 

print(f"The aspect ratio is {aspect_ratio:.0f}")

#Assignment

width = float(input("Please enter the width of the tire in mm: "))
ratio = float(input("Please enter the aspect ratio of the tire: "))
diameter = float(input("Please enter the diameter of the wheel in inches: "))

part_one_volume = (width * ratio) + (2540 * diameter)
part_two_volume = math.pi * width**2 * ratio
volume = (part_one_volume * part_two_volume) / 10000000 

print(f"The appriximate volume is {volume:.1f}")
