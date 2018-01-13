from selenium import webdriver
from firebase import firebase
firebase = firebase.FirebaseApplication('https://auth-7ba82.firebaseio.com',None)

import json
#data={'title':post.text}
#sent=json.dumps(data)
#result=firebase.post('/titles',sent)
result = firebase.get('/userProfile',None)
print result


chrome_path="/Users/firoprochainezo/Desktop/chromedriver"
driver=webdriver.Chrome(chrome_path)
driver.get("http://vancouver.craigslist.com")
driver.find_element_by_xpath("""//*[@id="hhh0"]/li[1]/a""").click()

posts=driver.find_elements_by_class_name("result-title")
id=0
for post in posts:
    if "bedroom" in post.text:
            print(id,post.text)
            data={'title':post.text}
            sent=json.dumps(data)
            firebase.post("/titles",sent)
    
