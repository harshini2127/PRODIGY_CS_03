# PRODIGY_CS_03
Password Complexity Checker with real-time analysis, gauge meter, and crack time estimation using Python and Tkinter.

# 🔐 Password Complexity Checker

## 📌 Project Overview

This project is a GUI-based Password Complexity Checker developed using Python and Tkinter. The application analyzes password strength in real-time based on various security parameters such as password length, uppercase letters, lowercase letters, numbers, and special characters.

The tool provides:

* Password strength analysis
* Real-time feedback
* Crack time estimation
* Dynamic semicircle gauge meter
* Password improvement suggestions

The project was designed to simulate modern password security analysis systems used in cybersecurity applications.

# 🚀 Features

✅ Real-time password analysis

✅ GUI-based application using Tkinter

✅ Show/Hide password functionality

✅ Password strength classification

✅ Dynamic semicircle gauge meter

✅ Moving needle indicator based on strength

✅ Estimated password crack time

✅ Password improvement suggestions

✅ Regex-based password validation

✅ Modern dark-themed user interface

# 🔧 Techniques Used

* Password Complexity Analysis
* Regular Expressions (Regex)
* Real-Time Event Handling
* GUI Development using Tkinter
* Canvas Graphics & Dynamic Needle Movement
* Password Security Policy Validation
* User Input Validation
* Dynamic UI Updates

# 🧠 Password Analysis Criteria

The application evaluates passwords based on:

| Criteria           | Description                              |
| ------------------ | ---------------------------------------- |
| Length             | Minimum 8 characters                     |
| Uppercase Letters  | At least one uppercase letter            |
| Lowercase Letters  | At least one lowercase letter            |
| Numbers            | At least one numeric digit               |
| Special Characters | At least one symbol or special character |

# 🔐 Password Strength Levels

| Score | Strength    |
| ----- | ----------- |
| 0 – 1 | Too Weak    |
| 2     | Weak        |
| 3     | Medium      |
| 4     | Strong      |
| 5     | Very Strong |

# ⏳ Crack Time Estimation

The application estimates approximate password cracking difficulty based on password strength.

Examples:

* Few Seconds
* Few Hours
* Several Months
* Several Years

# 🛠️ Technologies Used

* Python
* Tkinter
* Regular Expressions (`re` module)
* VS Code
* Git & GitHub

# 🎨 GUI Features

* Fullscreen responsive window
* Dark cybersecurity-themed interface
* Real-time password monitoring
* Interactive semicircle strength meter
* Dynamic moving needle visualization
* Live feedback system

# 🧠 How the Project Works

## 🔹 Password Input

The user enters a password into the input field.

## 🔹 Real-Time Analysis

As the user types:

* the password is analyzed automatically
* strength level updates dynamically
* feedback suggestions appear instantly

## 🔹 Regex Validation

The application uses Regular Expressions (`re`) to validate:

* uppercase letters
* lowercase letters
* digits
* special symbols

Example:

re.search(r"[A-Z]", password)

## 🔹 Gauge Meter

A semicircle gauge meter visually represents password strength using:

* dynamic needle movement
* strength levels from 0 to 5

## 🔹 Crack Time Estimation

The system estimates how difficult the password would be to crack based on its complexity score.

# ▶️ How to Run the Project

## 1️⃣ Clone Repository

git clone https://github.com/harshini2127/PRODIGY_CS_03.git

## 2️⃣ Navigate to Project Folder

cd PRODIGY_CS_03

## 3️⃣ Run the Program

python password_checker.py

# 📸 Screenshots

## Main GUI

<img width="1920" height="1080" alt="gui (2)" src="https://github.com/user-attachments/assets/836dbd20-2820-4def-9d97-a85bf2092c07" />

## Weak Password Detection

<img width="1920" height="1080" alt="too week" src="https://github.com/user-attachments/assets/46e73929-bdf1-4f2e-9201-e3c1b0179fd8" />

## Strong Password Detection

<img width="1920" height="1080" alt="very strong" src="https://github.com/user-attachments/assets/f6cda921-3658-4a89-9dee-d973d1da88de" />

# ⚠️ Limitations

* Crack time estimation is approximate and educational.
* The project does not check against online leaked password databases.
* Password entropy calculations are simplified.

# 🔮 Future Improvements

* Password entropy calculation
* Breached password detection using APIs
* Password generator integration
* Database-based password blacklist
* Export security reports
* Advanced password policy customization
* Animated gauge transitions
* Multi-theme support

# 👩‍💻 Author

Harshini Yekkaladevi

Cyber Security Student | Python Developer | SOC Analyst Aspirant
