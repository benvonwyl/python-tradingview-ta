class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def colour(text): 
    text = text.replace("STRONG_SELL",bcolors.BOLD + bcolors.FAIL + "STRONG_SELL" +bcolors.ENDC + bcolors.ENDC)
    text = text.replace("SELL", bcolors.FAIL + "SELL" + bcolors.ENDC)
    text = text.replace("STRONG_BUY", bcolors.BOLD + bcolors.OKGREEN + "STRONG_BUY" + bcolors.ENDC + bcolors.ENDC)
    text = text.replace("BUY", bcolors.OKGREEN + "BUY" + bcolors.ENDC)
    text = text.replace("NEUTRAL", bcolors.OKBLUE + "NEUTRAL" + bcolors.ENDC)
    return text 


