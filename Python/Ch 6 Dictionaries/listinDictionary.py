Favourite_languages={'Jitin':['Python','C++'],'Sara':['C','Go'],'Arjit':['Ruby','Java'],'Kartikeya':['Python'],}
for name,lanuages in Favourite_languages.items():
    print(f"{name} 's favourite Languages are:")
    for language in lanuages:
        print(f"\t{language.title()}")
    