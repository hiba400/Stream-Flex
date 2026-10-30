# Stream-Flex – Video Streaming Platform

**React | Flask | SQLite | Cloudflare Workers**

A modern video streaming platform featuring user authentication, video browsing, and video playback. Built with a React frontend and Flask backend, demonstrating full-stack development with Cloudflare Workers deployment support.

## Project Overview

Stream-Flex is a video streaming application that allows users to browse, discover, and watch videos. The platform includes user registration and login functionality, video categorization, and a responsive modern UI built with contemporary React technologies.

### Key Features

- **Video Library**: Browse videos by category (Trending, Popular, Recently Added, Recommended)
- **Video Playback**: Dedicated video player with details page
- **User Authentication**: Sign up and login with password hashing
- **Responsive Design**: Mobile-friendly interface with modern UI components
- **API Integration**: RESTful backend with Flask
- **Database**: SQLite with SQLAlchemy ORM
- **Deployment Ready**: Cloudflare Workers configuration included

## Technology Stack

| Category | Technologies |
|----------|--------------|
| **Frontend** | React 19, TypeScript, Vite, TanStack Router, TanStack Query |
| **Backend** | Flask, Flask-SQLAlchemy, Flask-Migrate, Flask-CORS |
| **Database** | SQLite (currently implemented), PostgreSQL (planned enhancement) |
| **Authentication** | Werkzeug password hashing |
| **Styling** | Tailwind CSS 4, Radix UI components |
| **Deployment** | Cloudflare Workers, Vite |
| **Build Tools** | Bun, Vite, ESLint, Prettier |

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     Frontend (React + Vite)                      │
│                     http://localhost:5173                         │
└──────────────────────┬──────────────────────────────────────────┘
                       │ HTTP
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Backend (Flask API)                           │
│                    http://localhost:5000                         │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│                     SQLite Database                               │
│                     app.db                                        │
└─────────────────────────────────────────────────────────────────┘
```

## Repository Structure

```text
Stream-Flex/
├── backend/                        # Flask backend application
│   ├── app/
│   │   ├── __init__.py            # Flask app factory
│   │   ├── config.py              # Application configuration
│   │   ├── extensions.py          # SQLAlchemy, Migrate, CORS
│   │   ├── models.py              # Video and User models
│   │   └── routes.py              # API endpoints
│   ├── instance/                 # SQLite database (auto-generated)
│   ├── .env                      # Environment variables (empty in repo)
│   ├── requirements.txt          # Python dependencies
│   ├── run.py                    # Application entry point
│   ├── seed.py                   # Database seeding script
│   └── test_auth.py              # Authentication tests
├── frontend/                       # React frontend application
│   ├── src/
│   │   ├── components/           # Reusable UI components
│   │   │   ├── ui/               # Radix UI components
│   │   │   ├── Footer.tsx
│   │   │   ├── HeroBanner.tsx
│   │   │   ├── Loader.tsx
│   │   │   ├── Navbar.tsx
│   │   │   ├── VideoCard.tsx
│   │   │   └── VideoRow.tsx
│   │   ├── routes/               # TanStack Router pages
│   │   │   ├── index.tsx          # Home page
│   │   │   ├── details.$videoId.tsx  # Video details
│   │   │   ├── player.$videoId.tsx   # Video player
│   │   │   ├── login.tsx          # Login page
│   │   │   ├── signup.tsx         # Sign up page
│   │   │   └── __root.tsx        # Root layout
│   │   ├── services/             # API service layer
│   │   │   └── api.ts            # API client
│   │   ├── hooks/                # Custom React hooks
│   │   ├── lib/                  # Utility functions
│   │   ├── types/                # TypeScript types
│   │   ├── main.tsx              # Application entry
│   │   ├── router.tsx            # Router configuration
│   │   └── styles.css            # Global styles
│   ├── public/
│   │   └── favicon.png           # Favicon
│   ├── .env                      # Environment variables
│   ├── .gitignore                # Git ignore patterns
│   ├── bun.lockb                # Bun lock file
│   ├── bunfig.toml              # Bun configuration
│   ├── components.json          # TanStack components config
│   ├── eslint.config.js          # ESLint configuration
│   ├── index.html               # HTML template
│   ├── package.json             # NPM dependencies
│   ├── package-lock.json         # NPM lock file
│   ├── prettier.config.js        # Prettier configuration
│   ├── tsconfig.json            # TypeScript configuration
│   ├── vite.config.ts            # Vite configuration
│   └── wrangler.jsonc           # Cloudflare Workers config
├── .gitignore                    # Git ignore patterns
└── README.md                     # This file
```

## Installation

### Prerequisites

- Python 3.8+
- Node.js 18+ or Bun
- Git

### Backend Setup

1. **Navigate to backend directory**
   ```bash
   cd backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/macOS
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables**
   ```bash
   # Create .env file
   echo "SECRET_KEY=your-secret-key-here" > .env
   echo "DATABASE_URL=sqlite:///app.db" >> .env
   ```

5. **Initialize database**
   ```bash
   python seed.py
   ```

6. **Run backend**
   ```bash
   python run.py
   ```

   Backend will start on `http://localhost:5000`

### Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   # or
   bun install
   ```

3. **Set environment variables**
   ```bash
   # .env file (already exists)
   VITE_API_URL=http://localhost:5000
   ```

4. **Run development server**
   ```bash
   npm run dev
   # or
   bun run dev
   ```

   Frontend will start on `http://localhost:5173`

## API Documentation

### Authentication Endpoints

