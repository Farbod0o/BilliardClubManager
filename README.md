# BilliardClubManager 🎱

BilliardClubManager is a web application designed for managing billiard clubs. It allows club managers to track table usage, calculate costs based on time played, and generate daily and monthly revenue reports. The project uses Flask and Socket.IO for real-time updates and includes a responsive front end for easy monitoring.

---

## Features

- **Table Management**: Start and stop sessions for each billiard table.
- **Real-Time Notifications**: Updates table status and cost calculations in real-time.
- **Revenue Tracking**: Calculates daily and monthly revenue reports.
- **Responsive Interface**: Access the app on desktops, tablets, and mobile devices.

---

## Installation

### Prerequisites

- Python 3.7+
- Flask and Flask-SocketIO
- SQLAlchemy for database management
- Eventlet or Gevent for real-time functionality

### Step-by-Step Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/BilliardClubManager.git
   cd BilliardClubManager
2. Run the application:

   ```bash
   python app.py
3. Access the application at http://localhost:5000 in your web browser.

### Technologies Used
Backend: Flask, Flask-SocketIO, SQLAlchemy
Frontend: HTML, CSS, JavaScript
Real-Time Communication: Eventlet for Socket.IO support
Database: SQLite 

### License
This project is licensed under the MIT License.

