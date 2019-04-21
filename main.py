import io,os
from app import app
from flask_sqlalchemy import SQLAlchemy
import sqlite3 as sql
from flask import jsonify,flash,request,Blueprint,g,send_from_directory,redirect,url_for,render_template,session,abort
from werkzeug import generate_password_hash, check_password_hash,secure_filename
from flask_restful import Api,Resource,fields
from passlib.hash import pbkdf2_sha256 as sha256
from marshmallow import Schema,fields as ma_fields,post_load
from flask_jwt import JWT
from werkzeug.security import safe_str_cmp
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from flask_httpauth import HTTPBasicAuth
from flask_bcrypt import Bcrypt
import jwt
import datetime
import os
from flask import Flask
import psycopg2

app=Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'




auth = HTTPBasicAuth()



@app.route('/add',methods=['POST'])
def add_user():
    try:
        _json = request.json
        ids = _json['ID']
        user_id = _json['user_id']
        vehicle_model_id = _json['vehicle_model_id']
        package_id = _json['package_id']
        travel_type_id = _json['travel_type_id']
        from_area_id = _json['from_area_id']
        to_area_id = _json['to_area_id']
        from_city_id = _json['from_city_id']
        to_city_id = _json['to_city_id']
        from_date = _json['from_date']
        to_date = _json['to_date']
        online_booking = _json['online_booking']
        mobile_site_booking = _json['mobile_site_booking']
        booking_created = _json['booking_created']
        from_lat = _json['from_lat']
        from_long = _json['from_long']
        to_lat = _json['to_lat']
        to_long = _json['to_long']
        Car_Cancellation = _json['Car_Cancellation']
        if ids  and user_id and vehicle_model_id  and request.method == 'POST':            
            con = psycopg2.connect(database = "testdb", user = "postgres", password = "pass123", host = "localhost", port = "5432")
            cur = con.cursor()
            cur.execute("INSERT INTO datasss (ID,user_id,vehicle_model_id,package_id,travel_type_id,from_area_id,to_area_id,from_city_id,to_city_id,from_date,to_date,online_booking,mobile_site_booking,booking_created,from_lat,from_long,to_lat,to_long,Car_Cancellation)  VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(ids,user_id,vehicle_model_id,package_id,travel_type_id,from_area_id,to_area_id,from_city_id,to_city_id,from_date,to_date,online_booking,mobile_site_booking,booking_created,from_lat,from_long,to_lat,to_long,Car_Cancellation))
            con.commit()
            print("data written")
            return jsonify("data entered successfully")
        else:
            print("not entered")
            return jsonify("data was not entered")

    except Exception as e:
        print(e)
        con.rollback()

    finally:
        cur.close()
        con.close()


@app.route('/datas')
def users():
    try:
        con = psycopg2.connect(database = "testdb", user = "postgres", password = "pass123", host = "localhost", port = "5432")
        cur = con.cursor()
        cur.execute("SELECT * FROM datasss")
        rows = cur.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

    finally:
        cur.close()
        con.close()


@app.route('/delete/<ids>')
def delete_user(ids):
    try:
        con = psycopg2.connect(database = "testdb", user = "postgres", password = "pass123", host = "localhost", port = "5432")
        cur = con.cursor()
        cur.execute("SELECT * FROM datasss WHERE ID = %s",(ids,))
        row = cur.fetchone()
        if(row==None):
            return jsonify('DATA DOES NOT EXIST')
        cur.execute("DELETE FROM datasss WHERE ID = %s",(ids,))
        con.commit()
        resp = jsonify('DATA deleted successfully')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cur.close()
        con.close()



@app.route('/update',methods=['POST'])
def update_user():
    try:
        _json = request.json
        ids = _json['ID']
        user_id = _json['user_id']
        vehicle_model_id = _json['vehicle_model_id']
        package_id = _json['package_id']
        travel_type_id = _json['travel_type_id']
        from_area_id = _json['from_area_id']
        to_area_id = _json['to_area_id']
        from_city_id = _json['from_city_id']
        to_city_id = _json['to_city_id']
        from_date = _json['from_date']
        to_date = _json['to_date']
        online_booking = _json['online_booking']
        mobile_site_booking = _json['mobile_site_booking']
        booking_created = _json['booking_created']
        from_lat = _json['from_lat']
        from_long = _json['from_long']
        to_lat = _json['to_lat']
        to_long = _json['to_long']
        Car_Cancellation = _json['Car_Cancellation']
        if ids  and user_id and vehicle_model_id  and request.method == 'POST':            
            con = psycopg2.connect(database = "testdb", user = "postgres", password = "pass123", host = "localhost", port = "5432")
            cur = con.cursor()
            cur.execute("SELECT * FROM datasss WHERE ID = %s",(ids,))
            row = cur.fetchone()
            if(row==None):
                return jsonify('DATA TO BE UPDATED DOES NOT EXISTS')
            cur.execute("UPDATE datasss SET vehicle_model_id = %s,package_id=%s,travel_type_id=%s,from_area_id=%s,to_area_id=%s,from_city_id=%s,to_city_id=%s,from_date=%s,to_date=%s,online_booking=%s,mobile_site_booking=%s,booking_created=%s,from_lat=%s,from_long=%s,to_lat=%s,to_long=%s,Car_Cancellation=%s  WHERE ID = %s",(vehicle_model_id,package_id,travel_type_id,from_area_id,to_area_id,from_city_id,to_city_id,from_date,to_date,online_booking,mobile_site_booking,booking_created,from_lat,from_long,to_lat,to_long,Car_Cancellation,ids))
            con.commit()
            resp = jsonify('User updated successfully')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)

    finally:
        cur.close()
        con.close()



if __name__ == "__main__":
    app.run(debug=True)
    app.secret_key = os.urandom(10)

    
