import cx_Oracle

dsn = cx_Oracle.makedsn('80.65.65.66', '1521', 'etflab')
con = cx_Oracle.connect(user='BP03', password='o3tUtwdn', dsn=dsn)

print(con.version)
con.close()
