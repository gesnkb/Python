num_list = [6, 5, 3, 8, 4, 2, 5, 4, 11, 43, 1, 17, 27, 90, 77, 62, 51, 47, 82, 86, 20]

#prints number
numbers_count = len(num_list)
print("This list has", numbers_count, "items")

#prints sum
sum = 0
for value in num_list:
    sum = sum + value
print("The sum is", sum)

#prints average 
average = sum / numbers_count
print("The average is:", average)

print(" ")
#prints value & index
print("Printing all list items")
i = 0
while i < numbers_count:
    print("Item", i,":", num_list[i])
    i += 1

print(" ")
#prints every other item
print("Printing every other list item")
for i in range(numbers_count):
    x = num_list[i]
    if i % 2 == 0:
       print("Item", i, ":", x)
    
    
 
    


    
