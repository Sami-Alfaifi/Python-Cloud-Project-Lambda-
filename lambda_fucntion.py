import mysql.connector
import json
import boto3

db = mysql.connector.connect(
        host = "database-2.cpoqmy6e2sw9.eu-north-1.rds.amazonaws.com",
        user = "admin",
        password = "",
        database = "superstore"
)

cursor = db.cursor()

query = '''
select customerID, sum(sales) as total_sales
from orders
group by customerID
order by total_sales desc
limit 10
'''

cursor.execute(query)

result = cursor.fetchall()

result_dict = {"customerID":{i: customerID for i, (customerID, total_sales) in s) in enumerate(result)}}

with open('result.json', 'w') as json_file:
        json.dump(result_dict, json_file)

cursor.close()
db.close()

s3 = boto3.client('s3', aws_access_key_id='', aws_secret_acret_access_key='')

s3.upload_file('result.json', 'samialfifi', 'input/result.json')

