cities={
    "Mumbai":{
        'country':'India',
        'population':'20 million',
        'fact':"Mumbai is called financial capital of India.",
    },
    "Tokyo":{
        'country':'Japan',
        'population':"37 million",
        'fact':"Japan is known as biggest metropolitan city.",
    },
    "NewYork":{
         'country':'America',
         'population':"8.2 million",
         'fact':"NewYork is known as 'Big Apple'." ,   
    } ,   
    
}
for city,info in cities.items():
    print(f"City:{city}")
    for key,value in info.items():
        print(f"{key.capitalize()}:{value}")
    print()    
    