from selenium import webdriver
import selenium
import pandas as pd
browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://scraping-for-beginner.herokuapp.com/ranking/')


titles=[]
ranks=[]
all_categorys=[]

for page in range(1,4):
    url = 'https://scraping-for-beginner.herokuapp.com/ranking/?page={}'.format(page)
    browser.get(url)


    #地名
    elems_rankingBox = browser.find_elements_by_class_name('u_areaListRankingBox')
    for elem_rankingBox in elems_rankingBox:
        elem_title=elem_rankingBox.find_element_by_class_name('u_title').find_element_by_tag_name('h2')
        title = elem_title.text.split('\n')[1]
        titles.append(title)
    
    #評価
    elems = browser.find_elements_by_class_name('u_categoryTipsItem ')
    for elem in elems:
        evaluates=[]
        categorys= elem.find_elements_by_class_name('is_rank')
        #観光地ごとの4つの評価を取得
        for category in categorys:
            evaluate = category.find_element_by_class_name('evaluateNumber')
            evaluates.append(evaluate.text)
        all_categorys.append(evaluates)

print(titles)
print(all_categorys)
