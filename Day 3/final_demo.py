# Import the PyAutoGUI library for keyboard/mouse automation
import pyautogui

# Import the time library for delays
import time

# Import datetime module (not used currently, but available if needed)
from datetime import datetime


# Enable emergency stop by moving mouse to top-left corner
pyautogui.FAILSAFE = True

# Add a 0.5-second pause after every PyAutoGUI command
pyautogui.PAUSE = 0.5


# Display status message in terminal
print("Step 1: Open Google Chrome...")

# Wait 2 seconds before starting
time.sleep(2)


# Open Windows Start Menu
pyautogui.press('win')

# Wait for Start Menu to appear
time.sleep(1)


# Type Chrome into Windows Search
pyautogui.write('chrome', interval=0.15)

# Wait for search results
time.sleep(1)


# Press Enter to launch Chrome
pyautogui.press('enter')

# Wait for Chrome to fully load
time.sleep(3)


# Display next step message
print("Step 2: Go to the website...")


# Focus Chrome's address bar
pyautogui.hotkey('ctrl', 'l')

# Wait 1 second
time.sleep(1)


# Type AccuWeather URL
pyautogui.write(
    'https://www.accuweather.com/en/in/chennai/206671/weather-forecast/206671',
    interval=0.05
)

# Wait 1 second
time.sleep(1)


# Press Enter to navigate to URL
pyautogui.press('enter')

# Wait for webpage to load completely
time.sleep(5)


# Display status message
print("Step 3: Copy the full page content...")


# Select everything on the webpage
pyautogui.hotkey('ctrl', 'a')

# Wait 1 second
time.sleep(1)


# Copy selected content to clipboard
pyautogui.hotkey('ctrl', 'c')

# Wait 1 second
time.sleep(1)


# Display status message
print("Step 4: Open Notepad and paste the data...")


# Open Windows Start Menu again
pyautogui.press('win')

# Wait 1 second
time.sleep(1)


# Search for Notepad
pyautogui.write('notepad', interval=0.15)

# Wait 1 second
time.sleep(1)


# Open Notepad
pyautogui.press('enter')

# Wait for Notepad to load
time.sleep(2)


# Paste clipboard contents into Notepad
pyautogui.hotkey('ctrl', 'v')

# Wait 2 seconds
time.sleep(2)


# Print completion message
print("Automation completed successfully!")