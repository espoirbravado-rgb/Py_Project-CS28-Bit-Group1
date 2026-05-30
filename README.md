# Py_Project-CS28-Bit-Group1
# WattaFaso-Manager 
## Water Distribution Network Management System

---

# 📝 Project Description

**WattaFaso-Manager** is a console-based application developed in Python as part of the *Programming I with Python* module at the Burkina Institute of Technology (BIT).

The project was designed as a simplified management solution for a water distribution organization. It allows users to manage subscribers, monitor water consumption, automate billing, process payments, and generate simple analyses related to network operations.

The main objective of the project was to develop a realistic application integrating the major concepts studied in Python, including:
- object-oriented programming,
- file handling,
- data structures,
- functions,
- modules,
- and software development best practices.

---

# 🚀 Main Features

## 📋 Subscriber Management
- Add new subscribers
- Automatic generation of unique subscriber codes
- Display of subscriber registry
- Management of social and commercial subscribers

## 💧 Consumption Management
- Recording consumption meter readings
- Automatic consumption calculation
- Updating subscriber records

## 💰 Billing and Payments
- Automatic invoice calculation
- Payment management
- Management of unpaid balances
- Change calculation

## ⚠️ Monitoring and Analysis
- Detection of abnormal consumption
- Simple anti-fraud alert system
- Logistical dashboard

## 💾 Data Persistence
- Saving data into text files
- Automatic subscriber loading
- Protection against certain file-reading errors

---

# 🛠️ Technologies Used

- **Language:** Python 3.x
- **Paradigm:** Object-Oriented Programming (OOP)
- **Storage:** Text files (`.txt`)
- **Modules Used:**
  - `datetime`
  - `os`
  - standard Python exception handling

The project follows `snake_case` naming conventions and the main PEP 8 style recommendations.

---

# 📂 Project Structure

```text
WattaFaso-Manager/
│
├── README.md                
├── main.py                  
│
├── data/                    
│   ├── __init__.py          
│   ├── subscribed.txt
│   └── history.txt
│
├── models/                  
│   ├── __init__.py          
│   └── models.py
│
├── services/              
│   ├── __init__.py          
│   ├── services.py
│   └── operations.py
│
└── utils/                   
    ├── __init__.py          
    ├── database.py
    └── config.py
```

## File Description

| File | Role |
|---|---|
| `main.py` | Main entry point of the application |
| `models.py` | Definition of classes and object-oriented logic |
| `database.py` | Data saving and loading management |
| `operations.py` | Business operations management |
| `services.py` | Analytical services and dashboard |
| `config.py` | System constants and configuration parameters |
| `__init__.py` | Allows folders to be treated as importable Python packages |

---

# 📐 Object-Oriented Architecture (OOP)

The project applies the four fundamental principles of object-oriented programming.

## 1. Encapsulation
Sensitive object data is protected using private attributes and manipulated through dedicated methods.

## 2. Abstraction
Internal complexity is hidden behind simple methods to provide a clear and user-friendly system.

## 3. Inheritance
A parent class named `Abonne` is used to centralize shared behaviors.

Two specialized classes inherit from this parent class:
- `SocialSubscriber`
- `CommercialSubscriber`

## 4. Polymorphism
The `calculer_facture()` method is redefined in each class to apply different billing rules depending on the subscriber type.

---

# 📋 Data Structures Used

The project uses several Python data structures in meaningful ways:

## 📘 Dictionaries
The main subscriber registry is stored in a dictionary, allowing fast access using subscriber codes.

## 📗 Lists
Lists are used for temporary storage of alerts and analysis reports.

## 📙 Tuples
Tuples are used to store immutable constants and billing parameters.

---

# 💻 How to Run the Project

## 1. Install Python
Make sure Python 3 is installed on your machine.

## 2. Download the Project
Clone or download the GitHub repository.

## 3. Open a Terminal
Navigate to the project root directory.

## 4. Run the Application

```bash
python main.py
```

## 5. Usage
Use the menu options to navigate through the system.

To exit the application safely:
- use the dedicated exit option,
- or press `Ctrl + C`.

---

# 👨‍💻 Project Team

| Member | GitHub |
|---|---|
| AKPATSI Kossi Magloire | [@espoirbravado-rgb](https://github.com/espoirbravado-rgb) |
| BAGNAN Sonia | [@soniabagnan-commits](https://github.com/soniabagnan-commits) |
| BAGUEYA Bibata | [@bibatabagueya-netizen](https://github.com/bibatabagueya-netizen) |
| BALBONE Arielle Naomie | [@ariellebalbone-hash](https://github.com/ariellebalbone-hash) |
| BAKO Alice Carine | [@BAKOAlice65](https://github.com/BAKOAlice65) |
| BATIANA Abdoul Aziz | [@azizbatiana46-cell](https://github.com/azizbatiana46-cell) |

---

## 👥 Member Contributions
The distribution of tasks was organized by modules and specific responsibilities to ensure architectural consistency and professional delivery:

- **AKPATSI Kossi Magloire (Lead Developer)**: Software architecture, package management, development of `main.py` (entry point), technical drafting of the `README.md`, and content creation for the PowerPoint presentation.
- **BATIANA Abdoul Aziz**: Data persistence and file management (`database.py`), and Visual Designer of the PowerPoint presentation.
- **BAGNAN Sonia**: Development of business logic and operation modules (`operations.py`, `services.py`).
- **BAGUEYA Bibata**: System configuration (`config.py`) and PEP 8 style compliance.
- **BALBONE Arielle Naomie**: Implementation of OOP classes and structures (`models.py`).
- **BAKO Alice Carine**: Data management services and analytical reporting (`services.py`).

  ---
  
# 👥 Acknowledgements

This project was carried out in an academic context at the Burkina Institute of Technology (BIT) for learning purposes related to:
- Python software development,
- object-oriented programming,
- and project management using Git and GitHub.

Special thanks to the teaching staff for their technical guidance and project supervision.
