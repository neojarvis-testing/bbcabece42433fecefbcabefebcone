import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="class")
def driver(request):
    chrome_options = Options()
    driver = webdriver.Remote(
        command_executor="http://localhost:4444",
        options=chrome_options
    )
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("driver")
class TestApp:

    def test_case1(self):
        self.driver.get("https://www.example.com/")
        assert self.driver.title == "Example Domain"
        
    def test_case2(self):
        self.driver.get("https://www.google.com/")
        assert self.driver.title == "Google"
    
    def test_case3(self):
        self.driver.get("https://www.facebook.com")
        print(self.driver.title)
        assert self.driver.title == "Facebook - log in or sign u"
