import sqlite3
import pandas as pd
conn = sqlite3.connect('data.sqlite')

# select all records from orderdetails and products and join them using their common key productCode and display the first 10.
q = """
SELECT *
 FROM orderdetails
      JOIN products
      ON orderdetails.productCode = products.productCode
      LIMIT 10;
"""
print(pd.read_sql(q, conn))


# select all records from orderdetails and display the first 10:
q = """
SELECT *
 FROM orderdetails
 LIMIT 10;
"""
print(pd.read_sql(q, conn))


# select all records from products and display the first 10:
q = """
SELECT *
 FROM products
 LIMIT 10;
"""
print(pd.read_sql(q, conn))