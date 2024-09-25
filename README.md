# **Late Night Inspiration**

## **Project Overview**

### Inspiration Behind the Project
Have you ever experienced a moment where, just before going to sleep, a brilliant idea strikes? You feel the urge to act on it, but the energy to get up and search for more details is gone. Often, we promise ourselves to remember and act on the idea the next day, but more often than not, we forget. 

This exact issue has been my experience for a long time, and I decided it was time to solve it. “Late Night Inspiration” is my solution—a Python-based app designed to capture these fleeting moments of creativity, store them, and give reminders until they are acted upon.

### Problem Statement
Many great ideas are lost due to lack of immediate action or simply forgetting. Late Night Inspiration aims to capture these ideas and ensure they aren't forgotten, providing users with gentle reminders until they have explored or acted upon the idea.

---

## **Tech Stack**

- **Python**: For backend development.
- **FastAPI**: To build a RESTful API for managing ideas.
- **MySQL**: As the primary database for storing ideas and reminders.
- **APScheduler**: For scheduling reminder tasks.
- **Pydantic**: For data validation.
- **Docker (future scope)**: Will be implemented for containerization and easy deployment.
  
---

## **Current Features**

- **Idea Creation**: Users can submit their ideas through the app.
- **Idea Storage**: All ideas are saved securely in a MySQL database.
- **Reminders**: The app will send reminders to ensure the idea is explored or acted upon.
- **CRUD Functionality**: Users can create, read, update, and delete their ideas.
  
---

## **Project Structure**

Here is the structure of the project:

```
project-root/
│
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── endpoints/
│   │   │   │   ├── ideas.py
│   │   │   │   └── users.py
│   │   │   └── __init__.py
│   ├── core/
│   │   └── config.py
│   ├── db/
│   │   ├── init_db.py
│   │   ├── models/
│   │   │   ├── ideas.py
│   │   │   └── users.py
│   │   └── session.py
│   ├── services/
│   │   ├── idea_service.py
│   │   └── user_service.py
│   ├── tasks/
│   │   └── scheduler.py
│   ├── utils/
│   │   └── hashing.py
│   └── main.py
├── tests/
│   ├── test_ideas.py
│   └── test_users.py
├── .env
├── requirements.txt
└── README.md
```

---

## **Setup and Installation**

### Prerequisites
Ensure you have the following installed:
- Python 3.10+
- MySQL
- FastAPI
- APScheduler

### Steps to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/QuantumVik/late_Night_Inspiration.git
   cd late_Night_Inspiration
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up MySQL:
   - Create a new database called `ideas`.
   - Update the `.env` file with your database credentials.

4. Run the app:
   ```bash
   uvicorn app.main:app --reload
   ```

5. Access the API at `http://127.0.0.1:8081`.

---

## **API Endpoints**

### **Ideas**
- **POST /ideas**: Add a new idea.
- **GET /ideas**: Retrieve all ideas.
- **PUT /ideas/clarification/{id}**: Add clarification to an idea.
- **PATCH /ideas/{id}**: Update parts of an idea.
- **DELETE /ideas/{id}**: Delete an idea.

---

## **Future Scope**
I plan to build a full mobile application on Android/iOS in the future, expanding on the current backend functionality. The app will be integrated with notifications to provide users a seamless experience with reminders and idea management.

---

## **Contribution**
Contributions are welcome! If you have any feature requests or find a bug, feel free to create an issue or submit a pull request.

---

## **License**
This project is licensed under the MIT License.

---

This README provides an informative yet personal overview of your project. It also includes future directions and technical details, making it ideal for your GitHub repository.
