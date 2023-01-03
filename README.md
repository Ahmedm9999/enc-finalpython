# enc-finalpython

Student's name : Ahmed Massalha
ID : 311575245

In this Assignment, I will create a key to encrypt a file and copy it to another file, and also through the same key I will decrypt and get the original text of the file, every time the user can create a new key whenever the user wishes, and the user can replace the key with another whenever he wants, but when changing the key it will Encrypt the file differently than before.
I will also attach the task requirements step by step, and by running the files, you can make sure that everything works as required, thanks

Read the Substitution cipher from wikipedia.
We'll create a program that can:

- create encryption keys, convert them to decryption keys
- save and load keys to files (ex:  my-key.key)
- accept a clear-text file and encrypt it using an encryption key
- Accept an encrypted file, and decrypt.
- There is always the "current key"  (the created, or loaded key)
- You should write a CLI (command line interface) that a user can use to support all of these actions (see example file).

- Programming instructions:
- Create a directory called "enc" under python
Write a modular program, with different modules for specific tasks; For example:
- an subs module to handle the cli
- enckey file to handle the creation of keys
- Your main file should be called subs.pi
- All code should be placed inside functions, except ONE line that should call the entry function
- Small functions, each function should do just ONE thing, good and meaningful names....
- You cannot submit files, your code should be in your git repository,
