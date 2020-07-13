from selenium import webdriver
#script to crawl wikipedia and make a dict

browser = webdriver.Chrome()
browser.get('https://en.wikipedia.org/wiki/List_of_effects')

for i in range(27):
    effects = browser.find_elements_by_xpath(f'//*[@id="mw-content-text"]/div/ul[{i}]/li')
    for x in range(len(effects)):
        effect = effects[x].text
        neweffect = effect.replace(')','')
        effectlist = neweffect.split('(')
        effectresult = {'Title': 'title','Keywords':[]}
        for y in range(len(effectlist)):
            if y == 0:
                 effectresult['Title'] = effectlist[0]
            else:
                effectresult['Keywords'].append(effectlist[y])
        print(effectresult)            

        


browser.close()

