age = int(input("What is your age? "))
is_citizen = str(input("Are you a citizen of the U.S? "))
residency = int(input("how long have you been a resident of the U.S? "))
if age < 35:
    print("your age is not eligiable to run for president!")
else:
    print("your age is eligable to run for president!")
if is_citizen == "yes":
    print("your citizenship makes you eligiable to run for president!")
elif is_citizen == "no":
    print("becasue you do not have citizenship, you are not eligable to run for president!")
else:
    print("please type in the correct options to continue")
if residency < 14:
    print("you have not been a resident for long enough to be eligable to run for president! ")
else:
    print("you have been a resident for long enough to be eligable to run for president! ")