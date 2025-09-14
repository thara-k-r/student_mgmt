# Student Management System (Flask)

A simple Student Management System built with **Python Flask**.  
This app allows you to **add, view, update, and delete** student details such as name, age, course, and grade.

---

## 🚀 Features
- Add a new student  
- View all students  
- Update student details  
- Delete a student  
- SQLite database for storage  

---

## 🛠️ Installation & Setup

### 1. Clone the repo
git clone https://github.com/your-username/student_mgmt.git
cd student_mgmt

### 2. Create a virtual environment
python -m venv venv

Activate it:

- **macOS/Linux**
  source venv/bin/activate

- **Windows**
  venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run the app
python app.py

App will be available at 👉 http://127.0.0.1:5000/

---

## 📂 Project Structure
student_mgmt/
│-- app.py            # Main Flask app
│-- models.py         # Database model (Student)
│-- requirements.txt  # Dependencies
│-- templates/        # HTML templates
│-- static/           # CSS, JS, etc.
│-- .gitignore        # Ignored files

---

## ⚠️ Notes
- Do **NOT** commit students.db to GitHub.  
- Instead, use requirements.txt to install dependencies.  
- Database will auto-create when you first run the app.

---

## 📜 License
This project is open-source and free to use.
