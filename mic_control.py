import win32api
import win32gui

WM_APPCOMMAND = 0x319
WM_BASE_HEX = 0xFFFF + 1
 
APPCOMMAND_MICROPHONE_VOLUME_DOWN = WM_BASE_HEX * 25
APPCOMMAND_MICROPHONE_VOLUME_UP = WM_BASE_HEX * 26

def mute_mic():
    hwnd_active = win32gui.GetForegroundWindow()
    for x in range(50):
        win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_DOWN)

def unmute_mic():
    hwnd_active = win32gui.GetForegroundWindow()
    for x in range(50):
        win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_UP)
