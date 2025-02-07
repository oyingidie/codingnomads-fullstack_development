# 0. Write the necessary code to calculate the volume and surface area
#    of a cylinder with a radius of 3.14 and a height of 5.
# 1. Print out the result.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

radius = 3.14
height = 5

# volume of a cylinder = πr²h
volume = (22/7) * (radius ** 2) * height

# surface area of a cylinder = 2πrh + 2πr²
first_term = 2 * (22/7) * radius * height # 2πrh (curved surface area)
second_term = 2 * (22/7) * (radius ** 2) # 2πr² (top and bottom)
surface_area = first_term + second_term

print("Volume of the cylinder: ", volume)
print("Surface area of the cylinder: ", surface_area)
