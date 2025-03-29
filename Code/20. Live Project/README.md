# 🧮 Python GUI Calculator - Final Project

<img src="app screenshot.jpg" alt="Calculator Interface" width="250">
A professional calculator built with Python and Tkinter using MVC architecture

## 📋 Project Overview
**Lecture 20 Implementation** | **March 28, 2025**  
**Instructor**: Shaida Muhammad Sherpao  
**Language**: Python 3.12  
**GUI Framework**: Tkinter

This project is part of Python Ramzan FREE online Course (2025), Pashto.

## 🚀 Features
✅ Basic operations (`+`, `-`, `*`, `/`)  
✅ Error handling (division by zero, invalid inputs)  
✅ Clean, responsive interface  
✅ MVC architecture pattern  
✅ Pashto/English compatible codebase  

## 🛠️ How to Run
# Navigate to project directory
`cd Code/20.\ Live\ Project/`

# Run the calculator
`python main.py` or `Calculator.exe`



## 🏗️ Project Structure
```bash
.
├── main.py          # Application entry point
├── view.py          # GUI implementation (Tkinter)
├── controller.py    # Business logic handler
├── model.py         # Calculation engine
├── styles.py        # UI configuration
├── exceptions.py    # Custom error classes
└── README.md        # This file
```

## 🔧 Key Components
### 1. Model (`model.py`)
- Handles all calculations
- Manages calculator state
- Implements operation logic

### 2. View (`view.py`)
- Creates the user interface
- Button layout and styling
- Display management

### 3. Controller (`controller.py`)
- Mediates between View and Model
- Processes user input
- Manages error states

## 💻 Development Guide
### Adding New Features:
1. **New Operations**:
   ```python
   # In model.py
   def calculate(self):
       if self.operation == '^':
           return self.stored_value ** current_value
   ```

2. **UI Improvements**:
   ```python
   # In styles.py
   SCIENTIFIC_BG = "#5D6D7E"  # New color for scientific buttons
   ```

3. **Extending Functionality**:
   ```python
   # In controller.py
   def handle_scientific(self, func):
       try:
           result = func(self.model.current_input)
           self.view.update_display(result)
       except Exception as e:
           self.view.show_error(str(e))
   ```



## 📚 Learning Resources
1. [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
2. [MVC Pattern Explained](https://realpython.com/the-model-view-controller-mvc-paradigm-summarized-with-legos/)
3. [Python Exception Handling](https://realpython.com/python-exceptions/)

## 👥 How to Contribute
1. Fork the repository
2. Create a new branch (`git checkout -b feature/new-operation`)
3. Commit changes (`git commit -m 'Add square root functionality'`)
4. Push to branch (`git push origin feature/new-operation`)
5. Open a Pull Request

## 📜 License
This project is part of the [Python FREE Online Ramzan Course 2025](https://github.com/ShaidaSherpao/Python-Ramzan-Course-2025)  
Licensed under [MIT License](../../LICENSE)

---

*"The best way to learn is by building real projects!"* - Shaida Muhammad Sherpao