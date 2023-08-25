from selenium import webdriver
from time import sleep
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pandas as pd
import os

current_dir = os.getcwd()
print(current_dir)


def brand(url, p_a, p_b):
    browser = webdriver.Chrome()
    browser.get(url)

    sleep(randint(5, 8))
    
    link_brand = []
    link_logo = []

    # click brand
    click_brand = WebDriverWait(browser, randint(7, 9)).until(
        ec.element_to_be_clickable((By.XPATH, f'/html/body/div[6]/div[{p_a}]/section/div[1]/div/div[{p_b}]')))
    click_brand.click()

    sleep(randint(3, 6))

    # manu show all stores after click brand
    manu = browser.find_elements(By.XPATH, f'/html/body/div[6]/div[{p_a}]/section/div[1]/div/div[{p_b}]/div[2]/div[1]')
    for m in manu:
        tag_link = m.find_elements(By.TAG_NAME, 'a')
        for t in tag_link:
            # get link brand
            print(t.get_attribute('href'))
            link_brand.append(t.get_attribute('href'))

            # get link logo
            tag_img = t.find_elements(By.TAG_NAME, 'img')
            if len(tag_img) > 0:
                for i in tag_img:
                    print(i.get_attribute('src'))
                    link_logo.append(i.get_attribute('src'))
            else:
                print('link logo')
                link_logo.append('')

        sleep(randint(4, 8))
    browser.close()

    return link_brand, link_logo

