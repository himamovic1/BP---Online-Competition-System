from competition import db, create_app

if __name__ == '__main__':
	app = create_app('development')

	with app.app_context():
		ctx = app.test_request_context('/')
		ctx.push()

		print("DATABASE: " + app.config.get('SQLALCHEMY_DATABASE_URI'))
		ans = input("Do you want to destroy existing database and create new database?")

		if ans not in ('Y', 'y'):
			exit()

		db.drop_all()
		db.create_all()
		print("End")