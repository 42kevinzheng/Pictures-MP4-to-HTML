import os
import sys
import webbrowser




fileName = str(input("Enter the name of the html file you want to create: "))
f = open(fileName + '.html', 'w')
path = str(input("Enter in the path to the folder: "))  # asked the user for the folder path
folder = os.listdir(path)



for file in folder:
    if file.endswith(".png") or file.endswith("jpg") or file.endswith("gif"):
        message = ("<img src=\"" + path + "\\" + str(file) + "\"" + "height=\"500\">")
        f.write(str(message))
    if file.endswith(".mp4"):
        video = ("<video type=\"video\\mp4\" src=\"" + path + "\\" + file + "\"" + " width=\"480\" height=\"360\"  loop controls> </video>")
        f.write(video)

print("It is done,the \"" + fileName + ".html\" file is created in the folder where you've put this program.")
f.close()
webbrowser.open_new_tab(fileName+'.html')
print("You can now view the \"" + fileName + ".html\" file in your default web browser")

