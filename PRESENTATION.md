## **Rail Fence Cipher**
is a transposition cipher, **not** substitution cipher, that arranges the plaintext into a zig zag pattern and read in rows starting from the top to bottom (also known as zig zag cipher)  

A **Substitution Cipher** replaces characters from the plaintext into other characters or symbols.

A **Transposition Cipher** scrambles the order of the characters in the plaintext. Characters remain the same.


## **History**
Transposition ciphers were originally invented by the ancient Greeks using the a tool, called the **scytale**.

![image of scytale](https://github.com/Stuycs-K/final-project-3-jianz-wangi/blob/main/scytale.png)

- paper was wrapped around a rod and the message was written across; letters are scrambled after removed from the rod
- sender and reciver must have a rod with the same diameter to decrypt the message

Now, we've simplified the process to paper.

Using the Rail Fence cipher, we can reproduce the same encryption message as the scytale if the number of coils on the rod is the same as the number of rows in the Rail Fence cipher.


## **How it Works** 

Let's work through how the Rail Fence works!!

The Rail fence cipher takes in 2 inputs, the plaintext that we are encrypting and the number of rails (or key) used during encryption.

Plaintext: `cybersecurity is fun!`

Key = `3`

| c |   |   |   | r |   |   |   | u |   |   |   | y |   |   |   | u |   |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|   | y |   | e |   | s |   | c |   | r |   | t |   | i |   | f |   | n |
|   |   | b |   |   |   | e |   |   |   | i |   |   |   | s |   |   |   |

For this cipher, the key is the # of rows we create in our table. Then each character from the plaintext is written diagonally down until you reach the bottom of the key, then you work diagonally up, until you hit the first row again and continnue this pattern until the last letter in your plaintext. This creates the zig zag/rail fence pattern.

To get our ciphertext, we start from the top left corner and read of each letter from left to right, top to bottom.

Ciphertext: `cruyuyescrtifnbeis`

<br>

What happens if we increase the Key = `5` ?

| c |   |   |   |   |   |   |   | u |   |   |   |   |   |   |   | u |   |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|   | y |   |   |   |   |   | c |   | r |   |   |   |   |   | f |   | n |
|   |   | b |   |   |   | e |   |   |   | i |   |   |   | s |   |   |   |
|   |   |   | e |   | s |   |   |   |   |   | t |   | i |   |   |   |   |
|   |   |   |   | r |   |   |   |   |   |   |   | y |   |   |   |   |   |

Ciphertext: `cuuycrfnbeisestiry`

We get a different ciphertext! The message and columns in our table have remained the same, but our Key was changed to 5, so our rows have also been increased to 5.

Now let's try doubling the Key!! (Key = 10)

| c |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|   | y |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | n |
|   |   | b |   |   |   |   |   |   |   |   |   |   |   |   |   | u |   |   
|   |   |   | e |   |   |   |   |   |   |   |   |   |   |   | f |   |   |
|   |   |   |   | r |   |   |   |   |   |   |   |   |   | s |   |   |   |
|   |   |   |   |   | s |   |   |   |   |   |   |   | i |   |   |   |   |
|   |   |   |   |   |   | e |   |   |   |   |   | y |   |   |   |   |   |
|   |   |   |   |   |   |   | c |   |   |   | t |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   | u |   | i |   |   |   |   |   |   |   |   
|   |   |   |   |   |   |   |   |   | r |   |   |   |   |   |   |   |   |

Ciphertext: `cynbuefrssieyctuir`



What do you notice about the ciphertext?

Because the key is so big, every other letter of the ciphertext is the same as the plaintext.



Based off of this situation, what will happen if the Key is greater than the length of Plaintext?

Plaintext = Ciphertext !!



### **Advantages:**  
- Simple and easy to encode
- Doesn’t require specialized software
- Primarily used to teach 

### **Disadvantages:**
- Weak and very vulnerable to a variety of attacks (i.e. brute force, known-plaintext attack, etc.)
- Not effective for longer messages
- Letter frequencies do not change; the same as the unencrypted messages
- The key has severe limitations; Must be less than half the length of the message


### **How do we encode/decode this process?**

*DEMO ON BOARD!!*

[Homework](https://github.com/Stuycs-K/final-project-3-jianz-wangi/blob/main/HOMEWORK.md)


