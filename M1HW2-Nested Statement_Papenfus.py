# Nested Control Statements (3.16 page 114)
# January 28, 2020
# CSC 121 M1HW2 - NESTED CONTROL STATEMENT
# Bettina Papenfus


def range(list1):  
    largest = list1[0]  
    lowest = list1[0]  
    largest2 = None
    lowest2 = None
    for item in list1[1:]:      
        if item > largest:  
            largest2 = largest 
            largest = item  
        elif largest2 == None or largest2 < item:  
            largest2 = item  
        if item < lowest:  
            lowest2 = lowest 
            lowest = item  
        elif lowest2 == None or lowest2 > item:  
            lowest2 = item  

    print("        Largest set of Numbers         ")
    print(" ")          
    print("      Largest element is:", largest       )
    print("    Second Largest element is:", largest2 )
    print(" ")
    
    print("---------------------------------------")
    
    print(" ")
    print("         Smallest set of Numbers          ")
    print(" ")
    print("       Smallest element is:", lowest       )  
    print("   Second Smallest element is:", lowest2   )  
    print(" ")
print("===================================================================")  
  
list1 = [108, 43, 85, 94, 36, 50, 8, 64, 71, 22] 
range(list1) 

print("==================================================================") 
  
       #####################################################
       # Python program to find largest, smallest,         #  
       # second largest and second smallest in a           #
       # list using if and elif statements                 #
       # Repeating statement to display different results  #
       #####################################################