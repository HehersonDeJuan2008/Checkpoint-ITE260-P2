def get_average(a1, a2, a3):
    return (a1 + a2 + a3) / 3

def get_status(score):
    if score >= 90:
        return "Excellent"
    elif score >= 80:
        return "Very Good"
    elif score >= 75:
        return "Passed"
    else:
        return "Failed"

students = int(input("How many students? "))

for i in range(students):
    print("\nStudent")
    name = input("Enter name: ")
    
    act1 = float(input("Activity 1: "))
    act2 = float(input("Activity 2: "))
    act3 = float(input("Activity 3: "))
    
    average = get_average(act1, act2, act3)
    status = get_status(average)
    
    print("Average:", round(average, 2))
    print("Status:", status)
