from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from parsel import Selector
from time import sleep
import csv

# arquivo csv
writer = csv.writer(open('output.csv', 'w', encoding='utf-8'))
writer.writerow(['Nome', 'Headline', 'URL'])

# Chrome diver
driver = webdriver.Chrome(r'C:\Users\Andre\Documents/chromedriver')

# LINKEDIN

# acessar LinkedIn
driver.get('https://www.linkedin.com')
sleep(1)

# clicar no botão de login
# driver.find_element_by_css_selector('a.nav__button-secondary').click()
driver.find_element_by_xpath('//a[text()="Entrar"]').click()
sleep(3)

# preencher usuario
# usuario_input = driver.find_element_by_css_selector('input#username')
usuario_imput = driver.find_element_by_name('session_key')
usuario_imput.send_keys("senaandref@gmail.com")

# preencher senha
senha_imput = driver.find_element_by_name('session_password')
senha_imput.send_keys("@uss0454")

# clicar para logar
# driver.find_element_by_css_selector("button.btn__primary--large").click()
# driver.find_element_by_xpath('//button[text()="Sign in"]').click()
senha_imput.send_keys(Keys.ENTER)
sleep(3)

# GOOGLE
driver.get('https://www.google.com')
sleep(1)

# selecionar campo de busca
# campo_busca = driver.find_element_by_xpath('//input[@name="q"]')
busca_imput = driver.find_element_by_name('q')

# fazer busca no google
busca_imput.send_keys('site: linkedin.com/in AND "data scientist" AND "São José dos Campos"')
busca_imput.send_keys(Keys.ENTER)
sleep(2)

# extrair lista de perfis
list_perfil = driver.find_elements_by_xpath('//div[@class="yuRUbf"]/a')
lista_perfil = [i.get_attribute('href') for i in list_perfil]

# extrair informacoes individuais
for perfil in lista_perfil:
    driver.get(perfil)
    sleep(4)
    response = Selector(text=driver.page_source)

    nome = response.xpath('//title/text()').extract_first().split(" | ")[0]
    headline = response.xpath('//div[@class="text-body-medium break-words"]/text()').extract_first().strip()
    url_perfil = driver.current_url

    # escrever no arquivo csv
    writer.writerow([nome, headline, url_perfil])

# sair do driver
driver.quit()
