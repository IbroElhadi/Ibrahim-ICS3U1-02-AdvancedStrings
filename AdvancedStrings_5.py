def remove_all(result, string):
    return string.replace(result, '')

print(remove_all("an", "banana") == "ba")
print(remove_all("cyc", "bicycle") == "bile")
print(remove_all("iss", "Mississippi") == "Mippi")
print(remove_all("eggs", "bicycle") == "bicycle")