import matplotlib.pyplot as plt
import json

with open('all_books.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

star_2 = []
star_3 = []
star_4 = []
star_5 = []

print(len(data["kitaplar"]) , " adet kitap mevcut.")
for item in data["kitaplar"]:
    if item['BookStars'] == 2:star_2.append(item["BookStars"])
    if item['BookStars'] == 3: star_3.append(item["BookStars"])
    if item['BookStars'] == 4: star_4.append(item["BookStars"])
    if item['BookStars'] == 5: star_5.append(item["BookStars"])
    else: pass

    
labels = '2 star', '3 star', '4 star', '5 star'
sizes = [len(star_2), len(star_3), len(star_4), len(star_5)]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()