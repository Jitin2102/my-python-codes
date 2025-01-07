def get_full_name(firstName,lastName,middleName=""):
    full_name=f"{firstName} {middleName} {lastName}"
    return full_name.title()
CR=get_full_name('sumit','jaat')
print(CR)