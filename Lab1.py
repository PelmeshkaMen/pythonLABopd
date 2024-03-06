from bs4 import BeautifulSoup
import requests


def parse():
    url = 'https://omgtu.ru/general_information/faculties/'

    page = requests.get(url,verify=False)
    print(page.status_code)
    soup = BeautifulSoup(page.text, "html.parser")
    block = soup.find('div',id='pagecontent')
    description=''
    for data in block:
        if data.find('a') :
            description += data.text.strip() + '\n'

    f = open('one','w', encoding='UTF-8')
    f.write(description)
    f.close()



parse()
#div class="main__content"
#590
