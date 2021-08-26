import requests
from bs4 import BeautifulSoup
from collections import Counter
import re


class WordCount(object):
    def get_text(self, url):
    # '문자열 수집'
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        return soup.text

    def get_list(self, text):
        # '단어 리스트로 변환'
        return text.split()

    def __call__(self, url):
        text = self.get_text(url)
        words = self.get_list(text)
        counter = Counter(words)
        return counter


class KorWordCount(WordCount):
    def get_list(self, text):
        '한글로만 구성된 단어만 추출'
        words = text.split()
        return [word for word in words if re.match(r'^[ㄱ-힣]+$', word)] # list comprehension 문법



if __name__ == "__main__":
    # wordcount = WordCount()
    # print(wordcount('https://www.inhandplus.com'))
    korwordcount = KorWordCount()
    print(korwordcount('https://www.inhandplus.com'))



