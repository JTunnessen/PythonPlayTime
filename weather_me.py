#! python3
# weather_me.py - Launches a weather page in the browser using an city, state from the command line or clipboard
import webbrowser, sys, pyperclip


if len(sys.argv) > 1:
	# Get city, state from the command line.
	city = ' '.join(sys.argv[1:])
	state = ' '.join(sys.argv[1:])
else:
	# Get address from clipboard.
	city_state = pyperclip.paste()

webbrowser.open('https://weather.yahoo.com/united-states/' + city_state)