pi = 3.142
while True:
    try:
        radius_cone = float(input("Enter the cone's radius: "))
        height_cone = float(input("Enter the cone's height: "))
        volume_cone = pi*(radius_cone*radius_cone)*(height_cone/3)
        print("The volume is: ",volume_cone)
        break
    except ValueError:
        print("That is not a valid number. Please try again...")

