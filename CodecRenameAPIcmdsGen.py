# Desired Output format:
#xconfiguration SIP Authentication UserName: "lhr16-15.eventscart"
#xconfiguration SIP DisplayName: "LHR16-15.EventsCart"
#xconfiguration SIP URI: "lhr16-15.eventscart@haystack.amazon.com"
#xconfiguration SystemUnit Name: "LHR16-15.EventsCart"
#xconfiguration SIP Authentication Password: "123456789123456789123456789="


import csv
import sys

with open('provisioning-results-SIP.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        UserID = row['User ID']
        UserIDCaps = row['User ID'].upper()
        SIPAuthPassword = row['SIP Auth Password']
        sys.stdout = open(UserIDCaps + ".txt",'wt')
        print("xconfiguration SIP Authentication UserName: \"" + UserID + "\"")
        print("xconfiguration SIP DisplayName: \"" + UserIDCaps + "\"")
        print("xconfiguration SIP URI: \"" + UserID + "@haystack.amazon.com\"")
        print("xconfiguration SystemUnit Name: \"" + UserIDCaps + "\"")
        print("xconfiguration SIP Authentication Password: \"" + SIPAuthPassword + "\"")
        print()
