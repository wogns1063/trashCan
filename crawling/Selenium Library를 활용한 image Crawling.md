# Selenium Library를 활용한 image Crawling

machine learning을 학습하기 전 학습할 이미지를 <strong>Selenium, Chromedriver</strong>를 사용하여 수집합니다.

## Selenium 
1. 코드 설명 
 -  (코드1)
    ```
    # 밑으로 홈페이지를 내렷을 때 정보가 나오는 경우 selenium 사용
    !pip install selenium
    from selenium import webdriver
    import os
    import time
    
    #찾고자 하는 검색어를 url로 만들어 준다.
    searchterm = 'takeout-Cup'
    url = "https://www.google.com/search?q="+searchterm+"&sxsrf=ACYBGNTHN8_c2BkwWl-c_nJ78-X7jh9lHw:1569220968104&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjC1ILTq-bkAhVSPnAKHbF-AiUQ_AUIEigB&biw=1366&bih=657"
    
    #chrome webdriver 사용하여 브라우저를 실행
    browser = webdriver.Chrome("./chromedriver.exe")
    browser.get(url)
    
    ```
    1. Crawling을 하기 전에 URL을 분석해야 한다. 
    2. 위의 코드에서 searchterm 부분을 수정하면 구글에서 해당 단어를 검색한 이미지 사이트가 나온다.
        * (ex)
          ![searchterm = takeout-Cup](https://user-images.githubusercontent.com/48505947/68844984-0ac76e00-070e-11ea-9fce-0cdad849aa90.png)
    3. webdriver로 chrome을 사용한다.
-  (코드2)
    ```
    # 검색 결과를 늘리기 위하여 스크롤 다운
    for _ in range(10):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
    
    # 소스코드가 있는 경로에 '검색어' 폴더가 없으면 만들어준다.
    # (이미지 저장 폴더를 위해)
    if not os.path.exists(searchterm):
        os.mkdir(searchterm)
    
    #현재 수집된 이미지 수를 나타내는 변수
    succounter = 0
    #class name 이 THL인 요소를 모두 가지고 온다.
    img_list = browser.find_elements_by_class_name('THL2l')
    for idx, x in enumerate(img_list):
        try: 
            save_path = os.path.join(searchterm, str(idx)+".png")
            #이미지 저장
            x.screenshot(save_path)
            succounter = succounter + 1
            
            ranning_test = "ranning: " +str(succounter)+"/" +str(len(img_list))
            print(ranning_test)
            
        except:
            print("can't get img")
    
    print(succounter, "succesfully download")
    ```
    1. chrome이 실행된 이후 스크롤 다운 기능을 넣어 자동으로 사이트를 내려가며 이미지를 다운 받는다.
    2. 다운 받은 이미지를 'searchterm'과 동일한 폴더에 넣는다.
    3. Crawling에서 제일 중요한 해당 사이트의 태그를 분석한다. 수집하려는 이미지가   div 태그의 class name이 "THL2l" 에 존재한다. 따라서, browser.find_elements_by_class_name('THL2l)을 사용하여 해당 태그를 가져와 해당 이미지를 저장한다.
- 결과
    1. 해당 폴더 안에 이미지가 수집되었다.
        ![](https://user-images.githubusercontent.com/48505947/68846135-e8365480-070f-11ea-8591-af290dca27c1.png)
    2. 수집된 이미지.
        ![](https://user-images.githubusercontent.com/48505947/68846290-2b90c300-0710-11ea-8682-9ba66bb2a691.png)
    
2. Selenium과 관련된 정보는 [Selenium 사이트](https://selenium-python.readthedocs.io/)를 참고하였다.     
           