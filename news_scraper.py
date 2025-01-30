import requests
from bs4 import BeautifulSoup


main_url = input('Enter url: ')

#article_choice = input('Enter your article choice: ')

up_to_page =int(input("Enter up to what page number: "))

for page in range(1,up_to_page+1):
    page_url =''
    page_url = main_url +'&page='+str(page)
    page_status= requests.get(page_url).status_code

    if page_status == 200:

        page_content = requests.get(page_url).content
        soup = BeautifulSoup(page_content, 'html.parser')
        articles = soup.find_all('article')

        for article in articles:

            article_type = article.find('span',{'data-test': 'article.type'}).text.strip()

            if article_type == "News":
                article_content = article.find('a',{"data-track-action":"view article"})

                article_content = article_content['href']

                articlie_link = "https://www.nature.com" + article_content

                articlie_page = requests.get(articlie_link)

                soup2 = BeautifulSoup(articlie_page.content, 'html.parser')
                article_body = soup2.find('p',{"class": "article__teaser"}).text.strip()


                title = article.find("h3").text.strip()


                title= title.replace('?','_')
                title = title.replace(':', '_')
                new_file = open(title+'.txt','w',encoding= 'utf-8')
                new_file.write(article_body)
                new_file.close()

                print('Article saved')


#