# Временные данные для демонстрации приложения
# Используется когда база данных недоступна

TEMP_LEVELS = [
    {"id": 1, "title": "Основы DOM", "order_index": 1},
    {"id": 2, "title": "Поиск и выбор элементов", "order_index": 2},
    {"id": 3, "title": "Изменение контента и стилей", "order_index": 3},
    {"id": 4, "title": "События и обработчики", "order_index": 4},
    {"id": 5, "title": "Создание и удаление элементов", "order_index": 5}
]

TEMP_SECTIONS = [
    # Уровень 1
    {"id": 1, "level_id": 1, "title": "Что такое DOM", "order_index": 1},
    {"id": 2, "level_id": 1, "title": "Структура DOM-дерева", "order_index": 2},
    {"id": 3, "level_id": 1, "title": "Навигация по DOM", "order_index": 3},
    
    # Уровень 2
    {"id": 4, "level_id": 2, "title": "Методы поиска элементов", "order_index": 1},
    {"id": 5, "level_id": 2, "title": "Селекторы CSS в JavaScript", "order_index": 2},
    {"id": 6, "level_id": 2, "title": "Работа с коллекциями элементов", "order_index": 3},
    
    # Уровень 3
    {"id": 7, "level_id": 3, "title": "Изменение текста и HTML", "order_index": 1},
    {"id": 8, "level_id": 3, "title": "Работа с атрибутами", "order_index": 2},
    {"id": 9, "level_id": 3, "title": "Изменение стилей", "order_index": 3},
    
    # Уровень 4
    {"id": 10, "level_id": 4, "title": "Основы событий", "order_index": 1},
    {"id": 11, "level_id": 4, "title": "Типы событий", "order_index": 2},
    {"id": 12, "level_id": 4, "title": "Event объект", "order_index": 3},
    
    # Уровень 5
    {"id": 13, "level_id": 5, "title": "Создание новых элементов", "order_index": 1},
    {"id": 14, "level_id": 5, "title": "Вставка элементов в DOM", "order_index": 2},
    {"id": 15, "level_id": 5, "title": "Удаление элементов", "order_index": 3}
]

TEMP_LESSONS = [
    {
        "id": 1,
        "section_id": 1,
        "title": "Введение в DOM",
        "order_index": 1,
        "content": {
            "theory": "<h2>Что такое DOM?</h2><p><strong>DOM (Document Object Model)</strong> - это программный интерфейс для HTML и XML документов. Он представляет страницу как структурированное дерево объектов, которое можно изменять с помощью JavaScript.</p><h3>Основные концепции:</h3><ul><li>Каждый HTML элемент - это объект в DOM</li><li>DOM представляет документ как иерархическое дерево</li><li>JavaScript может изменять структуру, стиль и содержимое</li></ul><h3>Пример простого DOM дерева:</h3><pre><code class=\"language-html\">&lt;html&gt;\n  &lt;head&gt;\n    &lt;title&gt;Моя страница&lt;/title&gt;\n  &lt;/head&gt;\n  &lt;body&gt;\n    &lt;h1&gt;Заголовок&lt;/h1&gt;\n    &lt;p&gt;Параграф текста&lt;/p&gt;\n  &lt;/body&gt;\n&lt;/html&gt;</code></pre><p>В JavaScript мы можем получить доступ к любому элементу и изменить его:</p><pre><code class=\"language-javascript\">// Получаем элемент\nconst heading = document.querySelector(\"h1\");\n\n// Изменяем его содержимое\nheading.textContent = \"Новый заголовок!\";\n\n// Изменяем стиль\nheading.style.color = \"blue\";</code></pre>",
            "quiz": [
                {
                    "question": "Что означает аббревиатура DOM?",
                    "options": ["Document Object Model", "Dynamic Object Management", "Data Object Model", "Document Oriented Markup"],
                    "correct_answer": 0
                },
                {
                    "question": "Как DOM представляет HTML документ?",
                    "options": ["Как строку текста", "Как дерево объектов", "Как массив элементов", "Как базу данных"],
                    "correct_answer": 1
                },
                {
                    "question": "Что можно делать с DOM с помощью JavaScript?",
                    "options": ["Только читать содержимое", "Только изменять стили", "Изменять структуру, стиль и содержимое", "Только добавлять новые элементы"],
                    "correct_answer": 2
                }
            ],
            "tasks": [
                "Создайте HTML страницу с заголовком h1 и абзацем p. Откройте консоль браузера и попробуйте изменить текст заголовка с помощью JavaScript.",
                "Используя консоль браузера, измените цвет текста абзаца на красный.",
                "Попробуйте добавить новый атрибут class для заголовка через консоль."
            ]
        }
    },
    {
        "id": 2,
        "section_id": 4,
        "title": "Методы поиска элементов",
        "order_index": 1,
        "content": {
            "theory": "<h2>Методы поиска элементов в DOM</h2><p>JavaScript предоставляет несколько способов найти элементы на странице. Выбор правильного метода зависит от ваших потребностей.</p><h3>Основные методы поиска:</h3><h4>1. getElementById()</h4><p>Находит элемент по его ID (самый быстрый метод):</p><pre><code class=\"language-javascript\">const element = document.getElementById(\"myId\");\nconsole.log(element);</code></pre><h4>2. getElementsByClassName()</h4><p>Находит все элементы с определенным классом:</p><pre><code class=\"language-javascript\">const elements = document.getElementsByClassName(\"myClass\");\nconsole.log(elements.length);</code></pre><h4>3. querySelector()</h4><p>Находит первый элемент, соответствующий CSS селектору:</p><pre><code class=\"language-javascript\">const element = document.querySelector(\".myClass\");\nconst elementById = document.querySelector(\"#myId\");</code></pre>",
            "quiz": [
                {
                    "question": "Какой метод самый быстрый для поиска элемента?",
                    "options": ["querySelector()", "getElementsByClassName()", "getElementById()", "querySelectorAll()"],
                    "correct_answer": 2
                },
                {
                    "question": "Что возвращает getElementsByClassName()?",
                    "options": ["Один элемент", "HTMLCollection", "Array", "NodeList"],
                    "correct_answer": 1
                },
                {
                    "question": "Какой метод использует CSS селекторы?",
                    "options": ["getElementById()", "getElementsByTagName()", "querySelector()", "getElementsByClassName()"],
                    "correct_answer": 2
                }
            ],
            "tasks": [
                "Создайте HTML с элементами разных типов и найдите элемент по ID.",
                "Используйте getElementsByClassName() для поиска элементов с классом.",
                "Попробуйте querySelectorAll() для поиска всех параграфов."
            ]
        }
    }
]