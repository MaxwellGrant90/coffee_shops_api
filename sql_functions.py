from sqlalchemy import create_engine, text
from sqlalchemy import insert



username = 'dev'
password = 'passworddev'
hostname = '34.67.84.68'
port= '5432'
dbName = 'coffee'
uri= f'postgresql+psycopg2://{username}:{password}@{hostname}:{port}/{dbName}'
engine = create_engine(uri)
conn = engine.connect()


def all_shops():
    stmt = text('''
    SELECT id, "name", "type", rating, review,
            price, delivery, dinein, takeout,
            country, area_code
    FROM coffee.shops
    ''')
    results = conn.execute(stmt).fetchall()
    table = []
    for result in results:
        record = {'id': results[0], 'name': results[1], 
                    'type': results[2], 'rating': results[3], 
                    'review': results[4], 'price': results[5], 
                    'delivery': results[6], 'dinein': results[7],
                     'takeout': results[8], 'country': results[9], 
                     'area_code': results[10]}
        table.append(record)
    return table

def first_twenty_shops():
    stmt = text('''
    SELECT id, "name", "type", rating, review,
            price, delivery, dinein, takeout,
            country, area_code
    FROM coffee.shops
    ORDER BY rating DESC
    LIMIT 20
    ''')
    results = conn.execute(stmt).fetchall()
    table = []
    for result in results:
        record = {'id': results[0], 'name': results[1], 
                    'type': results[2], 'rating': results[3], 
                    'review': results[4], 'price': results[5], 
                    'delivery': results[6], 'dinein': results[7],
                     'takeout': results[8], 'country': results[9], 
                     'area_code': results[10]}
        table.append(record)
    return table