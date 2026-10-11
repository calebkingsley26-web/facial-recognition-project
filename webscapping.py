import bs4
import requests

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

highest_rating_books = []

for page in range(1, 51):
    page_url = base_url.format(page)
    results = requests.get(page_url)
    results.raise_for_status()
    soup = bs4.BeautifulSoup(results.text, 'html.parser')

    books = soup.select('.product_pod')

    for book in books:
        rating = book.select('.star-rating.Four') or book.select('.star-rating.Five')
        if rating:
            book_title = book.select('a')[1]['title']
            highest_rating_books.append(book_title)

for title in highest_rating_books:
    print(title)


