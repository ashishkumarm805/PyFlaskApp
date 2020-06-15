def update(db,name,address):
    for i in db:
        i.account=name
        i.address=address
        return (db)