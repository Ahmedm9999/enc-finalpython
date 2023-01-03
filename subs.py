import random
import json


key = {}
keyname={}
keyslist = {}
keysfound = {}
def main_cli():
    
    while True:
        new_command = input('subs> ')
        if new_command == 'done':
            break
        else:
            mycomm = new_command.split()
            if mycomm[0]=="newkey":
                newkey(mycomm[1])
            elif mycomm[0]=="enc":
                 encrypt(mycomm[1],mycomm[2])

            elif mycomm[0]=="dec":
                 decrypt(mycomm[1],mycomm[2])

            elif mycomm[0]=="save":
                save(mycomm[1])     
            elif mycomm[0]=="load":
                load(mycomm[1])     
            elif mycomm[0]=="info":
                info()     
            else:
                print('no such command')    

def newkey(keyname):

    global keyslist
    global key
    abc='abcdefghijklmnopqrstuvwxyz'  
    abc_list = list(abc)
    abc_shuffled_list = abc_list.copy()  
    random.shuffle(abc_shuffled_list) 
    
    key = { abc_list[i]:abc_shuffled_list[i] for i in range(len(abc_list))}
    keyslist[keyname] = key
    

    # keyslist['my-key'] = key
    # print('A new key called '+ keyslist['my-key'] + ' was created') 

    

def save(filename):

    global keysfound

    newfilename = filename+'.key'
    f1 = open(newfilename,'w')
    json.dump(list(keyslist.values())[-1],f1)

    keysfound[str(list(keyslist.values())[-1])] = filename
    
    print('Enc/Dec keys saved in my-key.key file!') 

def info():

    
    value1 = {i for i in keyslist if keyslist[i]==key}
    print("Current Key :",str(value1))

    #convert key to string

    keystring = str(key)

    if keystring in keysfound:
        print('state: saved in ' + keysfound[keystring])

    else:
        print('state : not saved')  

    # printing the key 
    print('Encryption: \n')
    for x, y in key.items():
        print(x, y)
    
    # printing the key 
    print('Decryption: \n')
    for x, y in key.items():
        print(y, x)

def load(keyfilename):

    global key
    try:
        filename=keyfilename+'.key'
        f1 = open(filename,'r')

        # read the data file the key file
        mykey = f1.read()

        # reconstructing the key as a dictionary
        key = json.loads(mykey)
        print('Key from file ' + keyfilename + ' loaded') 
    except:
        print('No such key')    

def encrypt(originalfile,encryptedfile):


    f = open(originalfile, "r")
    filetext = f.read()


    # keytext = {"a": "h", "b": "i", "c": "m", "d": "v", "e": "s", "f": "t", "g": "q", "h": "y", "i": "r", "j": "j", "k": "a", "l": "d", "m": "k", "n": "b", "o": "z", "p": "l", "q": "n", "r": "x", "s": "p", "t": "u", "u": "f", "v": "o", "w": "e", "x": "c", "y": "w", "z": "g"}
    # filetext = 'nmab'
    
    encrypted=""
    for letter in filetext:
        if letter.lower() in key:   
            encrypted += key[letter]  
            
        else:
            encrypted += letter

    with open(encryptedfile, 'w') as f:
        f.write(encrypted)
    
    print("File " + originalfile + " was encrypted into " + encryptedfile)



def decrypt(encfile,clearfile):
    
    
    swappedkey = {value:key for key, value in key.items()}

   

    print(swappedkey)
    
    # reads the encrypted file
    f = open(encfile, "r")
    filetext = f.read()


    decryptedtext=""

    for letter in filetext:
        if letter.lower() in swappedkey:
            decryptedtext += swappedkey[letter]
        else:
            decryptedtext += letter    

    with open(clearfile, 'w') as f:
        f.write(decryptedtext)
    
    print("File " + encfile + " was decrypted into " + clearfile)

main_cli()           