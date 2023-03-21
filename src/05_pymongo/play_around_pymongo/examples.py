import pymongo

conn_str = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn_str) # equivalent of open terminal session

# can be anythins client.nazwa_bazy
db = client.the_small_bookstore

if db.books.count_documents({}) == 0:
    print("Inserting data")
    # insert some data...
    r = db.books.insert_one({'title': 'The third book', 'isbn': '73738584947384'})
    print(r, type(r))
    r = db.books.insert_one({'title': 'The forth book', 'isbn': '181819884728473'})
    print(r.inserted_id)
else:
    print("Books already inserted, skipping")

books_count = db.books.count_documents({})
print(f"There are {books_count} books in database")

# in python we gain basic dict
book = db.books.find_one({'isbn': '73738584947384'})
print(book, type(book))

# Sample editing document
book['favorited_by'] = []
book['favorited_by'].append(100)
db.books.update_one({'_id': book.get('_id')}, {"$set": book})

book = db.books.find_one({'isbn': '73738584947384'})
print(book)

# Edit without getting whole object from document -> use special operators $addToSet
db.books.update_one({'isbn': '181819884728473'}, {'$addToSet': {'wwwwwww_by': 120}})
book = db.books.find_one({'isbn': '181819884728473'})
print(book)

