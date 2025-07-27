-- JavaScript DOM Course - Тестовые данные
-- Заполнение базы данных образцами контента для курса

-- Вставляем уровни курса
INSERT INTO levels (title, order_index) VALUES 
('Основы DOM', 1),
('Поиск и выбор элементов', 2),
('Изменение контента и стилей', 3),
('События и обработчики', 4),
('Создание и удаление элементов', 5);

-- Вставляем разделы для Уровня 1: Основы DOM
INSERT INTO sections (level_id, title, order_index) VALUES 
(1, 'Что такое DOM', 1),
(1, 'Структура DOM-дерева', 2),
(1, 'Навигация по DOM', 3);

-- Вставляем разделы для Уровня 2: Поиск и выбор элементов
INSERT INTO sections (level_id, title, order_index) VALUES 
(2, 'Методы поиска элементов', 1),
(2, 'Селекторы CSS в JavaScript', 2),
(2, 'Работа с коллекциями элементов', 3);

-- Вставляем разделы для Уровня 3: Изменение контента и стилей
INSERT INTO sections (level_id, title, order_index) VALUES 
(3, 'Изменение текста и HTML', 1),
(3, 'Работа с атрибутами', 2),
(3, 'Изменение стилей', 3);

-- Вставляем разделы для Уровня 4: События и обработчики
INSERT INTO sections (level_id, title, order_index) VALUES 
(4, 'Основы событий', 1),
(4, 'Типы событий', 2),
(4, 'Event объект', 3);

-- Вставляем разделы для Уровня 5: Создание и удаление элементов
INSERT INTO sections (level_id, title, order_index) VALUES 
(5, 'Создание новых элементов', 1),
(5, 'Вставка элементов в DOM', 2),
(5, 'Удаление элементов', 3);

-- Урок 1.1: Что такое DOM
INSERT INTO lessons (section_id, title, order_index, content) VALUES 
(1, 'Введение в DOM', 1, '{
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
}');

-- Урок 1.2: Структура DOM-дерева
INSERT INTO lessons (section_id, title, order_index, content) VALUES 
(1, 'Структура DOM-дерева', 2, '{
  "theory": "<h2>Структура DOM-дерева</h2><p>DOM представляет HTML документ как иерархическое дерево узлов. Каждый элемент, атрибут и текст являются узлами в этом дереве.</p><h3>Типы узлов:</h3><ul><li><strong>Element Node</strong> - HTML элементы (div, p, h1, etc.)</li><li><strong>Text Node</strong> - текстовое содержимое элементов</li><li><strong>Attribute Node</strong> - атрибуты элементов</li><li><strong>Document Node</strong> - корневой узел документа</li></ul><h3>Иерархия узлов:</h3><pre><code class=\"language-html\">&lt;div id=\"container\"&gt;\n  &lt;h2&gt;Заголовок&lt;/h2&gt;\n  &lt;p&gt;Первый параграф&lt;/p&gt;\n  &lt;p&gt;Второй параграф&lt;/p&gt;\n&lt;/div&gt;</code></pre><p>В этом примере:</p><ul><li><code>div</code> - родительский элемент</li><li><code>h2</code> и <code>p</code> - дочерние элементы</li><li>Элементы <code>p</code> являются siblings (братские элементы)</li></ul><h3>Навигация по дереву:</h3><pre><code class=\"language-javascript\">const container = document.getElementById(\"container\");\n\n// Получаем дочерние элементы\nconst children = container.children;\nconsole.log(children.length); // 3\n\n// Получаем первый дочерний элемент\nconst firstChild = container.firstElementChild;\nconsole.log(firstChild.tagName); // H2\n\n// Получаем родительский элемент\nconst heading = document.querySelector(\"h2\");\nconst parent = heading.parentElement;\nconsole.log(parent.id); // container</code></pre>",
  "quiz": [
    {
      "question": "Что является корневым узлом DOM-дерева?",
      "options": ["html элемент", "body элемент", "Document узел", "head элемент"],
      "correct_answer": 2
    },
    {
      "question": "Как называются элементы, которые находятся на одном уровне иерархии?",
      "options": ["Родительские", "Дочерние", "Братские (siblings)", "Корневые"],
      "correct_answer": 2
    },
    {
      "question": "Какое свойство используется для получения всех дочерних элементов?",
      "options": ["childNodes", "children", "childElements", "descendants"],
      "correct_answer": 1
    }
  ],
  "tasks": [
    "Создайте HTML с nested структурой: div > ul > 3 li элемента. Через консоль получите доступ к ul и выведите количество его дочерних элементов.",
    "Получите второй li элемент и найдите его родительский элемент через JavaScript.",
    "Используя firstElementChild и nextElementSibling, переберите все элементы списка."
  ]
}');

