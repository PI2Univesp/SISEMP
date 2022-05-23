import psycopg2

connection_db = psycopg2.connect(
    host='ec2-52-6-29-180.compute-1.amazonaws.com',
    database='de874qgpim8kg1',
    user='zcssdletmyznxc',
    password='b88b81d4f415211fb5d2226f92ac0ea5cac75ebc78975471a44ef49452f22841'
)

action_db = connection_db.cursor()

sql = 'select *  from cliente'

action_db.execute(sql)

datas = action_db.fetchall()

for r in datas:
    print(r)

action_db.close()
connection_db.close()