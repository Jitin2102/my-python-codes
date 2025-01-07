Favourite_languages={'Jitin':'Python','Sara':'C','Arjit':'Ruby','Kartikeya':'Python',}
polling=['Jitin','Sarah','Adarsh','Arjit','Kartikeya','Arsh','Arpit']
for person in polling:
    if person in Favourite_languages.keys():
        print(f"{person},Thanks  for participating in poll.")
    else:
        print(f"{person},Please participate in the poll. ")    