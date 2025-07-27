/**
 * Admin panel JavaScript functionality
 */

document.addEventListener('DOMContentLoaded', function() {
    initializeAdmin();
});

function initializeAdmin() {
    // Initialize drag and drop for reordering (future enhancement)
    initDragAndDrop();
    
    // Initialize image upload functionality
    initImageUpload();
    
    // Initialize form validations
    initFormValidations();
    
    // Initialize keyboard shortcuts
    initKeyboardShortcuts();
    
    console.log('Admin panel initialized');
}

/**
 * Initialize drag and drop functionality for reordering items
 */
function initDragAndDrop() {
    // This would be implemented for reordering levels, sections, and lessons
    // For now, keeping it simple as per requirements
    console.log('Drag and drop ready for future implementation');
}

/**
 * Initialize image upload functionality
 */
function initImageUpload() {
    const imageUploadModal = document.getElementById('imageUploadModal');
    const imageUploadForm = document.getElementById('imageUploadForm');
    const imageFile = document.getElementById('imageFile');
    const imageUploadProgress = document.getElementById('imageUploadProgress');
    const imageUploadBar = document.getElementById('imageUploadBar');
    
    if (!imageUploadForm) return;
    
    // Handle image upload form submission
    imageUploadForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const file = imageFile.files[0];
        if (!file) {
            alert('Пожалуйста, выберите файл');
            return;
        }
        
        // Validate file type
        const allowedTypes = ['image/png', 'image/jpeg', 'image/jpg', 'image/webp', 'image/svg+xml'];
        if (!allowedTypes.includes(file.type)) {
            alert('Неподдерживаемый тип файла. Используйте PNG, JPG, WEBP или SVG.');
            return;
        }
        
        // Validate file size (5MB)
        const maxSize = 5 * 1024 * 1024;
        if (file.size > maxSize) {
            alert('Файл слишком большой. Максимальный размер: 5MB.');
            return;
        }
        
        uploadImage(file);
    });
    
    // Drag and drop functionality for image upload
    const dropZone = document.querySelector('.image-drop-zone');
    if (dropZone) {
        dropZone.addEventListener('dragover', function(e) {
            e.preventDefault();
            this.classList.add('drag-over');
        });
        
        dropZone.addEventListener('dragleave', function(e) {
            e.preventDefault();
            this.classList.remove('drag-over');
        });
        
        dropZone.addEventListener('drop', function(e) {
            e.preventDefault();
            this.classList.remove('drag-over');
            
            const files = e.dataTransfer.files;
            if (files.length > 0) {
                imageFile.files = files;
                uploadImage(files[0]);
            }
        });
    }
}

/**
 * Upload image to server
 */
function uploadImage(file) {
    const imageUploadProgress = document.getElementById('imageUploadProgress');
    const imageUploadBar = document.getElementById('imageUploadBar');
    
    // Show progress
    imageUploadProgress.classList.remove('hidden');
    imageUploadBar.style.width = '0%';
    
    const formData = new FormData();
    formData.append('file', file);
    
    // Create XMLHttpRequest for progress tracking
    const xhr = new XMLHttpRequest();
    
    // Track upload progress
    xhr.upload.addEventListener('progress', function(e) {
        if (e.lengthComputable) {
            const percentComplete = (e.loaded / e.total) * 100;
            imageUploadBar.style.width = percentComplete + '%';
        }
    });
    
    // Handle response
    xhr.addEventListener('load', function() {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);
            if (response.url) {
                // Insert image URL into TinyMCE editor
                if (typeof tinymce !== 'undefined') {
                    const editor = tinymce.activeEditor;
                    if (editor) {
                        editor.insertContent(`<img src="${response.url}" alt="Uploaded image" style="max-width: 100%; height: auto;">`);
                    }
                }
                closeImageUpload();
                alert('Изображение успешно загружено!');
            } else {
                alert('Ошибка загрузки: ' + (response.error || 'Неизвестная ошибка'));
            }
        } else {
            alert('Ошибка загрузки изображения');
        }
        
        // Hide progress
        imageUploadProgress.classList.add('hidden');
    });
    
    // Handle errors
    xhr.addEventListener('error', function() {
        alert('Ошибка загрузки изображения');
        imageUploadProgress.classList.add('hidden');
    });
    
    // Send request
    xhr.open('POST', '/bod/upload_image');
    xhr.send(formData);
}

/**
 * Close image upload modal
 */
function closeImageUpload() {
    const modal = document.getElementById('imageUploadModal');
    const form = document.getElementById('imageUploadForm');
    const progress = document.getElementById('imageUploadProgress');
    
    if (modal) modal.classList.add('hidden');
    if (form) form.reset();
    if (progress) progress.classList.add('hidden');
}

/**
 * Open image upload modal
 */
function openImageUpload() {
    const modal = document.getElementById('imageUploadModal');
    if (modal) modal.classList.remove('hidden');
}

/**
 * Initialize form validations
 */
function initFormValidations() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        // Add real-time validation
        const inputs = form.querySelectorAll('input[required], textarea[required]');
        inputs.forEach(input => {
            input.addEventListener('blur', function() {
                validateField(this);
            });
            
            input.addEventListener('input', function() {
                // Clear error state when user starts typing
                this.classList.remove('error');
            });
        });
        
        // Validate on submit
        form.addEventListener('submit', function(e) {
            let isValid = true;
            
            inputs.forEach(input => {
                if (!validateField(input)) {
                    isValid = false;
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                alert('Пожалуйста, заполните все обязательные поля');
            }
        });
    });
}

/**
 * Validate individual form field
 */
function validateField(field) {
    const value = field.value.trim();
    const isValid = value.length > 0;
    
    if (isValid) {
        field.classList.remove('error');
        field.classList.add('valid');
    } else {
        field.classList.remove('valid');
        field.classList.add('error');
    }
    
    return isValid;
}

/**
 * Initialize keyboard shortcuts
 */
function initKeyboardShortcuts() {
    document.addEventListener('keydown', function(e) {
        // Ctrl+S to save (prevent browser save dialog)
        if (e.ctrlKey && e.key === 's') {
            e.preventDefault();
            const form = document.querySelector('form');
            if (form) {
                form.submit();
            }
        }
        
        // Escape to close modals
        if (e.key === 'Escape') {
            closeAllModals();
        }
    });
}

/**
 * Close all open modals
 */
function closeAllModals() {
    const modals = document.querySelectorAll('.modal, [id$="Modal"]');
    modals.forEach(modal => {
        modal.classList.add('hidden');
    });
}

/**
 * Auto-save functionality (future enhancement)
 */
function initAutoSave() {
    // This could be implemented to auto-save form data
    console.log('Auto-save ready for future implementation');
}

/**
 * Bulk operations (future enhancement)
 */
function initBulkOperations() {
    // This could be implemented for bulk delete/edit operations
    console.log('Bulk operations ready for future implementation');
}

/**
 * Statistics and analytics (future enhancement)
 */
function initAnalytics() {
    // This could track admin usage patterns
    console.log('Analytics ready for future implementation');
}

// Make functions available globally
window.AdminPanel = {
    openImageUpload,
    closeImageUpload,
    uploadImage,
    validateField,
    closeAllModals
};

// Add CSS classes for form validation
const style = document.createElement('style');
style.textContent = `
    .error {
        border-color: #ef4444 !important;
        box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.1) !important;
    }
    
    .valid {
        border-color: #10b981 !important;
        box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1) !important;
    }
    
    .drag-over {
        border-color: #3b82f6 !important;
        background-color: #dbeafe !important;
    }
`;
document.head.appendChild(style);
