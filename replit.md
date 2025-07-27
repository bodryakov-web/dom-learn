# JavaScript DOM Course

## Overview

This is a Flask-based web application for a JavaScript DOM learning course. The application provides a structured learning platform with levels, sections, and lessons. It includes an admin panel for content management and uses PostgreSQL (Supabase) as the backend database for storing course content.

## User Preferences

Preferred communication style: Simple, everyday language.
Development approach: Minimal code, simple implementation, optimized for free tier usage.

## System Architecture

### Backend Architecture
The application uses Flask as the web framework with a simple modular structure:
- **Flask Application**: Main web server handling HTTP requests and responses
- **Supabase Integration**: External database service for data persistence
- **Session Management**: Flask sessions for admin authentication
- **Template Rendering**: Jinja2 templates for server-side HTML generation

### Frontend Architecture
- **Static HTML/CSS/JS**: Traditional server-rendered pages with progressive enhancement
- **Tailwind CSS**: Utility-first CSS framework for styling
- **Vanilla JavaScript**: Custom JavaScript for interactive features (quiz, admin panel)
- **Prism.js**: Syntax highlighting for code examples
- **TinyMCE**: Rich text editor for lesson content in admin panel

### Database Architecture
Uses Supabase (PostgreSQL) with the following table structure:
- **levels**: Course levels with ordering
- **sections**: Sections within levels 
- **lessons**: Individual lessons with JSONB content storage

## Key Components

### Core Application (app.py, main.py)
- Flask application setup with basic configuration
- Session management and security settings
- ProxyFix middleware for deployment compatibility

### Data Layer (supabase_client.py, models.py)
- **SupabaseClient**: Wrapper class for database operations
- **Data Models**: Python dataclasses for type consistency
- CRUD operations for levels, sections, and lessons

### Web Routes (routes.py)
- **Public Routes**: Course content viewing (index, level pages, lessons)
- **Admin Routes**: Content management interface
- **Authentication**: Simple login system for admin access
- **File Upload**: Image upload functionality with validation

### Frontend Components
- **Quiz System**: Interactive multiple-choice questions with immediate feedback
- **Responsive Design**: Mobile-first approach using Tailwind CSS
- **Admin Interface**: Content creation and editing tools
- **Code Highlighting**: Syntax highlighting for JavaScript examples

## Data Flow

### Content Viewing Flow
1. User requests course content → Flask routes
2. Routes query Supabase for data → SupabaseClient
3. Data formatted using models → Template rendering
4. HTML served to browser with embedded JavaScript for interactivity

### Admin Content Management Flow
1. Admin login → Session-based authentication
2. Admin creates/edits content → Form submission to Flask
3. Flask validates and processes data → SupabaseClient operations
4. Database updated → Redirect to admin dashboard

### Quiz Interaction Flow
1. Lesson page loads with quiz data → JavaScript initialization
2. User selects answers → Client-side validation and feedback
3. Results calculated and displayed → No server communication needed

## External Dependencies

### Backend Dependencies
- **Flask**: Web framework for Python
- **Supabase**: Backend-as-a-Service for database and authentication
- **Werkzeug**: WSGI utilities (ProxyFix for deployment)
- **PIL/Pillow**: Image processing for file uploads

### Frontend Dependencies
- **Tailwind CSS**: Utility-first CSS framework (CDN)
- **Prism.js**: Syntax highlighting library (CDN)
- **TinyMCE**: Rich text editor for admin panel (CDN)
- **Feather Icons**: Icon library for admin interface (CDN)

### Environment Variables
- `SUPABASE_URL`: Supabase project URL
- `SUPABASE_KEY`: Supabase anon/public API key
- `SESSION_SECRET`: Flask session encryption key

## Deployment Strategy

### Development Setup
- Flask development server on port 5000
- Debug mode enabled for development
- Local environment variables for configuration

### Production Considerations
- Uses ProxyFix middleware for reverse proxy compatibility
- Environment-based configuration
- Session security with configurable secret key
- Image upload with size and type validation

### Hosting Requirements
- Python 3.x environment
- File system access for static assets and uploads
- External Supabase database connection
- Support for environment variables

The application follows a traditional MVC pattern with server-side rendering, making it simple to deploy and maintain while providing a rich learning experience for JavaScript DOM concepts.