# Library Management System 🌐📚

A distributed system for managing library operations with separate Frontend and Admin APIs, built using FastAPI, MongoDB, PostgreSQL, and Redis.

## 🚀 Overview

This library management application provides a robust, scalable solution for library operations, featuring separate APIs for frontend and admin functionalities.

## ✨ Features

### 👤 Frontend API (MongoDB)
- User enrollment with detailed profile information
- Advanced book browsing with comprehensive filters
- Flexible book borrowing system
- Real-time catalogue updates

### 🔧 Admin API (PostgreSQL)
- Comprehensive book catalogue management
- User enrollment tracking
- Detailed borrowing status monitoring
- Cross-service data synchronization

## 🛠 Technologies Stack

| Category | Technologies |
|----------|--------------|
| Web Framework | FastAPI |
| Frontend Database | MongoDB |
| Admin Database | PostgreSQL |
| Caching/Messaging | Redis |
| Containerization | Docker |
| ODM/ORM | Beanie, SQLAlchemy |

## 📂 Project Structure
```
library-app/
├── frontend/     # Frontend API service
├── admin/        # Admin API service
└── docker-compose.yml
```

## 🔧 Installation & Setup

### Prerequisites
- Docker
- Docker Compose

### Quick Start
```bash
# Clone the repository
git clone https://github.com/yourusername/library-management-system.git
cd library-management-system

# Start services
docker-compose up --build
```

## 🌐 API Endpoints

### Frontend API (http://localhost:8000)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/users/` | POST | Enroll new user |
| `/books/` | GET | List available books |
| `/books/{id}` | GET | Get book details |
| `/books/{id}/borrow` | POST | Borrow a book |

### Admin API (http://localhost:8001)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/admin/books/` | POST | Add new book |
| `/admin/books/{id}` | DELETE | Remove book |
| `/admin/users/` | GET | List all users |
| `/admin/borrowed-books/` | GET | List borrowed books |

## 🔄 Data Synchronization

### Book Updates Workflow
1. Admin API publishes changes to Redis
2. Frontend API subscribes to Redis channels
3. Real-time sync between PostgreSQL and MongoDB

### User & Borrowing Data Flow
1. Frontend API publishes user activities
2. Admin API maintains read-optimized data

## 🧪 Testing

### Running Tests
```bash
# Frontend tests
docker-compose exec frontend pytest app/

# Admin tests
docker-compose exec admin pytest app/
```