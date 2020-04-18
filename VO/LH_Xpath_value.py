
class LH_Xpath_value:

    # 환경 설정
    def inviromentSetting(self):
        self.chromedriver ='C:/Users/seo/Desktop/chromedriver/chromedriver.exe'
        self.url ='http://apply.lh.or.kr/'
    
    
    # 팝업 xpath
    def popup(self):
        self.popup_xpath1='//*[@id="mainframe_ChildFrame_sys_open_pop45_form_Button02ImageElement"]/img'

        self.popup_xpath2='//*[@id="mainframe_ChildFrame_sys_open_pop6_form_Button02ImageElement"]/img'

        self.popup_xpath3='//*[@id="mainframe_ChildFrame_sys_open_pop44_form_Button02ImageElement"]/img'

    

    # 1.분양 2.임대 3.신혼부부 구분
    def houseType(self):
        self.sale_xpath='//*[@id="mainframe_ChildFrame_form_div_Work_frm_div_Work_div_Form_btn_HsInfoListImageElement"]/img'

        self.retal_xpath='//*[@id="mainframe_ChildFrame_form_div_Work_frm_div_Work_div_Form_btn_LsHsInfoList"]/div[2]'

        self.dreamtown_xpath='//*[@id="mainframe_ChildFrame_form_div_Work_frm_div_Work_div_Form_btn_NwhtInfoList"]/div[2]'


    # 날짜 조건을 받기 위한 xpath
    def DateType(self):
        self.startdate_xpath='//*[@id="mainframe_ChildFrame_form_div_Work_frm_div_Work_div_Form_Div01_Div01_div_Calendar_mae_SearchStartDate"]'

        self.enddate_xpath='//*[@id="mainframe_ChildFrame_form_div_Work_frm_div_Work_div_Form_Div01_Div01_div_Calendar_mae_SearchEndDate"]'

        self.term_botton_xpath='//*[@id="mainframe_ChildFrame_form_div_Work_frm_div_Work_div_Form_Div01_Div01_btn_Search"]/div'
