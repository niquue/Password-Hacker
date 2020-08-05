# Password-Hacker
All sorts of creatures lurk around the Internet, including trolls, pirates, miners – and hackers.
This project connects to a secret server without knowing the password. Using brute force method to generate a password to login to the server.

This project makes use of work with iterators and generators, the itertools module – one of the most powerful features of Python, developing a client app and connecting to a server using the socket module,
and use of JSON and the time module.

# Brute Force
In cryptography, a brute-force attack consists of an attacker submitting many passwords or passphrases with the hope of eventually guessing correctly. The attacker systematically checks all possible passwords and passphrases until the correct one is found. Alternatively, the attacker can attempt to guess the key which is typically created from the password using a key derivation function. This is known as an exhaustive key search. 
A brute-force attack is a cryptanalytic attack that can, in theory, be used to attempt to decrypt any encrypted data[1] (except for data encrypted in an information-theoretically secure manner). Such an attack might be used when it is not possible to take advantage of other weaknesses in an encryption system (if any exist) that would make the task easier.

When password-guessing, this method is very fast when used to check all short passwords, but for longer passwords other methods such as the dictionary attack are used because a brute-force search takes too long. Longer passwords, passphrases and keys have more possible values, making them exponentially more difficult to crack than shorter ones.

Brute-force attacks can be made less effective by obfuscating the data to be encoded making it more difficult for an attacker to recognize when the code has been cracked or by making the attacker do more work to test each guess. One of the measures of the strength of an encryption system is how long it would theoretically take an attacker to mount a successful brute-force attack against it.

Brute-force attacks are an application of brute-force search, the general problem-solving technique of enumerating all candidates and checking each one. 
Source(https://en.wikipedia.org/wiki/Brute-force_attack)
