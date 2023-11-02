from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from pprint import pprint


from .scrapper import Scrapper, FindElement, ExtractElementToHTML, ExtractContentPageByUrl, ExtractAllDataWithEngine
from .parser import ParserHtml
from .data_frame import *

scrapper = Scrapper(webdriver=webdriver.Firefox)

content_page_by_url = ExtractContentPageByUrl(driver=scrapper.driver)
content_page_by_url.execute(url="https://ge.globo.com/futebol/brasileirao-serie-a/")

sleep(2)

find_element = FindElement(driver=scrapper.driver) 
element = find_element.execute(by=By.XPATH, value="/html/body/div[2]/main/div[2]/div/section[1]/article/section[1]")

extract_element_to_html = ExtractElementToHTML()  
html_content = extract_element_to_html.execute(element=element)

parser = ParserHtml(engine=BeautifulSoup)
engine = parser.execute(html_content=html_content)

extract_all_data = ExtractAllDataWithEngine(engine=engine)
tables = extract_all_data.execute(_type="table")

data_frame_reader = DataFrameReader(tables)
dataframes = data_frame_reader.read_dataframes()

data_frame_concatenator = DataFrameConcatenator()
df = data_frame_concatenator.concat_dataframes(dataframes, axis=1)

column_remover = DataFrameColumnRemove()
df = column_remover.remove_columns(df, ['Classificação.2', 'ÚLT. JOGOS'])

slicer = DataFrameSlicer()
df = slicer.slice_column(df, 'Classificação.1', -3)

scrapper.driver.close()