#### Sign Up
```http
POST /api/signup
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "password123"
}
```

**Response:** `201 Created` with user data

#### Login
```http
POST /api/login
Content-Type: application/json

{
  "email": "john@example.com",
  "password": "password123"
}
```

**Response:** `200 OK` with user data or `401 Unauthorized`

### Video Endpoints

#### Get All Videos
```http
GET /api/videos
```

**Response:** Array of video objects

#### Get Single Video
```http
GET /api/videos/<video_id>
```

**Response:** Single video object

### Data Models

#### Video
```json
{
  "id": 1,
  "title": "Big Buck Bunny",
  "description": "Video description",
  "thumbnail_url": "https://...",
  "video_url": "https://...",
  "duration": "10 min",
  "category": "Trending"
}
```

#### User
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}
```

## Features by Page

### Home Page (`/`)
- Hero banner with call-to-action
- Video rows by category (Trending, Popular, Recently Added, Recommended)
- Video cards with thumbnails and metadata
- Responsive grid layout

### Video Details (`/details/:videoId`)
- Detailed video information
- Thumbnail and metadata display
- Link to video player

### Video Player (`/player/:videoId`)
- HTML5 video player
- Full-screen support
- Video controls

### Login (`/login`)
- Email and password form
- Authentication with backend
- Error handling

### Sign Up (`/signup`)
- Name, email, and password form
- Password validation
- User registration

## Database Seeding

The project includes a seeding script (`seed.py`) that populates the database with sample videos from Google's sample video library. Categories include:
- Trending
- Popular
- Recently Added
- Recommended

Run the seeder:
```bash
cd backend
python seed.py
```

## Cloudflare Workers Deployment

The project includes Cloudflare Workers configuration (`wrangler.jsonc`) for serverless deployment.

### Deployment Steps

1. **Build the frontend**
   ```bash
   cd frontend
   npm run build
   ```

2. **Configure Cloudflare Workers**
   ```bash
   npx wrangler login
   ```

3. **Deploy**
   ```bash
   npx wrangler deploy
   ```

## Security Considerations

- **Password Hashing**: Uses Werkzeug's `generate_password_hash` with BCrypt
- **SQL Injection Prevention**: SQLAlchemy ORM with parameterized queries
- **CORS**: Configured for API access
- **Environment Variables**: Sensitive data in `.env` files (not committed)
- **Input Validation**: Basic validation on backend endpoints

**Important**: Change `SECRET_KEY` in production. Use a strong, randomly generated key.

## Testing

### Authentication Tests

Run the included authentication test suite:
```bash
cd backend
python test_auth.py
```

Tests cover:
- User registration
- Duplicate email handling
- Login with valid credentials
- Login with invalid credentials

## Troubleshooting

### Backend Won't Start

1. Check Python version (3.8+ required)
2. Ensure virtual environment is activated
3. Verify dependencies are installed
4. Check database file permissions

### Frontend Won't Start

1. Check Node.js version (18+ required)
2. Ensure dependencies are installed
3. Verify `VITE_API_URL` in `.env` matches backend URL
4. Check port 5173 is not in use

### API Connection Errors

1. Ensure backend is running on port 5000
2. Check CORS configuration in `backend/app/__init__.py`
3. Verify `VITE_API_URL` in frontend `.env`
4. Check browser console for specific error messages

### Database Issues

1. Delete `backend/instance/app.db` and re-run `seed.py`
2. Check SQLite write permissions
3. Verify database URL in `.env`

## Development Tools

### Code Formatting

```bash
cd frontend
npm run format    # Prettier
npm run lint      # ESLint
```

### Build Production

```bash
cd frontend
npm run build
```

### Preview Production Build

```bash
cd frontend
npm run preview
```

## Implementation Status

| Feature | Status | Notes |
|---------|--------|-------|
| Video Browsing | ✅ Complete | Categories, search |
| Video Playback | ✅ Complete | HTML5 player |
| User Authentication | ✅ Complete | Signup/Login |
| Password Hashing | ✅ Complete | BCrypt |
| Database Seeding | ✅ Complete | Sample videos |
| API Endpoints | ✅ Complete | RESTful API |
| Responsive UI | ✅ Complete | Mobile-friendly |
| Cloudflare Deployment | ✅ Configured | wrangler.jsonc |
| Video Upload | ⏳ Not Implemented | |
| User Profiles | ⏳ Not Implemented | |
| Video Categories Management | ⏳ Not Implemented | |
| Search Functionality | ⏳ Not Implemented | |
| Comments/Reviews | ⏳ Not Implemented | |

## Future Enhancements

- Video upload functionality
- User profile management
- Video categorization by users
- Advanced search and filtering
- Comments and reviews system
- Watch history and favorites
- Video recommendations based on viewing history
- PostgreSQL database support for production scalability
- Video streaming optimization
- Subtitle support
- Progress tracking

## Database Implementation Note

**Current Implementation**: The project currently uses SQLite as the database. This is a lightweight, file-based database suitable for development and small-scale deployments.

**Planned Enhancement**: PostgreSQL support is planned for production environments to enable better scalability, concurrent access, and advanced database features. The application is architected to support database migration through SQLAlchemy's database abstraction layer.

## License

No license has been selected for this project. All rights reserved to the author.

## Author

**Hiba Ben Adou**

Computer Engineering Student – ENSA Tangier

This project demonstrates full-stack web development with React and Flask, modern UI design with Radix UI and Tailwind CSS, and cloud deployment with Cloudflare Workers.
