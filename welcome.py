# Hey this is cool coding stuff i did on sunday


students = ["James", "Kareem", "Brian", "Zabdiel", "Pamauk"]

for student in students:
    print(student + " is going to crush next week!")



    def birthday_generator(age):
        new_age = age + 1
        return f"you just had a birthday, you are now {new_age} years old"
    print(birthday_generator(16))
    print(birthday_generator(29))


    #adding in more code so we can see the commit error message!

    print("Hello I love to write out code its so fun!")

def birthday_generator2(age):
        new_age = age + 1
        if new_age < 21:
             return f"you just had a birthday, you are now {new_age}"
        elif new_age > 21 and new_age <50:
             return f"We wont tell anyone its your {new_age} birthday, your secret is safe!"
print(birthday_generator(16))
print(birthday_generator(29))
print(birthday_generator(70))