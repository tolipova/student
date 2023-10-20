def biology(rating):
    return rating
def math(rating):
    return rating
def history(rating):
    return(rating)
def russian_l(rating):
    return rating
student_name = []
student_raiting =[]
while True:
    name = input("Enter the student name: ")
    student_name.append(name)
        

    print("Subjects")
    print("1/biology")
    print("2/math")
    print("3/history")
    print("4/russian_l")
    choice = input("Choice number (1,2,3,4,5)")
    if choice == '1':
        a = (input(f"enter the rating {biology} to {name}: "))
        student_raiting.append(a)
    elif choice == '2':
        a = (input(f"enter the rating {math} to {name}: "))
        student_raiting.append(a)

    elif choice == '3':
        a = (input(f"enter the rating {history}  to {name}: "))
        student_raiting.append(a)

    elif choice == '4':
        a =(input(f"enter the rating {russian_l} to {name}: "))
        student_raiting.append(a)

    elif choice == 'exit':
        break
    elif choice == '5':
        print(student_raiting)
    else:
        print("error")      
        
    




        

        
