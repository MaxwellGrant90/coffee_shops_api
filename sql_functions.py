from sqlalchemy import create_engine, text
from sqlalchemy import insert



username = 'dev'
password = ''
hostname = ''
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
                    'type': result[2], 'rating': result[3], 
                    'review': result[4], 'price': result[5], 
                    'delivery': result[6], 'dinein': result[7],
                     'takeout': result[8], 'country': result[9], 
                     'area_code': result[10]}
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
        record = {'id': result[0], 'name': result[1], 
                    'type': result[2], 'rating': result[3], 
                    'review': result[4], 'price': result[5], 
                    'delivery': result[6], 'dinein': result[7],
                     'takeout': result[8], 'country': result[9], 
                     'area_code': result[10]}
        table.append(record)
    return table
