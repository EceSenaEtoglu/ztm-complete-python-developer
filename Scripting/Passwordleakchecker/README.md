# Password Leak Checker

This project is my implementation of an exercise from the course "ZTM Python Developer Zero To Mastery."

## What is it?

Password Leak Checker allows you to determine how many times the passwords you provide have been detected in data breaches, using the following source: [Have I Been Pwned](https://haveibeenpwned.com/Passwords).

To get started, follow these steps:
1. Check the "Is It Safe To Use" section below.
2. Prepare a text file containing passwords (one per line) that you want to check against data breaches.

## How does it work?

The script leverages the API of Have I Been Pwned (HIBP). Passwords are hashed using the SHA-1 algorithm. However, only the first 5 characters of the hash are sent to HIBP, as outlined in this [implementation guide](https://blog.cloudflare.com/validating-leaked-passwords-with-k-anonymity/).

For a comprehensive explanation, please refer to the [Have I Been Pwned Passwords page](https://haveibeenpwned.com/Passwords).

## Is it safe to use?

According to [HIBP's privacy statement](https://haveibeenpwned.com/Privacy), "HIBP never receives the original password nor enough information to discover the original password." Additionally, no identifying information about the password owner is stored.

While it's fun to test common passwords like "hello" or "1234," it's important to note that this tool **might not be safe for use with your own passwords**. 

After some research I saw that it is pointed out in [Vertex Cyber Security's article](https://www.vertexcybersecurity.com.au/should-i-use-have-i-been-pwned-hibps/), the hashing method (SHA-1) used here is no longer considered secure. However the creator of the website "Troy Hunt" is a well known web security consultant.

Since security was not the point of the exercise, I'm publishing this project.
