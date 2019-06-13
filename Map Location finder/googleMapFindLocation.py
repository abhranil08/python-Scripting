import webbrowser,sys,os,pyperclip

chrome_path = '/usr/bin/google-chrome %s' 
if len(sys.argv)>1:
	location = "".join(sys.argv[1:])
else:
	location = pyperclip.paste()

webbrowser.get(chrome_path).open_new_tab("https://www.google.com/maps/place/"+location)
