
tags_gen_page_start = dict(
    main_tags_a=".find('div', {'class': 'list-content js-cat _js-ga_view-list_catalog'}).find_all('a')",
    pagins=".find('div', {'class': 'pagination'}).find('div', {'class': 'pagin-content'})."
           "find('a', {'class': 'pagin-elem pagin-page js-last-page'}).text"
    )

tags_into_a = dict(
    name=".find('span', {'class': '_js-analytics'}).get('data-name')",
    url_individual_page=".get('href')",
    price_now=".find('div', {'class': 'bottom'}).find('div', {'class': 'price'}).find('span').text",
    discount=".find('div', {'class': 'bottom'}).find('div', {'class': 'old-price_wrap'})."
             "find('span', {'class': 'discount'}).text",
    old_price=".find('div', {'class': 'bottom'}).find('div', {'class': 'old-price_wrap'})."
              "find('span', {'class': 'old-price'}).text",
    in_stock=".find('div', {'class': 'bottom'}).find('div', {'class' : 'cart-goods-alert'}).text",
    url_small_picture=".find('div', {'class': 'top'}).find('div', {'class': 'swiper'})."
                      "find('img').get('src')"
    )

tags_indiv_page = dict(
    article=".find('div', {'class': 'product-main'}).find('div', {'class': 'product-info'})."
            "find('div', {'class': 'brief-characteristics'}).find('div', {'class': 'brief-characteristics__item'})."
            "find('span').text",
    country=".find('div', {'id': 'characteristic'}).find('div', {'class': 'list'})."
            "find_all('div', {'class': 'item'})[1].find('div', {'class': 'right'}).find('a').text",
    size=".find('div', {'class': 'product-main'}).find('div', {'id': 'main-info'})."
         "find_all('div', {'class': 'brief-characteristics__item'})[1].find('span').text",
    unit_of_value=".find('div', {'id': 'main-info'}).find('div', {'class': 'price'}).text[-9:]"
    )

tags_price_individ_page = dict(
    price_now=".find('div', {'class': 'product-main'}).find('div', {'id': 'main-info'})."
              "find('div', {'class': 'price'}).find('span').text",
    price_with_discount=".find('div', {'class': 'product-main'}).find('div', {'id': 'main-info'})."
                        "find('div', {'class': 'price _color-red'}).find('span').text",
    old_price=".find('div', {'class': 'product-main'}).find('div', {'id': 'main-info'})."
              "find('div', {'class': 'old-price_wrap'}).find('span',{'class': 'old-price'}).text",
    discount=".find('div', {'class': 'product-main'}).find('div', {'id': 'main-info'})."
             "find('div', {'class': 'old-price_wrap'}).find('span',{'class': 'discount'}).text",
    )
