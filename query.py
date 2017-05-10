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
# It's a flask-sqlalchemy object representing the query itself not the results
# of the query.



# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?
# Association tables are an intermediate table between two tables but only 
# contains information about the other two tables relationship. 
# Association tables manage many to many relationships.




# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the brand_id of ``ram``.
q1 = Brand.query.filter(Brand.brand_id == 'ram').all()

# Get all models with the name ``Corvette`` and the brand_id ``che``.
q2 = Model.query.filter((Model.name=='Corvette') & (Model.brand_id=='che')).all()

# Get all models that are older than 1960.
q3 = db.session.query(Model).filter(Model.year > 1960).all()

# Get all brands that were founded after 1920.
q4 = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with ``Cor``.
q5 = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = Brand.query.filter((Brand.founded < 1950) | (Brand.discontinued != None)).all()

# Get all models whose brand_id is not ``for``.
q8 = Model.query.filter(Model.brand_id != 'for').all()


# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(y):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""
    results = db.session.query(Model.name, 
                                Brand.name, 
                                Brand.headquarters).join(Brand).filter(Model.year==y).all()

    for model in results:
        print model[0], model[1], model[2]


def get_brands_summary():
    """Prints out each brand name (once) and all of that brand's models,
    including their year, using only ONE database query."""
    results = db.session.query(Brand.name, 
                                Model.name, 
                                Model.year).join(Model).order_by(Brand.name)
    results = results.all()

    for i in range(len(results)-1):
        if results[i][0] != results[i+1][0]:
            print results[i][0]
            print '\t {}, {}'.format(results[i][1], results[i][2])

        else:
            print '\t {}, {}'.format(results[i][1], results[i][2])


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    results = Brand.query.filter(Brand.name.like('%{}%'.format(mystr)))
    return results.all()

def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    results = Model.query.filter((Model.year > start_year) & (Model.year < end_year))

    return results.all()




