import requests
from bs4 import BeautifulSoup
from csv import writer

url = "https://www.pararius.com/apartments/den-haag"
html = requests.get(url)

soup = BeautifulSoup(html.content, 'html.parser')
lists = soup.findAll('section', class_="listing-search-item")

with open('renting.csv', 'w', encoding='utf8', newline='') as file:
    thewriter = writer(file)
    header = ['Title', 'Location', 'Price', 'Area', 'Number of rooms']
    thewriter.writerow(header)

    for list in lists:
        title = list.find('a', class_="listing-search-item__link--title").text.replace('\n', '')
        location = list.find('div', class_="listing-search-item__sub-title").text.replace('\n', '')
        price = list.find('div', class_="listing-search-item__price").text.replace('\n', '')
        area = list.find('li',
                          class_="illustrated-features__item illustrated-features__item--surface-area").text.replace(
            '\n','')
        number_of_rooms = list.find('li',
                                     class_="illustrated-features__item illustrated-features__item--number-of-rooms").text.replace(
            '\n','')

        info = [title, location, price, area, number_of_rooms]
        thewriter.writerow(info)



def main():
    pass


if __name__ == "__main__":
    main()
