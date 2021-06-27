from selenium import webdriver
import selenium
import pandas as pd
browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://scraping-for-beginner.herokuapp.com/ranking/')

#1つの観光地の取得

elem_rankingBox = browser.find_element_by_class_name('u_areaListRankingBox')
elem_title=elem_rankingBox.find_element_by_class_name('u_title')
title = elem_title.text 
#タイトルの要らない部分を除去。タグで更にしぼってもOK 
title.split('\n')[1]

#総合評価の取得
elem_rank=elem_rankingBox.find_element_by_class_name('u_rankBox ') 
rank = elem_rank.text 
print(rank)

#楽しさ評価の取得
elem = browser.find_element_by_class_name('u_categoryTipsItem ')
elem = elem.find_elements_by_class_name('is_rank')[0]
elem = elem.find_element_by_class_name('evaluateNumber')


#複数の観光地の取得
titles=[]
elems_rankingBox = browser.find_elements_by_class_name('u_areaListRankingBox')

for elem_rankingBox in elems_rankingBox:
    elem_title=elem_rankingBox.find_element_by_class_name('u_title').find_element_by_tag_name('h2')
    title = elem_title.text.split('\n')[1]
    titles.append(title)
print(titles)


#観光地ごとのループ
all_evaluates=[]
elems = browser.find_elements_by_class_name('u_categoryTipsItem ')
for elem in elems:
    evaluates=[]
    categorys= elem.find_elements_by_class_name('is_rank')
    #観光地ごとの4つの評価を取得
    for category in categorys:
        evaluate = category.find_element_by_class_name('evaluateNumber')
        evaluates.append(evaluate.text)
    all_evaluates.append(evaluates)
print(all_evaluates)


#pandas形式に変換
df=pd.DataFrame()
df['名前']=titles

df_categorys= pd.DataFrame(all_evaluates)
df_categorys.columns=['楽しさ','人','形式','アクセス']
##DF結合
df=pd.concat([df,df_categorys],axis=1)

df.to_csv('観光地情報.csv')
print(df)


    