-- Урок 2.1: Методы поиска элементов
INSERT INTO lessons (section_id, title, order_index, content) VALUES 
(4, 'Методы поиска элементов', 1, '{
  "theory": "<h2>Методы поиска элементов в DOM</h2><p>JavaScript предоставляет несколько способов найти элементы на странице. Выбор правильного метода зависит от ваших потребностей.</p><h3>Основные методы поиска:</h3><h4>1. getElementById()</h4><p>Находит элемент по его ID (самый быстрый метод):</p><pre><code class=\"language-javascript\">const element = document.getElementById(\"myId\");\nconsole.log(element); // &lt;div id=\"myId\"&gt;...&lt;/div&gt;</code></pre><h4>2. getElementsByClassName()</h4><p>Находит все элементы с определенным классом:</p><pre><code class=\"language-javascript\">const elements = document.getElementsByClassName(\"myClass\");\nconsole.log(elements.length); // количество найденных элементов\n\n// Перебираем найденные элементы\nfor (let i = 0; i < elements.length; i++) {\n  console.log(elements[i]);\n}</code></pre><h4>3. getElementsByTagName()</h4><p>Находит все элементы определенного тега:</p><pre><code class=\"language-javascript\">const paragraphs = document.getElementsByTagName(\"p\");\nconst allDivs = document.getElementsByTagName(\"div\");</code></pre><h4>4. querySelector()</h4><p>Находит первый элемент, соответствующий CSS селектору:</p><pre><code class=\"language-javascript\">const element = document.querySelector(\".myClass\");\nconst elementById = document.querySelector(\"#myId\");\nconst firstParagraph = document.querySelector(\"p\");</code></pre><h4>5. querySelectorAll()</h4><p>Находит все элементы, соответствующие CSS селектору:</p><pre><code class=\"language-javascript\">const elements = document.querySelectorAll(\".myClass\");\nconst allParagraphs = document.querySelectorAll(\"p\");\n\n// Перебираем с помощью forEach\nelements.forEach(element => {\n  console.log(element);\n});</code></pre>",
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
    "Создайте HTML с элементами разных типов (div, p, span) и разными классами. Найдите элемент по ID и выведите его в консоль.",
    "Используйте getElementsByClassName() чтобы найти все элементы с определенным классом и изменить их цвет фона.",
    "С помощью querySelectorAll() найдите все параграфы внутри div и добавьте им границу через JavaScript."
  ]
}');

