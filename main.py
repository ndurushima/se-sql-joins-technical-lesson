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


# select all records in orderdetails and products and join them on productCode with the USING() clause, and return the first 10 records:
q = """
SELECT *
 FROM orderdetails
   JOIN products
     USING(productCode)
 LIMIT 10;
"""
print(pd.read_sql(q, conn))


# The following query produces the same result as the previous ones, using aliases od and p for orderdetails and products, respectively:
q = """
SELECT *
 FROM orderdetails AS od
   JOIN products AS p
     ON od.productCode = p.productCode
 LIMIT 10;
"""
print(pd.read_sql(q, conn))


# select all records from products and join them with all records in orderdetails on productcode using LEFT JOIN, then execute the query and store it in a dataframe named df:
q = """
SELECT *
 FROM products
   LEFT JOIN orderdetails
     USING(productCode);
"""
df = pd.read_sql(q, conn)

print("Number of records returned:", len(df))
print("Number of records where order details are null:", len(df[df.orderNumber.isnull()]))

print(df[df.orderNumber.isnull()])


#join customers using the alias c with employees using the alias e on the foreign keys salesRepEmployeeNumber and employeeNumber, and order the result by employeeNumber, then type the code to execute the query:
q = """
SELECT *
 FROM customers AS c
      JOIN employees AS e
      ON c.salesRepEmployeeNumber = e.employeeNumber
      ORDER By employeeNumber;
"""
print(pd.read_sql(q, conn))

conn.close()