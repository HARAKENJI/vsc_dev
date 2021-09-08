from main.models import Entry
from main import db

def init():
    entry1 = Entry(jcode = '0001', temp = '36.1')
    db.session.add(entry1)
    db.session.commit()
    entry2 = Entry(jcode = '0002', temp = '35.8')
    db.session.add(entry2)
    db.session.commit()
    entries = Entry.query.all()
    entries
