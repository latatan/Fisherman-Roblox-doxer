import requests as rq
import os
import sys

plat = sys.platform

class system:
    def color_init():
        if plat.startswith('win'):
            return 'cls'
        elif plat.startswith('linux'):
            return 'clear'
        elif plat.startswith('darwin'):
            return 'clear'
        else:
            return 'clear'
    class color_os:
        BLACK = "\033[0;30m"
        RED = "\033[0;31m"
        GREEN = "\033[0;32m"
        BROWN = "\033[0;33m"
        BLUE = "\033[0;34m"
        PURPLE = "\033[0;35m"
        CYAN = "\033[0;36m"
        LIGHT_GRAY = "\033[0;37m"
        DARK_GRAY = "\033[1;30m"
        LIGHT_RED = "\033[1;31m"
        LIGHT_GREEN = "\033[1;32m"
        YELLOW = "\033[1;33m"
        LIGHT_BLUE = "\033[1;34m"
        LIGHT_PURPLE = "\033[1;35m"
        LIGHT_CYAN = "\033[1;36m"
        LIGHT_WHITE = "\033[1;37m"
        BOLD = "\033[1m"
        FAINT = "\033[2m"
        ITALIC = "\033[3m"
        UNDERLINE = "\033[4m"
        BLINK = "\033[5m"
        NEGATIVE = "\033[7m"
        CROSSED = "\033[9m"
        END = "\033[0m"
    class banner:
        text = '''
         ______ _     _                                       
        |  ____(_)   | |                                      
        | |__   _ ___| |__   ___ _ __   _ __ ___   __ _ _ __  
        |  __| | / __| '_ \ / _ \ '__| | '_ ` _ \ / _` | '_ \ 
        | |    | \__ \ | | |  __/ |    | | | | | | (_| | | | |
        |_|    |_|___/_| |_|\___|_|    |_| |_| |_|\__,_|_| |_|
                                                                                                     
        '''
        thumb = f'        \033[1;31mCreator\033[0m :'
    def send_rq():
        print(f"{system.color_os.LIGHT_WHITE}Please write the keywords, so we can fetch you the format information.{system.color_os.END}")
        text = str(input(f"{system.color_os.DARK_GRAY + system.color_os.FAINT}Keywords {system.color_os.END}: "))
        print(f"{system.color_os.LIGHT_WHITE}Enter the limits' rate for sharp fetch min - 10, max - 100{system.color_os.END}")
        text2 = int(input(f"{system.color_os.DARK_GRAY}Limits {system.color_os.END}: "))
        if text2 >= 10:
            if text2 <= 100:
                args = text.replace(" ", "+")
                api = f'https://users.roblox.com/v1/users/search?keyword={args}&limit={text2}'
                print(f'''{system.color_os.BOLD + system.color_os.LIGHT_RED}I'm sending request to{system.color_os.LIGHT_WHITE} : Address = {api}{system.color_os.END}''')
                req = rq.get(api)
                return req
            else:
                print(f'{system.color_os.FAINT + system.color_os.LIGHT_RED}Max at 100 letters, retry with less than 100{system.color_os.END}')
                return False
        else:
            print(f'{system.color_os.FAINT + system.color_os.LIGHT_RED}The rate must be more than 10{system.color_os.END}')
            return False
    def list(req):
        count = 0
        data = None
        list = ['']
        for i in req.json()["data"]:
                count += 1
                data = str(i)
                print(f'{system.color_os.LIGHT_GREEN}{count} {system.color_os.LIGHT_RED + data}{system.color_os.END}')
                list.append(data)
        return list
    def id(limit, list):
        num = int(input(f"{system.color_os.BOLD+system.color_os.LIGHT_WHITE}Selection{system.color_os.END} : "))
        if num <= limit:
            print(f'{system.color_os.LIGHT_GREEN}{num} {system.color_os.LIGHT_BLUE}{list[num]}{system.color_os.END}')
        else:
            return print(f'{system.color_os.PURPLE + system.color_os.NEGATIVE}Failed to get Data : out of selections{system.color_os.END}')
    def direction(a,b):
        print(f'{system.color_os.BOLD + system.color_os.LIGHT_WHITE}Please Choose mode to fetch\n1 - selection\n2 - username\n3 - displayname{system.color_os.END}')
        core = int(input(f"{system.color_os.DARK_GRAY}Enter {system.color_os.END}:"))
        if core == 1:
            system.id(a,b)
        else:
            print('In next update')

if __name__ == '__main__':
    os.system(system.color_init())
    print(f'{system.color_os.BOLD+system.color_os.LIGHT_CYAN}{system.banner.text }{system.banner.thumb + system.color_os.LIGHT_WHITE + rq.get("https://raw.githubusercontent.com/latatan/users/main/banner.txt").text}\nPlatform {system.color_os.END}: {sys.platform}')
    req = system.send_rq()
    if req:
        if req.status_code == 200:
            print(f"\nPage : {req.json()['nextPageCursor']}\n\n\n")
            list = system.list(req)
            req.close()
            system.direction(len(list), list)
        else:
            if req.status_code == 429:
                print('Check parameters or too many requests .')
            else:
                print(req.status_code, "Contact to support")

    else:
        if req.status_code == 429:
            print('code 429 : Too many requests . Please slow down ! ')
        else:
            print(f'{system.color_os.LIGHT_PURPLE + system.color_os.NEGATIVE}Failed to get Data : Rate limits (10 to 100){system.color_os.END}')

 
