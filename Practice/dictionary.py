# d={
#     "name": "dictionary",
#     "description": "Wow!You are very bully.",
#     "version": "1.0",
#     "author": "Jitin Kumar",
#     "license": "MIT"
# }
# print(d)
# for key,value in d.items():
#     print(key , ":", value)
# print(d["description"])    

d={
    "good": "excellent",
    "bad": "poor",
    "happy": "joyful",
    "sad": "unhappy",
    "angry": "mad",
    "surprised": "astonished",
    "verbal": "spoken"
}
key=input("Enter key to search:")
if key in d:
    print( key, ":", d[key])
else:
    print("Key not found in the dictionary.") 