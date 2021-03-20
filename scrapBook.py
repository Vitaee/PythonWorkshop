import requests, json
from bs4 import BeautifulSoup


class ScrapBooks:
    def __init__(self):
        self.my_json = {"kitaplar":[]}

        self.user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}




    def start(self):
        book_hrefs = []
        for i in range(1 , 6):
            base_url = f"http://books.toscrape.com/catalogue/page-{i}.html"
            req = requests.get(base_url, headers=self.user_agent)
            soup = BeautifulSoup(req.content, 'html.parser')

            to_href = soup.find_all('div', class_='image_container')
            for item in to_href:
                book_hrefs.append("http://books.toscrape.com/catalogue/" + item.find('a')['href'])


        self.scrap(book_hrefs)

    def scrap(self, books ):
        z = 1
        while books:
            print(f"{z}. kitap çekiliyor..")
            req = requests.get(books[0], headers=self.user_agent)
            soup = BeautifulSoup(req.content, 'html.parser')


            book_name = soup.find('div', class_='col-sm-6 product_main').find('h1').text

            book_price = soup.find('p', class_='price_color').text
            book_price = book_price.replace('£', '')

            book_stock_info = soup.find('p' , attrs={'class':'instock availability'})
            book_stock_info = book_stock_info.text.strip()


            book_stars = soup.find('p' , class_='star-rating')


            if book_stars['class'][1] == 'One': book_stars = 1

            elif book_stars['class'][1] == 'Two': book_stars = 2

            elif book_stars['class'][1] == 'Three': book_stars = 3

            elif book_stars['class'][1] == 'Four': book_stars = 4

            else: book_stars = 5

            table_data = soup.find('table', class_='table table-striped')

            book_upc = table_data.find('tr').find('td').text

            book_image = soup.find('div',class_='item active')
            book_image = "http://books.toscrape.com/catalogue/" + book_image.find('img')['src']

            book_category = soup.find('ul', class_='breadcrumb')

            book_category = book_category.find_all('li')[2].text.strip()

            to_js = {
                'BookName':book_name,
                'BookPrice':book_price,
                'BookStock':book_stock_info,
                'BookStars':book_stars,
                'BookUpc':book_upc,
                'BookImg':book_image,
                'BookCategory':book_category,
                'BookHref':books[0]
            }

            self.my_json['kitaplar'].append(to_js)


            books.pop(0)
            z += 1



        self.save()

    def save(self):
        with open('all_books.json', 'w', encoding='utf-8') as file:
            json.dump(self.my_json , file, ensure_ascii=False, indent=4)

        print("veriler kayıt edildi..")









book_scrapper = ScrapBooks()
book_scrapper.start()



