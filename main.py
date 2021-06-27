from  selenium import webdriver
from selenium.webdriver.chrome.options import Options

import pandas as pd 


#処理終了後にブラウザを終了しないようにdetachオプションをつける
options = Options()
options.add_experimental_option('detach', True)
browser = webdriver.Chrome('chromedriver.exe', options=options)
 #指定のURLにアクセス
browser.get('https://scraping-for-beginner.herokuapp.com/login_page')

#要素を取得,入力
elem_username = browser.find_element_by_id('username')
elem_username.send_keys('imanishi')

elem_password = browser.find_element_by_id('password')
elem_password.send_keys('kohei')

elem_login_btn = browser.find_element_by_id('login-btn')
elem_login_btn.click()

#IDで指定して取得
elem = browser.find_element_by_id('name')
print(elem.text)

profile_ids = ['company','birthday','come_from','hobby']
for ids in profile_ids:
    profile_elem = browser.find_element_by_id(ids)
    print(profile_elem.text.replace('\n',','))

#タグで指定して取得
elem_th = browser.find_element_by_tag_name('th')
elems_th = browser.find_elements_by_tag_name('th')
elems_td = browser.find_elements_by_tag_name('td')

print(elems_th[0].text)
# XXX elems_th.text  XXX

#リストに格納
keys = []
for elem_th in elems_th:
    key = elem_th.text
    keys.append(key)

values = []
for elem_td in elems_td:
    value = elem_td.text
    values.append(value)


#CSV 出力
df = pd.DataFrame()
df['項目']  = keys
df['値']  =values

df.to_csv('講師情報.csv', index=False)



