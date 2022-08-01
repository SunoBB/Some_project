

import random
import time


banner1 = """

\033[1;31m

 ▄ .▄ ▄▄▄·  ▄▄▄· ▄▄▄· ▄· ▄▌    ▄▄▄▄· ▪  ▄▄▄  ▄▄▄▄▄ ▄ .▄·▄▄▄▄   ▄▄▄·  ▄· ▄▌
██▪▐█▐█ ▀█ ▐█ ▄█▐█ ▄█▐█▪██▌    ▐█ ▀█▪██ ▀▄ █·•██  ██▪▐███▪ ██ ▐█ ▀█ ▐█▪██▌
██▀▐█▄█▀▀█  ██▀· ██▀·▐█▌▐█▪    ▐█▀▀█▄▐█·▐▀▀▄  ▐█.▪██▀▐█▐█· ▐█▌▄█▀▀█ ▐█▌▐█▪
██▌▐▀▐█ ▪▐▌▐█▪·•▐█▪·• ▐█▀·.    ██▄▪▐█▐█▌▐█•█▌ ▐█▌·██▌▐▀██. ██ ▐█ ▪▐▌ ▐█▀·.
▀▀▀ · ▀  ▀ .▀   .▀     ▀ •     ·▀▀▀▀ ▀▀▀.▀  ▀ ▀▀▀ ▀▀▀ ·▀▀▀▀▀•  ▀  ▀   ▀ •

\033[1;m

    Happy Birthday | Shall we play a game..?

    I like to See Ya happy... *** :)

        """

banner2 = """

\033[1;31m

 ▄  █ ██   █ ▄▄  █ ▄▄ ▀▄    ▄     ███   ▄█ █▄▄▄▄    ▄▄▄▄▀ ▄  █ ██▄   ██  ▀▄    ▄
█   █ █ █  █   █ █   █  █  █      █  █  ██ █  ▄▀ ▀▀▀ █   █   █ █  █  █ █   █  █
██▀▀█ █▄▄█ █▀▀▀  █▀▀▀    ▀█       █ ▀ ▄ ██ █▀▀▌      █   ██▀▀█ █   █ █▄▄█   ▀█
█   █ █  █ █     █       █        █  ▄▀ ▐█ █  █     █    █   █ █  █  █  █   █
   █     █  █     █    ▄▀         ███    ▐   █     ▀        █  ███▀     █ ▄▀
  ▀     █    ▀     ▀                        ▀              ▀           █
       ▀                                                              ▀

\033[1;m

    Happy Birthday | Shall we play a game..?

    I like to See Ya hacking... *** :)

        """

stream = (banner1, banner2)

print (random.choice(stream))
time.sleep(1)


def happy_birthday():

    first_name = input("\n[+] First name: ")
    first_name = " ".join(i.capitalize() for i in first_name.split())
    print( "\n")

    happy = "Happy Birthday to You.."

    print( "###########################################")
    print( "\t" + "Happy Birthday " + (first_name))
    print( "###########################################\n")
    time.sleep(2)

    for x in range(2):
        print(happy)
        time.sleep(2)
        print(happy)
        time.sleep(1.5)

        print( "Happy Birthday", first_name, "..!")
        time.sleep(1)
        print(happy + "\n")
        time.sleep(1)

        for x in range(3):
            print ("Hip Hip Hooray..!\n")
            time.sleep(1)

    print ("\t###########################################")
    print ("\t\tHappy Birthday", first_name, "..!")
    print ("\t\tHave some fun today :) ")
    print ("\t###########################################\n")


happy_birthday()



