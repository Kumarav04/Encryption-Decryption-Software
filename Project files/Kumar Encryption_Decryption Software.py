from datetime import date
import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import sys
from time import time,localtime,strftime
import pickle
from random import randint
import csv

    
def intro():
    global opt
    print('\t\t\t\t\t\t\t╔═════════════════════════════════════════════╗')
    print('\t\t\t\t\t\t\t║━━━━━━━━━━━━━━━━━━━━━━━━━━━║')
    print('\t\t\t\t\t\t\t║ Welcome to Encryption & Decryption Software ║')
    print('\t\t\t\t\t\t\t║━━━━━━━━━━━━━━━━━━━━━━━━━━━║')
    print('\t\t\t\t\t\t\t║ By: Kumaravendhan Ravichandran              ║')
    print('\t\t\t\t\t\t\t║ Class: 12-B                                 ║')
    print('\t\t\t\t\t\t\t║ Roll No.12                                  ║')
    print('\t\t\t\t\t\t\t║ FAIPS-DPS Kuwait                            ║')
    print('\t\t\t\t\t\t\t║═════════════════════════════════════════════║')
    print('\t\t\t\t\t\t\t║Date:',date.today(),'                            ║')
    print('\t\t\t\t\t\t\t╚═════════════════════════════════════════════╝')
    print('Maximize your window for the best experience')
    print('Press Enter to open the MAIN MENU..')
    input()
    
def filesearcher():
    global path
    global exe
    
    def time_convert(sec):
        mins = sec // 60
        sec = sec % 60
        mins = mins % 60
        print('Time elapsed: ',int(mins),'Minutes',int(sec),'seconds')
        
    def exe_input():
        global exe
        if opt=='3':
            exe=input('''
Please enter the extention of the file along with the file name. Eg. .txt/.jpg
Enter the name of the file to find its path OR Enter MANUAL to input path manually ''') 
            found=0
        elif opt=='1':
            exe=input('''
Please enter the extention of the file along with the file name. Eg. .txt/.jpg
Enter the name of the file to Encrypt OR Enter MANUAL to input path manually ''')
        elif opt=='2':
            exe=input('''
Please enter the extention of the file along with the file name. Eg. .txt/.jpg
Enter the name of the file to Decrypt OR Enter MANUAL to input path manually ''')
        elif opt=='4':
            if opt4=='1':
                exe=input('''
Please enter the extention of the file along with the file name. Eg. .txt/.jpg
Enter the name of the file to Attach in the Email OR Enter MANUAL to input path manually ''')
            elif opt4=='2' or opt4=='4':
                exe=input('''
Please enter the extention of the file along with the file name. Eg. .txt/.jpg
Enter the name of the file to Encrypt and Attach in the Email OR Enter MANUAL to input path manually ''')
    if opt=='4' and opt4=='5':
            exe=fname
            found=1
    elif opt=='1' and opt2=='3':
            exe=f_name
            found=1
    else:
        exe_input()
    while exe.upper()=='MANUAL':
        path=input('Enter the file path\nOR press B to go back ')
        if path.upper()!='B':
            found=1
            break
        else:
            exe_input()
    if exe.upper()!='MANUAL':
        if opt=='1' and opt2=='3':
            way=input("\nEnter The drive where this python file is saved (C/D) (Enter 'E' if it is running from an external drive) ")
        elif opt=='4' and opt4=='5':
            way=input("\nEnter The drive where this python file is saved (C/D) (Enter 'E' if it is running from an external drive) ")
        else:
            way=input("\nEnter C Drive or D Drive (Enter 'E' if you are searching for a file from an external drive) ")
        while way.upper()!='E' and way.upper()!='C' and way.upper()!='C DRIVE' and way.upper()!='C: DRIVE' and way.upper()!='CDRIVE' and way.upper()!='C:DRIVE' and way.upper()!='C:' and way.upper()!='D' and way.upper()!='D DRIVE' and way.upper()!='D: DRIVE' and way.upper()!='DDRIVE' and way.upper()!='D:DRIVE' and way.upper()!='D:':
            print('Invalid input. Pleasy try again')
            way=input('Enter C Drive or D Drive ')
            if way.upper()=='C' or way.upper()=='C DRIVE' or way.upper()=='C: DRIVE' or way.upper()=='CDRIVE' or way.upper()=='C:DRIVE' or way.upper()=='C:':
                break
            elif way.upper()=='D' or way.upper()=='D DRIVE' or way.upper()=='D: DRIVE' or way.upper()=='DDRIVE' or way.upper()=='D:DRIVE' or way.upper()=='D:':
                break
            elif way.upper()=='E':
                break
            else:
                continue
        if way.upper()=='C' or way.upper()=='C DRIVE' or way.upper()=='C: DRIVE' or way.upper()=='CDRIVE' or way.upper()=='C:DRIVE' or way.upper()=='C:':
            way='C:\\'
        elif way.upper()=='D' or way.upper()=='D DRIVE' or way.upper()=='D: DRIVE' or way.upper()=='DDRIVE' or way.upper()=='D:DRIVE' or way.upper()=='D:':
            way='D:\\'
        elif way.upper()=='E': #Applicable only when searching files from external drives such as a USB
            way='E:\\'
        print('Searching...')
        found=0
        start_time=time()
        try:
            for root, dirs, files in os.walk(way):
                for name in files:
                    if name==exe: #Checks if file name matches
                        path=(os.path.abspath(os.path.join(root, name))) #Gets the path of the file
                        found=1
            if found==1:
                end_time=time()
                time_elapsed=end_time-start_time
                print('Location Found!')
                time_convert(time_elapsed)
                print('The path of file : ',path)# print path of file 
                if opt=='3':
                    print('\nPress Enter to continue')
                    input()
            elif found==0:
                print('File not found')
                ask=input('Would you like to retry or enter the file path manually?(Retry/Manual) ')
                if ask.upper()=='RETRY':
                    filesearcher()
                elif ask.upper()=='MANUAL':
                    path=input('Enter the file path ')
                    found=1
                else:
                    while ask.upper()!='RETRY' and ask.upper()!='MANUAL':
                        print('Invalid Input. Please try again.\n')
                        if ask.upper()=='RETRY':
                            filesearcher()
                        elif ask.upper()=='MANUAL':
                            path=input('Enter the file path ')
                            found=1
                        else:
                            continue
        except Exception:
            print('An error occured. Please try again.')
            filesearcher()

            
