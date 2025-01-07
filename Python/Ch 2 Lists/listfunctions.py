motorcycles=['honda','yamha','suzuki']
print(motorcycles)
# last_owned=motorcycles.pop(1)
# first_owned=motorcycles.pop(0)
# print(f"The last motorcycle I owned was a {last_owned.title()}.")
# print(f"The first motorcycle I owned was a {first_owned.title()}.")
del motorcycles[0]
print(motorcycles)
suzuki='suzuki'
motorcycles.remove(suzuki)
print(motorcycles)
