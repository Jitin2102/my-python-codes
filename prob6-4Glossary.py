glossary_2={'Sharp':'Blunt','Fast':'Slow','Top':'Bottom','Alive':'Dead','Fertile':'Barren'}
favourite_languages={'Jitin':'Python','Sara':'C','Arjit':'Ruby','Kartikeya':'Python',}
favourite_languages.update(glossary_2)
for key,value in favourite_languages.items():
    print(f"{key}:{value}")
    