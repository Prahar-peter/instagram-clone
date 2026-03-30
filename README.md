# Instagram Clone - Full Stack Application

A modern Instagram-inspired web application built with Flask and vanilla JavaScript.

## 🎯 Features

- ✅ **User Authentication** - Sign up and login functionality
- ✅ **Post Creation** - Create posts with text and image URLs
- ✅ **Like/Unlike** - Like and unlike posts
- ✅ **Comments** - Add and view comments on posts
- ✅ **Share Posts** - Share post content via clipboard
- ✅ **Modern UI** - Instagram-style interface with responsive design
- ✅ **REST API** - Complete backend API with proper error handling
- ✅ **SQLite Database** - Persistent data storage

## 🏗️ Architecture

### Backend
- **Framework**: Flask (Python)
- **Database**: SQLite with SQLAlchemy ORM
- **API**: RESTful endpoints with JSON responses
- **CORS**: Enabled for frontend access

### Frontend
- **HTML5/CSS3/JavaScript** - No build process required
- **Vanilla JS** - No frontend framework dependencies
- **Fetch API** - For backend communication
- **LocalStorage** - For authentication persistence

### Key Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/users` | POST | Create new user |
| `/api/users/username/<name>` | GET | Get user by username |
| `/api/posts` | GET/POST | Get all posts or create new |
| `/api/posts/<id>` | GET/DELETE | Get or delete post |
| `/api/comments` | POST | Add comment |
| `/api/likes` | POST | Like post |
| `/api/likes/<id>` | DELETE | Unlike post |

## 📦 Project Structure

```
instagram-clone/
├── app/
│   ├── __init__.py       # Flask app factory
│   ├── models.py         # Database models (User, Post, Comment, Like, Follow)
│   └── routes.py         # API endpoints
├── frontend/
│   └── index.html        # Single-page application
├── venv/                 # Python virtual environment
├── run.py                # Application entry point
├── test_api.py          # API tests (23 tests)
├── create_test_users.py # Populate test data
└── .gitignore           # Git ignore rules
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Git (for version control)

### Installation

1. **Clone the repository** (once on GitHub):
```bash
git clone https://github.com/YOUR_USERNAME/instagram-clone.git
cd instagram-clone
```

2. **Create virtual environment**:
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**:
```bash
pip install flask flask-sqlalchemy flask-cors
```

4. **Run the backend**:
```bash
python run.py
```
Backend runs on: `http://localhost:5000`

5. **Run the frontend** (in another terminal):
```bash
cd frontend
python -m http.server 8000
```
Frontend runs on: `http://localhost:8000`

## 🧪 Testing

Run the test suite:
```bash
pytest test_api.py -v
```

All 23 tests should pass ✅

## 📝 Test Users

Pre-populated test users (ready to log in):
- `alice_johnson`
- `bob_smith`
- `charlie_brown`
- `diana_prince`
- `eve_watson`

## 🔄 Network Access

Access from any device on the same network:
- Replace `localhost` with your IP address
- Example: `http://10.106.37.52:8000`

## 📦 Dependencies

### Backend
- Flask 2.3.2
- Flask-SQLAlchemy 3.0.5
- Flask-Cors 4.0.0
- python-dotenv

### Frontend
- None (pure HTML/CSS/JavaScript)

## 🐛 Troubleshooting

### "User not found" error
- Make sure you're using exact test usernames
- Check that the API is running on port 5000

### "Failed to fetch" error
- Verify both frontend (8000) and backend (5000) servers are running
- Check firewall settings if accessing from another device
- Use the correct IP address for network access

### Post creation fails
- Ensure you're logged in with a valid user
- Check API health: `http://localhost:5000/api/health`

## 📋 Database Schema

### User
- id (Primary Key)
- username (Unique)
- email (Unique)
- bio
- created_at

### Post
- id (Primary Key)
- content
- image_url
- user_id (Foreign Key)
- created_at
- updated_at

### Comment
- id (Primary Key)
- text
- user_id (Foreign Key)
- post_id (Foreign Key)
- created_at

### Like
- id (Primary Key)
- user_id (Foreign Key)
- post_id (Foreign Key)
- created_at

## 🚀 Deployment

For production deployment, use a proper WSGI server:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 📄 License

Open source - feel free to use and modify!

## 👨‍💻 Author

Built with ❤️ as a learning project

## 🔗 Push to GitHub

To push this project to GitHub:

1. **Install Git** (if not already installed)

2. **Navigate to project directory**:
```bash
cd f:\Documents\Pthyon\instagram-clone
```

3. **Initialize git** (if not done):
```bash
git init
```

4. **Configure git**:
```bash
git config user.name "Your Name"
git config user.email "your-email@github.com"
```

5. **Add all files**:
```bash
git add .
```

6. **Create initial commit**:
```bash
git commit -m "Initial commit: Instagram Clone - Full Stack App"
```

7. **Create repository on GitHub** at https://github.com/new
   - Name it: `instagram-clone`

8. **Add remote and push**:
```bash
git remote add origin https://github.com/YOUR_USERNAME/instagram-clone.git
git branch -M main
git push -u origin main
```

Done! Your project is now on GitHub! 🎉
