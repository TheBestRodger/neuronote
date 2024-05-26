from pyArango.connection import Connection

def make_conn_to_db(username="root", password="", db_name = "ProjectDB"):
    conn = Connection(username=username, password=password)
    db = conn[db_name]
    return db

def GetCursorToCollectionFromDB(collection = 'Fanfics'):
    db = make_conn_to_db()
    query = f'FOR doc IN {collection} RETURN doc'
    cursor = db.AQLQuery(query, rawResults=True)
    return cursor



