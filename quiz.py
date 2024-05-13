questions = ("What does HTTPS stand for?",
             "2.Which of the following is NOT an example of a strong password?",
             "3.What does IoT stand for?",
             "4.What type of attack involves flooding a network or server with excessive traffic to disrupt normal operation?",
             "5.What is the purpose of a VPN?",
             "6.What is the first line of defense against malware?",
             "7.What is the term for an authorized individual gaining access to data or systems beyond their permission level?")

options = (("A. HyperText Transfer Protocol Secure", "B. HyperText Transfer Protocol Standard",
            "C. HyperText Transfer Program Server", "D. HyperText Transfer Procedure Service"),
           ("A. 123456", "B. P@ssw0rd!", "C. CorrectHorseBatteryStaple", "D. Tr0ub4dor&3"),
           ("A. Internet of Things", "B. Internet over Telephone", "C. Internal Operating Technology",
            "D. Internet over Transmission"),
           ("A. Phishing", "B. Spoofing", "C. DDoS (Distributed Denial of Service)", "D. Man-in-the-Middle"),
           ("A. To speed up internet connection", "B. To create a secure connection over a public network",
            "C. To store passwords securely", "D. To protect against viruses"),
           ("A. Anti-virus software", "B. Firewall", "C. User awareness and education",
            "D. Intrusion Detection System (IDS)"),
           ("A. Hacking", "B. Cracking", "C. Unauthorized access", "D. Insider threat"))

answers = ("A", "A", "A", "C", "B", "C", "D")

guesses = []
score = 0
question_numbers = 0

for question in questions:
    print("________________________________________________________")
    print(question)
    for option in options[question_numbers]:
        print(option)

    guess = input("Enter (A, B, C, D) ").upper()
    guesses.append(guess)
    if guess == answers[question_numbers]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_numbers]} is the correct answer")
    question_numbers += 1

print("________________________________________________________")
print("                       RESULTS                          ")
print("________________________________________________________")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()
print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")

