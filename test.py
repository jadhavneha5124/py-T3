import psycopg2
connect=psycopg2.connect(dbname="postgres", user="postgres", password="512454" ,host="localhost", port="5432")
print("connected succesfully")