-- Урок 3.1: Изменение текста и HTML
INSERT INTO lessons (section_id, title, order_index, content) VALUES 
(7, 'Изменение текста и HTML', 1, '{
  "theory": "<h2>Изменение содержимого элементов</h2><p>JavaScript позволяет изменять содержимое HTML элементов несколькими способами. Важно понимать разницу между различными свойствами.</p><h3>Основные свойства для изменения содержимого:</h3><h4>1. textContent</h4><p>Изменяет только текстовое содержимое элемента (безопасно):</p><pre><code class=\"language-javascript\">const element = document.getElementById(\"myElement\");\nelement.textContent = \"Новый текст\";\n\n// HTML теги будут отображены как текст\nelement.textContent = \"&lt;strong&gt;Жирный текст&lt;/strong&gt;\";\n// Результат: &lt;strong&gt;Жирный текст&lt;/strong&gt; (как обычный текст)</code></pre><h4>2. innerHTML</h4><p>Позволяет вставлять HTML код (потенциально небезопасно):</p><pre><code class=\"language-javascript\">const element = document.getElementById(\"myElement\");\nelement.innerHTML = \"&lt;strong&gt;Жирный текст&lt;/strong&gt;\";\n// Результат: Жирный текст (HTML будет выполнен)\n\n// Можно добавлять сложную разметку\nelement.innerHTML = `\n  &lt;h3&gt;Заголовок&lt;/h3&gt;\n  &lt;p&gt;Параграф с &lt;em&gt;курсивом&lt;/em&gt;&lt;/p&gt;\n  &lt;ul&gt;\n    &lt;li&gt;Элемент списка&lt;/li&gt;\n  &lt;/ul&gt;\n`;</code></pre><h4>3. outerHTML</h4><p>Заменяет весь элемент, включая его теги:</p><pre><code class=\"language-javascript\">const element = document.getElementById(\"myElement\");\n// Было: &lt;div id=\"myElement\"&gt;Старый текст&lt;/div&gt;\n\nelement.outerHTML = \"&lt;p&gt;Новый параграф&lt;/p&gt;\";\n// Стало: &lt;p&gt;Новый параграф&lt;/p&gt;</code></pre><h4>Практический пример:</h4><pre><code class=\"language-html\">&lt;div id=\"content\"&gt;\n  &lt;h2&gt;Старый заголовок&lt;/h2&gt;\n  &lt;p&gt;Старый текст&lt;/p&gt;\n&lt;/div&gt;</code></pre><pre><code class=\"language-javascript\">const content = document.getElementById(\"content\");\n\n// Изменяем только текст заголовка\nconst heading = content.querySelector(\"h2\");\nheading.textContent = \"Новый заголовок\";\n\n// Добавляем HTML в параграф\nconst paragraph = content.querySelector(\"p\");\nparagraph.innerHTML = \"Текст с &lt;strong&gt;выделением&lt;/strong&gt;\";</code></pre>",
  "quiz": [
    {
      "question": "Какое свойство безопасно использовать для вставки пользовательского текста?",
      "options": ["innerHTML", "outerHTML", "textContent", "innerText"],
      "correct_answer": 2
    },
    {
      "question": "Что произойдет при использовании outerHTML?",
      "options": ["Изменится только содержимое", "Элемент будет полностью заменен", "Добавится новый элемент", "Ничего не произойдет"],
      "correct_answer": 1
    },
    {
      "question": "Какое свойство позволяет вставлять HTML разметку?",
      "options": ["textContent", "innerText", "innerHTML", "textHTML"],
      "correct_answer": 2
    }
  ],
  "tasks": [
    "Создайте div с текстом и измените его содержимое с помощью textContent. Попробуйте вставить HTML теги и посмотрите на результат.",
    "Используйте innerHTML чтобы создать список покупок внутри существующего div элемента.",
    "Создайте функцию, которая принимает текст и безопасно вставляет его в элемент (используя textContent)."
  ]
}');

