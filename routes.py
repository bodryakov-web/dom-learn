import os
import json
import logging
from flask import render_template, request, redirect, url_for, jsonify, session, flash
from werkzeug.utils import secure_filename
from app import app
from supabase_client import supabase_client
from models import create_sample_lesson_content
import uuid
from PIL import Image
import io

logger = logging.getLogger(__name__)

# Admin credentials
ADMIN_LOGIN = "bodryakov.web"
ADMIN_PASSWORD = "Anna-140275"

# Allowed image extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp', 'svg'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def is_admin():
    return session.get('admin_logged_in', False)

@app.route('/')
def index():
    """Main page showing all levels and sections"""
    initialize_sample_data()  # Create sample data if needed
    levels = supabase_client.get_all_levels()
    
    # Get sections for each level
    levels_with_sections = []
    for level in levels:
        sections = supabase_client.get_sections_by_level(level['id'])
        level_data = level.copy()
        level_data['sections'] = sections
        levels_with_sections.append(level_data)
    
    return render_template('index.html', levels=levels_with_sections)

@app.route('/level-<int:level_order>')
def level_page(level_order):
    """Level page showing sections and lessons"""
    levels = supabase_client.get_all_levels()
    level = None
    
    for l in levels:
        if l['order_index'] == level_order:
            level = l
            break
    
    if not level:
        return "Level not found", 404
    
    sections = supabase_client.get_sections_by_level(level['id'])
    
    # Get lessons for each section
    sections_with_lessons = []
    for section in sections:
        lessons = supabase_client.get_lessons_by_section(section['id'])
        section_data = section.copy()
        section_data['lessons'] = lessons
        sections_with_lessons.append(section_data)
    
    return render_template('level.html', level=level, sections=sections_with_lessons)

@app.route('/level-<int:level_order>/section-<int:section_order>-<section_name>/lesson-<int:lesson_order>-<lesson_name>')
def lesson_page(level_order, section_order, section_name, lesson_order, lesson_name):
    """Individual lesson page"""
    levels = supabase_client.get_all_levels()
    level = None
    
    for l in levels:
        if l['order_index'] == level_order:
            level = l
            break
    
    if not level:
        return "Level not found", 404
    
    sections = supabase_client.get_sections_by_level(level['id'])
    section = None
    
    for s in sections:
        if s['order_index'] == section_order:
            section = s
            break
    
    if not section:
        return "Section not found", 404
    
    lessons = supabase_client.get_lessons_by_section(section['id'])
    lesson = None
    
    for l in lessons:
        if l['order_index'] == lesson_order:
            lesson = l
            break
    
    if not lesson:
        return "Lesson not found", 404
    
    # Find previous and next lessons
    current_index = None
    for i, l in enumerate(lessons):
        if l['id'] == lesson['id']:
            current_index = i
            break
    
    prev_lesson = None
    next_lesson = None
    if current_index is not None:
        if current_index > 0:
            prev_lesson = lessons[current_index - 1]
        if current_index < len(lessons) - 1:
            next_lesson = lessons[current_index + 1]
    
    return render_template('lesson.html', 
                         level=level, 
                         section=section, 
                         lesson=lesson, 
                         lessons=lessons,
                         prev_lesson=prev_lesson,
                         next_lesson=next_lesson)

# Admin routes
@app.route('/bod')
def admin_login():
    """Admin login page"""
    if is_admin():
        return redirect(url_for('admin_dashboard'))
    return render_template('admin/login.html')

@app.route('/bod/login', methods=['POST'])
def admin_login_post():
    """Handle admin login"""
    login = request.form.get('login')
    password = request.form.get('password')
    remember = request.form.get('remember') == 'on'
    
    if login == ADMIN_LOGIN and password == ADMIN_PASSWORD:
        session['admin_logged_in'] = True
        if remember:
            session.permanent = True
            app.permanent_session_lifetime = 30 * 24 * 60 * 60  # 30 days
        return redirect(url_for('admin_dashboard'))
    else:
        flash('Неверный логин или пароль', 'error')
        return redirect(url_for('admin_login'))

