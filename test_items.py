
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_basket_button(browser):
    print("start test basket")
    browser.implicitly_wait(3)
    browser.get(link)
    basket_button = browser.find_element_by_xpath("//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    assert basket_button, 'there is no basket button'
    print("finish test basket")
