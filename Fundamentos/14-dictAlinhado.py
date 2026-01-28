import pprint

filmDict = {
    "Filme1": {
      "title": "Inception",
      "director": "Christopher Nolan",
      "year": 2010,
      "genre": ["Science Fiction", "Action", "Adventure"]},
      "Filme2": {
      "title": "The Matrix",
      "director": "The Wachowskis",
      "year": 1999,
      "genre": ["Science Fiction", "Action"]
      }}
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(filmDict)
pp.pprint(filmDict["Filme1"]["director"]) 
pp.pprint(filmDict["Filme2"].get("year"))
filmDict["Filme1"]["rating"] = 8.8  
pp.pprint(filmDict)