import sqlite3
import pandas as pd
conn = sqlite3.connect('data.sqlite')


q = """
SELECT *
 FROM orderdetails
      JOIN products
      ON orderdetails.productCode = products.productCode
      LIMIT 10;
"""
print(pd.read_sql(q, conn))