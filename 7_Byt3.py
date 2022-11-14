import requests
import threading
from colorama import Fore, Back, Style


print(
        Fore.BLUE +
         """
OOOOOOOOOOOOOOOOOOOO LLLLLLLLLLLLLLLLL    IIIIIIII         IIIII CCCCCCCCCCCCCCCCCCCCCCCCCCC   YYYYYYYYYYYYYYYYYY
OOOOOO        OOOO   LLLLL     LLLLLLLLL    IIIIIIII        IIIII CCCC     CCCCCCC     CCCC     YYYYYYYYYYYYYYYY
OOOOO        OOOO    LLLLL       LLLLLLLL    IIIIIIII        IIII  CCC     CCCCCCC     CCC             YYYYYYY 
OOOO        OOOO     LLLLL        LLLLLLL     IIIIIIII      IIII    CC     CCCCCCC     CC            YYYYYYYY
          OOOO       LLLLL       LLLLLLL        IIIIIIII  IIII       C     CCCCCCC     C            YYYYYYYY 
         OOOO        LLLLL    LLLLLLLL           IIIIIIIIIIII              CCCCCCC                 YYYYYYYY
        OOOO         LLLLLLLLLLLLLLLL             IIIIIIIII                CCCCCCC                YYYYYYYY
       OOOO          LLLLLLLLLLLLLLLLLL           IIIIIIII                 CCCCCCC               YYYYYYYYY
      OOOO           LLLLL    LLLLLLLLLLL         IIIIIIII                 CCCCCCC                 YYYYYYYY 
     OOOO            LLLLL      LLLLLLLLLL        IIIIIIII                 CCCCCCC                   YYYYYYY
    OOOO             LLLLL        LLLLLLLL        IIIIIIII                 CCCCCCC                     YYYYYYY 
  OOOO               LLLLL      LLLLLLLL          IIIIIIII                 CCCCCCC                      YYYYYYY
 OOOO                LLLLL     LLLLLLLLL          IIIIIIII                 CCCCCCC                        YYYYYYY
OOOO                 LLLLL    LLLLLLLLL           IIIIIIII                 CCCCCCC               YYYYYYYYYYYYYYYYYY
OOO                  LLLLLLLLLLLLLLLLLL           IIIIIIII                 CCCCCCC               YYYYYYYYYYYYYYYYYYY                                                                       
  
     
                                          [ twitter.com/Tonycodh ]
                                          [ github.com/chegeanthony ]
        """ + Fore.RESET)

print()
print()
file = open('url.txt','r')
payloads = open('payloads.txt','r')
def Send_req(url,payload):
    #while url[-1] != '=':
     #   url = url[:-1]
    url = url.replace("=",f"={payload}")

    try:

        res = requests.get(url)
        if payload in res.text:
           print(Fore.GREEN +'XSS Found   -->','   ' , f"{url}" + Fore.RESET)


    except Exception as e:
        pass
file = file.readlines()
for payload in payloads:
    for url in file:
        url = url.strip('\n')
        payload = payload.strip('\n')
        threading.Thread(target=Send_req,args=(url,payload,)).start()