@app.route('/bod/logout')
def admin_logout():
    """Admin logout"""
    session.pop('admin_logged_in', None)
    return redirect(url_for('admin_login'))

@app.route('/bod/dashboard')
def admin_dashboard():
    """Admin dashboard"""
    if not is_admin():
        return redirect(url_for('admin_login'))
    
    levels = supabase_client.get_all_levels()
    
    # Get sections and lessons for each level
    levels_with_data = []
    for level in levels:
        sections = supabase_client.get_sections_by_level(level['id'])
        sections_with_lessons = []
        for section in sections:
            lessons = supabase_client.get_lessons_by_section(section['id'])
            section_data = section.copy()
            section_data['lessons'] = lessons
            sections_with_lessons.append(section_data)
        
        level_data = level.copy()
        level_data['sections'] = sections_with_lessons
        levels_with_data.append(level_data)
    
    return render_template('admin/dashboard.html', levels=levels_with_data)

# Admin CRUD operations
@app.route('/bod/create_level', methods=['POST'])
def create_level():
    if not is_admin():
        return redirect(url_for('admin_login'))
    
    title = request.form.get('title')
    if title:
        levels = supabase_client.get_all_levels()
        order_index = len(levels) + 1
        supabase_client.create_level(title, order_index)
    
    return redirect(url_for('admin_dashboard'))

@app.route('/bod/update_level/<int:level_id>', methods=['POST'])
def update_level(level_id):
    if not is_admin():
        return redirect(url_for('admin_login'))
    
    title = request.form.get('title')
    if title:
        supabase_client.update_level(level_id, title)
    
    return redirect(url_for('admin_dashboard'))

@app.route('/bod/delete_level/<int:level_id>', methods=['POST'])
def delete_level(level_id):
    if not is_admin():
        return redirect(url_for('admin_login'))
    
    supabase_client.delete_level(level_id)
    return redirect(url_for('admin_dashboard'))

@app.route('/bod/create_section/<int:level_id>', methods=['POST'])
def create_section(level_id):
    if not is_admin():
        return redirect(url_for('admin_login'))
    
    title = request.form.get('title')
    if title:
        sections = supabase_client.get_sections_by_level(level_id)
        order_index = len(sections) + 1
        supabase_client.create_section(level_id, title, order_index)
    
    return redirect(url_for('admin_dashboard'))

@app.route('/bod/update_section/<int:section_id>', methods=['POST'])
def update_section(section_id):
    if not is_admin():
        return redirect(url_for('admin_login'))
    
    title = request.form.get('title')
    if title:
        supabase_client.update_section(section_id, title)
    
    return redirect(url_for('admin_dashboard'))

@app.route('/bod/delete_section/<int:section_id>', methods=['POST'])
def delete_section(section_id):
    if not is_admin():
        return redirect(url_for('admin_login'))
    
    supabase_client.delete_section(section_id)
    return redirect(url_for('admin_dashboard'))

@app.route('/bod/create_lesson/<int:section_id>', methods=['POST'])
def create_lesson(section_id):
    if not is_admin():
        return redirect(url_for('admin_login'))
    
    title = request.form.get('title')
    if title:
        lessons = supabase_client.get_lessons_by_section(section_id)
        order_index = len(lessons) + 1
        
        # Create lesson with sample content if it's the first lesson
        content = None
        if order_index == 1:  # First lesson gets sample content
            content = create_sample_lesson_content()
        
        supabase_client.create_lesson(section_id, title, order_index, content)
    
    return redirect(url_for('admin_dashboard'))

@app.route('/bod/edit_lesson/<int:lesson_id>')
def edit_lesson(lesson_id):
    if not is_admin():
        return redirect(url_for('admin_login'))
    
    lesson = supabase_client.get_lesson_by_id(lesson_id)
    if not lesson:
        return "Lesson not found", 404
    
    return render_template('admin/edit_lesson.html', lesson=lesson)

