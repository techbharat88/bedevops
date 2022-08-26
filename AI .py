import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
#import wikipedia #pip install wikipedia
import webbrowser
import os
import paramiko
import time
from openpyxl import load_workbook
import smtplib
import sys
#from PIL import ImageGrab

#os.chdir(r'home/devops/Automation_project')



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(f'Good Morning! it is {hour}')

    elif hour>=12 and hour<18:
        speak(f'Good Afternoon! it is {hour}')   

    else:
        speak(f'Good Evening! it is {hour}')  

    speak("I am Sirene Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please")  
        return "None"
    return query

def Basic_troubleshoot(ip, user, pw, cmd1):

    # Open a socket,copy the output
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect("10.87.161.8", port=22, username="ax5b2638413", password="Payal@9571207401")
    chan = client.invoke_shell()
    time.sleep(3)
    chan.send('ssh {}\n'.format(Login))
    time.sleep(3)
    chan.send('Payal@9571207401\n')
    time.sleep(3)
    chan.send('sh ver | i uptime |ROM\n')
    time.sleep(2)
    chan.send('sh ip int brief\n')
    time.sleep(2)
    chan.send('\n')
    time.sleep(2)
    chan.send('sh int | i CRC\n')
    time.sleep(2)
    chan.send('\n')
    time.sleep(2)
    chan.send('sh process cpu history\n')
    time.sleep(2)
    chan.send('\n')
    time.sleep(0.5)
    chan.send('\n')
    time.sleep(0.5)
    chan.send('\n')
    time.sleep(0.5)
    chan.send('\n')
    time.sleep(0.5)
    chan.send('\n')
    time.sleep(2)
    chan.send('sh clock\n')
    time.sleep(2)
    output = chan.recv(999999999)
    subnets = str(output).splitlines()
    ##print(subnets)
    #snapshot = ImageGrab.grab()
    #save_path = "C:\\Users\\B2638413\\Music\Python T\\MySnapshot.jpg"
    #snapshot.save(save_path)
    #output = chan.recv(999999999)
    client.close()
    return output.decode("utf-8")





if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        

        if 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open snow' in query:
            webbrowser.open("sgts.service-now.com")

        elif 'triggers' in query:
            webbrowser.open("https://prd.zbxweb.sgt.saint-gobain.net")

        elif 'bandwidth' in query:
            webbrowser.open("https://prd.zbxweb.sgt.saint-gobain.net/sgt_zbp/")

        elif 'netflow' in query:
            webbrowser.open("https://netflow.sgt.saint-gobain.net")
        
        elif 'profile' in query:
            webbrowser.open("onehr.saint-gobain.com")
        
        elif 'pause' in query:
            while True:
                try:
                    time.sleep(1)  # do something here
                    print (" '.' ")

                except KeyboardInterrupt:
                    break
                    

        
        elif 'telecom' in query:
            webbrowser.open("sgts.service-now.com/telecom")
        
        elif 'stop' in query:
            speak("Thank you sir, you can call me anytime. Have a great day ! bye")
            break
        
        elif 'attendance' in query:
            webbrowser.open("onehr.saint-gobain.com/indectimecard/lms/EmpTimings.aspx")


        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'C:\\Users\\B2638413\\Music\\song'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\B2638413\\AppData\\Local\\Programs\\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
           

        elif 'remote' in query:
            codePath = "C:\\WINDOWS\\system32\\mstsc.exe"
            os.startfile(codePath)

        elif 'note' in query:
            codePath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(codePath)
            speak("What should I say?")
            content = takeCommand()
            speak("File name please")
            print("file name please")
            filename= takeCommand()
            with open(f'{filename}.txt',"a") as f:
               
                f.write(f'\n {content}')




        elif 'login' in query:
            try:
                speak("Please help me with site code")
                ip_address="zangief.sgt.saint-gobain.net"
                Login = str(input("your Connectection code is : "))
                speak("Abhi Dekhtaa hu")
                
                response = os.system('ping {} -n 2\n'.format(Login))
                if response == 0:
                    try:
                        output = Basic_troubleshoot(ip_address, 'ax5b2638413', 'Payal@9571207401', Login)
                        subnets = str(output).splitlines()
                        for j in subnets:
                            print(j)
                            #print('\n')
                        #print(subnets)
                        #sys.stdout=open("test.txt","w")
                        #sys.stdout.close()
                        

                        #print(' \n'*4)
                        #print('Finished!\n')
                    
                    except Exception as e:
                        print(e)
                        speak("Sorry I am unable to login")
                else:
                    print("Host is not reachable")
            except:
                print("Sorry I am failed")
            
        
