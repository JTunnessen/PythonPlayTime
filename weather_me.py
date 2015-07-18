#! python3
# weather_me.py - Launches a weather page in the browser using an city, state from the command line or clipboard
import webbrowser, sys, pyperclip


if len(sys.argv) > 1:
	# Get city, state from the command line.
	city_state = ' '.join(sys.argv[1:])
else:
	# Get address from clipboard.
	#city_state = pyperclip.paste()
	break

webbrowser.open('https://weather.yahoo.com/united-states/' + state + '/' + city)

# DID NOT FINISH OR CLEAN UP ___ LOOKING FOR A BETTER WEATHER PAGE TO PLAY WITH