import unittest, base64, time, os, subprocess, pytz, allure, json, urllib3, behave, behave_html_formatter
from behave import *
from support.ambiente import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'que estou no site da google')
def open_google(context):
    context.driver = webdriver.Edge()
    context.driver.get('https://www.google.com/gmail/about/')
    time.sleep(3)
    #context.driver.find_element_by_class_name('button dropdown__options__option button--low').click()
    print('teste1')
    elemento = context.driver.find_element(By.XPATH, "/html/body/main/div[1]/div/div/div/div/div[1]/div[3]/div[1]")
    elemento.click()
    elemento2 = elemento.find_element(By.XPATH, "/html/body/main/div[1]/div/div/div/div/div[1]/div[3]/div[1]/details/div/a[1]" )
    elemento2.click()
    inputName = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section/div/div/div/div[1]/div[1]/div/div[1]/div/div[1]/input")
    inputName.send_keys("Luciano")
    time.sleep(60)

@given(u'tento criar um usuario com sucesso')
def step_impl(context):
    ...

@then(u'acesso minha caixa de entrada')
def step_impl(context):
    ...


@then(u'finaliza o fluxo')
def step_impl(context):
    ...