def fileencrypter():
    global key
    try:
        key=randint(1,256) # randomly producing encryption key. Cannot be more than 256 as max value for bytearray is 265
        print('Key for encryption:',key)

        fin=open(path, 'rb')# open file for reading purpose
        image=fin.read()# storing file data in variable "image"
        fin.close()
        image=bytearray(image)# converting image into byte array to perform encryption easily on numeric data

        for index, values in enumerate(image): # performing XOR operation on each value of bytearray
            image[index] = values ^ key
            
        fin=open(path, 'wb') # opening file for writing purpose
        fin.write(image)  # writing encrypted data in image 
        fin.close()
        print('Encryption Done...')
        if opt=='1' and opt2=='1' or opt=='1' and opt2=='3':
            t=localtime()
            timenow=strftime("%H:%M:%S",t)
            with open('Encryption_Logs.csv','a',newline='\n') as encrfile:
                c=csv.writer(encrfile)
                rec=[date.today(),timenow,exe,key]
                c.writerow(rec)
            print("Press Enter to continue")
            input()
    except Exception:
        print('An error occured. Please try again.')
        fileencrypter()

        
def filedecrypter():
    global key1
    if opt=='2' and opt3=='1' or opt=='2' and opt3=='3':
        print('Note : Encryption key and Decryption key must be same.')
        key1=int(input('Enter the key to the decrypt the file: '))
    else:
        key1=key
    fin=open(path, 'rb') # open file for reading purpose
    image=fin.read() # storing file data in variable "image"
    fin.close()
    image=bytearray(image) # converting image into byte array to perform decryption easily on numeric data

    for index, values in enumerate(image): # performing XOR operation on each value of bytearray
        image[index] = values ^ key1
  
    fin=open(path, 'wb') # opening file for writting purpose
    fin.write(image) # writing decrypted data in image
    fin.close()
    if opt=='2' and opt3=='1':
        print('Decryption Done...')
        t=localtime()
        timenow=strftime("%H:%M:%S",t)
        with open('Decryption_Logs.csv','a',newline='\n') as decrfile:
                c=csv.writer(decrfile)
                rec=[date.today(),timenow,exe,key1]
                c.writerow(rec)
        print("Press Enter to continue")
        input()
    '''
    except Exception:
        print('An error occured. Please try again.')
        filedecrypter()'''


def encrypttext():
    global ran
    global body
    global r
    try:
        r=''
        ran=randint(100,1999) #Generates a random encryption key 
        if opt=='4' and opt4=='3':
            m=body
            for i in range(0, len(m)):
                r+=chr(ord(m[i])+ran) #Uses ASCII to change the ordinal values of each character of the string
            body=r
        elif opt=='4' and opt4=='4':
            m=body
            for i in range(0, len(m)):
                r+=chr(ord(m[i])+ran)
            body=r
        else:
            m=input('Enter message for encryption: ')
            for i in range(0, len(m)):
                r+=chr(ord(m[i])+ran)
        print('Key to decryption:',ran)
        print('Encrypted message:',r,'\n MESSAGE ENCRYPTED SUCCESSFULLY\n')
        if opt=='1' and opt2=='2':
            print('Press Enter to continue')
            input()
            
    except Exception:
        print('An error occured. Please try again.')
        encrypttext()

        
