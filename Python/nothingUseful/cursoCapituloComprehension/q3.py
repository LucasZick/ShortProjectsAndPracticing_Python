from itertools import count


phrase = "Practice Problems to Drill List Comprehension in Your Head."

countSpaces = len([char for char in phrase if char == " "])

print(countSpaces)