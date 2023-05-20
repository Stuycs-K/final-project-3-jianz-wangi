## **Rail Fence Cipher**
is a transposition cipher, **not** substitution cipher, that arranges the plaintext into a zig zag pattern and read in rows starting from the top to bottom (also known as zig zag cipher)  

A **Substitution Cipher** replaces characters from the plaintext into other characters or symbols.

A **Transposition Cipher** scrambles the order of the characters in the plaintext. Characters remain the same.
<br>

### **History**
Transposition ciphers were originally invented by the ancient Greeks using the a tool, called the **scytale**.

![image of scytale](https://github.com/Stuycs-K/final-project-3-jianz-wangi/blob/main/scytale.png)

- paper was wrapped around a rod and the message was written across; letters are scrambled after removed from the rod
- sender and reciver must have a rod with the same diameter to decrypt the message

Now, we've simplified the process to paper.

Using the Rail Fence cipher, we can reproduce the same encryption message as the scytale if the number of coils on the rod is the same as the number of rows in the Rail Fence cipher.
<br>

### **How it Works** 
rail fence cipher rows and columns    


**Advantages:**  
- simple and easy to encode
- don't need a program

**Disadvantages:**
- weak, can be easily brute forced
- limitation of key = half the length of the message
- letter frequencies are the same as unencrpted messages

<!-- **Encode** 

**Decode** -->

<!-- insert demo here too(?) -->
<br>

### **Homework:**
