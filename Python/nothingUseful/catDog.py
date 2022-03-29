def cat_dog(str):
    dogs = str.count('dog')
    cats = str.count('cat')
    return(cats is dogs)

print(cat_dog('catcatcatdogdogcatdogdogcat'))
