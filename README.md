# TypingTyrant
This is a console based application that gives feedback on the accuracy of typing, no matter what program is being used. It does this by checking if/whether the Backspace key is pressed and comparing it to the number of character typed since the last time the Backspace key was pressed. The program ignores consecutive backspace pressed, as typically the backspace key has to be pressed several times to correct one typo that was made earlier. 
The program keeps track of average accuracy through a running average. When the average gets below a preset value in addition to providing feedback on the typing accuray the program also start proving audible feedback, i.e. it starts beeping every time the backspace key is pressed. This is super annoying... And that is exactly the idea, good reason to watch what you type!

Future updates could include an easier way to set the accuracy benchmark or a way to set the benchmark based on current performance, such that it would be both achievable and motivating. 
Futhermore the program could be converted from a console application to something on screen that periodically gives feedback by flashing a message or icon or the like. 

There are two versions availble:A CPP version that works on Windows and a Python version that works on Linux. 

Happy typing!

## Credits 
Parts of this project incorperates code borrowed from: https://github.com/hiamandeep/py-keylogger/
And this project would not be possible without the pyxhook module! 


## Potential future updates 
Open for contributions of others!
- Make the Python version available for Windows
- Add install notes
- Keep track of commonly made mistakes
- Update to a more current version of pyxhook

