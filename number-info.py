import phonenumbers
from colorama import Style, Fore

print(f'''{Fore.BLUE}
  _   _                       _                             ___            __         
 | \ | |  _   _   _ __ ___   | |__     ___   _ __          |_ _|  _ __    / _|   ___  
 |  \| | | | | | | '_ ` _ \  | '_ \   / _ \ | '__|  _____   | |  | '_ \  | |_   / _ \ 
 | |\  | | |_| | | | | | | | | |_) | |  __/ | |    |_____|  | |  | | | | |  _| | (_) |
 |_| \_|  \__,_| |_| |_| |_| |_.__/   \___| |_|            |___| |_| |_| |_|    \___/ 
 Gather info about phone numbers.
                                                                                      
{Style.RESET_ALL}''')


def askNumber():
    number = input("Input a phone number: ")

    if len(number) >= 4 and number[0] == "+":
        pass
    else:
        print(f"{Fore.RED}Invalid number...{Style.RESET_ALL}")
        quit(1)

    from phonenumbers import geocoder
    ch_number = phonenumbers.parse(number, "CH")

    numInfo1 = geocoder.description_for_number(ch_number, "en")

    if numInfo1 == "":
        numInfo1 = "null"
    else:
        pass

    print(f'{Fore.BLUE}Country: {Fore.GREEN}{numInfo1}{Style.RESET_ALL}')

    from phonenumbers import carrier
    service_number = phonenumbers.parse(number, "R0")

    numInfo2 = carrier.name_for_number(service_number, "en")

    if numInfo2 == "":
        numInfo2 = "null"
    else:
        pass

    print(f'{Fore.BLUE}Carrier: {Fore.GREEN}{numInfo2}{Style.RESET_ALL}')

    from phonenumbers import timezone
    the_number = phonenumbers.parse(number, "SWE")

    numInfo3 = timezone.time_zones_for_number(the_number)

    numInfo3 = numInfo3[0]

    print(f'{Fore.BLUE}Timezone: {Fore.GREEN}{numInfo3}{Style.RESET_ALL}')


while True:
    askNumber()
