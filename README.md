---

# **IT Support Ticketing System**

This project is a simple IT Support Ticketing System designed to allow users to create, categorize, and store support tickets based on their urgency level (`Low`, `Medium`, or `High`). The system includes a Flask backend, a PostgreSQL database for storing ticket information, and an HTML frontend for user interaction.

---

## **Features**
- Users can submit support tickets via an intuitive HTML form.
- Tickets are categorized by urgency: `Low`, `Medium`, or `High`.
- Tickets include the customer's name, issue description, urgency level, and department.
- Data is stored in a PostgreSQL database, with separate tables for each urgency level.
- The system is designed to handle common operations like:
  - **Create**: Submit a new support ticket.
  - **Database Schema Management**: Automatically creates or updates tables as required.

---

## **Technologies Used**
1. **Backend**: Flask (Python)
2. **Frontend**: HTML, CSS, JavaScript
3. **Database**: PostgreSQL
4. **Library**: Flask-CORS for cross-origin request handling

---

## **Setup and Installation**

### **1. Prerequisites**
- Python 3.x installed
- PostgreSQL installed and running
- Basic knowledge of terminal/command prompt

---

### **2. Clone the Repository**
Clone the project repository:
```bash
git clone https://github.com/your-repository-url.git
cd your-repository-folder
```

---

### **3. Set Up the Database**
1. Log in to your PostgreSQL server:
   ```bash
   psql -U postgres
   ```
2. Create a database named `ticket_system`:
   ```sql
   CREATE DATABASE ticket_system;
   ```
3. Exit `psql`:
   ```bash
   \q
   ```

---

### **4. Install Dependencies**
Install the required Python libraries using pip:
```bash
pip install flask psycopg2 flask-cors
```

---

### **5. Configure the Database Schema**
Run the `main.py` script to create or update the necessary database tables:
```bash
python main.py
```

---

### **6. Start the Flask Backend**
Run the Flask app:
```bash
python Flask_Backup.py
```
The backend will start on `http://localhost:5000`.

---

### **7. Open the Frontend**
1. Open the `Main Page.html` file in your browser.
2. Fill out the form with the following fields:
   - **Customer Name**
   - **Issue Description**
   - **Urgency**: Select from `Low`, `Medium`, or `High`.
   - **Department**: Select from `IT Networking`, `IT Software`, `IT Hardware`, or `IT Support`.
3. Click **Submit Ticket** to save the data.

---

## **How It Works**

1. **HTML Form Submission**:
   - The form sends a POST request to the Flask backend at `http://localhost:5000/tickets`.

2. **Flask Backend**:
   - Validates the incoming data.
   - Determines the urgency level and inserts the ticket into the appropriate table (`low_urgency`, `medium_urgency`, or `high_urgency`).

3. **PostgreSQL Database**:
   - Stores ticket information for each urgency level in separate tables.

---

## **Testing the System**
- Submit a ticket through the HTML form and check the database to verify the data:
   ```sql
   SELECT * FROM low_urgency;
   SELECT * FROM medium_urgency;
   SELECT * FROM high_urgency;
   ```

---

## **Project File Structure**
```
|-- Flask_Backup.py          # Flask backend for ticket handling
|-- main.py                  # Script to create/update database tables
|-- Main Page.html           # Frontend HTML form for ticket submission
|-- README.md                # Documentation for the project
```

---

## **Example Usage**

### **Submitting a Ticket**
- **Customer Name**: John Doe  
- **Issue Description**: Cannot access the company VPN.  
- **Urgency**: High  
- **Department**: IT Networking  

The data will be saved in the `high_urgency` table and assigned a unique `ticket_id`.

---

## **Future Enhancements**
- Add ticket retrieval functionality (View All Tickets).
- Implement user authentication for ticket management.
- Add email notifications for submitted tickets.
- Enhance the UI with a modern framework (e.g., React or Bootstrap).

---

## **License**
This project is licensed under the MIT License. Feel free to use and modify it as needed.

---
