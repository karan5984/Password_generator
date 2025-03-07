# Password_generator

# Random Password Generator

## 📌 Overview
This is a **Random Password Generator** written in Python. The program allows users to create secure passwords based on different categories, such as numbers, lowercase letters, uppercase letters, and symbols. Users can also choose the password length and opt for unique characters.

## 🚀 Features
- Generates random passwords based on user-specified categories:
  - Numeric (0-9)
  - Lowercase letters (a-z)
  - Uppercase letters (A-Z)
  - Symbols (~, @, #, $, %, &, *, ?, -, _)
- Allows users to input their desired password length.
- Users can select multiple categories at once.
- Ensures uniqueness in passwords if required.
- Provides instructions and details about password generation.
- Uses Python's `random` module for secure password generation.

## 🛠️ Installation
To run this program on your local machine:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/random-password-generator.git
   ```
2. **Navigate to the project directory:**
   ```sh
   cd random-password-generator
   ```
3. **Run the Python script:**
   ```sh
   python password_generator.py
   ```

## 📖 Usage
Upon running the script, you will be presented with a task menu:
```
TASK LIST:
1️⃣ Generate Password
2️⃣ Instructions/Information
3️⃣ Exit the Program
```
### 🎯 How to Generate a Password
1. Select option `1` to generate a password.
2. Enter the desired password length.
3. Choose one or multiple categories for the password:
   - `1` for Numeric
   - `2` for Lowercase Letters
   - `3` for Uppercase Letters
   - `4` for Symbols
   - `5` for Default (All categories included)
4. Choose whether you want unique characters in your password (`y/n`).
5. Your secure password will be generated and displayed.
6. Press `Enter` to generate another password with the same settings, or `1` to modify the settings.

## 🖥️ Example Run
```
Enter the length for the password: 12
Choose category numbers: 134
Do you want every character in your password to be unique? (y/n): y

Your password: A8$4r?F2-@K3
```

## 🤝 Contributing
If you’d like to contribute to this project, feel free to:
- Fork the repository
- Create a new branch (`git checkout -b feature-branch`)
- Make your changes and commit (`git commit -m 'Added a new feature'`)
- Push to your branch (`git push origin feature-branch`)
- Open a Pull Request

## 🌟 Support
If you find this project helpful, feel free to give it a ⭐ on GitHub!

