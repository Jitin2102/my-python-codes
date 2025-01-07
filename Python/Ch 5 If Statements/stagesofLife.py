def life_stage(age):
    if age<0:
        return "Invalid age"
    elif age<2:
        return "baby"
    elif age<4 :
        return "toddler"
    elif age<13 :
        return "kid"
    elif age<20:
        return "teenager"
    elif age<65:
        return "adult"
    else:
        return "elder" 
age=int(input("Enter your age: "))
stage=life_stage(age)
print(f"At {age} years old, you are in the {stage} stage of life.")                  
        