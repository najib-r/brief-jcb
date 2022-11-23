from bs4 import BeautifulSoup
import requests

def pyJobnumberSearch(word):   
    address='https://jobcentrebrunei.gov.bn/web/guest/search-job?'
    newword=address+word
    page=requests.get(newword)
    soup = BeautifulSoup(page.content, 'html.parser')
    phrase_extract=soup.select_one('.search-total-label')
    all_words = phrase_extract.text.split()
    print(all_words[0])

pyJobnumberSearch('sort=modified-&start=1&q=')

