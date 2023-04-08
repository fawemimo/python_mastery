from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://github.com')

signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()


username_box = browser.find_element_by_id('login_field')
username_box.send_keys('f.owolabi81')

password_box = browser.find_element_by_id('password')
password_box.send_keys('todayisweer')

password_box.submit()

assert 'f.owolabi' in browser.page_source

profile_link = browser.find_element_by_class_name('user-proifil')
link_label = profile_link.get_attribute('innerHTML')

assert 'f.owol'

browser.quit()