from bs4 import BeautifulSoup
import requests
import re

def pyJobnumberSearch(word):   
    address='https://jobcentrebrunei.gov.bn/web/guest/search-job?'
    newword=address+word
    page=requests.get(newword)
    soup = BeautifulSoup(page.content, 'html.parser')
    phrase_extract=soup.select_one('.search-total-label')
    all_words = phrase_extract.text.split()
    return all_words[0]

pyJobnumberSearch('sort=modified-&start=1&q=')

def pyJobdetailsFetch(word):   
    jobs={}
    jobs_keys=[]
    jobs_values=[]
    address='https://jobcentrebrunei.gov.bn/web/guest/search-job?'
    newword=address+word
    page=requests.get(newword)
    soup = BeautifulSoup(page.content, 'html.parser')
    phrase_extract=soup.findAll('h4')
    salary_extract = soup.findAll('li', text=re.compile('^\$.*(Daily|Monthly)$'))
    for tag in phrase_extract:
        jobs_keys.append(tag.text.strip())
    for tag in salary_extract:
        jobs_values.append(tag.text.strip())

    jobs = {jobs_keys[i]: jobs_values[i] for i in range(len(jobs_keys))}
    return jobs
    

pyJobdetailsFetch('sort=modified-&start=1&q=')