def product(url, class_name, p_a, p_b, p_i, p_i_bp):
    browser = webdriver.Chrome()
    browser.get(url)

    sleep(randint(3, 8))
    
    names = []
    links = []
    current_prices = []
    old_prices = []
    percent_discounts = []
    ratings = []
    brands = []
    series = []

    # click button brand
    WebDriverWait(browser, randint(7, 9)).until(
        ec.element_to_be_clickable((By.XPATH, f'/html/body/div[6]/div[{p_a}]/section/div[1]/div/div[{p_b}]'))).click()

    sleep(randint(3, 6))

    # box brand > show brand
    box_brand = browser.find_elements(By.XPATH,
                                      f'/html/body/div[6]/div[{p_a}]/section/div[1]/div/div[{p_b}]/div[2]/div[1]')
    for m in box_brand:
        # count brand sell at thegioididong
        count_brand = m.find_elements(By.CLASS_NAME, 'c-btnbox.filter-manu')

    sleep(randint(3, 5))

    # click button brand > cancel
    WebDriverWait(browser, randint(7, 9)).until(
        ec.element_to_be_clickable((By.XPATH, f'/html/body/div[6]/div[{p_a}]/section/div[1]/div/div[{p_b}]'))).click()


    # for loop click to a brand
    for t in range(1, len(count_brand) + 1):
        # click button brand
        WebDriverWait(browser, randint(7, 9)).until(ec.element_to_be_clickable(
            (By.XPATH, f'/html/body/div[6]/div[{p_a}]/section/div[1]/div/div[{p_b}]'))).click()

        sleep(randint(3, 6))

        # click a brand
        WebDriverWait(browser, randint(7, 9)).until(ec.element_to_be_clickable(
            (By.XPATH, f'/html/body/div[6]/div[{p_a}]/section/div[1]/div/div[{p_b}]/div[2]/div[1]/a[{t}]'))).click()

        sleep(randint(3, 6))

        see_results = browser.find_elements(By.CLASS_NAME, 'btn-filter-readmore.prevent.disabled')
        if len(see_results) > 0:
            # click cancel: if brand not have product
            WebDriverWait(browser, randint(7, 9)).until(ec.element_to_be_clickable(
                (By.XPATH, f'/html/body/div[6]/div[{p_a}]/section/div[1]/div/div[{p_b}]/div[2]/div[2]/a[1]'))).click()
        else:
            # click view: if brand have less than 1 product
            WebDriverWait(browser, randint(7, 9)).until(ec.element_to_be_clickable(
                (By.XPATH, f'/html/body/div[6]/div[{p_a}]/section/div[1]/div/div[{p_b}]/div[2]/div[2]/a[2]'))).click()

        box_filter = browser.find_elements(By.XPATH, f'/html/body/div[6]/div[{p_a}]/section/div[2]/div')
        # have box filter
        if len(box_filter) > 0:
            name_filter = []
            for b in box_filter:
                # count filter
                count_filter = b.find_elements(By.CLASS_NAME, 'c-btnbox')
                name_filter.append(b.text)

            filters = []
            for f in name_filter:
                filters.append(f.split('\n'))

            # for loop click filter a brand
            for i in range(1, len(count_filter) + 1):
                # click filter a brand
                WebDriverWait(browser, randint(4, 6)).until(ec.element_to_be_clickable(
                    (By.XPATH, f'/html/body/div[6]/div[{p_a}]/section/div[2]/div/a[{i}]'))).click()

                sleep(randint(2, 4))

                # find button 'see more'
                see_more = browser.find_elements(By.CLASS_NAME, 'view-more')
                while len(see_more) > 0:
                    try:
                        # click see more: if have button see more (number product more than 20 will exists button see more), and click until button 'see more' no longer appear
                        WebDriverWait(browser, randint(2, 4)).until(ec.element_to_be_clickable(
                            (By.XPATH, f'/html/body/div[6]/section/div[{p_i}]/div[2]/a'))).click()
                    except:
                        break

                items = browser.find_elements(By.CLASS_NAME, class_name)

                # for loop get data
                for a in range(1, len(items) + 1):
                    print(filters[0][i - 1])
                    series.append(filters[0][i - 1])

                    print(t)
                    if t < 10:
                        brands.append('0' + str(t))
                    else:
                        brands.append(str(t))

                        # name product
                    name = browser.find_elements(By.XPATH, f'/html/body/div[6]/section/div[{p_i}]/ul/li[{a}]/a[1]/h3')
                    for n in name:
                        print(n.text)
                        names.append(n.text)

                    # link product
                    link = browser.find_elements(By.XPATH, f'/html/body/div[6]/section/div[{p_i}]/ul/li[{a}]/a[1]')
                    for l in link:
                        print(l.get_attribute('href'))
                        links.append(l.get_attribute('href'))

                    # current price product
                    current_price = browser.find_elements(By.XPATH,
                                                          f'/html/body/div[6]/section/div[{p_i}]/ul/li[{a}]/a[1]/strong[1]')
                    if len(current_price) > 0:
                        for cp in current_price:
                            print(cp.text)
                            current_prices.append(cp.text)
                    else:
                        current_prices.append('')

                    box_p = browser.find_elements(By.XPATH,
                                                  f'/html/body/div[6]/section/div[{p_i}]/ul/li[{a}]/a[1]/div[{p_i_bp}]')
                    if len(box_p) > 0:
                        for bp in box_p:
                            # old price product
                            old_price = bp.find_elements(By.CLASS_NAME, 'price-old.black')
                            if len(old_price) > 0:
                                for op in old_price:
                                    print(op.text)
                                    old_prices.append(op.text)
                            else:
                                old_prices.append('')

                            # percent discount product
                            percent_discount = bp.find_elements(By.CLASS_NAME, 'percent')
                            if len(percent_discount) > 0:
                                for pp in percent_discount:
                                    print(pp.text)
                                    percent_discounts.append(pp.text)
                            else:
                                print('percent')
                                percent_discounts.append('')
                    else:
                        print('old price')
                        print('percent')
                        old_prices.append('')
                        percent_discounts.append('')

                    rating = browser.find_elements(By.XPATH,
                                                   f'/html/body/div[6]/section/div[{p_i}]/ul/li[{a}]/div[1]/p[2]')
                    if len(rating) > 0:
                        for r in rating:
                            print(r.text)
                            ratings.append(r.text)
                    else:
                        print('rating')
                        ratings.append('')

                WebDriverWait(browser, randint(5, 8)).until(
                    ec.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[2]/section/ul/li[2]/a'))).click()

        # don't have 'box filter'
        else:
            # button 'see more'
            see_more = browser.find_elements(By.CLASS_NAME, 'view-more')
            while len(see_more) > 0:
                try:
                    # click see more: if have button see more (number product more than 20 will exists button see more), and click until button 'see more' no longer appear
                    WebDriverWait(browser, randint(2, 4)).until(ec.element_to_be_clickable(
                        (By.XPATH, f'/html/body/div[6]/section/div[{p_i}]/div[2]/a'))).click()
                except:
                    break

            items = browser.find_elements(By.CLASS_NAME, class_name)

            # for loop get data
            for a in range(1, len(items) + 1):
                print('series')
                series.append('')

                print(t)
                if t < 10:
                    brands.append('0' + str(t))
                else:
                    brands.append(str(t))

                    # name product
                name = browser.find_elements(By.XPATH, f'/html/body/div[6]/section/div[{p_i}]/ul/li[{a}]/a[1]/h3')
                for n in name:
                    print(n.text)
                    names.append(n.text)

                link = browser.find_elements(By.XPATH, f'/html/body/div[6]/section/div[{p_i}]/ul/li[{a}]/a[1]')
                for l in link:
                    print(l.get_attribute('href'))
                    links.append(l.get_attribute('href'))

                current_price = browser.find_elements(By.XPATH,
                                                      f'/html/body/div[6]/section/div[{p_i}]/ul/li[{a}]/a[1]/strong[1]')
                if len(current_price) > 0:
                    for cp in current_price:
                        print(cp.text)
                        current_prices.append(cp.text)
                else:
                    current_prices.append('')

                box_p = browser.find_elements(By.XPATH,
                                              f'/html/body/div[6]/section/div[{p_i}]/ul/li[{a}]/a[1]/div[{p_i_bp}]')
                if len(box_p) > 0:
                    for bp in box_p:
                        # old price product
                        old_price = bp.find_elements(By.CLASS_NAME, 'price-old.black')
                        if len(old_price) > 0:
                            for op in old_price:
                                print(op.text)
                                old_prices.append(op.text)
                        else:
                            old_prices.append('')

                        # percent discount product
                        percent_discount = bp.find_elements(By.CLASS_NAME, 'percent')
                        if len(percent_discount) > 0:
                            for pp in percent_discount:
                                print(pp.text)
                                percent_discounts.append(pp.text)
                        else:
                            print('percent')
                            percent_discounts.append('')
                else:
                    print('old price')
                    print('percent')
                    old_prices.append('')
                    percent_discounts.append('')

                rating = browser.find_elements(By.XPATH, f'/html/body/div[6]/section/div[{p_i}]/ul/li[{a}]/div[1]/p[2]')
                if len(rating) > 0:
                    for r in rating:
                        print(r.text)
                        ratings.append(r.text)
                else:
                    print('rating')
                    ratings.append('')

        browser.get(url)

    sleep(randint(3, 6))

    browser.close()

    return names, current_prices, old_prices, percent_discounts, ratings, links, brands, series

def build_to_brand_data(link_brand, link_logo):
    brand = pd.DataFrame()

    brand['link'] = link_brand
    brand['link_logo'] = link_logo

    index = []
    for i in range(1, len(brand)+1):
        if i < 10:
            index.append('0' + str(i))
        else:
            index.append(str(i))

    brand['brand_id'] = index

    return brand

def build_to_product_data(genre_name, names, current_prices, old_prices, percent_discounts, ratings, links, brands, series):
    product = pd.DataFrame()

    product['product_name'] = names
    product['current_price'] = current_prices
    product['price'] = old_prices
    product['percent_discount'] = percent_discounts
    product['rating'] = ratings
    product['link'] = links
    product['brand_id'] = brands
    product['series'] = series

    genres = []
    for i in range(1, len(product)+1):
        genres.append(genre_name)

    product['genre_name'] = genres

    return product

def scrape(typeProduct, url, className):
    link_brand, link_logo = brand(url, 4, 3)
    names, current_prices, old_prices, percent_discounts, ratings, links, brands, series = (
         product(url, className, 4, 3, 3, 4))

    brand_data = build_to_brand_data(link_brand, link_logo)
    product_data = build_to_product_data(typeProduct, names, current_prices, old_prices, percent_discounts, ratings, links, brands, series)

    return brand_data, product_data
    
phone_url = 'https://www.thegioididong.com/dtdd'
phone_class_name = 'item.ajaxed.__cate_42'

laptop_url = 'https://www.thegioididong.com/laptop'
laptop_class_name = 'item.__cate_44'

# ===== crape phone
phone_brands , phones = scrape('phone', phone_url, phone_class_name)

phone_brands.to_csv(current_dir + '/../data/raw_data/phone_brand.csv', index=False)
phones.to_csv(current_dir + '/../data/raw_data/phone.csv', index=False)

# ===== crape laptop
laptop_brands , laptops = scrape('laptop', laptop_url, laptop_class_name)

laptop_brands.to_csv(current_dir + '/../data/raw_data/laptop_brand.csv', index=False)
laptops.to_csv(current_dir + '/../data/raw_data/laptop.csv', index=False)

