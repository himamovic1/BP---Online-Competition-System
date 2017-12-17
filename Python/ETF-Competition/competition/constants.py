from competition import User, Field, Competition, Student, Role, Administrator, Result, Participation


# Database seed method
def seed(database):
    """
        Function that makes an initial database data seed
        so we could have something to work on after DB init.
    """

    # User roles are inserted first
    Role.insert_roles()

    # List of object to be added to DB
    users = []

    # Users
    s1 = Student(name='John', surname='Doe', email='john.doe@gmail.com', index_number='10000', study_year=3)
    s1.password = "demo"
    users.append(s1)

    s2 = Student(name='Demo', surname='User', email='demo@test.com', index_number='10001', study_year=2)
    s2.password = "demo"
    users.append(s2)

    s3 = Student(name='Mary', surname='Lilly', email='mary@test.com', index_number='10002', study_year=1)
    s3.password = 'student'
    users.append(s3)

    a1 = Administrator(name='Some', surname='Body', email='once@told.me', position='Assistent')
    a1.password = 'admin'
    users.append(a1)

    a2 = Administrator(name='Eddy', surname='Maiden', email='eddy@666.com', position='Professor')
    a2.password = 'admin'
    users.append(a2)

    a3 = Administrator(name='Master', surname='Yoda', email='lost@you.are', position='Professor')
    a3.password = 'admin'
    users.append(a3)

    a4 = Administrator(name='Qui Gon', surname='Gin', email='sw@all.ower', position='Professor')
    a4.password = 'admin'
    users.append(a4)

    # Fields
    fields = [
        Field(name='Baze podataka'),
        Field(name='Operativna istraživanja'),
        Field(name='Optimizacija resursa'),
        Field(name='Paralelni računarski sistemi'),
        Field(name='Multimedijalni sistemi'),
    ]

    # Competitions
    competitions = [
        Competition("Prvo takmičenje", "11.12.2018", 1),
        Competition("Drugo takmičenje", "11.01.2018", 2),
        Competition("Treće takmičenje", "01.12.2018", 3)
    ]

    # Seeding the data to db session
    data = fields + competitions + users

    for o in data:
        database.session.add(o)

    database.session.flush()

    users[1].participations.append(
        Participation(user_id=users[1].id, competition_name=competitions[0].name, competition_date=competitions[0].date)
    )
    users[1].participations.append(
        Participation(user_id=users[1].id, competition_name=competitions[1].name, competition_date=competitions[1].date)
    )
    users[1].participations.append(
        Participation(user_id=users[1].id, competition_name=competitions[2].name, competition_date=competitions[2].date)
    )
    users[4].competitions.append(competitions[1])

    database.session.flush()

    data.append(Result(participation_id=0, points_scored=10))
    data.append(Result(participation_id=1, points_scored=15))
    data.append(Result(participation_id=2, points_scored=20))