-- Урок 4.1: Основы событий
INSERT INTO lessons (section_id, title, order_index, content) VALUES 
(10, 'Основы событий в DOM', 1, '{
  "theory": "<h2>События в JavaScript</h2><p>События - это действия, которые происходят в браузере: клики мышью, нажатия клавиш, загрузка страницы и многое другое. JavaScript позволяет \"слушать\" эти события и реагировать на них.</p><h3>Что такое событие?</h3><p>Событие - это сигнал о том, что что-то произошло. Браузер генерирует события автоматически, а мы можем написать код, который будет выполняться при возникновении определенных событий.</p><h3>Способы добавления обработчиков событий:</h3><h4>1. HTML атрибуты (не рекомендуется)</h4><pre><code class=\"language-html\">&lt;button onclick=\"alert(\"Привет!\")\"&gt;Нажми меня&lt;/button&gt;</code></pre><h4>2. DOM свойства</h4><pre><code class=\"language-javascript\">const button = document.getElementById(\"myButton\");\nbutton.onclick = function() {\n  alert(\"Кнопка нажата!\");\n};</code></pre><h4>3. addEventListener() (рекомендуется)</h4><pre><code class=\"language-javascript\">const button = document.getElementById(\"myButton\");\n\nbutton.addEventListener(\"click\", function() {\n  alert(\"Кнопка нажата!\");\n});\n\n// Или с arrow function\nbutton.addEventListener(\"click\", () => {\n  alert(\"Кнопка нажата!\");\n});</code></pre><h3>Преимущества addEventListener:</h3><ul><li>Можно добавить несколько обработчиков на одно событие</li><li>Можно удалить обработчик с помощью removeEventListener</li><li>Больше контроля над поведением события</li></ul><h3>Популярные события:</h3><ul><li><strong>click</strong> - клик мышью</li><li><strong>mouseover</strong> - наведение мыши</li><li><strong>keydown</strong> - нажатие клавиши</li><li><strong>load</strong> - загрузка страницы</li><li><strong>submit</strong> - отправка формы</li></ul><h4>Практический пример:</h4><pre><code class=\"language-html\">&lt;button id=\"colorButton\"&gt;Изменить цвет&lt;/button&gt;\n&lt;div id=\"colorBox\" style=\"width: 100px; height: 100px; background: red;\"&gt;&lt;/div&gt;</code></pre><pre><code class=\"language-javascript\">const button = document.getElementById(\"colorButton\");\nconst box = document.getElementById(\"colorBox\");\n\nbutton.addEventListener(\"click\", function() {\n  // Генерируем случайный цвет\n  const colors = [\"red\", \"blue\", \"green\", \"yellow\", \"purple\", \"orange\"];\n  const randomColor = colors[Math.floor(Math.random() * colors.length)];\n  \n  box.style.backgroundColor = randomColor;\n});</code></pre>",
  "quiz": [
    {
      "question": "Какой способ добавления обработчиков событий рекомендуется использовать?",
      "options": ["HTML атрибуты", "DOM свойства", "addEventListener()", "Все способы равнозначны"],
      "correct_answer": 2
    },
    {
      "question": "Сколько обработчиков можно добавить на одно событие с помощью addEventListener?",
      "options": ["Только один", "Максимум два", "Неограниченное количество", "Максимум десять"],
      "correct_answer": 2
    },
    {
      "question": "Какое событие происходит при клике мышью?",
      "options": ["mouseclick", "click", "press", "tap"],
      "correct_answer": 1
    }
  ],
  "tasks": [
    "Создайте кнопку и добавьте обработчик события click с помощью addEventListener. При нажатии кнопка должна менять свой текст.",
    "Создайте div элемент и добавьте обработчики событий mouseover и mouseout, которые будут менять цвет фона при наведении мыши.",
    "Добавьте два разных обработчика на одну кнопку и убедитесь, что оба выполняются при клике."
  ]
}');