@app.route('/bod/update_lesson/<int:lesson_id>', methods=['POST'])
def update_lesson(lesson_id):
    if not is_admin():
        return redirect(url_for('admin_login'))
    
    title = request.form.get('title')
    theory = request.form.get('theory', '')
    
    # Parse quiz data
    quiz_data = []
    quiz_count = 0
    while f'quiz_{quiz_count}_question' in request.form:
        question = request.form.get(f'quiz_{quiz_count}_question')
        if question:
            options = [
                request.form.get(f'quiz_{quiz_count}_option_0', ''),
                request.form.get(f'quiz_{quiz_count}_option_1', ''),
                request.form.get(f'quiz_{quiz_count}_option_2', ''),
                request.form.get(f'quiz_{quiz_count}_option_3', '')
            ]
            correct_answer = int(request.form.get(f'quiz_{quiz_count}_correct', 0))
            
            quiz_data.append({
                'question': question,
                'options': options,
                'correct_answer': correct_answer
            })
        quiz_count += 1
    
    # Parse tasks data
    tasks_data = []
    tasks_count = 0
    while f'task_{tasks_count}' in request.form:
        task = request.form.get(f'task_{tasks_count}')
        if task:
            tasks_data.append(task)
        tasks_count += 1
    
    content = {
        'theory': theory,
        'quiz': quiz_data,
        'tasks': tasks_data
    }
    
    supabase_client.update_lesson(lesson_id, title, content)
    return redirect(url_for('admin_dashboard'))

@app.route('/bod/delete_lesson/<int:lesson_id>', methods=['POST'])
def delete_lesson(lesson_id):
    if not is_admin():
        return redirect(url_for('admin_login'))
    
    supabase_client.delete_lesson(lesson_id)
    return redirect(url_for('admin_dashboard'))

@app.route('/bod/upload_image', methods=['POST'])
def upload_image():
    if not is_admin():
        return jsonify({'error': 'Unauthorized'}), 401
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed'}), 400
    
    # Check file size
    file.seek(0, os.SEEK_END)
    file_size = file.tell()
    file.seek(0)
    
    if file_size > MAX_FILE_SIZE:
        return jsonify({'error': 'File too large'}), 400
    
    try:
        # Generate unique filename
        filename = secure_filename(file.filename or "image")
        unique_filename = f"{uuid.uuid4()}_{filename}"
        
        # Read file content
        file_content = file.read()
        
        # If it's an image (not SVG), process it
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            try:
                image = Image.open(io.BytesIO(file_content))
                # Convert to RGB if necessary
                if image.mode in ('RGBA', 'LA', 'P'):
                    background = Image.new('RGB', image.size, (255, 255, 255))
                    if image.mode == 'P':
                        image = image.convert('RGBA')
                    background.paste(image, mask=image.split()[-1] if image.mode == 'RGBA' else None)
                    image = background
                
                # Save optimized version
                output = io.BytesIO()
                image.save(output, format='JPEG', quality=85, optimize=True)
                file_content = output.getvalue()
                unique_filename = unique_filename.rsplit('.', 1)[0] + '.jpg'
            except Exception as e:
                logger.error(f"Error processing image: {e}")
        
        # Upload to Supabase Storage
        public_url = supabase_client.upload_image(unique_filename, file_content)
        
        if public_url:
            return jsonify({'url': public_url})
        else:
            return jsonify({'error': 'Failed to upload image'}), 500
            
    except Exception as e:
        logger.error(f"Error uploading image: {e}")
        return jsonify({'error': 'Upload failed'}), 500

# Initialize sample data on first request
def initialize_sample_data():
    """Initialize database with sample data if it's empty"""
    try:
        levels = supabase_client.get_all_levels()
        if not levels:
            logger.info("Creating sample data...")
            level = supabase_client.create_level("Основы DOM", 1)
            if level:
                section = supabase_client.create_section(level['id'], "Введение в DOM", 1)
                if section:
                    content = create_sample_lesson_content()
                    supabase_client.create_lesson(section['id'], "Что такое DOM", 1, content)
    except Exception as e:
        logger.error(f"Error creating sample data: {e}")
