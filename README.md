# Encryption Decryption Software
## A Cyber Security Python Project

### **An Overview** <br>
The Encryption & Decryption Software is a Python program developed in the Python IDE.
The main application of this software is to protect files and messages by encrypting them using a key and decrypting them when needed. It also holds the ability to send Emails natively from the python console.
Attachments and body of the Email can be encrypted and sent without logging in through a browser or Email application.
The program can also hold the logs of encryption, decryption and Emailing so that a record can be maintained.
Initial Idea
The idea for this project was born with a small experiment with ASCII values of characters in Python. ASCII, also known as American Standard Code for Information Interchange is a character encoding standard for electronic communication. Each character has its own ASCII value. 
 In Python, we can convert uppercase characters to lowercase characters and vice-versa using ordinal operations of the ASCII value of alphabets. 
Thus, incrementing the ASCII value of each character in a sentence by a random number would render the sentence unreadable unless decrypted. 

### **The Encryption and decryption software** <br>
The Encryption and Decryption software is responsible for all the encrypting and decrypting functions of this project. It can encrypt Text, Images and other types of files.
                        
### **File Encryption** <br>
Files are encrypted by reading the file, obtaining the binary code of the file and performing an XOR operation on the file using the binary code of a randomly generated number between 0 and 256.
The randomly generated number must be between 0 and 256 as the maximum value for byte array is 256.
The file is decrypted by performing a reverse XOR by prompting the user to input the key that was randomly generated and given to the user.

### **Text Encryption** <br>
Text inputted by the user is encrypted by incrementing the ASCII values of each character of the text inputted by the user by a randomly generated number.
While decrypting, the software prompts the user to input the encrypted text and the random number by which the ASCII value of characters were increased. This random number serves as the key for decryption.

### **Advanced Encryption and Decryption** <br>
Advanced encryption encrypts the text inputted by the user and writes it into a text file (Notepad file). It then automatically encrypts the text file into which the encrypted message has been written into. The software will return 2 different keys: one for the text in the file and one for the file itself. 
While decrypting, the software will first ask the user to input the key to decrypt the file then the key to decrypt the text in the file. The software will then read the file and display the fully decrypted message. 

### **Encryption/Decryption Logs** <br>
The software holds the ability to maintain log record of every instance when a file was encrypted or decrypted. It includes the date and time at which the file was encrypted/decrypted, the name of the file and the key to decrypt the file. Encryption and Decryption logs can also be searched with file name.
This function works only when a file is encrypted or decrypted locally in the computer. The Email Logs function will maintain records of Encrypted Files sent using the Emailing Function.

### **The File Searcher** <br>
The File Searcher serves as a local file search engine in the software. It is similar to the File Explorer in Windows. The main application of this function in the software is to find and return the absolute path of a file and use it for encrypting, decrypting or emailing it. 
It prompts the user to input the file name along with its extension. It then asks the user to input the drive in which the file should be searched for.
This process has been achieved by using os.walk to search for the file and os.path.abspath(os.path.join(root,name)) to create the final path. 

### **EMAILING FUNCTION** <br>
The Emailing function is a main segment of this project. It works completely locally from the python console using SMTP (Simple Mail Transfer Protocol) without requiring to open any browser or Email Application. It prompts the user to enter the receiver Email address and gives the option to enter a subject, body and attach files.
Email used in demonstration: kumarpython2021@gmail.com

### **Regular Email**
This operation sends email normally without any encryption of at all. The user can still attach files to the email. 

### **Encrypted Emails** <br>
The encrypted emails operations gives the user an option to encrypt the text (body) and attachments in the email. The software can automatically encrypt and return the keys to decrypt them as and when the user inputs the body or chooses a file for attachment. The software also gives the user an option to send Advance Encrypted Emails. The keys to decrypt all kinds of encryptions will automatically get attached to the body of the email.

### **Email Logs** <br>
Similar to Encryption/Decryption logs, this software holds the ability to maintain log records of every email sent using it. It displays the date and time at which the email was sent, the sender and receiver Email address, the subject of the Email and The Encryption and Decryption Keys if any portion of the Email was encrypted.
The user will have an option to search for Email Logs with the Subject of the email and an option to delete all Email Logs.
	If the body of the Email was encrypted, then the key to decrypt it will be displayed in the Email Logs
	If the Attachment of the email was encrypted, then the key to decrypt the file will be displayed in the Email Logs
	If both Text and Attachment was encrypted the, then the key to decrypt each of them will be displayed in the Email Logs
	If an Advance Encrypted Email was sent then the 2 keys to decrypt it will be displayed in the Email Logs.

### **Email Presets** <br>
In order to provide a more user-friendly interface, the Emailing function has an option to save Email presets so that the user can keep a set of Receiver Emails that he/she uses regularly. This preset can be used while the software prompts the user to input a receiver Email Address.


### **Conclusion** <br>
This is a short synopsis explaining the details of the software. This cyber security themed project has many applications in real life. It can be used to make confidential communications and share files and messages without the fear of it being leaked. It can be used by secret service organizations, military communications and other tech-oriented sectors.
Further improvements can be made to this software by including a user-friendly GUI, a more efficient method to search for files, etc.
Cyber security is currently a high demand branch of Computer Science. As cyber threats continue to increase day by day, both private and government organizations look out for creative and efficient methods to protect their data from falling into the wrong hands. Amidst this, this project serves as an attempt to contribute to protection of data and safe communications.
Footnotes
-	This project was done in parts then compiled and optimized for use as a software, i.e. the file searcher, file encryption/decryption, text encryption/decryption, etc. were programmed in parts then compiled together.
-	In case the user inputs a wrong key while decrypting a file, the file will get permanently corrupted and impossible to recover. It is recommended to be careful while entering the key to decrypt files. However, if a file received  through email is being decrypted then the file can be downloaded again and decrypted using the right key.
-	All inputs prompted by the software have been validated and in case the user inputs something wrong the software will prompt again. Error messages will not be shown by Python IDLE as try-except has been used to show appropriate error messages without breaking the flow of the program.
-	While being sent through email, encrypted files can be decrypted at the receiver’s end only if this software is present on the receiver’s computer.
-	If this software is copied to a portable drive like USB which contains portable python application, then it can be executed in any computer even if it doesn’t have python installed in it. This has been tested and verified.

