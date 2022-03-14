
def cone_volume():
    while True:
        try:
            pi = 3.142
            radius_cone = float(input("Enter the cone's radius: "))
            height_cone = float(input("Enter the cone's height: "))
            volume_cone = pi*(radius_cone*radius_cone)*(height_cone/3)
            print("The volume is: ",volume_cone)
            break
        except ValueError:
            print("That is not a valid number. Please try again...")
    return volume_cone

def cube_volume():
    while True:
        try:
            length_cube = float(input("Enter the cube's length: "))
            volume_cube =(length_cube*length_cube*length_cube)
            print("The volume is: ",volume_cube)
            break
        except ValueError:
            print("That is not a valid number. Please try again...")
    return volume_cube

def cylinder_volume():
    while True:
        try:
            pi = 3.142
            radius_cyl = float(input("Enter the radius of the cylinder: "))
            height_cyl = float(input("Enter the height of the cylinder: "))
            volume_cyl =(pi*radius_cyl*radius_cyl*height_cyl)
            print("The volume is: ",volume_cyl)
            break
        except ValueError:
            print("That is not a valid number. Please try again...")
    return volume_cyl
    


print("Please Select the Calculation you would like to perform (Selection should be 1, 2 or 3")
print("1. Calculate the volume of a cone")
print("2. Calculate the volume of a cube")
print("3. Calculate the volume of a cylinder")
choice = input("Please enter the number of your desired calculation: ")

if (choice == "1"):
    total = cone_volume()
    choice = input("Please enter the number of your desired calculation: ")
if (choice == "2"):
    total = cube_volume()
    choice = input("Please enter the number of your desired calculation: ")
if (choice == "3"):
    total = cylinder_volume()
    choice = input("Please enter the number of your desired calculation: ")
else:
    print("That is not a valid selection. Please enter 1, 2 or 3")
    exit()
    
    

