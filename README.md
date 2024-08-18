

# Simple Calculator

This project is a *Simple Calculator* developed using C programming. It performs basic arithmetic operations like addition, subtraction, multiplication, and division. This project is ideal for beginners who want to learn the fundamentals of C programming, including working with functions, loops, and conditional statements.

## Features

- *Basic Arithmetic Operations:* The calculator can perform the following operations:
  - Addition (+)
  - Subtraction (-)
  - Multiplication (*)
  - Division (/)

- *User-Friendly Interface:* The program offers a straightforward text-based interface where users can input numbers and choose the desired operation.

- *Input Validation:* The calculator checks for valid input, including preventing division by zero, and provides appropriate error messages.

- *Continuous Operation:* After completing a calculation, the user is prompted to perform another calculation or exit the program.

## Requirements

- A C compiler (such as GCC)
- Basic understanding of C programming, including functions, loops, and conditional statements

## How It Works

1. *User Input:* The program prompts the user to input two numbers and then choose the arithmetic operation they want to perform.

2. *Operation Selection:* Based on the user's input, the program performs the selected arithmetic operation. It handles the four basic operations (addition, subtraction, multiplication, division).

3. *Result Display:* The program displays the result of the calculation to the user.

4. *Continuous Operation:* After displaying the result, the user can choose to perform another calculation or exit the program. The calculator continues to run until the user decides to exit.

5. *Error Handling:* The program includes basic error handling, such as checking for division by zero and ensuring that the user inputs valid numbers.

## Code Structure

- *main.c:* Contains the main function, which drives the program's menu and controls the calculator's flow.
- *calculator.h:* Header file that defines function prototypes and any necessary macros.
- *calculator.c:* Implements the functions for performing the arithmetic operations and handling user input.

## Installation and Usage

1. Clone this repository:
   bash
   git clone https://github.com/yourusername/simple-calculator.git
   
   
2. Navigate to the project directory:
   bash
   cd simple-calculator
   

3. Compile the program:
   bash
   gcc main.c calculator.c -o simpleCalculator
   

4. Run the program:
   bash
   ./simpleCalculator
   

5. *Using the Calculator:* Follow the on-screen prompts to input numbers and select operations. The result will be displayed after each calculation, with an option to perform another calculation or exit.

## Future Enhancements

- *Advanced Operations:* Add more complex operations like exponentiation, square root, and modulus.
- *Graphical User Interface (GUI):* Implement a GUI for a more user-friendly experience.
- *Memory Functions:* Incorporate features like storing previous results for use in subsequent calculations.

## Contributing

Contributions are welcome! If you have ideas for new features or improvements, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

