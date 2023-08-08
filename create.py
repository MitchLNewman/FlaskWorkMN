from app import db, app, Person, Countries, Cities

with app.app_context():
    db.drop_all()
    db.create_all()

    testuser = Person(first_name='Grooty',last_name='Toot') # Extra: this section populates the table with an example entry
    db.session.add(testuser)
    db.session.commit()

    uk = Countries(name = 'United Kingdom') #Add example to countries table
    db.session.add(uk)
    db.session.commit()

# Here we reference the country that london belongs to useing 'country', this is what we named the backref variable in db.relationship()
    ldn = Cities(name='London', country = uk)
    mcr = Cities(name='Manchester', country = Countries.query.filter_by(name='United Kingdom').first())

    db.session.add(ldn)
    db.session.add(mcr)
    db.session.commit()

    print(f"Cities in the UK are: {uk.cities[0].name}, {uk.cities[1].name}")
    print(f"London's country is: {ldn.country.name}")
    print(f"Manchester's country is: {ldn.country.name}")