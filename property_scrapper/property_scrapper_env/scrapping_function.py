from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


hyderabad = "https://www.99acres.com/search/property/buy/hyderabad-all?city=38&preference=S&area_unit=1&res_com=R"
delhi = "https://www.99acres.com/search/property/buy/delhi?city=1075722&keyword=delhi&preference=S&area_unit=1&res_com=R"
mumbai = "https://www.99acres.com/search/property/buy/mumbai?keyword=mumbai&preference=S&area_unit=1&budget_min=0&res_com=R&isPreLeased=N"
lucknow = "https://www.99acres.com/search/property/buy/lucknow?keyword=lucknow&preference=S&area_unit=1&budget_min=0&res_com=R&isPreLeased=N"
agra = "https://www.99acres.com/search/property/buy/agra?keyword=agra&preference=S&area_unit=1&budget_min=0&res_com=R&isPreLeased=N"
ahmedabad = "https://www.99acres.com/search/property/buy/ahmedabad?keyword=ahmedabad&preference=S&area_unit=1&budget_min=0&res_com=R&isPreLeased=N"
kolkata = "https://www.99acres.com/search/property/buy/kolkata?keyword=kolkata&preference=S&area_unit=1&budget_min=0&res_com=R&isPreLeased=N"
jaipur = "https://www.99acres.com/search/property/buy/jaipur?keyword=jaipur&preference=S&area_unit=1&budget_min=0&res_com=R&isPreLeased=N"
chennai = "https://www.99acres.com/search/property/buy/chennai?keyword=chennai&preference=S&area_unit=1&budget_min=0&res_com=R&isPreLeased=N"
bengaluru = "https://www.99acres.com/search/property/buy/bengaluru?keyword=bengaluru&preference=S&area_unit=1&budget_min=0&res_com=R&isPreLeased=N"

target_urls = [hyderabad, delhi, mumbai, lucknow, ahmedabad, kolkata, jaipur, chennai, bengaluru]

def scrape_property_data():
    driver = webdriver.Chrome()
    property_list = []

    global target_urls
    for url in target_urls:
        driver.get(url)

        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, "projectTuple__descCont")))

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        for property_element in soup.find_all('div', class_='projectTuple__descCont'):
            name = property_element.find('a').text
            cost = property_element.find('span').text
            h2 = property_element.find('h2').text
            property_type = h2[:h2.index('in')]
            city = h2[h2.rindex(',')+2:]
            area = property_element.find('span', class_='caption_subdued_medium configurationCards__cardAreaSubHeadingOne').text
            locality = h2[h2.index('in')+3:h2.rindex(',')]

            properties = {"Name": name, "Cost": cost, "Property Type": property_type,
                          "Area": area, "Locality": locality, "City": city}
            property_list.append(properties)

    driver.quit()
    return property_list
