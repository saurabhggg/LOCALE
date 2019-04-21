import psycopg2

conn = psycopg2.connect(database='testdb', user = 'postgres', password = 'pass123', host = 'localhost', port = '5432')

print ("Opened database successfully")

cur = conn.cursor()
cur.execute('''CREATE TABLE datasss
      (ID INT PRIMARY KEY     NOT NULL,
      user_id           TEXT    NOT NULL,
      vehicle_model_id           TEXT    NOT NULL,
      package_id           TEXT    ,
      travel_type_id           TEXT    ,
      from_area_id           TEXT   ,
      to_area_id           TEXT    ,
      from_city_id           TEXT   ,
      to_city_id           TEXT    ,
      from_date           TEXT   ,
      to_date           TEXT ,
      online_booking           TEXT    ,
      mobile_site_booking          TEXT    ,
      booking_created           TEXT   ,
      from_lat           TEXT    ,
      from_long           TEXT   ,
      to_lat           TEXT    ,
      to_long           TEXT   ,
      Car_Cancellation           TEXT );''')

print ("Table created successfully")

conn.commit()
conn.close()
