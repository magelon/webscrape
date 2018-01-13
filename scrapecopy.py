from selenium import webdriver
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred=credentials.Certificate('auth.json')
firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://auth-7ba82.firebaseio.com'
})

ref=db.reference('titles')
snapshot=ref.get()

print(snapshot)

import json
#data={'title':post.text}
#sent=json.dumps(data)
#result=firebase.post('/titles',sent)



#chrome_path="/Users/firoprochainezo/Desktop/chromedriver"
#driver=webdriver.Chrome(chrome_path)
#driver.get("https://sfbay.craigslist.org")
#driver.find_element_by_xpath("""//*[@id="hhh0"]/li[1]/a""").click()

#posts=driver.find_elements_by_class_name("result-title")
id=0
#for post in posts:
    #if "bedroom" in post.text:
            #print(id,post.text)
            #print(post.text)
            #data={'title':post.text}
            #sent=json.dumps(data)
            #firebase.post("/titles",data)
    
