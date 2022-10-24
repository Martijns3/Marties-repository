# Models go here

from peewee import *

db = SqliteDatabase("betsy-webshop.db")

class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    user_name = CharField(unique=True)
    user_address = CharField()
    user_postcode = CharField()
    user_city = CharField()
    user_country = CharField()


class Billinginfo(BaseModel):
    user_id = ForeignKeyField(User)
    card_type = CharField()
    card_number = FixedCharField(max_length=16)
    exp_date = CharField()
    cvc = FixedCharField(max_length=3)


class Tags(BaseModel):
    tag_name = CharField(unique=True)


class Product(BaseModel):
    product_owner = ForeignKeyField(User)
    product_name = CharField()
    product_description = CharField()
    product_ppu = DecimalField(
        decimal_places=2,
        auto_round=True,
        rounding="ROUND_HALF_UP",
        constraints=[Check("product_ppu >= 0")],
    )
    product_quantity = IntegerField(constraints=[Check("product_quantity >= 0")])
    tags = ManyToManyField(Tags)

    class Meta:
        indexes = ((("product_owner_id", "product_name"), True),)


class Transactions(BaseModel):
    product_id = ForeignKeyField(Product)
    user_id = ForeignKeyField(User)
    quantity = IntegerField(constraints=[Check("quantity > 0")])


Product_tag = Product.tags.get_through_model()