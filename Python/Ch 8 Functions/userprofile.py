def build_profile(first,last,**user_profile):  ## ** MEANS PYTHON IS TOLD TO DECLARE A DICTIONARY
    user_profile['first_name']= first.title()
    user_profile['last_name']= last.title()
    return user_profile
user_profile=build_profile('albert','einstein',Location='Princeton',Field='Physics')
print(user_profile)