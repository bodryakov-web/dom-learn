/**
 * Quiz functionality for lesson pages
 * Handles multiple choice questions with immediate feedback
 */

let quizData = [];
let answeredQuestions = new Set();

/**
 * Initialize quiz functionality
 * @param {Array} data - Quiz questions data from the server
 */
function initQuiz(data) {
    quizData = data || [];
    answeredQuestions.clear();
    
    if (quizData.length === 0) {
        console.log('No quiz data provided');
        return;
    }
    
    console.log(`Initializing quiz with ${quizData.length} questions`);
    
    // Add event listeners to all quiz options
    const quizQuestions = document.querySelectorAll('.quiz-question');
    quizQuestions.forEach((questionElement, questionIndex) => {
        initQuizQuestion(questionElement, questionIndex);
    });
}

/**
 * Initialize a single quiz question
 * @param {Element} questionElement - The question container element
 * @param {Number} questionIndex - Index of the question
 */
function initQuizQuestion(questionElement, questionIndex) {
    const options = questionElement.querySelectorAll('.quiz-option input[type="radio"]');
    const resultContainer = questionElement.querySelector('.quiz-result');
    const feedbackContainer = questionElement.querySelector('.quiz-feedback');
    
    if (!options.length || !resultContainer || !feedbackContainer) {
        console.error(`Quiz question ${questionIndex} missing required elements`);
        return;
    }
    
    // Add click handlers to all options
    options.forEach((option, optionIndex) => {
        option.addEventListener('change', function() {
            if (answeredQuestions.has(questionIndex)) {
                // Already answered, don't allow changes
                return;
            }
            
            handleQuizAnswer(questionIndex, optionIndex, questionElement);
        });
    });
}

/**
 * Handle quiz answer selection
 * @param {Number} questionIndex - Index of the question
 * @param {Number} selectedOption - Index of selected option
 * @param {Element} questionElement - The question container element
 */
function handleQuizAnswer(questionIndex, selectedOption, questionElement) {
    if (answeredQuestions.has(questionIndex)) {
        return; // Already answered
    }
    
    // Mark question as answered
    answeredQuestions.add(questionIndex);
    
    const questionData = quizData[questionIndex];
    if (!questionData) {
        console.error(`No data found for question ${questionIndex}`);
        return;
    }
    
    const correctAnswer = questionData.correct_answer;
    const isCorrect = selectedOption === correctAnswer;
    
    // Show visual feedback on options
    showOptionFeedback(questionElement, selectedOption, correctAnswer);
    
    // Show result message
    showQuizResult(questionElement, isCorrect, questionData.options[correctAnswer]);
    
    // Disable all options for this question
    disableQuestionOptions(questionElement);
    
    // Track progress (could be enhanced for analytics)
    console.log(`Question ${questionIndex + 1}: ${isCorrect ? 'Correct' : 'Incorrect'}`);
}

/**
 * Show visual feedback on quiz options
 * @param {Element} questionElement - The question container element
 * @param {Number} selectedOption - Index of selected option
 * @param {Number} correctAnswer - Index of correct answer
 */
function showOptionFeedback(questionElement, selectedOption, correctAnswer) {
    const options = questionElement.querySelectorAll('.quiz-option');
    
    options.forEach((optionElement, index) => {
        const radio = optionElement.querySelector('input[type="radio"]');
        
        if (index === correctAnswer) {
            // Mark correct answer
            optionElement.classList.add('correct');
            
            // Add checkmark icon
            const checkmark = document.createElement('span');
            checkmark.innerHTML = ' ✓';
            checkmark.className = 'text-green-600 font-bold ml-2';
            optionElement.appendChild(checkmark);
            
        } else if (index === selectedOption && selectedOption !== correctAnswer) {
            // Mark incorrect selected answer
            optionElement.classList.add('incorrect');
            
            // Add X icon
            const cross = document.createElement('span');
            cross.innerHTML = ' ✗';
            cross.className = 'text-red-600 font-bold ml-2';
            optionElement.appendChild(cross);
        }
        
        // Disable the radio button
        radio.disabled = true;
    });
}

