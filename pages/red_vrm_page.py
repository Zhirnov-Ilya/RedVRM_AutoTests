from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RedVrmPage(BasePage):
    URL = "https://redvrm.red-soft.ru/"
    
    PAGE_TITLE = (By.XPATH, "//h1")
    DEMO_BUTTON = (By.XPATH, "//button[contains(text(), 'Получить демо-версию')]")
    CONSULT_BUTTON = (By.XPATH, "//button[contains(text(), 'Заказать консультацию')]")
    
    DEMO_POPUP = (By.XPATH, "//div[contains(@class, 'overlay_demo active')]")
    POPUP_TITLE = (By.XPATH, "//div[contains(@class, 'overlay_demo active')]//h3")
    POPUP_CLOSE = (By.XPATH, "//div[contains(@class, 'overlay_demo active')]//span[contains(@class, 'across')]")
    
    FAQ_QUESTION = (By.XPATH, "(//div[contains(@class, 'sub_spoiler-title')])[1]")
    FAQ_ANSWER = (By.XPATH, "(//div[contains(@class, 'sub_spoiler-content')])[1]")
    
    TAB_PROTOCOL = (By.XPATH, "//div[contains(@class, 'composition--btn') and contains(text(), 'Протокол')]")
    TAB_CLIENT = (By.XPATH, "//div[contains(@class, 'composition--btn') and contains(text(), 'Клиент')]")
    TAB_AGENT = (By.XPATH, "//div[contains(@class, 'composition--btn') and contains(text(), 'Агент')]")
    
    QUESTION_FORM = (By.XPATH, "//form[contains(@class, 'question-form')]")
    FORM_NAME = (By.XPATH, "//form[contains(@class, 'question-form')]//input[@name='form_text_6']")
    FORM_EMAIL = (By.XPATH, "//form[contains(@class, 'question-form')]//input[@name='form_email_8']")
    
    def open(self):
        self.open_url(self.URL)
        return self
    
    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)


    def click_demo_button(self):
        self.click(self.DEMO_BUTTON)
        return self
    
    def is_demo_popup_visible(self):
        return self.is_element_visible(self.DEMO_POPUP)
    
    def get_popup_title(self):
        return self.get_text(self.POPUP_TITLE)
    
    def close_popup(self):
        self.click(self.POPUP_CLOSE)
        return self
    

    def scroll_to_faq(self):
        self.scroll_to_element(self.FAQ_QUESTION)
        return self
    
    def click_faq_question(self):
        self.click(self.FAQ_QUESTION)
        return self

    def is_faq_answer_visible(self):
        return self.is_element_visible(self.FAQ_ANSWER)
 

    def scroll_to_tabs(self):
        self.scroll_to_element(self.TAB_PROTOCOL)
        return self

    def click_client_tab(self):
        self.click(self.TAB_CLIENT)
        return self
    
    def click_agent_tab(self):
        self.click(self.TAB_AGENT)
        return self

 
    def scroll_to_form(self):
        self.scroll_to_element(self.QUESTION_FORM)
        return self
    
    def fill_name(self, name):
        self.type_text(self.FORM_NAME, name)
        return self
    
    def fill_email(self, email):
        self.type_text(self.FORM_EMAIL, email)
        return self
    
    def get_name_value(self):
        return self.find_element(self.FORM_NAME).get_attribute("value")
    
    def get_email_value(self):
        return self.find_element(self.FORM_EMAIL).get_attribute("value")