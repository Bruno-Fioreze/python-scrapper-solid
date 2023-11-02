class Scrapper:
    def __init__(self, webdriver):
        self.driver = webdriver()

class ExtractContentPageByUrl:
    def __init__(self, driver):
        self.driver = driver

    def execute(self, url):
        return self.driver.get(url)

class FindElement:
    def __init__(self, driver):
        self.driver = driver

    def execute(self, by, value):
        element = self.driver.find_element(by, value)
        return element

class ExtractElementToHTML:
    def html(self, element):
        return element.get_attribute('outerHTML') 


class ExtractAllDataWithEngine:
    def __init__(self, engine):
        self.engine = engine

    def execute(self, _type):
        return self.engine.find_all(_type)