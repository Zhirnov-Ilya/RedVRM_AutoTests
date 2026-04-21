import pytest
from pages.red_vrm_page import RedVrmPage

class TestRedVrm:
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page = RedVrmPage(driver)
        self.page.open()
    
    def test_page_title(self):

        assert "РЕД ВРМ" in self.page.get_page_title()
    
    def test_demo_popup(self):

        self.page.click_demo_button()
        assert self.page.is_demo_popup_visible()
        assert self.page.get_popup_title() == "Заявка на демо-версию"
        
        self.page.close_popup()
        assert not self.page.is_demo_popup_visible()
    
    def test_faq_accordion(self):

        self.page.scroll_to_faq()
        self.page.click_faq_question()
        assert self.page.is_faq_answer_visible()
    
    def test_tabs_switch(self):

        self.page.scroll_to_tabs()
        self.page.click_client_tab()
        self.page.click_agent_tab()
    
    @pytest.mark.parametrize("email", [
        "test@mail.ru",
        "invalid-email",
        "user@company.com"
    ])
    def test_form_fill_email(self, email):

        self.page.scroll_to_form()
        self.page.fill_name("Тест")
        self.page.fill_email(email)
        
        assert self.page.get_email_value() == email