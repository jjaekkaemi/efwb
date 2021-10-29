#!/usr/bin/python
# -*- coding: utf-8 -*-
print ("module [backend_model.database] loaded")
from datetime import datetime, timedelta

from sqlalchemy.sql.expression import true
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import random
import hashlib
from sqlalchemy import or_,and_
import os
import json
import uuid


from flask_sqlalchemy import SQLAlchemy


class DBManager:
    db = None

    @staticmethod
    def init(app):
        # print "-- DBManager init()"
        db = SQLAlchemy(app)
        DBManager.db = db

    @staticmethod
    def init_db():
        print("-- DBManager init_db()")
        db = DBManager.db
        db.drop_all()
        db.create_all()
        DBManager.insert_dummy_data()

    @staticmethod
    def clear_db():
        print("-- DBManager clear_db()")
        DBManager.db.drop_all()

    @staticmethod
    def insert_dummy_data():
        print ('insert_dummy_data')

        DBManager.insert_dummy_groups()
        DBManager.insert_dummy_users()
        DBManager.insert_dummy_users_groups()
        DBManager.insert_dummy_gateways()
        DBManager.insert_dummy_bands()
        DBManager.insert_dummy_users_gateways()
        DBManager.insert_dummy_gateways_bands()
        DBManager.insert_dummy_users_bands()
        #DBManager.insert_dummy_sensor_data()
        #DBManager.insert_dummy_event_data()
    def password_encoder(password):
        pass1 = hashlib.sha1(password).digest()
        pass2 = hashlib.sha1(pass1).hexdigest()
        hashed_pw = "*" + pass2.upper()
        return hashed_pw

    def get_random_date():
        end = datetime.utcnow()
        start = end + timedelta(days=-60)

        random_date = start + timedelta(
            # Get a random amount of seconds between `start` and `end`
            seconds=random.randint(0, int((end - start).total_seconds())),
        )

        return random_date

    def password_encoder_512(password):
        h = hashlib.sha512()
        h.update(password.encode('utf-8'))
        return h.hexdigest()

    def get_random_ip():
        ip_list = [u'28.23.43.1', u'40.12.33.11', u'100.123.234.11', u'61.34.22.44', u'56.34.56.77', u'123.234.222.55']

        return ip_list[random.randrange(0, 6)]

    def insert_dummy_users():
        print("insert_dummy_users")
        from backend.db.table_band import Users

        user = Users()
        user.uid = 1000
        user.username = "admin"
        user.password = DBManager.password_encoder_512("1234")
        user.name = "dtriple"
        DBManager.db.session.add(user)


        user = Users()
        user.uid = 2000
        user.username = "dtriple"
        user.password = DBManager.password_encoder_512("1234")
        user.name = "demo"
        DBManager.db.session.add(user)
        DBManager.db.session.commit()
    def insert_dummy_groups():
        print("insert_dummy_groups")
        from backend.db.table_band import Groups

        group = Groups()
        group.gid = 1000
        group.groupname = "dtriple"
        group.permission = 0


        DBManager.db.session.add(group)

        group = Groups()
        group.gid = 2000
        group.groupname = "demo"
        group.permission = 1


        DBManager.db.session.add(group)
        DBManager.db.session.commit()

    def insert_dummy_users_groups():
        print("insert_dummy_users_groups")
        from backend.db.table_band import UsersGroups
        users_groups = UsersGroups()
        users_groups.FK_uid = 1
        users_groups.FK_gid = 1

        DBManager.db.session.add(users_groups)
        users_groups = UsersGroups()
        users_groups.FK_uid = 2
        users_groups.FK_gid = 2

        DBManager.db.session.add(users_groups)
        DBManager.db.session.commit()
    def insert_dummy_gateways():
        print("insert_dummy_gateways")
        from backend.db.table_band import Gateways
        gateways = Gateways()
        gateways.pid = 1
        gateways.alias = "dtriple"
        gateways.ip = "192.168.0.105"
        gateways.lat = 36.1195513
        gateways.lng = 128.3444692
        DBManager.db.session.add(gateways)

        gateways = Gateways()
        gateways.pid = 2
        gateways.alias = "demo"
        gateways.ip = "192.168.0.69"
        gateways.lat = 36.1195513
        gateways.lng = 128.3444692
        DBManager.db.session.add(gateways)
        DBManager.db.session.commit()

    def insert_dummy_bands():
        print("insert_dummy_bands")
        from backend.db.table_band import Bands
        bands = Bands()
        bands.bid = "0X11010F01"
        bands.alias = "d1"
        bands.name = "h"
        bands.gender = 1
        bands.birth = "1997-09-01"
        
        DBManager.db.session.add(bands)

        bands = Bands()
        bands.bid ="0X11010F02"
        bands.alias = "d2"
        bands.name = "j"
        bands.gender = 0
        bands.birth = "1997-09-01"
        
        DBManager.db.session.add(bands)

        bands = Bands()
        bands.bid = "0X11010F03"
        bands.alias = "d3"
        bands.name = "p"
        bands.gender = 0
        bands.birth = "1997-09-01"
        
        DBManager.db.session.add(bands)

        bands = Bands()
        bands.bid = "0X11010F04"
        bands.alias = "d4"
        bands.name = "h"
        bands.gender = 0
        bands.birth = "1997-09-01"
        
        DBManager.db.session.add(bands)

        bands = Bands()
        bands.bid = "0X11010F05"
        bands.alias = "d5"
        bands.name = "k"
        bands.gender = 1
        bands.birth = "1997-09-01"
        
        DBManager.db.session.add(bands)

        bands = Bands()
        bands.bid = "0X11010F06"
        bands.alias = "d6"
        bands.name = "j"
        bands.gender = 0
        bands.birth = "1997-09-01"
        
        DBManager.db.session.add(bands)

        bands = Bands()
        bands.bid = "0X11010F07"
        bands.alias = "d7"
        bands.name = "s"
        bands.gender = 0
        bands.birth = "1997-09-01"
        
        DBManager.db.session.add(bands)

        bands = Bands()
        bands.bid = "0X11010F08"
        bands.alias = "d8"
        bands.name = "s"
        bands.gender = 0
        bands.birth = "1997-09-01"
        
        DBManager.db.session.add(bands)

        bands = Bands()
        bands.bid = "0X11010F09"
        bands.alias = "d9"
        bands.name = "r"
        bands.gender = 0
        bands.birth = "1997-09-01"
        
        DBManager.db.session.add(bands)

        bands = Bands()
        bands.bid = "0X11010F10"
        bands.alias = "d10"
        bands.name = "r"
        bands.gender = 0
        bands.birth = "1997-09-01"
        


        DBManager.db.session.add(bands)
        bands = Bands()
        bands.bid = "0X11010F11"
        bands.alias = "d11"
        bands.name = "h"
        bands.gender = 1
        bands.birth = "1997-09-01"
        
        DBManager.db.session.add(bands)

        bands = Bands()
        bands.bid = "0X11010F12"
        bands.alias = "d12"
        bands.name = "j"
        bands.gender = 0
        bands.birth = "1997-09-01"
        
        DBManager.db.session.add(bands)

        bands = Bands()
        bands.bid = "0X11010F13"
        bands.alias = "d13"
        bands.name = "p"
        bands.gender = 0
        bands.birth = "1997-09-01"
        
        DBManager.db.session.add(bands)

        bands = Bands()
        bands.bid = "0X11010F14"
        bands.alias = "d14"
        bands.name = "h"
        bands.gender = 0
        bands.birth = "1997-09-01"
        
        DBManager.db.session.add(bands)

        bands = Bands()
        bands.bid = "0X11010F15"
        bands.alias = "d15"
        bands.name = "k"
        bands.gender = 1
        bands.birth = "1997-09-01"
        
        DBManager.db.session.add(bands)

        bands = Bands()
        bands.bid = "0X11010F16"
        bands.alias = "d16"
        bands.name = "j"
        bands.gender = 0
        bands.birth = "1997-09-01"
        
        DBManager.db.session.add(bands)

        bands = Bands()
        bands.bid = "0X11010F17"
        bands.alias = "d17"
        bands.name = "s"
        bands.gender = 0
        bands.birth = "1997-09-01"
        
        DBManager.db.session.add(bands)

        bands = Bands()
        bands.bid = "0X11010F18"
        bands.alias = "d18"
        bands.name = "s"
        bands.gender = 0
        bands.birth = "1997-09-01"
        
        DBManager.db.session.add(bands)

        bands = Bands()
        bands.bid = "0X11010F19"
        bands.alias = "d19"
        bands.name = "r"
        bands.gender = 0
        bands.birth = "1997-09-01"
        
        DBManager.db.session.add(bands)

        bands = Bands()
        bands.bid = "0X11010F20"
        bands.alias = "d20"
        bands.name = "r"
        bands.gender = 0
        bands.birth = "1997-09-01"
        
        DBManager.db.session.add(bands)        
        DBManager.db.session.commit()

    def insert_dummy_users_gateways():
        print("insert_dummy_users_gateways")
        from backend.db.table_band import UsersGateways
        users_gateways = UsersGateways()
        users_gateways.FK_pid = 1
        users_gateways.FK_uid = 1
        DBManager.db.session.add(users_gateways)

        users_gateways = UsersGateways()
        users_gateways.FK_pid = 2
        users_gateways.FK_uid = 2
        DBManager.db.session.add(users_gateways)
        DBManager.db.session.commit()

    def insert_dummy_gateways_bands():
        print("insert_dummy_gateways_bands")
        from backend.db.table_band import GatewaysBands
        gateways_bands = GatewaysBands()
        gateways_bands.FK_pid = 1
        gateways_bands.FK_bid = 1
        DBManager.db.session.add(gateways_bands)

        gateways_bands = GatewaysBands()
        gateways_bands.FK_pid = 1
        gateways_bands.FK_bid = 2
        DBManager.db.session.add(gateways_bands)
        gateways_bands = GatewaysBands()
        gateways_bands.FK_pid = 1
        gateways_bands.FK_bid = 3
        DBManager.db.session.add(gateways_bands)  

        gateways_bands = GatewaysBands()
        gateways_bands.FK_pid = 1
        gateways_bands.FK_bid = 4
        DBManager.db.session.add(gateways_bands) 

        gateways_bands = GatewaysBands()
        gateways_bands.FK_pid = 1
        gateways_bands.FK_bid = 5
        DBManager.db.session.add(gateways_bands) 

        gateways_bands = GatewaysBands()
        gateways_bands.FK_pid = 1
        gateways_bands.FK_bid = 6
        DBManager.db.session.add(gateways_bands) 

        gateways_bands = GatewaysBands()
        gateways_bands.FK_pid = 1
        gateways_bands.FK_bid = 7
        DBManager.db.session.add(gateways_bands) 

        gateways_bands = GatewaysBands()
        gateways_bands.FK_pid = 1
        gateways_bands.FK_bid = 8
        DBManager.db.session.add(gateways_bands) 

        gateways_bands = GatewaysBands()
        gateways_bands.FK_pid = 1
        gateways_bands.FK_bid = 9
        DBManager.db.session.add(gateways_bands) 

        gateways_bands = GatewaysBands()
        gateways_bands.FK_pid = 1
        gateways_bands.FK_bid = 10
        DBManager.db.session.add(gateways_bands) 



        gateways_bands = GatewaysBands()
        gateways_bands.FK_pid = 1
        gateways_bands.FK_bid = 11
        DBManager.db.session.add(gateways_bands) 

        gateways_bands = GatewaysBands()
        gateways_bands.FK_pid = 1
        gateways_bands.FK_bid = 12
        DBManager.db.session.add(gateways_bands) 

        gateways_bands = GatewaysBands()
        gateways_bands.FK_pid = 1
        gateways_bands.FK_bid = 13
        DBManager.db.session.add(gateways_bands) 

        gateways_bands = GatewaysBands()
        gateways_bands.FK_pid = 1
        gateways_bands.FK_bid = 14
        DBManager.db.session.add(gateways_bands)  
        
        gateways_bands = GatewaysBands()
        gateways_bands.FK_pid = 1
        gateways_bands.FK_bid = 15
        DBManager.db.session.add(gateways_bands) 

        gateways_bands = GatewaysBands()
        gateways_bands.FK_pid = 1
        gateways_bands.FK_bid = 16
        DBManager.db.session.add(gateways_bands)  

        gateways_bands = GatewaysBands()
        gateways_bands.FK_pid = 1
        gateways_bands.FK_bid = 17
        DBManager.db.session.add(gateways_bands) 

        gateways_bands = GatewaysBands()
        gateways_bands.FK_pid = 1
        gateways_bands.FK_bid = 18
        DBManager.db.session.add(gateways_bands)   

        gateways_bands = GatewaysBands()
        gateways_bands.FK_pid = 1
        gateways_bands.FK_bid = 19
        DBManager.db.session.add(gateways_bands) 

        gateways_bands = GatewaysBands()
        gateways_bands.FK_pid = 1
        gateways_bands.FK_bid = 20
        DBManager.db.session.add(gateways_bands)                   
        DBManager.db.session.commit()
    def insert_dummy_users_bands():
        print("insert_dummy_users_bands")
        from backend.db.table_band import UsersBands

        for b in range(20):
            users_bands = UsersBands()
            users_bands.FK_bid = b+1
            if b>9 :
                users_bands. FK_uid = 2
                DBManager.db.session.add(users_bands)
                users_bands.FK_uid = 1
                DBManager.db.session.add(users_bands)
            else :
                users_bands.FK_uid = 1
                DBManager.db.session.add(users_bands)
            
            
                
        DBManager.db.session.commit()
    def insert_dummy_sensor_data():
        print("insert_dummy_sensor_data")
        from backend.db.table_band import SensorData 
        data = SensorData()
        data.FK_bid = 1
        data.start_byte = 1
        data.sample_count = 1
        data.fall_detect = 1
        data.battery_level = 1
        data.hrConfidence = 1
        data.spo2Confidence = 1
        data.hr = 50
        data.spo2 = 50

        data.motionFlag = True
        data.scdState = 0
        data.activity = 1
        data.walk_steps = 50
        data.run_steps = 50
       

        data.x = 80
        data.y = 80
        data.z = 80
        data.t = 80
        data.h = 80

        data.rssi = -32

        DBManager.db.session.add(data)

        data = SensorData()
        data.FK_bid = 1
        data.start_byte = 1
        data.sample_count = 1
        data.fall_detect = 1
        data.battery_level = 1
        data.hrConfidence = 1
        data.spo2Confidence = 1
        data.hr = 50
        data.spo2 = 50
        
        data.motionFlag = True
        data.scdState = 0
        data.activity = 1
        data.walk_steps = 50
        data.run_steps = 50
       

        data.x = 80
        data.y = 80
        data.z = 80
        data.t = 80
        data.h = 80

        data.rssi = -32     
        DBManager.db.session.add(data)

        data = SensorData()
        data.datetime = '2021-08-18 1:00'
        data.FK_bid = 1
        data.start_byte = 1
        data.sample_count = 1
        data.fall_detect = 1
        data.battery_level = 1
        data.hrConfidence = 1
        data.spo2Confidence = 1
        data.hr = 50
        data.spo2 = 50
        
        data.motionFlag = True
        data.scdState = 0
        data.activity = 1
        data.walk_steps = 50
        data.run_steps = 50
       

        data.x = 80
        data.y = 80
        data.z = 80
        data.t = 80
        data.h = 80

        data.rssi = -32     
        DBManager.db.session.add(data)

        data = SensorData()
        data.datetime = '2021-08-18 1:30'
        data.FK_bid = 1
        data.start_byte = 1
        data.sample_count = 1
        data.fall_detect = 1
        data.battery_level = 1
        data.hrConfidence = 1
        data.spo2Confidence = 1
        data.hr = 75
        data.spo2 = 50
        
        data.motionFlag = True
        data.scdState = 0
        data.activity = 1
        data.walk_steps = 50
        data.run_steps = 50
       

        data.x = 80
        data.y = 80
        data.z = 80
        data.t = 80
        data.h = 80

        data.rssi = -32     
        DBManager.db.session.add(data)

        data = SensorData()
        data.datetime = '2021-08-18 2:00'
        data.FK_bid = 1
        data.start_byte = 1
        data.sample_count = 1
        data.fall_detect = 1
        data.battery_level = 1
        data.hrConfidence = 1
        data.spo2Confidence = 1
        data.hr = 50
        data.spo2 = 50
        
        data.motionFlag = True
        data.scdState = 0
        data.activity = 1
        data.walk_steps = 50
        data.run_steps = 50
       

        data.x = 80
        data.y = 80
        data.z = 80
        data.t = 80
        data.h = 80

        data.rssi = -32     
        DBManager.db.session.add(data)
        DBManager.db.session.commit()
        
    def insert_dummy_event_data():
        from backend.db.table_band import Events
        event = Events()
        event.FK_bid = 1
        event.event = 0
        event.value = -70
        DBManager.db.session.add(event)
        event = Events()
        event.FK_bid = 1
        event.event = 1
        event.value = 70
        DBManager.db.session.add(event)
        event = Events()
        event.FK_bid = 1
        event.event = 2
        event.value = 0
        DBManager.db.session.add(event)      
        event = Events()
        event.FK_bid = 1
        event.event = 3
        event.value = 0
        DBManager.db.session.add(event)   
        event = Events()
        event.FK_bid = 1
        event.event = 4
        event.value = 0
        DBManager.db.session.add(event)  

        from backend.db.table_band import Events
        event = Events()
        event.FK_bid = 2
        event.event = 0
        event.value = -30
        DBManager.db.session.add(event)
        event = Events()
        event.FK_bid = 2
        event.event = 1
        event.value = 50
        DBManager.db.session.add(event)
        event = Events()
        event.FK_bid = 2
        event.event = 2
        event.value = 0
        DBManager.db.session.add(event)      
        event = Events()
        event.FK_bid = 2
        event.event = 3
        event.value = 0
        DBManager.db.session.add(event)  
        event = Events()
        event.FK_bid = 2
        event.event = 4
        event.value = 3
        DBManager.db.session.add(event)          
        DBManager.db.session.commit()
