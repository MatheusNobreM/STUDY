filmDict = {
    "title": "Inception",
    "director": "Christopher Nolan",
    "year": 2010,
    "genre": ["Science Fiction", "Action", "Adventure"]}

print(filmDict)
print(filmDict["director"])
print(filmDict.get("year"))
filmDict["rating"] = 8.8
print(filmDict)

print(filmDict.keys())
print(filmDict.values())
print(filmDict.items())
filmDict.pop("genre")
print(filmDict)