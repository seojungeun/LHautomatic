from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import time
import requests
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains


chromedriver='C:/Users/seo/Desktop/chromedriver.exe'

url='http://apply.lh.or.kr/'

browser = webdriver.Chrome(chromedriver)

browser.get(url)

 

handles = browser.window_handles

size =len(handles)

parent_handle = browser.current_window_handle

for x in range (size):

    if handles[x] != parent_handle:

        browser.switch_to_window(handles[x])

        print(browser.title)

        browser.close()

        break

 

browser.switch_to_window(parent_handle)

 

# 팝업 xpath 값을 지속적으로 바뀌니 수시로 확인이 필요함

browser.implicitly_wait('10')

popup_button=browser.find_element_by_xpath('//*[@id="mainframe_ChildFrame_sys_open_pop45_form_Button02ImageElement"]/img')

popup_button.click()

popup_button2=browser.find_element_by_xpath('//*[@id="mainframe_ChildFrame_sys_open_pop6_form_Button02ImageElement"]/img')

popup_button2.click()

popup_button3=browser.find_element_by_xpath('//*[@id="mainframe_ChildFrame_sys_open_pop44_form_Button02ImageElement"]/img')

popup_button3.click()

 

 

# 분양 sale_path 임대 retal_path 신혼부부 dreamtown_path

sale_path='//*[@id="mainframe_ChildFrame_form_div_Work_frm_div_Work_div_Form_btn_HsInfoListImageElement"]/img'

retal_path='//*[@id="mainframe_ChildFrame_form_div_Work_frm_div_Work_div_Form_btn_LsHsInfoList"]/div[2]'

dreamtown_path='//*[@id="mainframe_ChildFrame_form_div_Work_frm_div_Work_div_Form_btn_NwhtInfoList"]/div[2]'

totlaSelect_xpath='//*[@id="mainframe_ChildFrame_form_div_Work_frm_div_Work_div_Form_tab_GroupMenu_tab_MenuAll_tabbutton"]'

 

step_one_button=browser.find_element_by_xpath(sale_path)

step_one_button.click()

 

#전체검색하여 페이지 넘기기 테스트용

# totlaSelect_xpath='//*[@id="mainframe_ChildFrame_form_div_Work_frm_div_Work_div_Form_tab_GroupMenu_tab_MenuAll_tabbutton"]'

# total_bt=browser.find_element_by_xpath(totlaSelect_xpath)

# total_bt.click()

 

 

# 셀리니움은 화면에 보이는것만 값 을 받기 때문에 스크롤 내려주기 처리가 필요함 

# NoSuchElementException 일 때 페이지 전환 종료 및 수집 종료

# nextPaage_xpath='//*[@id="mainframe_ChildFrame_form_div_Work_frm_div_Work_div_Form_Div01_div_Paging_btn_Paging02TextBoxElement"]/div'

# next_page=browser.find_element_by_xpath(nextPaage_xpath)

 
# num_of_pagedowns = 50

 

# while num_of_pagedowns:

#     ac.send_keys(Keys.PAGE_DOWN)

#     time.sleep(0.3)

#     num_of_pagedowns -= 1

#     try:

#         next_page=browser.find_element_by_xpath(nextPaage_xpath)

#         next_page.click()

 

#     except:

#         None

 

#수집 일자 조건받기

# startdate_path='//*[@id="mainframe_ChildFrame_form_div_Work_frm_div_Work_div_Form_Div01_Div01_div_Calendar_mae_SearchStartDate"]'

# enddate_path='//*[@id="mainframe_ChildFrame_form_div_Work_frm_div_Work_div_Form_Div01_Div01_div_Calendar_mae_SearchEndDate"]'

# term_botton_path='//*[@id="mainframe_ChildFrame_form_div_Work_frm_div_Work_div_Form_Div01_Div01_btn_Search"]/div'

# time.sleep(2)

# startdate=browser.find_element_by_xpath(startdate_path)

# enddate=browser.find_element_by_xpath(enddate_path)

 

# browser.implicitly_wait(10)

# ac=ActionChains(browser)

# ac.move_to_element(startdate)

# ac.send_keys_to_element(startdate,'0101').perform()

 

browser.implicitly_wait(4)

 

# 다음 버튼을 누르기 위한 대기시간

# ac.move_to_element(enddate)

# ac.send_keys_to_element(enddate,'0201').perform()

 

# term_botton=browser.find_element_by_xpath(term_botton_path)

# term_botton.click()




try:
        # 리스트 탐색 변수
        list_number=4

        step_two_path='//*[@id="mainframe_ChildFrame_form_div_Work_frm_div_Work_div_Form_Div01_Grid00_body_gridrow_'+str(list_number)+'_cell_'+str(list_number)+'_2"]'

        step_two_botton=browser.find_element_by_xpath(step_two_path)

    

        stbt=step_two_botton.text

        print(stbt)

        step_two_botton.click()

except: 
        time.sleep(6)
        browser.close()

    # 

    #참고 현재페이지에서 뒤로가기가 가능함

    # browser.back()

    

    

    

#분양공고 다운로드 받기위한 함수 1

def upcount(browser,down_number):

    down_number=down_number+1

    return download_step(browser,down_number)



#분양공고 다운로드 받기위한 함수 (건들이면 안됨 시작 에서부터 up_count 하는 방식)
down_number=0

def download_step(browser,down_number):

    try:

        browser.implicitly_wait(10)

        dlpath='//*[@id="mainframe_ChildFrame_form_div_Work_frm_div_Work_div_Form_Div0'+str(down_number)+'_div_SnotAhflScrollableInnerContainerElement_inner"]'    

        download=browser.find_element_by_xpath(dlpath)

        name=download.text

        download.click()

        print(name)

    except NoSuchElementException:

        upcount(browser,down_number)

browser.close()        

download_step(browser,down_number)









