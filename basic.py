from app import db, Admins, Sites

def add_admins():
    yonathan = Admins(firstName='Yonathan', lastName='Shtrum')
    ortal = Admins(firstName='Ortal', lastName='Levi')
    db.session.add_all([yonathan,ortal])
    db.session.commit()
    return Admins.query.all()

# print(Admins.query.all())
#yonatan = Admins.query.filter_by(firstName='Yonathan').first()
# print(yonatan.lastName, yonatan.id)


def add_site():
    TROT = Sites(name="TROT", sysadmin_id="1")
    db.session.add(TROT)
    db.session.commit()


#add_admins()
add_site()