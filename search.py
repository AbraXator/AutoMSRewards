import pygetwindow as gw
import pyautogui
import random
import os
import string
import subprocess
import time

parent_dir = os.getenv('LOCALAPPDATA') + "/"
#parent_dir = "C:/Users/Adam/Desktop/"
my_dir = "AutoMSRewards"
directory = os.path.join(parent_dir, my_dir)
file_dir = directory + "/used.txt"


def main():
    subprocess.call("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe")
    time.sleep(0.5)
    select_window()
    for i in range(5):
        handle_controls(generate_string())

def handle_controls(search_input):
    pyautogui.press('backspace')
    pyautogui.moveTo(500, 50)
    pyautogui.leftClick()
    pyautogui.write(search_input)
    pyautogui.press('enter')

def select_window():
    all_windows = gw.getAllTitles()
    edge_window = None
    searched_term = "Edge"

    for window in all_windows:
        if searched_term in window:
            edge_window = gw.getWindowsWithTitle(window)[0]

    if edge_window != None:
        edge_window.activate()
        edge_window.maximize()
        
        return True
    else:
        print(f'Could not find window with {searched_term} in title.')
        return False
    
def handle_files(str):
    try:
        os.mkdir(directory)
    except OSError as e:
        print(e)

def write_into_file(str):
    with open(file_dir, '+a') as f:
        f.write(str + "\n")
        f.close()
    
def generate_string():
    f = open(file_dir, 'r')
    read_text = f.read()
    list = read_text.split("\n")
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(characters) for _ in range(random.randrange(2, 30)))
    while random_string in list:
        random_string = ''.join(random.choice(characters) for _ in range(random.randrange(2, 30)))

    write_into_file(random_string)
    f.close()
    return random_string

if __name__ == "__main__":
    main()