/**
 * Show quiz result message
 * @param {Element} questionElement - The question container element
 * @param {Boolean} isCorrect - Whether the answer was correct
 * @param {String} correctAnswerText - Text of the correct answer
 */
function showQuizResult(questionElement, isCorrect, correctAnswerText) {
    const resultContainer = questionElement.querySelector('.quiz-result');
    const feedbackContainer = questionElement.querySelector('.quiz-feedback');
    
    if (!resultContainer || !feedbackContainer) {
        return;
    }
    
    // Show result container
    resultContainer.classList.remove('hidden');
    
    // Set feedback message and styling
    if (isCorrect) {
        feedbackContainer.className = 'quiz-feedback p-3 rounded-lg correct';
        feedbackContainer.innerHTML = `
            <div class="flex items-center">
                <svg class="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                </svg>
                <span><strong>Правильно!</strong> Отличная работа!</span>
            </div>
        `;
    } else {
        feedbackContainer.className = 'quiz-feedback p-3 rounded-lg incorrect';
        feedbackContainer.innerHTML = `
            <div class="flex items-start">
                <svg class="w-5 h-5 mr-2 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
                </svg>
                <div>
                    <div><strong>Неправильно.</strong></div>
                    <div class="text-sm mt-1">Правильный ответ: <strong>${correctAnswerText}</strong></div>
                </div>
            </div>
        `;
    }
    
    // Add animation
    feedbackContainer.style.opacity = '0';
    feedbackContainer.style.transform = 'translateY(-10px)';
    
    setTimeout(() => {
        feedbackContainer.style.transition = 'all 0.3s ease';
        feedbackContainer.style.opacity = '1';
        feedbackContainer.style.transform = 'translateY(0)';
    }, 100);
}

/**
 * Disable all options for a question after it's answered
 * @param {Element} questionElement - The question container element
 */
function disableQuestionOptions(questionElement) {
    const options = questionElement.querySelectorAll('.quiz-option input[type="radio"]');
    const labels = questionElement.querySelectorAll('.quiz-option');
    
    options.forEach(option => {
        option.disabled = true;
    });
    
    labels.forEach(label => {
        label.style.cursor = 'default';
        label.classList.remove('hover:bg-gray-50');
    });
}

/**
 * Get quiz statistics (for future enhancements)
 * @returns {Object} Quiz statistics
 */
function getQuizStats() {
    const totalQuestions = quizData.length;
    const answeredCount = answeredQuestions.size;
    const unansweredCount = totalQuestions - answeredCount;
    
    return {
        total: totalQuestions,
        answered: answeredCount,
        unanswered: unansweredCount,
        completed: answeredCount === totalQuestions
    };
}

/**
 * Reset quiz (for future enhancements)
 */
function resetQuiz() {
    answeredQuestions.clear();
    
    // Reset all visual feedback
    const quizQuestions = document.querySelectorAll('.quiz-question');
    quizQuestions.forEach((questionElement, questionIndex) => {
        // Reset options
        const options = questionElement.querySelectorAll('.quiz-option');
        options.forEach(optionElement => {
            optionElement.classList.remove('correct', 'incorrect');
            optionElement.style.cursor = 'pointer';
            optionElement.classList.add('hover:bg-gray-50');
            
            // Remove feedback icons
            const icons = optionElement.querySelectorAll('span');
            icons.forEach(icon => {
                if (icon.innerHTML.includes('✓') || icon.innerHTML.includes('✗')) {
                    icon.remove();
                }
            });
            
            // Enable radio buttons
            const radio = optionElement.querySelector('input[type="radio"]');
            if (radio) {
                radio.disabled = false;
                radio.checked = false;
            }
        });
        
        // Hide results
        const resultContainer = questionElement.querySelector('.quiz-result');
        if (resultContainer) {
            resultContainer.classList.add('hidden');
        }
    });
    
    console.log('Quiz reset');
}

/**
 * Export functions for use in other scripts or console debugging
 */
window.Quiz = {
    initQuiz,
    getQuizStats,
    resetQuiz
};

// For backwards compatibility
window.initQuiz = initQuiz;

console.log('Quiz module loaded');