def decrypttext():
    global r
    global m
    try:
        r=''
        if opt=='2' and opt3=='3':
            pass
        else:
            m=input('Enter message to decrypt: ')
        q=int(input('Enter the key to decrypt '))
        for i in range(0,len(m)):
            r=r+chr(ord(m[i])-q) #Reverses the encryption done by changing the ordinal values of characters of a string
        print('Decrypted message:',r,'\nMESSAGE DECRYPTED SUCCESSFULLY\n')
        if opt=='2' and opt3=='2':
            print('Press Enter to continue')
            input()
    except Exception:
        print('An error occured. Please try again')
        decrypttext()

        
def onlyemailing():
    global body
    sender= "kumarpython2021@gmail.com"  #Sended email can be changed as per the user's wish
    password = input('Enter the email password and press Enter ')

    def sentemaillogs():
        t=localtime()
        timenow=strftime("%H:%M:%S",t)
        if opt4=='2':
            encrkey=key
            textencrkey=''
            advkey1=''
            advkey2=''
        elif opt4=='3':
            textencrkey=ran
            encrkey=''
            advkey1=''
            advkey2=''
        elif opt4=='4':
            encrkey=key
            textencrkey=ran
            advkey1=''
            advkey2=''
        elif opt4=='5':
            advkey1=key
            advkey2=ran
            encrkey=''
            textencrkey=''
        elif opt4=='1':
            encrkey=''
            textencrkey=''
            advkey1=''
            advkey2=''
        with open('Email_Logs.csv','a',newline='\n') as emailfile: #Creates a log of every email sent. Automatically writes the encryption keys if any.
                c=csv.writer(emailfile)
                xyz=[date.today(),timenow,sender,receiver,subject,encrkey,textencrkey,advkey1,advkey2]
                c.writerow(xyz)
                            
    def preinput():
        try:
            global receiver
            receiver= input('\nEnter the reciever Email ID OR Press P to choose a preset email address. ') #Preset email contains the emails entered and saved from the presets menu by the user.
            if receiver.upper()=='P':
                preset=open('Email_presets.DAT','rb')
                temp=[]
                preset.seek(0, 2)
                eof=preset.tell()
                preset.seek(0)
                print('\t\t\t\t','EMAIL PRESETS')
                while preset.tell()<eof:
                    emp=pickle.load(preset)
                    print('\t\t\t',emp[0],'━',emp[1]) #Displays the preset emails
                    temp.append(emp[0])
                preset.close()
                preinp=input('\nEnter the index number of the preset email you would like to use OR press B to go back: ')
                if preinp.upper()!='B':
                    try:
                        if int(preinp) in temp:
                            preset2=open('Email_presets.DAT','rb')
                            while preset2.tell()<eof:
                                rec=pickle.load(preset2)
                                if int(preinp)==rec[0]:
                                    receiver=rec[1]
                            preset2.close()
                            return receiver
                    except Exception:
                        print('Invalid Input. Please try again')
                        preinput()
                else:
                    preinput()
            elif receiver.upper()!='P':
                if '@' and '.' not in receiver:
                    print('Invalid Email ID. Please try again')
                    preinput()
        except Exception:
            print('An error occured. Please try again')
            preinput()
            
    preinput()
    try:
        print('\nSending to: ',receiver)
        sub=input('\nWould you like to enter a subject?(y/n) ')
        while sub.upper()!='Y' and sub.upper()!='N':
            print('Invalid input. Pleasy try again')
            sub=input('\nWould you like to enter a subject?(y/n) ')
            if sub.upper()=='Y' or sub.upper=='N':
                break
            else:
                continue
        if sub.upper()=='Y':
            subject = input('Enter subject of email ')
        elif sub.upper()=='N':
            subject=''
        if opt=='4' and opt4=='3' or opt=='4' and opt4=='4':
            bod='Y'
        else:
            bod=input('\nWould you like to enter a body to the email?(y/n) ')
        while bod.upper()!='Y' and bod.upper()!='N':
            print('Invalid input. Pleasy try again')
            bod=input('\nWould you like to enter a body to the email?(y/n) ')
            if bod.upper()=='Y' or bod.upper=='N':
                break
            else:
                continue
        if bod.upper()=='Y':
            body = input('Enter body of Email ')
        elif bod.upper()=='N':
            body=''
        
        if opt=='4' and opt4=='1' or opt=='4' and opt4=='3':
            file=input('\nWould you like to attach a file?(y/n) ')
        else:
            file='Y'
        while file.upper()!='Y' and file.upper()!='N':
            print('Invalid input. Pleasy try again')
            file=input('\nWould you like to attach a file?(y/n) ')
            if file.upper()=='Y' or file.upper=='N':
                break
            else:
                continue
        if file.upper()=='Y':
            filesearcher()
            if opt=='4' and opt4=='2':
                fileencrypter()
                body+='\nKey to the encryption of the file is: '
                body+=str(key)
            elif opt=='4' and opt4=='4':
                fileencrypter()
                encrypttext()
                body+='\nThis Email contains an encrypted file.\nKey to the encryption of the file is: '
                body+=str(key)
                body+='\nThe body of this Email contains encrypted text message.\nKey to the encryption text is: '
                body+=str(ran)
            elif opt=='4' and opt4=='5':
                fileencrypter()
                body+='\nKey to the encryption of the file is: '
                body+=str(key)
                body+='\nKey to encryption of text inside the file: '
                body+=str(ran)
            file_name=input('\nWould you like to enter a name for the file you are attaching?(y/n) ')
            while file_name.upper()!='Y' and file_name.upper()!='N':
                print('Invalid input. Pleasy try again')
                file_name=input('\nWould you like to enter a name for the file you are attaching?(y/n) ')
                if file_name.upper()=='Y' or file_name.upper=='N':
                    break
                else:
                    continue
            if file_name.upper()=='Y':
                filename=input('Enter your desired file name ') 
                if path[-5:]=='.docx' or path[-5:]=='.xlsx': #Using the path of the file to get the  extension so that the file doesn't lose its original type while getting emailed.
                    filename+=(path[-5:])
                elif path[-3]=='.py':
                    filename+=(path[-3])
                else:
                    filename+=(path[-4:])
            elif file_name.upper()=='N':
                filename='NoName'
                if path[-5:]=='.docx' or path[-5:]=='.xlsx':
                    filename+=(path[-5:])
                elif path[-3]=='.py':
                    filename+=(path[-3])
                else:
                    filename+=(path[-4:])
            else:
                print('Invalid Input')
            # Open file in binary mode
            with open(path, "rb") as attachment:
                # Add file as application/octet-stream
                # Email client can usually download this automatically as attachment
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            encoders.encode_base64(part) # Encode file in ASCII characters to send by email

            part.add_header(     # Add header as key/value pair to attachment part
                "Content-Disposition",
                f"attachment; filename= {filename}",   # Add attachment to message and convert message to string
            )
            message=MIMEMultipart()
            message["From"]=sender
            message["To"]=receiver
            message["Subject"]=subject
            
            # Add body to email
            message.attach(MIMEText(body, "plain"))
            message.attach(part)
            text = message.as_string()
            try:
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    if opt=='4' and opt4=='2':
                        filedecrypter()
                    elif opt=='4' and opt4=='4':
                        filedecrypter()
                    server.login(sender, password)
                    server.sendmail(sender, receiver, text)
                    sentemaillogs()
                    if opt=='4' and opt4=='2' or opt=='4' and opt4=='4':
                        print('File decrypted and restored in the source.')
                        print('Email Sent Successfully')
                    else:
                        print('Email Sent Successfully')
                    print("Press Enter to continue")
                    input()
                    if opt!=1:
                        pass
            except smtplib.SMTPAuthenticationError: #Prompts an error message if the email credentials are wrong
                if opt=='4' and opt4=='2' or opt=='4' and opt4=='4':
                        print('File decrypted and restored in the source.')
                print('Invalid Credentials. Please try again ')
                choice=input('Would you like to try again?(y/n) ')
                if choice=='y':
                    onlyemailing()
                elif choice=='n':
                    print('Thank you for using the emailing service!')
                    print("Press Enter to continue")
                    input()
        elif file.upper()=='N':
            if opt=='4' and opt4=='3':
                encrypttext()
                body+='\nThe body of this Email contains encrypted text message.\nKey to encryption the text is: '
                body+=str(ran)
            message=MIMEMultipart()
            message["From"]=sender
            message["To"]=receiver
            message["Subject"]=subject
            
            message.attach(MIMEText(body, "plain")) # Add body to email
            text = message.as_string()

            try:
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:   # Log in to server using secure context and send email
                    server.login(sender, password)
                    server.sendmail(sender, receiver, text)
                    sentemaillogs()
                    print('Email Sent Successfully')
                    print("Press Enter to continue")
                    input()
            
            except smtplib.SMTPAuthenticationError:
                print('Invalid Credentials. Please try again ')
                choice=input('Would you like to try again?(y/n) ')
                if choice=='y':
                    onlyemailing()
                elif choice=='n':
                    print('Thank you for using the emailing service!')
                    print("Press Enter to continue")
                    input()

    except Exception:
        print('An Error Occured. Please try again')
        onlyemailing()

        
