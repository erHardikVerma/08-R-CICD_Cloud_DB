import psycopg2

#conn is a connection a variable, with which i am connecting to supabase database. 
#syntax for the same is :- conn=psycopg2.connect( ) 
# psycopg2 is a library that talks with db 
# .connect() - function picks up and calls the desired db, so it require 5 variables (host, user, password, database, port) 
# 
# conn is a active connection which is reused in db whenever needed, can change it any name say :- "hardik's connection"   
table = psycopg2.connect(
    host="aws-1-ap-northeast-1.pooler.supabase.com", 
    user="postgres.bsconleyldkjrgwtzdyw", 
    password="hardik123verma", 
    database="postgres", 
    port="5432"
)

print("connected to supabase")
print(table)


