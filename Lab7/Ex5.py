celebs = ("Taylor Swift", "Lionel Messi", "The Weeknd", "Keanu Reeves", "Angelina Jolie")
ages = (36, 38, 36, 61, 50)

celbs_list = []
ages_list = []

for celeb in celebs:
    celbs_list.append(celeb)

ages_list = [age for age in ages]

celbs_dict ={"celbbrities": celbs_list, "ages": ages_list}

print(celbs_dict)   