-- Урок 5.1: Создание новых элементов
INSERT INTO lessons (section_id, title, order_index, content) VALUES 
(13, 'Создание новых элементов', 1, '{
  "theory": "<h2>Создание новых DOM элементов</h2><p>JavaScript позволяет динамически создавать новые HTML элементы и добавлять их на страницу. Это основа для интерактивных веб-приложений.</p><h3>Основные методы создания элементов:</h3><h4>1. document.createElement()</h4><p>Создает новый HTML элемент:</p><pre><code class=\"language-javascript\">// Создаем новый div\nconst newDiv = document.createElement(\"div\");\n\n// Создаем новый параграф\nconst newParagraph = document.createElement(\"p\");\n\n// Создаем новую кнопку\nconst newButton = document.createElement(\"button\");</code></pre><h4>2. Добавление содержимого и атрибутов</h4><pre><code class=\"language-javascript\">const newDiv = document.createElement(\"div\");\n\n// Добавляем текст\nnewDiv.textContent = \"Это новый div!\";\n\n// Добавляем HTML\nnewDiv.innerHTML = \"&lt;strong&gt;Жирный текст&lt;/strong&gt;\";\n\n// Добавляем класс\nnewDiv.className = \"myClass\";\n// или\nnewDiv.classList.add(\"myClass\");\n\n// Добавляем ID\nnewDiv.id = \"newElement\";\n\n// Добавляем произвольный атрибут\nnewDiv.setAttribute(\"data-value\", \"123\");</code></pre><h4>3. Создание элемента с атрибутами</h4><pre><code class=\"language-javascript\">// Создаем ссылку\nconst link = document.createElement(\"a\");\nlink.href = \"https://example.com\";\nlink.textContent = \"Перейти на сайт\";\nlink.target = \"_blank\";\n\n// Создаем изображение\nconst img = document.createElement(\"img\");\nimg.src = \"image.jpg\";\nimg.alt = \"Описание изображения\";\nimg.width = 200;</code></pre><h4>4. Создание списка динамически</h4><pre><code class=\"language-javascript\">// Создаем ul\nconst list = document.createElement(\"ul\");\n\n// Массив данных\nconst items = [\"Яблоко\", \"Банан\", \"Апельсин\"];\n\n// Создаем li для каждого элемента\nitems.forEach(item => {\n  const li = document.createElement(\"li\");\n  li.textContent = item;\n  list.appendChild(li);\n});\n\n// Добавляем список на страницу\ndocument.body.appendChild(list);</code></pre><h4>5. Создание сложной структуры</h4><pre><code class=\"language-javascript\">function createCard(title, description, imageUrl) {\n  // Создаем контейнер карточки\n  const card = document.createElement(\"div\");\n  card.className = \"card\";\n  \n  // Создаем изображение\n  const img = document.createElement(\"img\");\n  img.src = imageUrl;\n  img.alt = title;\n  \n  // Создаем заголовок\n  const h3 = document.createElement(\"h3\");\n  h3.textContent = title;\n  \n  // Создаем описание\n  const p = document.createElement(\"p\");\n  p.textContent = description;\n  \n  // Собираем все вместе\n  card.appendChild(img);\n  card.appendChild(h3);\n  card.appendChild(p);\n  \n  return card;\n}\n\n// Используем функцию\nconst myCard = createCard(\n  \"Заголовок карточки\", \n  \"Описание карточки\", \n  \"image.jpg\"\n);\n\ndocument.body.appendChild(myCard);</code></pre>",
  "quiz": [
    {
      "question": "Какой метод используется для создания нового HTML элемента?",
      "options": ["document.newElement()", "document.createElement()", "document.addElement()", "document.makeElement()"],
      "correct_answer": 1
    },
    {
      "question": "Как добавить CSS класс к созданному элементу?",
      "options": ["element.class = \"myClass\"", "element.addStyle(\"myClass\")", "element.className = \"myClass\"", "element.setClass(\"myClass\")"],
      "correct_answer": 2
    },
    {
      "question": "Что нужно сделать после создания элемента, чтобы он появился на странице?",
      "options": ["Ничего, элемент появится автоматически", "Добавить его в DOM с помощью appendChild", "Вызвать метод show()", "Установить свойство visible = true"],
      "correct_answer": 1
    }
  ],
  "tasks": [
    "Создайте новый параграф с текстом и добавьте его в конец body страницы.",
    "Создайте функцию, которая создает кнопку с заданным текстом и цветом фона.",
    "Создайте форму динамически: div контейнер, input поле, label и button для отправки."
  ]
}');