def emailpresets():
    try:
        f=open('Email_presets.DAT','rb')
        alist=[]
        f.seek(0,2)
        eof=f.tell()
        f.seek(0)
        while f.tell()<eof:
            rec=pickle.load(f)
            alist.append(rec[0])
            maxval=max(alist)
        f.close()
        f1=open('Email_presets.DAT','ab')
        data=input('Enter the email ID for preset ')
        while '@' and '.' not in data:  #Validates the email address before adding it to the presets
            print('Invalid Email Address')
            data=input('Enter the email ID for preset ')
            if '@' and '.' in data:
                break
            else:
                continue
        emp=[maxval+1,data]
        pickle.dump(emp,f1)
        f1.close()
        print('The email you entered has been added to Email Presets!')
        print("Press Enter to continue")
        input()
    except Exception:
        print('An Error occured. Please try again')
        emailpresets()

        
def deletepreset():
    try:
        f=open('Email_presets.DAT','rb')
        f.seek(0, 2)
        eof=f.tell()
        f.seek(0)
        while f.tell()<eof:
            emp=pickle.load(f)
            print('\t\t\t',emp[0],'━',emp[1])
        f.close()
        f1=open('Email_presets.DAT','rb')
        n=int(input('\nEnter the index number of the email that you would like to delete from the preset '))
        temp=[]
        found=0
        f1.seek(0, 2)
        eof=f1.tell()
        f1.seek(0)
        while f1.tell()<eof:
            rec=pickle.load(f1)
            if n==rec[0]:
                found=1
                pass
            else:
                temp.append(rec)
        f1.close()
        f2=open('Email_presets.DAT','wb')
        for j in temp:
            pickle.dump(j,f2)
        f2.close()
        if found==1:
            print('Record deleted successfully!')
            print("Press Enter to continue")
            input()
        elif found==0:
            print(n,'not found in the file')
    except Exception:
        print('An Error occured. Please try again')
        deletepreset()

        
