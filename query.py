"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?
"""
Answer: The data type of the returned value is an object.
It is returning the query object. In order to obtain the specific 
row objects we need to add .all() or .one() or .first() to retrive the
result.


# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

Answer: An association table is used to resolve many to many relationship 
in the database. Its self usually does not have extra info about itself, but 
contains references to columns to the primary key of other two tables. 
"""

# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the ``id`` of "ram."
q1 = Brand.query.filter_by(brand_id='ram').first()

# Get all models with the name "Corvette" and the brand_id "che."
q2 = Model.query.filter_by(name='Corvette',brand_id='che').all()

# Get all models that are older than 1960.
q3 = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
q4 = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor."
q5 = odel.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = Brand.query.filter((Brand.discontinued != None) | (Brand.founded == 1950)).all()

# Get any model whose brand_id is not "for."
q8 = Model.query.filter(Model.brand_id != 'for').all()



# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    models = db.session.query(Model.name, Brand.name,Brand.headquarters).filter(Model.year == year).all()

    for model in models:
        print "Model Name: " + str(model[0]) +" " + "Brand Name:" + str(model[1]) + " " + "Heaquarter:" + str(model[2])


def get_brands_summary():
    """Prints out each brand name and each model name with year for that brand
    using only ONE database query."""

    brands_info = db.session.query(Brand).all()

    for brand in brands_info:
        print "Brand Name:", brand.name
        for model in brand.models:
            print '\t', model.name, model.year



def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""
    if mystr:
        brand_info = Brand.query.filter(Brand.name.like('%'+ mystr+'%')).all()
        return brand_info

    return "you entered an empty string."

def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    model_objects = Model.query.filter(Model.year >= start_year, Model.year < end_year).all()
    return model_objects

