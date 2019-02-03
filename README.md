# Scooby

Scooby is a voice activated desktop app which targets to achieve complete voice automation.

### Flow:
1. The app gets activated when you speaks its name aloud which is "Hey Scooby!" 

2. Then you give voice commands of whatever task you want to perform. 

3. Natural Language Processing is used to detect key words which inturn helps to detect main task. For eg:
  - You give a command "Open Chrome."
  - The NLP model detects the task and forwards it to part of code which is responsible for the automation.
  - Then suppose you want to access one of the shortcuts from the homepage of Chrome say Youtube, you just need to say "Click Youtube"
  - The app takes care of the rest and opens youtube for you.
  - There are various other features like type,open,launch,double-click,right-click,play and pause the video, etc which are just a voice    command away from being accessed. No need to use keyboard and mouse for any of those tasks!!!
  - Even if there are multiple entries with same name, the program will display a screen-shot with all the entries numbered and you just need to speak the number of the entery you want to access.


#### Note: For this application to work, constant network connection is required.
#### Note: This application is only for windows

## Some basic Voice Commands
  - Open <appName>
  - Click <any text on Screen>(If there are multiple occurences, you need to enter the number according to the image             displayed on screen)
  - Double Click <any text on screen>(If there are multiple occurences, you need to enter the number according to the image         displayed on screen)
  - Play/Pause/(on going videos)
  - Go Back/Forward(Go back/forward in windows explorer or browsers)
  - Enter Url(for browsers)
  - Type <type text into current field>
  - Cut/Copy/Paste/SelectAll
  - Wait for 'x' seconds(Stop executing the program for 'x' seconds)
  - Press Enter/Esc/Ctrl/Alt/Del
  - Close (closes current application)
  - Exit (Stop execution until 'Hey Scobby')
  and many more
  
  ## Steps for Installation
  1. Install Conda (https://www.anaconda.com/distribution/)(version 19.15)
  2. Commands  for Conda Terminal
    - conda install -c conda-forge pywinauto <h5>OR</h5> conda install -c conda-forge/label/cf201901 pywinauto    
    - conda install -c conda-forge spacy
    - conda install -c conda-forge pillow
    - conda install -c conda-forge tesseract (https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-3.05.02-               20180621.exe)
    - conda install -c danielfrg spacy-en_core_web_sm     (sm:small,mb:medium,lg:large)
    - C:/path/to/condoa/pip.exe pytesseract
  3. python scooby_1.py 
  #Dev Tools
   1. conda install -c anaconda qt
   2.designer.exe (Run in terminal to edit GUI for the app) 
      
