
import VO.LH_Xpath_value as vh

class LH_aptDownload:

    def first_activity_function(self):

        self.browser = webdriver.Chrome(chromedriver)

        self.browser.get(url)

    

        handles = browser.window_handles

        size =len(handles)

        parent_handle = browser.current_window_handle

        for x in range (size):

            if handles[x] != parent_handle:

                browser.switch_to_window(handles[x])

                print(browser.title)

                browser.close()

                break

        

        # 팝업 xpath 값을 지속적으로 바뀌니 수시로 확인이 필요함

        browser.implicitly_wait('10')

        popup_button=browser.find_element_by_xpath(popup_xpath1)

        popup_button.click()

        popup_button2=browser.find_element_by_xpath(popup_xpath2)

        popup_button2.click()

        popup_button3=browser.find_element_by_xpath(popup_xpath3)

        popup_button3.click()

        

        # 분양 sale_path 임대 retal_path 신혼부부 dreamtown_path

        step_one_button=browser.find_element_by_xpath(sale_path)

        step_one_button.click()

    

    

    def dateCondition_activity_function(insd,ined):

        startdate=browser.find_element_by_xpath(startdate_xpath)

        enddate=browser.find_element_by_xpath(enddate_xpath)

    

        ac=ActionChains(browser)

        ac.move_to_element(startdate)

        ac.send_keys_to_element(startdate,insd).perform()

    

        browser.implicitly_wait(4)

    

        # 다음 버튼을 누르기 위한 대기시간

        ac.move_to_element(enddate)

        ac.send_keys_to_element(enddate,ined).perform()

    

        term_botton=browser.find_element_by_xpath(term_botton_xpath)

        term_botton.click()

    

    #리스트 돌아가면서 수집하는함수

    def list_RepetitionCycle_function(browser,listnumber):

        main_function()

    

    #작업중인 부분

    # 반복문을 타면서 a 값을 증가 시켜야함

    try:

        list_number=8

        step_two_path='//*[@id="mainframe_ChildFrame_form_div_Work_frm_div_Work_div_Form_Div01_Grid00_body_gridrow_'+str(list_number)+'_cell_'+str(list_number)+'_2"]'

        step_two_botton=browser.find_element_by_xpath(step_two_path)

    

        stbt=step_two_botton.text

        print(stbt)

        step_two_botton.click()

    except: 

        browser.close()

    

    #참고 현재페이지에서 뒤로가기가 가능함

    browser.back()

    

    

    

    #분양공고 다운로드 받기위한 함수 1

    def upcount(browser,down_number):

        down_number=down_number+1

        return download_step(browser,down_number)

    

    #분양공고 다운로드 받기위한 함수 2

    down_number=1

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

            

    download_step(browser,down_number)

    browser.close()

        



