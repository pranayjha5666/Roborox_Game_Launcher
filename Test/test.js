document.addEventListener('DOMContentLoaded', () => {
    const navToggle = document.querySelector('.nav-toggle');
    const navLinks = document.querySelector('.nav-links');
    const rightContainer = document.querySelector('.right-container');
  
    navToggle.addEventListener('click', () => {
      navLinks.classList.toggle('active');
      rightContainer.classList.toggle('active');
    });
  });
  