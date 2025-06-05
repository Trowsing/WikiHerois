/**
 * Theme Toggle Functionality for WikiHerois
 * 
 * This script handles switching between light and dark themes.
 * It saves the user's preference to localStorage for persistence between sessions.
 */

// Function to set the theme
function setTheme(themeName) {
  // Add or remove the dark-theme class from the body
  if (themeName === 'dark') {
    document.body.classList.add('dark-theme');
  } else {
    document.body.classList.remove('dark-theme');
  }
  
  // Save the current theme preference to localStorage
  localStorage.setItem('wikiHeroisTheme', themeName);
}

// Function to toggle between light and dark themes
function toggleTheme() {
  // Check if body currently has dark-theme class
  if (document.body.classList.contains('dark-theme')) {
    setTheme('light');
    updateToggleButtonText('🌙 Dark Mode');
  } else {
    setTheme('dark');
    updateToggleButtonText('☀️ Light Mode');
  }
}

// Function to update the toggle button text
function updateToggleButtonText(text) {
  const toggleButton = document.getElementById('theme-toggle');
  if (toggleButton) {
    toggleButton.textContent = text;
  }
}

// Initialize theme based on localStorage or system preference
function initTheme() {
  // Check if theme was previously set and stored in localStorage
  const savedTheme = localStorage.getItem('wikiHeroisTheme');
  
  if (savedTheme) {
    // Apply saved theme
    setTheme(savedTheme);
    updateToggleButtonText(savedTheme === 'dark' ? '☀️ Light Mode' : '🌙 Dark Mode');
  } else {
    // Check if user's system prefers dark mode
    const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');
    
    if (prefersDarkScheme.matches) {
      setTheme('dark');
      updateToggleButtonText('☀️ Light Mode');
    } else {
      setTheme('light');
      updateToggleButtonText('🌙 Dark Mode');
    }
  }
}

// Add event listener when DOM is fully loaded
document.addEventListener('DOMContentLoaded', function() {
  // Initialize theme
  initTheme();
  
  // Add click event listener to theme toggle button
  const themeToggle = document.getElementById('theme-toggle');
  if (themeToggle) {
    themeToggle.addEventListener('click', toggleTheme);
  }
});
