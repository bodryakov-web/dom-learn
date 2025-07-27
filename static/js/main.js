/**
 * Main JavaScript file for the DOM course website
 */

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

function initializeApp() {
    // Initialize smooth scrolling for anchor links
    initSmoothScrolling();
    
    // Initialize responsive navigation
    initResponsiveNav();
    
    // Initialize animations
    initAnimations();
    
    // Initialize tooltips and other UI enhancements
    initUIEnhancements();
    
    console.log('DOM Course app initialized');
}

/**
 * Initialize smooth scrolling for anchor links
 */
function initSmoothScrolling() {
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    
    anchorLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                const headerOffset = 80; // Account for fixed header
                const elementPosition = targetElement.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
                
                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
                
                // Update URL without triggering scroll
                history.pushState(null, null, targetId);
            }
        });
    });
}

/**
 * Initialize responsive navigation
 */
function initResponsiveNav() {
    // Mobile menu toggle (if needed in future)
    const mobileMenuButton = document.querySelector('[data-mobile-menu-toggle]');
    const mobileMenu = document.querySelector('[data-mobile-menu]');
    
    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', function() {
            const isExpanded = mobileMenuButton.getAttribute('aria-expanded') === 'true';
            
            mobileMenuButton.setAttribute('aria-expanded', !isExpanded);
            mobileMenu.classList.toggle('hidden');
        });
    }
}

/**
 * Initialize animations and transitions
 */
function initAnimations() {
    // Intersection Observer for fade-in animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Observe elements that should fade in
    const animateElements = document.querySelectorAll('.card, .lesson-content, .quiz-question');
    animateElements.forEach(el => {
        observer.observe(el);
    });
}

/**
 * Initialize UI enhancements
 */
function initUIEnhancements() {
    // Add loading states to forms
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function() {
            const submitButton = form.querySelector('button[type="submit"]');
            if (submitButton) {
                submitButton.disabled = true;
                submitButton.textContent = 'Загрузка...';
            }
        });
    });
    
    // Add hover effects to interactive elements
    const interactiveElements = document.querySelectorAll('.card, .nav-button, .quiz-option');
    interactiveElements.forEach(el => {
        el.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
        });
        
        el.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
    
    // Initialize copy to clipboard functionality for code blocks
    initCodeCopyButtons();
}

/**
 * Add copy buttons to code blocks
 */
function initCodeCopyButtons() {
    const codeBlocks = document.querySelectorAll('pre code');
    
    codeBlocks.forEach((codeBlock, index) => {
        const pre = codeBlock.parentElement;
        const button = document.createElement('button');
        
        button.className = 'absolute top-2 right-2 bg-gray-600 text-white px-2 py-1 rounded text-xs opacity-0 transition-opacity hover:opacity-100';
        button.textContent = 'Копировать';
        button.onclick = () => copyToClipboard(codeBlock.textContent, button);
        
        // Make pre element relative positioned
        pre.style.position = 'relative';
        pre.appendChild(button);
        
        // Show button on hover
        pre.addEventListener('mouseenter', () => {
            button.style.opacity = '1';
        });
        
        pre.addEventListener('mouseleave', () => {
            button.style.opacity = '0';
        });
    });
}

/**
 * Copy text to clipboard
 */
async function copyToClipboard(text, button) {
    try {
        await navigator.clipboard.writeText(text);
        const originalText = button.textContent;
        button.textContent = 'Скопировано!';
        button.className = button.className.replace('bg-gray-600', 'bg-green-600');
        
        setTimeout(() => {
            button.textContent = originalText;
            button.className = button.className.replace('bg-green-600', 'bg-gray-600');
        }, 2000);
    } catch (err) {
        console.error('Failed to copy text: ', err);
        button.textContent = 'Ошибка';
        button.className = button.className.replace('bg-gray-600', 'bg-red-600');
        
        setTimeout(() => {
            button.textContent = 'Копировать';
            button.className = button.className.replace('bg-red-600', 'bg-gray-600');
        }, 2000);
    }
}

/**
 * Utility function to debounce function calls
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * Utility function to check if element is in viewport
 */
function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

/**
 * Progress tracking (for future enhancement)
 */
function trackProgress(action, data) {
    // This could be enhanced to track user progress
    // For now, just log to console
    console.log('Progress:', action, data);
}

/**
 * Error handling
 */
window.addEventListener('error', function(e) {
    console.error('JavaScript error:', e.error);
    // Could be enhanced to send errors to a logging service
});

/**
 * Performance monitoring
 */
window.addEventListener('load', function() {
    const loadTime = performance.now();
    console.log(`Page loaded in ${Math.round(loadTime)}ms`);
});

// Export functions for use in other scripts
window.DOMCourse = {
    copyToClipboard,
    debounce,
    isInViewport,
    trackProgress
};
