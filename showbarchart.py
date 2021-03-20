import matplotlib.pyplot as plt
import json

with open('all_books.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

book_price1 = []
book_price2 = []
book_price3 = []

for i in data["kitaplar"]:
    if float(i['BookPrice']) >= 10.0 and float(i['BookPrice']) <= 25.0:
        book_price1.append("1")

    if float(i['BookPrice']) > 25.0 and float(i['BookPrice']) <= 50.0:
        book_price2.append("2")

    if float(i['BookPrice']) > 50.0:
        book_price3.append("3")

Country = ['10 - 25TL', '25 - 50Tl', '50TL Üzeri']
GDP_Per_Capita = [len(book_price1), len(book_price2), len(book_price3)]

plt.bar(Country, GDP_Per_Capita)
plt.title('Kitap Fiyatları')
plt.xlabel('Fiyatlar')
plt.show()