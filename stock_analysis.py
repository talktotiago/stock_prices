from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import pandas as pd

#specify chromedriver version to download and patch
import undetected_chromedriver as uc

uc.TARGET_VERSION = 87    

# or specify your own chromedriver binary (why you would need this, i don't know)

uc.install(
    executable_path='/home/tiago/Desktop/chromedriver/chromedriver',
)

opts = uc.ChromeOptions()
driver = uc.Chrome(options=opts)

stocks_to_search = ["Nike", "Johnson&Johnson", "ExxonMobil", "Petrobras", "Ambev", "Adidas", "Heineken"]
currency_chosen = "EUR"

company_name = []
stock_value = []
currency = []
average_in_points = []
average_in_percentage = [] 
stock_code = []
stock_location = []
timestamp = []

excerpt_title = []
excerpt_content = []
excerpt_key_facts = []


for i in range (0,len(stocks_to_search)):
    driver.get('https://www.google.com/search?q=stock+price '+stocks_to_search[i])
    company_name.append(driver.find_element_by_xpath('//*[@id="knowledge-finance-wholepage__entity-summary"]/div/g-card-section/div/g-card-section/div[1]/div/div').text)
    print(company_name)
    stock_value.append(driver.find_element_by_xpath('//*[@id="knowledge-finance-wholepage__entity-summary"]/div/g-card-section/div/g-card-section/div[2]/div[1]/span[1]/span/span[1]').text)
    print(stock_value)
    currency.append(driver.find_element_by_xpath('//*[@id="knowledge-finance-wholepage__entity-summary"]/div/g-card-section/div/g-card-section/div[2]/div[1]/span[1]/span/span[2]').text)
    print(currency)
    average_in_points.append(driver.find_element_by_xpath('//*[@id="knowledge-finance-wholepage__entity-summary"]/div/g-card-section/div/g-card-section/div[2]/div[1]/span[2]/span[1]').text)
    print(average_in_points)
    average_in_percentage.append(driver.find_element_by_xpath('//*[@id="knowledge-finance-wholepage__entity-summary"]/div/g-card-section/div/g-card-section/div[2]/div[1]/span[2]/span[2]/span[1]').text)
    print(average_in_percentage)
    stock_code.append(driver.find_element_by_xpath('//*[@id="knowledge-finance-wholepage__entity-summary"]/div/g-card-section/div/g-card-section/div[2]/div[2]/div/span[2]').text)
    print(stock_code)
    stock_location.append(driver.find_element_by_xpath('//*[@id="knowledge-finance-wholepage__entity-summary"]/div/g-card-section/div/g-card-section/div[2]/div[2]/div/span[1]').text)
    print(stock_location)
    timestamp.append(driver.find_element_by_xpath('//*[@id="knowledge-finance-wholepage__entity-summary"]/div/g-card-section/div/g-card-section/div[2]/div[1]/div[1]/span[1]/span[2]').text)
    print(timestamp)
    excerpt_content.append(driver.find_element_by_xpath('//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div[1]/div/div/div/span[1]').text)
    print(excerpt_content)
    excerpt_key_facts.append(driver.find_element_by_xpath('//*[@id="kp-wp-tab-overview"]/div[1]/div').text)
    print(excerpt_key_facts)

    
def Make_Excel():
    print("Gerando Excel")
    Salarios = {'Termo Utilizado': stocks_to_search,
        'Companhia' : company_name,
        'Cod Ação' :stock_code,
        'Preço': stock_value,
        'Moeda Negociada':currency,
        'Pontos': average_in_points,
        'Percentual' : average_in_percentage,
        'Bolsa' :stock_location,
        'Horário' : timestamp,
        'Texto Completo' : excerpt_key_facts,
        'Texto Paragrafo' : excerpt_content
            }
    df = pd.DataFrame(Salarios, columns = ['Companhia', 'Cod Ação', 'Preço', 'Moeda Negociada', 'Pontos', 'Percentual','Bolsa', 'Horário', 'Texto Completo', 'Texto Paragrafo'])
    df.to_excel (r'Analise.xlsx', index = False, header=True)
    print(df)

Make_Excel()
