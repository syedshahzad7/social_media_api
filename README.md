# Social Media API

A robust, production-ready REST API for a social media platform built with FastAPI, featuring user authentication, post management, and voting functionality.

## Features

- **User Authentication & Authorization**: Secure JWT-based authentication system
- **Post Management**: Full CRUD operations for creating, reading, updating, and deleting posts
- **Voting System**: Users can upvote/downvote posts with conflict prevention
- **Search & Pagination**: Query posts with search filters, limit, and offset parameters
- **Database Migrations**: Managed with Alembic for version-controlled schema changes
- **Comprehensive Testing**: Full test suite with pytest covering all endpoints
- **CI/CD Pipeline**: Automated testing and Docker deployment via GitHub Actions
- **Containerization**: Docker and Docker Compose setup for easy deployment

## Technology Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Authentication**: JWT (python-jose)
- **Password Hashing**: bcrypt via passlib
- **Database Migrations**: Alembic
- **Testing**: pytest
- **Containerization**: Docker & Docker Compose
- **CI/CD**: GitHub Actions
- **CORS**: Enabled for cross-origin requests

## Prerequisites

- Python 3.13+
- PostgreSQL
- Docker & Docker Compose (for containerized deployment)

## 🔧 Installation & Setup

### Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate 
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   DATABASE_HOSTNAME=localhost
   DATABASE_PORT=5432
   DATABASE_PASSWORD=your_password
   DATABASE_NAME=social-media-api
   DATABASE_USERNAME=postgres
   SECRET_KEY=your_secret_key_here
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

5. **Run database migrations**
   ```bash
   alembic upgrade head
   ```

6. **Start the development server**
   ```bash
   uvicorn app.main:app --reload
   ```

   The API will be available at `http://localhost:8000`

### Docker Deployment

1. **Build and run with Docker Compose**
   ```bash
   docker-compose -f docker-compose-prod.yml up -d
   ```

   The API will be available at `http://localhost:80`

## API Documentation

Once the server is running, visit:
- **Interactive API docs (Swagger UI)**: `http://localhost:8000/docs`
- **Alternative API docs (ReDoc)**: `http://localhost:8000/redoc`

## API Endpoints

### Authentication
- `POST /login` - User login (returns JWT token)

### Users
- `POST /users/` - Create new user account
- `GET /users/{id}` - Get user by ID

### Posts
- `GET /posts/` - Get all posts (supports search, pagination)
- `POST /posts/` - Create new post (authenticated)
- `GET /posts/{id}` - Get specific post
- `PUT /posts/{id}` - Update post (owner only)
- `DELETE /posts/{id}` - Delete post (owner only)

### Votes
- `POST /vote/` - Vote on a post (1 to upvote, 0 to remove vote)

## Running Tests

```bash
pytest -v -s
```

The test suite includes:
- User authentication tests
- Post CRUD operation tests
- Voting system tests
- Authorization and permission tests

## Database Schema

### Users Table
- `id` (Primary Key)
- `email` (Unique)
- `password` (Hashed)
- `created_at`
- `phone_number`

### Posts Table
- `id` (Primary Key)
- `title`
- `content`
- `published`
- `created_at`
- `owner_id` (Foreign Key → Users)

### Votes Table
- `user_id` (Primary Key, Foreign Key → Users)
- `post_id` (Primary Key, Foreign Key → Posts)

## CI/CD Pipeline

The project includes a GitHub Actions workflow that:
1. Runs all tests in an isolated environment
2. Builds a Docker image
3. Pushes the image to Docker Hub
4. Triggers on every push and pull request

## Security Features

- Password hashing with bcrypt
- JWT token-based authentication
- Protected routes requiring authentication
- Owner-based authorization for post modifications
- SQL injection prevention through SQLAlchemy ORM
- CORS configuration for controlled access


## Deployment

The application is containerized and can be deployed to any cloud platform supporting Docker:
- AWS (ECS, EC2)
- Google Cloud Platform
- Azure
- DigitalOcean
- Heroku


