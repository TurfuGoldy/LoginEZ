import time
import os
import getpass
import ctypes
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from colorama import Fore, init

init(autoreset=True)
if os.name == "nt":
    os.system("mode con: cols=138 lines=30")

def title(text):
	if os.name == "nt":
		ctypes.windll.kernel32.SetConsoleTitleW(f"Login-EZ | By Goldfire | {text}")
	else:
		print(f"\33]0;Login-EZ | By Goldfire | {text}\a", end="", flush=True)

def logo():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

	print(f"""{Fore.LIGHTBLUE_EX}
                                      ██╗      ██████╗  ██████╗ ██╗███╗   ██╗      ███████╗███████╗
                                      ██║     ██╔═══██╗██╔════╝ ██║████╗  ██║      ██╔════╝╚══███╔╝
                                      ██║     ██║   ██║██║  ███╗██║██╔██╗ ██║█████╗█████╗    ███╔╝ 
                                      ██║     ██║   ██║██║   ██║██║██║╚██╗██║╚════╝██╔══╝   ███╔╝  
                                      ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║      ███████╗███████╗
                                      ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝      ╚══════╝╚══════╝
						{Fore.LIGHTMAGENTA_EX}Connecting to a Discord token has never been easier ;)

{Fore.RESET}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n      
	""")

def login(token):
	title("Logging")

	logo()
	print(f"{Fore.LIGHTCYAN_EX}Logging into the account...")

	uc.install()

	options = webdriver.ChromeOptions()
	options.add_experimental_option("excludeSwitches", ["enable-logging"])
	driver = webdriver.Chrome(options=options)

	driver.get("https://discord.com/login")
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-mount"]/div[2]/div/div')))
	driver.execute_script('(function() {window.t = ' + f'"{token}";window.localStorage = document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage;window.setInterval(() => window.localStorage.token = `"$' + '{window.t}"`); window.location.reload();})();')
	try:
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[1]/section/div[2]')))
		
		title("Logged")

		logo()
		print(f"{Fore.LIGHTGREEN_EX}Successfully connected to the account.")

		time.sleep(999999)
	except:
		title(("Logging Error"))

		logo()
		print(f"{Fore.LIGHTRED_EX}Unable to log into the account. Please check that the token is valid.")

		time.sleep(10)
		init()

def init():
	title("Initialization")

	logo()
	token = getpass.getpass(f"{Fore.LIGHTYELLOW_EX}Enter Discord token (it will be hidden).\n~# ")
	logo()

	login(token)

if __name__ == "__main__":
	try:
		init()
	except KeyboardInterrupt:
		exit()