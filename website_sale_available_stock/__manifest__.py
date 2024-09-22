# License MIT (https://opensource.org/licenses/MIT).
# Copyright 2015-2017 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# Copyright 2015 Veronika veryberry <https://github.com/veryberry>
# Copyright 2016 Ilmir Karamov <https://it-projects.info/team/ilmir-k>
# Copyright 2016 Alex Comba <https://github.com/tafaRu>
# Copyright 2016 manawi <https://github.com/manawi>
# Copyright 2016 Florent Thomas <https://github.com/flotho>
# Copyright 2017-2018 Kolushov Alexandr <https://github.com/KolushovAlexandr>
# Copyright 2020 Artem Shurshilov <shurshilov.a@yandex.ru>
{
    "name": "Sale only available products on Website",
    "summary": """Sale only available products on Website stock available quantity website""",
    "version": "13.0.2",
    "author": "EURO ODOO, Shurshilov Artem,IT-Projects LLC, Ivan Yelizariev",
    "license": "Other OSI approved licence",  # MIT
    "category": "eCommerce",
    "support": "shurshilov.a@yandex.ru",
    "website": "https://eurodoo.com",
    "images": [
        "static/description/new-column.png",
        "static/description/disable-checkout.png",
        "static/description/disable-checkout.png",
    ],
    "price": 9.00,
    "currency": "EUR",
    "depends": ["website_sale", "stock", "delivery"],
    "data": ["views/website_sale_available_views.xml"],
    "installable": True,
}
