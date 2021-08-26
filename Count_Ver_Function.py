import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
def word_count(url):
    # 문자열 수집
    html = requests.get(url).text
    # 단어 리스트로 변환
    soup = BeautifulSoup(html, 'html.parser')
    words = soup.text.split()
    
    # 단어수 카운트
    counter = Counter(words)
    return counter


if __name__ == "__main__":
    print(word_count('https://www.inhandplus.com/'))
