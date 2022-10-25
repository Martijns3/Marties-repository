from models import *

def populate_test_database():

    db.connect()
    db.create_tables(
        [
            User,
            Tags,
            Product,
            Transactions,
            Billinginfo,
            Product_tag,
        ]
    )

    tags_data = [

        ("t-shirt"),
        ("summer"),
        ("winter"),
        ("spring"),
        ("fall"),
        ("white"),
        ("black"),
        ("red"),
        ("blue"),
        ("green"),
        ("yellow"),
        ("coat"),
        ("trousers"),
        ("men"),
        ("women"),
        ("kids"),
        ("sweater"),
        ("scarf"),
    ]

    user_data = [
        (("Max Maxxton", "74 Avenir Avenue", "90210", "Beverly Hills", "USA"),
            ("VISA", 4929699617162085, "9/2027", 932),
        
            [("t-shirt-blue", "blue t-shirt for men", 10.89, 4, ("men","blue", "summer","fall", "spring","t-shirt")),
            ("trousers","black skinny jeans for men", 29.99, 3, ("black", "men","trousers" )),
            ]
            ),
        (("Knut Stigmarsson","Hellsgatan 12", "7548", "Stocholm", "Sweden"),
            ("VISA", 4024007123461724, "9/2026", 160),
            
            [("yellow coat kids", "yellow coat for small child", 15.00, 1, ("kids","yellow", "winter","coat")),
            ("sweater","nice red sweaters for women", 39.99, 2, ("red", "women","sweater" )),
            ]
            ),
        (("Arie Appelstra","Kerkstraat 13", "1013CM", "Amsterdam", "Netherlands"),
            ("VISA", 4485579342500948, "12/2022", 741),
            
            [("t-shirt", "black t-shirt for men", 9.99, 6, ("men","black", "summer","fall", "spring","t-shirt")),
            ("woolen scarf","woolen scarf for men and women", 12.99, 4, ("men", "women","scarf" )),
            ]
            ),
        (("Alfred Alfredson","Alfredslane 123", "3267AB", "Rotterdam", "Netherlands"), 
            ("VISA", 4916120111034311, "2/2028", 340),
            [ 
            ]),
        (("Bert Bertson","Bertslane 231", "9432", "Genk", "Belgium"),
            ("VISA", 4532456108228738, "1/2025", 221),
            [
            ]),
        
        (("Candice Candicedottir","Ringbaan 1", "3245", "Antwerp", "Belgium"), 
            ("VISA", 4024007105785629, "3/2024", 660),
            [
            ]),
            ]

    transactions = [(2,1,1),(2,2,2), (5, 6, 2), (2,4,1), (1,3,1)]
    
    tag_map = {
        n: Tags.create(
            tag_name=n,
        )
        for n in tags_data
    }

    for user , billing_info, products in user_data:
        user = User.create(
            user_name = user[0],
            user_address = user[1],
            user_postcode = user[2],
            user_city = user[3],
            user_country = user[4],
        )
        
        billing_info = Billinginfo.create(
            user_id = user,
            card_type = billing_info[0],
            card_number = billing_info[1],
            exp_date = billing_info[2],
            cvc = billing_info[3],
            )
        
        for product_data in products:
            product = Product.create(
            product_owner= user,
            product_name = product_data[0],
            product_description = product_data[1],
            product_ppu = product_data[2],
            product_quantity = product_data[3],
            )

            product_tags = [tag_map[p] for p in product_data[4]]
            product.tags.add(product_tags)

    for transaction in transactions:
        transaction = Transactions.create(
            product_id = transaction[0],
            user_id = transaction[1],
            quantity = transaction[2],
        )
        
    db.close()
    
# populate_test_database()

#__TEST FUNCTIONS________________________________________________________________

def product_list():
    prod = Product.select()
    for p in prod:
        print(p.id, p.product_name, p.product_description, p.product_owner.user_name, p.product_quantity)
product_list()

def transactions_list():
    tr = Transactions.select()
    for p in tr:
        print(p.user_id.user_name, p.product_id.product_name, p.quantity)
# transactions_list()

def tags_list():
    tags = Tags.select()
    for tg in tags:
        print(tg.tag_name)
# tags_list()

def tags_per_product():
    for pr in Product.select():
        for x in pr.tags:
            print( x.tag_name, pr.product_name)
# tags_per_product()

def user_info_list():
    user = User.select()
    for p in user:
        print(p.id, p.user_name, p.user_address, p.user_city, p.user_postcode)
# user_info_list()

def show_billinginfo():
    for b in Billinginfo:
        print(b.user_id, b.card_type, b.card_number, b.exp_date, b.cvc)
# show_billinginfo()

def show_manytomany():
    for tg in Product_tag:
        print(tg.id,tg.product_id, tg.tags_id)
# show_manytomany()


