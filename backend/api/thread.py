from threading import Lock
from backend import socketio
from backend.db.service.query import *
import backend.api.socket as socket
from backend.api.crawling import *
from threading import Thread
import time

gateway_thread = None
airpressure_thread = None
thread_check = True
thread_lock = Lock()
def setGatewayLog(gid, gpid, check):
  print("[method] setGatewayLog")
  updateGatewaysConnect(gid, check)
  insertGatewaysLog(gid, check)
  if check == False:
    # dev =  selectBandsConnectGateway(gid)
    # for b in dev:
    #   insertConnectBandLog(b.id, 0)
    #   updateConnectBands(b.id, 0)
    gateway={
      "panid": gpid,
      "bandnum": 0,
      "connectstate": False
    }
    socket.socket_emit('gateway_connect', gateway)
    
# def gatewayCheck():
#   while True:
#     socketio.sleep(120)
#     # socketio.sleep(60)
#     print("gatewayCheck start")
#     try:
#       gateways = selectGatewayAll()
#       for g in gateways:
#         updateGatewaysThreadCheck(g.id)
#       gateways = selectGatewayAll()
#       for g in gateways:
#         time1 = g.connect_check_time.replace(tzinfo=None)
#         time2 = datetime.datetime.now(timezone('Asia/Seoul')).replace(tzinfo=None)
#         print(g.id, g.connect_check_time)
#         if (time2-time1).seconds > 120:
#           print(g.id, g.connect_state)
#           if g.connect_state==1 :
#               setGatewayLog(g.id, g.pid, False)
#           else:
#             dev = selectGatewayLog(g.id)
#             if dev is None:
#               setGatewayLog(g.id, g.pid, False)

#     except Exception as e:
#       print(e)
def gatewayCheck():
    # socketio.sleep(60)
    print("gatewayCheck start")
    time = datetime.datetime.now(timezone('Asia/Seoul')).replace(tzinfo=None)
    print(time)
    try:
      gateways = selectGatewayAll()
      for g in gateways:
        time1 = g.connect_check_time.replace(tzinfo=None)
        time2 = datetime.datetime.now(timezone('Asia/Seoul')).replace(tzinfo=None)
        print(g.id, g.connect_check_time)
        if (time2-time1).seconds > 120:
          print(g.id, g.connect_state)
          if g.connect_state==1 :
              setGatewayLog(g.id, g.pid, False)
          else:
            dev = selectGatewayLog(g.id)
            if dev is None:
              setGatewayLog(g.id, g.pid, False)

    except Exception as e:
      print(e)
# def gatewayCheck():
#     time.sleep(20)
#     # socketio.sleep(60)
#     print("gatewayCheck start")
#     try:
#       gateways = selectGatewayAll()
#       # for g in gateways:
#       #   updateGatewaysThreadCheck(g.id)
#       # gateways = selectGatewayAll()
#       for g in gateways:
#         time1 = g.connect_check_time.replace(tzinfo=None)
#         time2 = datetime.datetime.now(timezone('Asia/Seoul')).replace(tzinfo=None)
#         print(g.id, g.connect_check_time)
#         if (time2-time1).seconds > 120:
#           print(g.id, g.connect_state)
#           if g.connect_state==1 :
#               setGatewayLog(g.id, g.pid, False)
#           else:
#             dev = selectGatewayLog(g.id)
#             if dev is None:
#               setGatewayLog(g.id, g.pid, False)

#     except Exception as e:
#       print(e)
#     gatewayCheckThread()

def getAirpressureTask():
  while True:
    socketio.sleep(20)
    # socketio.sleep(60)
    print("getAltitud start")
    dev = selectGatewayAll()
    d = datetime.datetime.now(timezone('Asia/Seoul'))
    urldate = str(d.year)+"."+str(d.month)+"."+str(d.day)+"."+str(d.hour)
    trtemp, atemp = getAirpressure(urldate)
    if trtemp != 0 :
      for g in dev:
        updateGatewaysAirpressure(g.id, searchAirpressure(trtemp, atemp, g.location))

# def getAirpressureTask():
#     print("getAltitud start")
#     dev = selectGatewayAll()
#     d = datetime.datetime.now(timezone('Asia/Seoul'))
#     urldate = str(d.year)+"."+str(d.month)+"."+str(d.day)+"."+str(d.hour)
#     trtemp, atemp = getAirpressure(urldate)
#     if trtemp != 0 :
#       for g in dev:
#         updateGatewaysAirpressure(g.id, searchAirpressure(trtemp, atemp, g.location))

def gatewayCheckThread():
  global gateway_thread
  print("gateway_check")
  with thread_lock:
    if gateway_thread is None:
      gateway_thread = socketio.start_background_task(gatewayCheck)

# def gatewayCheckThread():
#   thread = Thread(target = gatewayCheck)
#   thread.daemon = True
#   thread.start()

def getAirpressureThread():
  global airpressure_thread
  global thread_check
  thread_check = False
  print("airpressure_check")
  with thread_lock:
    if airpressure_thread is None:
      airpressure_thread = socketio.start_background_task(getAirpressureTask)

def threadCheck():
  global thread_check
  return thread_check
