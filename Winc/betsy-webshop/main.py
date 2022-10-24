__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import *
from thefuzz import fuzz

def main():
    print(search("sweeter"))
    
    # print(list_user_products(2))
    
    # print(list_products_per_tag(1))
    
    # add_product_to_catalog(2,("Purple sweater XXL", 
    #                 "purple sweater for men and women en werewolves", 19.245, 2, 
    #                 ("men","blue","women","summer","sweater","aLiEn")))
    
    # update_stock(6,3)
    
    # purchase_product(1,6,2)
    
    # remove_product(7)
    
    # add_user(("Stefan Helleblad", "SverigesGatan 123","12457", "Stockholm", "Sweden"),
    # ("VISA",4563543028501625,"09/24",987))
    
    # remove_user(7)
    
    pass

def search(term):

# Onderstaande code zoekt ook in de tags, maar ik kon geen zoekfunctie vinden die goed omgaat met typo's om te implementeren in de join.
    # List =[]
    # prod = Product.select().join(Product_tag).join(Tags).where(fn.Lower(Product.product_name 
    #         .contains(term))).orwhere(fn.Lower(Product.product_description 
    #         .contains(term))).orwhere(fn.lower(Tags.tag_name.contains(term)))
    # for i in prod:
    #     if i not in List: 
    #         List.append(i)
    # return List

    List = []
    prod = Product.select()     
    for p in prod:
        if(fuzz.WRatio(p.product_name.lower(), term.lower()))>60:
            if p not in List:   
                List.append(p)
        elif(fuzz.WRatio(p.product_description.lower(), term.lower()))>60:
            if p not in List:
                List.append(p)
    return List


def list_user_products(user_id):
    List =[]
    for pr in Product.select():
        if pr.product_owner.id == user_id:
            List.append(pr)
    return List


def list_products_per_tag(tag_id):
    List = [] 
    for t in Product_tag.select():
        if (t.tags_id) == tag_id:
            List.append(t.product)
    return(List)


def add_product_to_catalog(user_id, product):
    try:
        p =Product.create(product_owner = user_id,
        product_name = product[0],
        product_description = product[1],
        product_ppu = product[2],
        product_quantity = product[3],
    )
        for t in product[4]:
            t=t.lower()
            tag, created = Tags.get_or_create(tag_name=t)
            add_tag = Tags.get(Tags.tag_name == str(t))
            p.tags.add(add_tag)
        return p
    except:
        print("Product could not be added. Check if: \n-item price not negative \n-quantity not negative\n-product already exists")


def update_stock(product_id, new_quantity):
    for product in Product.select().where(Product.id==product_id):
        if new_quantity >=0:
            product.product_quantity = new_quantity
            product.save()
        else:
            print("qauntity has to be bigger than 0")


def purchase_product(product_id, buyer_id, quantity):
    try:
        pr = Product.get(Product.id == product_id)
        if pr.product_quantity >= quantity:
            try:
                Transactions.create(product_id = product_id,user_id = buyer_id,quantity = quantity)
                updated_quantity = (pr.product_quantity - quantity)
                update_stock(product_id, updated_quantity)
            except:
                print("quantity has to be bigger than zero")
        else:
            print("not enough stock")
    except:
            print("product id not in list")


def remove_product(product_ids):
    for product in Product.select().join(Product_tag).where(Product.id==product_ids):
        product.delete_instance()
    for tg in Product_tag:
        if tg.product_id == product_ids:    
            tg.delete_instance()   


## extra functies________________________________________________

### alhoewel ik in de models.py voor het cardnumber en cvc code een FixedCharField heb gebruikt, heb ik in de "add user" 
# functie een check gemaakt voor de lengte van het cvc nummer en kaart nummer. Dit, omdat ik erachter kwam dat SQlite flexibel 
# schijnt om te gaan met de aangeboden data en dus bijv ook een cardnummer van 17 cijfers accepteert.
# De info heb ik van: https://www.sqlite.org/quirks.html (3. Flexible Typing)

def add_user(user, billing_info):
    if len(str(billing_info[1]))==16:
        if len(str(billing_info[3]))==3:
            try:
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
            except:
                print("user already exists")
        else:
            print("cvc needs to have 3 digits")
    else:
        print("cardnumber needs to have 16 digits")


def remove_user(user_ids):

    for bi in Billinginfo.select().join(User).where(Billinginfo.user_id == user_ids):
        bi.delete_instance()
    for us in User:
        if us.id == user_ids:    
            us.delete_instance() 


if __name__ == "__main__":
    main()