def Menufunction():
    global opt
    global opt2
    global opt3
    global opt4
    global fname
    global body
    global f_name
    global r
    global m
    global key1
    global key
    
    def Presetsfunction():
        try:
            presetmenu='''
                                                    ══════════════════
                                                    EMAIL PRESETS MENU
                                                    ══════════════════
                                                    
                                            Enter 1 to DISPLAY EMAIL PRESETS
                                            Enter 2 to ADD AN EMAIL PRESET
                                            Enter 3 to DELETE AN EMAIL PRESET
                                            
                                            Enter B to go back
                '''
            print(presetmenu)
            presetopt=input('Enter your option ')
            if presetopt.upper()=='B':
                email_menu()
            elif presetopt=='1':
                f=open('Email_presets.DAT','rb')
                f.seek(0,2)
                eof=f.tell()
                f.seek(0)
                while f.tell()<eof:
                    emp=pickle.load(f)
                    print('\t\t\t',emp[0],'━',emp[1])
                f.close()
                print('Press Enter to continue')
                input()
                Presetsfunction()
            elif presetopt=='2':
                emailpresets()
                Presetsfunction()
            elif presetopt=='3':
                deletepreset()
                Presetsfunction()
            else:
                print('Invalid Input. Please Try again')
                print('\nPress Enter to continue')
                input()
                encryptlogsfunc()
        except Exception:
            print('An Error occured. Please try again')
            Presetsfunction()
            
    def encryptlogsfunc():
        try:
            encryptlogsmenu='''
                                                ════════════════════
                                                ENCRYPTION LOGS MENU
                                                ════════════════════
                                        
                                Enter 1 to VIEW ENCRYPTION LOGS
                                Enter 2 to SEARCH FOR ENCRYPTION LOGS WITH FILE NAME
                                Enter 3 to DELETE ALL ENCRYPTION LOG RECORDS
                                
                                Enter B to go back
            '''
            print(encryptlogsmenu)
            optENCRMENU=input('Enter your option for Encryption Log ')
            if optENCRMENU.upper()=='B':
                if opt=='1':
                    encr_menu()
                elif opt=='6':
                    encr_decrlogs()
            elif optENCRMENU=='1':
                with open('Encryption_Logs.csv','r',newline='\n') as encrfile:
                    robj=csv.reader(encrfile)
                    for rec in robj:
                        print('{:<13}  {:<11}  {:<30}  {:<14}'.format(*rec))
                print('\nPress Enter to continue')
                input()
                encryptlogsfunc()
            elif optENCRMENU=='2':
                found=0
                encrfilename=input('Enter the file name along with the extension for which you would like to see the encryption logs for: ')
                with open('Encryption_Logs.csv','r',newline='\n') as encrfile:
                    robj=csv.reader(encrfile)
                    for rec in robj:
                        if rec[2]==encrfilename:
                            found=1
                            jkl=['Date','Time','File Name','Encryption Key']
                            print('{:<13}  {:<11}  {:<30}  {:<14}'.format(*jkl))
                            print('{:<13}  {:<11}  {:<30}  {:<14}'.format(*rec))
                if found==0:
                    print('Record not found')
                print('\nPress Enter to continue')
                input()
                encryptlogsfunc()
            elif optENCRMENU=='3':
                print('Press Enter to confirm to DELETE ALL ENCRYPTION LOGS')
                input()
                with open('Encryption_Logs.csv','r') as infile:
                    with open('temp.csv','w',newline='') as outfile:
                        robj=csv.reader(infile)
                        wobj=csv.writer(outfile)
                        found=0
                        for rec in robj:
                            if rec[0]!='Date':
                                pass
                            else:
                                wobj.writerow(rec)
                os.remove('Encryption_Logs.csv')
                os.rename('temp.csv','Encryption_Logs.csv')
                print('All Records Deleted.')
                print('\nPress Enter to continue')
                input()
                encryptlogsfunc()
            else:
                print('Invalid Input. Please Try again')
                print('\nPress Enter to continue')
                input()
                encryptlogsfunc()
        except Exception:
            print('An Error occured. Please try again')
            encryptlogsfunc()
            
    def decryptlogsfunc():
        try:
            decryptlogsmenu='''
                                                ════════════════════
                                                DECRYPTION LOGS MENU
                                                ════════════════════
                                        
                                Enter 1 to VIEW DECRYPTION LOGS
                                Enter 2 to SEARCH FOR DECRYPTION LOGS WITH FILE NAME
                                Enter 3 to DELETE ALL DECRYPTION LOG RECORDS
                                
                                Enter B to go back
            '''
            print(decryptlogsmenu)
            optDECRMENU=input('Enter your option for Decryption Log ')
            if optDECRMENU.upper()=='B':
                if opt=='2':
                    decr_menu()
                elif opt=='6':
                    encr_decrlogs()
            elif optDECRMENU=='1':
                with open('Decryption_Logs.csv','r',newline='\n') as decrfile:
                    robj=csv.reader(decrfile)
                    for rec in robj:
                        print('{:<13}  {:<11}  {:<30}  {:<14}'.format(*rec))
                print('\nPress Enter to continue')
                input()
                decryptlogsfunc()
            elif optDECRMENU=='2':
                found=0
                decrfilename=input('Enter the file name along with the extension for which you would like to see the decryption logs for: ')
                with open('Decryption_Logs.csv','r',newline='\n') as decrfile:
                    robj=csv.reader(decrfile)
                    for rec in robj:
                        if rec[2]==decrfilename:
                            found=1
                            jkl=['Date','Time','File Name','Decryption Key']
                            print('{:<13}  {:<11}  {:<30}  {:<14}'.format(*jkl))
                            print('{:<13}  {:<11}  {:<30}  {:<14}'.format(*rec))
                if found==0:
                    print('Record not found')
                print('\nPress Enter to continue')
                input()
                decryptlogsfunc()
            elif optDECRMENU=='3':
                print('Press Enter to confirm to DELETE ALL DECRYPTION LOGS')
                input()
                with open('Decryption_Logs.csv','r') as infile:
                    with open('temp.csv','w',newline='') as outfile:
                        robj=csv.reader(infile)
                        wobj=csv.writer(outfile)
                        found=0
                        for rec in robj:
                            if rec[0]!='Date':
                                pass
                            else:
                                wobj.writerow(rec)
                os.remove('Decryption_Logs.csv')
                os.rename('temp.csv','Decryption_Logs.csv')
                print('All Records Deleted.')
                print('\nPress Enter to continue')
                input()
                decryptlogsfunc()
            else:
                print('Invalid Input. Please Try again')
                print('\nPress Enter to continue')
                input()
                decryptlogsfunc()
        except Exception:
            print('An Error occured. Please try again')
            decryptlogsfunc()
            
    def encr_menu():
        global opt2
        global r
        global m
        global key1
        global key
        global f_name
        encryptmenu='''
                                ═══════════════
                                ENCRYPTION MENU
                                ═══════════════
                                
                        Enter 1 to ENCRYPT A FILE
                        Enter 2 to ENCRYPT TEXT
                        Enter 3 for ADVANCED ENCRYPTION
                        Enter 4 to open ENCRYPTION LOGS MENU
                        
                        Enter B to go back to MAIN MENU
        '''
        print(encryptmenu)
        opt2=input('Enter your option to Encrypt ')
        if opt2.upper()=='B':
            Menufunction()
        elif opt2=='1':
            filesearcher()
            fileencrypter()
            encr_menu()
        elif opt2=='2':
            encrypttext()
            encr_menu()
        elif opt2=='3':
            advencrinfo='''
                      ╔════════════════════════════════════════════════════════════════════════════╗
                      ║                                                                            ║
                      ║                          ADVANCED ENCRYPTION                               ║
                      ║   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   ║
                      ║ Advanced encryption encrypts the text inputted by the user and writes it   ║
                      ║ into a text file (Notepad file). It then automatically encrypts the text   ║
                      ║ file into which the encrypted message has been written into. The software  ║
                      ║ will return 2 different keys: one for the text in the file and one for the ║
                      ║ file itself. While Decrypting, the software will first ask the user to     ║
                      ║ input the key to decrypt the file then the key to decrypt the text in the  ║
                      ║ file. The software will then read the file and display the fully decrypted ║
                      ║ message.                                                                   ║
                      ║                                                                            ║
                      ║ Please note the 2 decryption keys given by the program carefully as the    ║
                      ║ original message cannot be decrypted otherwise.                            ║
                      ╚════════════════════════════════════════════════════════════════════════════╝
                      '''
            print(advencrinfo)
            print('Press enter to continue.. ')
            input()
            encrypttext()
            f_name=input('Enter the name of the notepad file ')
            f_name+='.txt'
            with open(f_name,'w',encoding="utf-8") as f:
                f.write(r)
            filesearcher()
            fileencrypter()
            encr_menu()
        elif opt2=='4':
            encryptlogsfunc()
        else:
            print('Invalid Input. Please Try again')
            print('\nPress Enter to continue')
            input()
            encr_menu()
            
    def decr_menu():
        global opt3
        global f_name
        global r
        global m
        global key1
        global key
        decryptmenu='''
                                ═══════════════
                                DECRYPTION MENU
                                ═══════════════
                                
                        Enter 1 to DECRYPT A FILE
                        Enter 2 to DECRYPT TEXT
                        Enter 3 for ADVANCED DECRYPTION
                        Enter 4 to open DECRYPTION LOGS MENU
                        
                        Enter B to go back to MAIN MENU
        '''
        print(decryptmenu)
        opt3=input('Enter your option to Decrypt ')
        if opt3.upper()=='B':
            Menufunction()
        elif opt3=='1':
            filesearcher()
            filedecrypter()
            decr_menu()
        elif opt3=='2':
            decrypttext()
            decr_menu()
        elif opt3=='3':
            filesearcher()
            filedecrypter()
            decr_file=open(path,'r',encoding="utf8")
            robj=decr_file.read()
            print('Encrypted text:',robj)
            m=robj
            decr_file.close()
            decrypttext()
            decr_menu()
        elif opt3=='4':
            decryptlogsfunc()
            decr_menu()
        else:
            print('Invalid Input. Please try again')
            print('\nPress Enter to continue')
            input()
            decr_menu()
            
    def email_menu():
        global opt4
        global fname
        global body
        global f_name
        global r
        global m
        global key1
        global key
        emailmenu='''
                                              ══════════
                                              EMAIL MENU
                                              ══════════
                                
                        Enter 1 to SEND A REGULAR EMAIL
                        Enter 2 to SEND AN EMAIL WITH ENCRYPTED FILE
                        Enter 3 to SEND AN EMAIL WITH ENCRYPTED TEXT
                        Enter 4 to SEND AN EMAIL WITH ENCRYPTED FILE AND ENCRYPTED TEXT
                        Enter 5 to SEND AN ADVANCED ENCRYPTED EMAIL
                        Enter 6 to VIEW EMAIL LOGS
                        Enter 7 to OPEN EMAIL PRESETS MENU
                        
                        Enter B to go back to MAIN MENU
        '''
        print(emailmenu)
        opt4=input('Enter your option to Email ')
        if opt4.upper()=='B':
            Menufunction()
        elif opt4=='1':
            onlyemailing()
            email_menu()
        elif opt4=='2':
            onlyemailing()
            email_menu()
        elif opt4=='3':
            onlyemailing()
            email_menu()
        elif opt4=='4':
            onlyemailing()
            email_menu()
        elif opt4=='5':
            advinstructions='''
                      ╔════════════════════════════════════════════════════════════════════════════╗
                      ║                                                                            ║
                      ║                        ADVANCED ENCRYPTED EMAIL                            ║
                      ║   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   ║
                      ║ An Advanced Encrypted Email encrypts the text inputted by the user and     ║
                      ║ writes it into a text file (Notepad file). It then automatically encrypts  ║
                      ║ the text file into which the encrypted message has been written into. The  ║
                      ║ encrypted file will be attached to the email. The software will return 2   ║
                      ║ different keys: one for the text in the file and one for the file itself.  ║
                      ║ These 2 keys will be automatically attached to the body of the email. While║
                      ║ Decrypting, the software will first ask the user to input the key to       ║
                      ║ decrypt the file then the key to decrypt the text in the file. The software║
                      ║ will then read the file and display the fully decrypted message.           ║
                      ║                                                                            ║
                      ║ Please note the 2 decryption keys given by the program carefully as the    ║
                      ║ original message cannot be decrypted otherwise.                            ║
                      ╚════════════════════════════════════════════════════════════════════════════╝
                      '''
            print(advinstructions)
            print('Press enter to continue.. ')
            input()
            encrypttext()
            fname=input('Enter the name of the notepad file')
            fname+='.txt'
            with open(fname,'w',encoding="utf-8") as f:
                f.write(r)
            onlyemailing()
            email_menu()
        elif opt4=='6':
            email_logs()
            email_menu()
        elif opt4=='7':
            Presetsfunction()
            email_menu()
            
    def encr_decrlogs():
        encrdecrmenu='''
                            ═════════════════════════════════
                            ENCRYPTION & DECRYPTION LOGS MENU
                            ═════════════════════════════════
                                
                          Enter 1 to OPEN ENCRYPTION LOGS MENU
                          Enter 2 to OPEN DECRYPTION LOGS MENU
                            
                          Enter B to go back to MAIN MENU
        '''
        print(encrdecrmenu)
        logopt=input('Enter your option ')
        if logopt.upper()=='B':
            Menufunction()
        elif logopt=='1':
            encryptlogsfunc()
            encr_decrlogs()
        elif logopt=='2':
            decryptlogsfunc()
            encr_decrlogs()
    def email_logs():
        emaillogsmenu='''
                                                 ═══════════════
                                                 EMAIL LOGS MENU
                                                 ═══════════════
                                            
                                      Enter 1 to VIEW EMAIL LOGS
                                      Enter 2 to SEARCH FOR EMAIL LOG WITH SUBJECT
                                      Enter 3 to DELETE ALL EMAIL LOGS
                                        
                                      Enter B to go back 
        '''
        if opt=='4':
            emailopt='1'
        elif opt=='5':
            print(emaillogsmenu)
            emailopt=input('Enter your option')   
        if opt=='B':
            if opt=='4':
                email_menu()
            elif opt==5:
                Menufunction()
        elif emailopt=='1':
            with open('Email_Logs.csv','r',newline='\n') as emailfile:
                readobj=csv.reader(emailfile)
                for abc in readobj:
                    print('{:<10}  {:<10}  {:<27}  {:<27}  {:<15}  {:<13}  {:<13}  {:<13}  {:<13}'.format(*abc))
            print('\nPress Enter to continue')
            input()
            if opt=='4':
                email_menu()
            else:
                email_logs()
        elif emailopt=='2':
            found=0
            emaillogname=input('Enter the subject of the email for which you would like to see the Email log for: ')
            with open('Email_Logs.csv','r',newline='\n') as eml:
                readobj=csv.reader(eml)
                for abc in readobj:
                    if abc[4].upper()==emaillogname.upper():
                        found=1
                        jkl=['Date','Time','Sender Email','Receiver Email','Subject','File Encr key','Text encr Key','AdvEncr Key1','AdvEncr Key2']
                        print('{:<10}  {:<10}  {:<27}  {:<27}  {:<15}  {:<13}  {:<13}  {:<13}  {:<13}'.format(*jkl))
                        print('{:<10}  {:<10}  {:<27}  {:<27}  {:<15}  {:<13}  {:<13}  {:<13}  {:<13}'.format(*abc))
            if found==0:
                print('Record not found')
            print('\nPress Enter to continue')
            input()
            email_logs()
        elif emailopt=='3':
            print('Press Enter to confirm to DELETE ALL EMAIL LOGS')
            input()
            with open('Email_Logs.csv','r') as infile:
                with open('temp.csv','w',newline='') as outfile:
                    readobj=csv.reader(infile)
                    writerobj=csv.writer(outfile)
                    found=0
                    for abc in readobj:
                        if abc[0]!='Date':
                            pass
                        else:
                            writerobj.writerow(abc)
            os.remove('Email_Logs.csv')
            os.rename('temp.csv','Email_Logs.csv')
            print('All Records Deleted.')
            print('\nPress Enter to continue')
            input()
            email_logs()
    try:
        menu='''
                                ═════════
                                MAIN MENU
                                ═════════
                                
                Enter 1 to open the ENCRYPTION SOFTWARE
                Enter 2 to open the DECRYPTION SOFTWARE
                Enter 3 to SEARCH FOR A FILE
                Enter 4 to open the EMAILING MENU
                Enter 5 to open the EMAIL LOGS MENU
                Enter 6 to open the ENCRYPTION/DECRYPTION LOGS MENU
                
                Enter R to RESTART
                Enter X to EXIT
        '''

        while True:
            print(menu)
            opt=input('Enter your option ')
            if opt.upper()=='R':
                intro()
                Menufunction()
            if opt=='1':
                encr_menu()
            elif opt=='2':
                decr_menu()
            elif opt=='3':
                filesearcher()
            elif opt=='4':
                email_menu()
            elif opt=='5':
                email_logs()
            elif opt=='6':
                encr_decrlogs()
            elif opt.upper()=='X':
                sys.exit('Thank you for using the Encryption Decryption Software!')
            else:
                print('Invalid Input. Please try again')
                
    except Exception:
        print('An Error occured. Please try again')
        Menufunction()
intro()
Menufunction()
