import os
import logging
import psycopg2
from psycopg2.extras import RealDictCursor
import json

logger = logging.getLogger(__name__)

class SupabaseClient:
    def __init__(self):
        self.db_url = os.environ.get("DATABASE_URL", "")
        self.conn = None
        self.next_id = 100  # Начальный ID для новых записей
        self._ensure_connection()

    def _ensure_connection(self):
        if self.conn is not None:
            try:
                # Проверяем, открыто ли соединение
                self.conn.cursor().execute('SELECT 1')
                return
            except Exception:
                self.conn = None
        if not self.db_url:
            logger.warning("DATABASE_URL not found in environment variables")
            return
        try:
            import urllib.parse
            parsed = urllib.parse.urlparse(self.db_url)
            connection_params = {
                'host': parsed.hostname,
                'port': parsed.port or 5432,
                'database': parsed.path.lstrip('/') or 'postgres',
                'user': parsed.username,
                'password': parsed.password,
                'cursor_factory': RealDictCursor,
                'sslmode': 'require',
                'connect_timeout': 15
            }
            self.conn = psycopg2.connect(**connection_params)
            self.conn.autocommit = True
            logger.info("Database connected successfully (reconnect)")
        except Exception as e:
            logger.error(f"Failed to connect to database: {e}")
            try:
                if '?' in self.db_url:
                    dsn = self.db_url
                else:
                    dsn = self.db_url + '?sslmode=require'
                self.conn = psycopg2.connect(
                    dsn=dsn,
                    cursor_factory=RealDictCursor,
                    connect_timeout=15
                )
                self.conn.autocommit = True
                logger.info("Database connected successfully (DSN method reconnect)")
            except Exception as e2:
                logger.error(f"DSN connection also failed: {e2}")
                self.conn = None

    def _create_tables(self):
        self._ensure_connection()
        if not self.conn:
            return
        
        try:
            cur = self.conn.cursor()
            
            # Create levels table
            cur.execute("""
                CREATE TABLE IF NOT EXISTS levels (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(255) NOT NULL,
                    order_index INTEGER NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Create sections table
            cur.execute("""
                CREATE TABLE IF NOT EXISTS sections (
                    id SERIAL PRIMARY KEY,
                    level_id INTEGER REFERENCES levels(id) ON DELETE CASCADE,
                    title VARCHAR(255) NOT NULL,
                    order_index INTEGER NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Create lessons table
            cur.execute("""
                CREATE TABLE IF NOT EXISTS lessons (
                    id SERIAL PRIMARY KEY,
                    section_id INTEGER REFERENCES sections(id) ON DELETE CASCADE,
                    title VARCHAR(255) NOT NULL,
                    order_index INTEGER NOT NULL,
                    content JSONB,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            cur.close()
            logger.info("Tables created successfully")
        except Exception as e:
            logger.error(f"Error creating tables: {e}")

    def is_connected(self):
        self._ensure_connection()
        return self.conn is not None

    # Levels operations
    def get_all_levels(self):
        self._ensure_connection()
        if not self.conn:
            return []
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM levels ORDER BY order_index")
            result = cur.fetchall()
            cur.close()
            return [dict(row) for row in result]
        except Exception as e:
            logger.error(f"Error fetching levels: {e}")
            return []

    def create_level(self, title, order_index):
        self._ensure_connection()
        if not self.conn:
            return None
        try:
            cur = self.conn.cursor()
            cur.execute(
                "INSERT INTO levels (title, order_index) VALUES (%s, %s) RETURNING *",
                (title, order_index)
            )
            result = cur.fetchone()
            cur.close()
            return dict(result) if result else None
        except Exception as e:
            logger.error(f"Error creating level: {e}")
            return None

    def update_level(self, level_id, title):
        self._ensure_connection()
        if not self.conn:
            return None
        try:
            cur = self.conn.cursor()
            cur.execute(
                "UPDATE levels SET title = %s, updated_at = CURRENT_TIMESTAMP WHERE id = %s RETURNING *",
                (title, level_id)
            )
            result = cur.fetchone()
            cur.close()
            return dict(result) if result else None
        except Exception as e:
            logger.error(f"Error updating level: {e}")
            return None

    def delete_level(self, level_id):
        self._ensure_connection()
        if not self.conn:
            return False
        try:
            cur = self.conn.cursor()
            cur.execute("DELETE FROM levels WHERE id = %s", (level_id,))
            cur.close()
            return True
        except Exception as e:
            logger.error(f"Error deleting level: {e}")
            return False

    # Sections operations
    def get_sections_by_level(self, level_id):
        self._ensure_connection()
        if not self.conn:
            return []
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM sections WHERE level_id = %s ORDER BY order_index", (level_id,))
            result = cur.fetchall()
            cur.close()
            return [dict(row) for row in result]
        except Exception as e:
            logger.error(f"Error fetching sections: {e}")
            return []

    def create_section(self, level_id, title, order_index):
        self._ensure_connection()
        if not self.conn:
            return None
        try:
            cur = self.conn.cursor()
            cur.execute(
                "INSERT INTO sections (level_id, title, order_index) VALUES (%s, %s, %s) RETURNING *",
                (level_id, title, order_index)
            )
            result = cur.fetchone()
            cur.close()
            return dict(result) if result else None
        except Exception as e:
            logger.error(f"Error creating section: {e}")
            return None

    def update_section(self, section_id, title):
        self._ensure_connection()
        if not self.conn:
            return None
        try:
            cur = self.conn.cursor()
            cur.execute(
                "UPDATE sections SET title = %s, updated_at = CURRENT_TIMESTAMP WHERE id = %s RETURNING *",
                (title, section_id)
            )
            result = cur.fetchone()
            cur.close()
            return dict(result) if result else None
        except Exception as e:
            logger.error(f"Error updating section: {e}")
            return None

    def delete_section(self, section_id):
        self._ensure_connection()
        if not self.conn:
            return False
        try:
            cur = self.conn.cursor()
            cur.execute("DELETE FROM sections WHERE id = %s", (section_id,))
            cur.close()
            return True
        except Exception as e:
            logger.error(f"Error deleting section: {e}")
            return False

    def get_section_by_id(self, section_id):
        self._ensure_connection()
        if not self.conn:
            return None
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM sections WHERE id = %s", (section_id,))
            result = cur.fetchone()
            cur.close()
            return dict(result) if result else None
        except Exception as e:
            logger.error(f"Error fetching section: {e}")
            return None

    # Lessons operations
    def get_lessons_by_section(self, section_id):
        self._ensure_connection()
        if not self.conn:
            return []
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM lessons WHERE section_id = %s ORDER BY order_index", (section_id,))
            result = cur.fetchall()
            cur.close()
            return [dict(row) for row in result]
        except Exception as e:
            logger.error(f"Error fetching lessons: {e}")
            return []

    def get_lesson_by_id(self, lesson_id):
        self._ensure_connection()
        if not self.conn:
            return None
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM lessons WHERE id = %s", (lesson_id,))
            result = cur.fetchone()
            cur.close()
            return dict(result) if result else None
        except Exception as e:
            logger.error(f"Error fetching lesson: {e}")
            return None

    def create_lesson(self, section_id, title, order_index, content=None):
        self._ensure_connection()
        if not self.conn:
            return None
        try:
            if content is None:
                content = {"theory": "", "quiz": [], "tasks": []}
            
            cur = self.conn.cursor()
            cur.execute(
                "INSERT INTO lessons (section_id, title, order_index, content) VALUES (%s, %s, %s, %s) RETURNING *",
                (section_id, title, order_index, json.dumps(content))
            )
            result = cur.fetchone()
            cur.close()
            return dict(result) if result else None
        except Exception as e:
            logger.error(f"Error creating lesson: {e}")
            return None

    def update_lesson(self, lesson_id, title=None, content=None):
        self._ensure_connection()
        if not self.conn:
            return None
        try:
            cur = self.conn.cursor()
            
            if title and content:
                cur.execute(
                    "UPDATE lessons SET title = %s, content = %s, updated_at = CURRENT_TIMESTAMP WHERE id = %s RETURNING *",
                    (title, json.dumps(content), lesson_id)
                )
            elif title:
                cur.execute(
                    "UPDATE lessons SET title = %s, updated_at = CURRENT_TIMESTAMP WHERE id = %s RETURNING *",
                    (title, lesson_id)
                )
            elif content:
                cur.execute(
                    "UPDATE lessons SET content = %s, updated_at = CURRENT_TIMESTAMP WHERE id = %s RETURNING *",
                    (json.dumps(content), lesson_id)
                )
            else:
                cur.close()
                return None
                
            result = cur.fetchone()
            cur.close()
            return dict(result) if result else None
        except Exception as e:
            logger.error(f"Error updating lesson: {e}")
            return None

    def delete_lesson(self, lesson_id):
        self._ensure_connection()
        if not self.conn:
            return False
        try:
            cur = self.conn.cursor()
            cur.execute("DELETE FROM lessons WHERE id = %s", (lesson_id,))
            cur.close()
            return True
        except Exception as e:
            logger.error(f"Error deleting lesson: {e}")
            return False

    def upload_image(self, file_path, file_content):
        # Simplified - just return a placeholder for now
        # In real implementation, this would upload to Supabase Storage
        return f"https://via.placeholder.com/600x400?text={file_path}"

# Global instance
supabase_client = SupabaseClient()