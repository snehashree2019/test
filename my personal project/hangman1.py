import requests
from bs4 import BeautifulSoup
import re
import random
word_list = []
new_list = []

url = 'https://www.ef.edu/english-resources/english-vocabulary/top-3000-words/'
html_data = requests.get(url)
soup = BeautifulSoup(html_data.text,'html.parser')
div_list = soup.find('div',attrs={'class':'field-item even'})
result = div_list.find_all('p')[1].text.strip()
new_result = re.sub(" ","",result)

word_list = new_result.split("\n\t")
guess_word = random.choice(word_list)

print(guess_word)
print("game begins")

my_word = '-'*len(guess_word)
my_word = list(my_word)
print(my_word)

var = input("Enter your guessing alphabets")
for pos,val in enumerate(guess_word):

    if val == var:
        my_word[pos]=val


print(my_word)




##for index,value in enumerate(guess_word):

##    if var == value:
##        print(index)
##        print(my_word[index])
##        my_word = my_word.replace(my_word[index],value,1)
##print(my_word)
