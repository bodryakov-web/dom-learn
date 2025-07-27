-- JavaScript DOM Course Database Schema
-- Execute this in your Supabase SQL Editor

-- Create levels table
CREATE TABLE IF NOT EXISTS levels (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    order_index INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create sections table
CREATE TABLE IF NOT EXISTS sections (
    id SERIAL PRIMARY KEY,
    level_id INTEGER REFERENCES levels(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    order_index INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create lessons table
CREATE TABLE IF NOT EXISTS lessons (
    id SERIAL PRIMARY KEY,
    section_id INTEGER REFERENCES sections(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    order_index INTEGER NOT NULL,
    content JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample data
INSERT INTO levels (title, order_index) VALUES 
('Основы DOM', 1),
('Событийная модель', 2),
('Манипуляции с DOM', 3),
('Продвинутые техники', 4);

-- Insert sections for Level 1
INSERT INTO sections (level_id, title, order_index) VALUES 
(1, 'Введение в DOM', 1),
(1, 'Поиск элементов', 2);

-- Insert sample lesson
INSERT INTO lessons (section_id, title, order_index, content) VALUES 
(1, 'Что такое DOM', 1, '{
  "theory": "<h2>Введение в JavaScript DOM</h2><p>Document Object Model (DOM) - это программный интерфейс для HTML и XML документов. Он представляет страницу так, что программы могут изменять структуру документа, стиль и содержимое.</p><h3>Основные концепции</h3><p>DOM представляет документ как дерево объектов. Каждый HTML элемент является объектом в этом дереве.</p><pre><code class=\"language-javascript\">// Получение элемента по ID\nconst element = document.getElementById(\"myElement\");\n\n// Изменение содержимого\nelement.textContent = \"Новый текст\";\n\n// Изменение стиля\nelement.style.color = \"blue\";</code></pre><p>С помощью JavaScript мы можем:</p><ul><li>Находить элементы на странице</li><li>Изменять содержимое элементов</li><li>Изменять стили элементов</li><li>Добавлять обработчики событий</li></ul>",
  "quiz": [
    {
      "question": "Что означает аббревиатура DOM?",
      "options": ["Document Object Model", "Dynamic Object Management", "Data Object Model", "Document Oriented Markup"],
      "correct_answer": 0
    },
    {
      "question": "Какой метод используется для получения элемента по ID?",
      "options": ["document.getElement()", "document.getElementById()", "document.findById()", "document.selectById()"],
      "correct_answer": 1
    },
    {
      "question": "Как изменить текстовое содержимое элемента?",
      "options": ["element.text = \"новый текст\"", "element.content = \"новый текст\"", "element.textContent = \"новый текст\"", "element.innerHTML = \"новый текст\""],
      "correct_answer": 2
    }
  ],
  "tasks": [
    "Создайте HTML страницу с элементом h1 и кнопкой. При нажатии на кнопку текст заголовка должен изменяться.",
    "Найдите все элементы с классом \"highlight\" и измените их цвет фона на желтый.",
    "Создайте функцию, которая добавляет новый элемент списка в существующий ul при клике на кнопку."
  ]
}');

-- Add indexes for better performance
CREATE INDEX IF NOT EXISTS idx_levels_order ON levels(order_index);
CREATE INDEX IF NOT EXISTS idx_sections_level_order ON sections(level_id, order_index);
CREATE INDEX IF NOT EXISTS idx_lessons_section_order ON lessons(section_id, order_index);