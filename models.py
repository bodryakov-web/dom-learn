"""
Simple data models for the application.
"""

def create_sample_lesson_content():
    """Create sample lesson content for testing"""
    return {
        "theory": """
        <h2>Введение в JavaScript DOM</h2>
        <p>Document Object Model (DOM) - это программный интерфейс для HTML и XML документов.</p>
        
        <h3>Основные концепции</h3>
        <p>DOM представляет документ как дерево объектов.</p>
        
        <pre><code class="language-javascript">
// Получение элемента по ID
const element = document.getElementById('myElement');

// Изменение содержимого
element.textContent = 'Новый текст';
        </code></pre>
        """,
        "quiz": [
            {
                "question": "Что означает аббревиатура DOM?",
                "options": [
                    "Document Object Model",
                    "Dynamic Object Management", 
                    "Data Object Model",
                    "Document Oriented Markup"
                ],
                "correct_answer": 0
            },
            {
                "question": "Какой метод используется для получения элемента по ID?",
                "options": [
                    "document.getElement()",
                    "document.getElementById()",
                    "document.findById()",
                    "document.selectById()"
                ],
                "correct_answer": 1
            }
        ],
        "tasks": [
            "Создайте HTML страницу с элементом h1 и кнопкой. При нажатии на кнопку текст заголовка должен изменяться."
        ]
    }

def create_sample_lesson_content():
    """Create sample lesson content for testing"""
    return {
        "theory": """
        <h2>Введение в JavaScript DOM</h2>
        <p>Document Object Model (DOM) - это программный интерфейс для HTML и XML документов. 
        Он представляет страницу так, что программы могут изменять структуру документа, стиль и содержимое.</p>
        
        <h3>Основные концепции</h3>
        <p>DOM представляет документ как дерево объектов. Каждый HTML элемент является объектом в этом дереве.</p>
        
        <pre><code class="language-javascript">
// Получение элемента по ID
const element = document.getElementById('myElement');

// Изменение содержимого
element.textContent = 'Новый текст';

// Изменение стиля
element.style.color = 'blue';
        </code></pre>
        
        <p>С помощью JavaScript мы можем:</p>
        <ul>
            <li>Находить элементы на странице</li>
            <li>Изменять содержимое элементов</li>
            <li>Изменять стили элементов</li>
            <li>Добавлять обработчики событий</li>
        </ul>
        """,
        "quiz": [
            {
                "question": "Что означает аббревиатура DOM?",
                "options": [
                    "Document Object Model",
                    "Dynamic Object Management",
                    "Data Object Model",
                    "Document Oriented Markup"
                ],
                "correct_answer": 0
            },
            {
                "question": "Какой метод используется для получения элемента по ID?",
                "options": [
                    "document.getElement()",
                    "document.getElementById()",
                    "document.findById()",
                    "document.selectById()"
                ],
                "correct_answer": 1
            },
            {
                "question": "Как изменить текстовое содержимое элемента?",
                "options": [
                    "element.text = 'новый текст'",
                    "element.content = 'новый текст'",
                    "element.textContent = 'новый текст'",
                    "element.innerHTML = 'новый текст'"
                ],
                "correct_answer": 2
            }
        ],
        "tasks": [
            "Создайте HTML страницу с элементом h1 и кнопкой. При нажатии на кнопку текст заголовка должен изменяться.",
            "Найдите все элементы с классом 'highlight' и измените их цвет фона на желтый.",
            "Создайте функцию, которая добавляет новый элемент списка в существующий ul при клике на кнопку."
        ]
    }
