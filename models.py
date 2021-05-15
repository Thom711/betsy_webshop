from peewee import *

db = SqliteDatabase('betsy.db')


class User(Model):
    name = CharField()

    class Meta:
        database = db


class User_Address(Model):
    user = ForeignKeyField(User, backref='address')
    street = CharField()
    postal_code = CharField()
    city = CharField()

    class Meta:
        database = db


class User_Billing(Model):
    user = ForeignKeyField(User, backref='billing')
    card_type = CharField()
    card_number = IntegerField()

    class Meta:
        database = db


class Product(Model):
    owner = ForeignKeyField(User, backref='products')
    name = CharField()
    description = CharField()
    price = FloatField()
    quantity = IntegerField()

    class Meta:
        database = db


class Tag(Model):
    name = CharField()

    class Meta:
        database = db


class ProductTag(Model):
    product = ForeignKeyField(Product)
    tag = ForeignKeyField(Tag)

    class Meta:
        database = db


class Transaction(Model):
    buyer = ForeignKeyField(User, backref='transactions')
    bought_product = ForeignKeyField(Product, backref='transactions')
    quantity = IntegerField()
    total_price = FloatField()
    bought_at = DateTimeField()

    class Meta:
        database = db


def init():
    connection = db.connect()

    if connection:
        print('Connected to database.')

    with db:
        db.create_tables([
            User,
            User_Address,
            User_Billing,
            Product,
            Tag,
            ProductTag,
            Transaction
        ])

        print('Created tables.')


def test_data():
    # User #1 - Betsy
    betsy = User.create(
        name='Betsy'
    )

    betsy_address = User_Address.create(
        user=betsy, 
        street='Hoofdstraat 34', 
        postal_code='1234 CD', 
        city='Amsterdam'
    )

    betsy_billing = User_Billing.create(
        user=betsy, 
        card_type='Rabobank', 
        card_number=12345678
    )

    knitted_sweater = Product.create(
        owner=betsy, 
        name='Knitted Sweater', 
        description='Warm home knitted sweater handmade by grandma Betsy',
        price=20.99,
        quantity=3
    )

    knitted_socks = Product.create(
        owner=betsy,
        name='Knitted Socks',
        description='Warm home knitted socks handmade by grandma Betsy',
        price=8.99,
        quantity=5
    )

    knitted_hat = Product.create(
        owner=betsy,
        name='Knitted Hat',
        description='Warm home knitted hat handmade by grandma Betsy',
        price=14.99,
        quantity=3
    )

    # User 2 - John
    john = User.create(
        name='John'
    )

    john_address = User_Address.create(
        user=john,
        street='Bijstraat 67b',
        postal_code='5678 AB',
        city='Leiden'
    )

    john_billing = User_Billing.create(
        user=john,
        card_type='ABN Amro',
        card_number=87654321
    )

    sausages = Product.create(
        owner=john,
        name='Sausages',
        description='Fresh sausages from the farm',
        price=1.99,
        quantity=25
    )

    steak = Product.create(
        owner=john,
        name='Steak',
        description='Fresh steak from the farm',
        price=7.45,
        quantity=10
    )

    chicken_drums = Product.create(
        owner=john,
        name='Chicken Drums',
        description='Fresh chicken drums from the farm',
        price=4.99,
        quantity=20
    )

    # User 3 - Thom
    thom = User.create(
        name='Thom'
    )

    thom_address = User_Address.create(
        user=thom,
        street='Gedempte Oude Gracht 5',
        postal_code='2010 GG',
        city='Haarlem'
    )

    thom_billing = User_Billing.create(
        user=thom,
        card_type='Bunq',
        card_number=56781234
    )

    fleece_sweater = Product.create(
        owner=thom,
        name='Fleece Sweater',
        description='Nice sweater from a shop in Bangladesh',
        price=9.99,
        quantity=5
    )

    sausages_2 = Product.create(
        owner=thom,
        name='Sausages',
        description='Fresh sausages!! Really!',
        price=2.99,
        quantity=50
    )

    drums = Product.create(
        owner=thom,
        name='Drums',
        description='A Drumkit..? Really?',
        price=1099,
        quantity=1
    )

    #Tags
    knitted = Tag.create(
        name='knitted'
    )

    fresh = Tag.create(
        name='fresh'
    )

    drums = Tag.create(
        name='drums'
    )

    farm = Tag.create(
        name='farm'
    )

    clothing= Tag.create(
        name='clothing'
    )

    food = Tag.create(
        name='food'
    )

    music = Tag.create(
        name='music'
    )

    # ProductTags
    # Betsy
    ProductTag.create(
        product=knitted_sweater,
        tag=knitted
    )

    ProductTag.create(
        product=knitted_sweater,
        tag=clothing
    )

    ProductTag.create(
        product=knitted_socks,
        tag=knitted
    )

    ProductTag.create(
        product=knitted_socks,
        tag=clothing
    )

    ProductTag.create(
        product=knitted_hat,
        tag=knitted
    )

    ProductTag.create(
        product=knitted_hat,
        tag=clothing
    )    

    # John
    ProductTag.create(
        product=sausages,
        tag=food
    )

    ProductTag.create(
        product=sausages,
        tag=fresh
    )

    ProductTag.create(
        product=sausages,
        tag=farm
    )

    ProductTag.create(
        product=steak,
        tag=food
    )

    ProductTag.create(
        product=steak,
        tag=fresh
    )

    ProductTag.create(
        product=steak,
        tag=farm
    )

    ProductTag.create(
        product=chicken_drums,
        tag=food
    )

    ProductTag.create(
        product=chicken_drums,
        tag=fresh
    )

    ProductTag.create(
        product=chicken_drums,
        tag=farm
    )

    ProductTag.create(
        product=chicken_drums,
        tag=drums
    )

    # Thom
    ProductTag.create(
        product=fleece_sweater,
        tag=clothing
    )

    ProductTag.create(
        product=sausages_2,
        tag=food
    )

    ProductTag.create(
        product=sausages_2,
        tag=fresh
    )

    ProductTag.create(
        product=drums,
        tag=drums
    )

    ProductTag.create(
        product=drums,
        tag=music
    )

    print('Database filled with test data.')