from competition import User, Field, Competition


def seed(database):
    """
        Function that makes an initial database data seed
        so we could have something to work on after DB init.
    """

    # List of object to be added to DB
    data = []

    # Users
    u1 = User(name='John', surname='Doe', email='john.doe@gmail.com')
    u1.password = "1DvaTri!"
    data.append(u1)

    u2 = User(name='Demo', surname='User', email='demo@test.com')
    u2.password = "demo"
    data.append(u2)

    # Fields
    data += [
        Field(name='Baze podataka'),
        Field(name='Operativna istraživanja'),
        Field(name='Optimizacija resursa'),
        Field(name='Paralelni računarski sistemi'),
        Field(name='Multimedijalni sistemi'),
    ]

    # Competitions
    data.append(Competition("Prvo takmičenje", "11.12.2018", 1))
    data.append(Competition("Drugo takmičenje", "11.01.2018", 1))
    data.append(Competition("Treće takmičenje", "01.12.2018", 1))

    # Seeding the data to db session
    for o in data:
        database.session.add(o)
