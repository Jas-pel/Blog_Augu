
import blogData from './data.js';

document.addEventListener('DOMContentLoaded', () => {
    const navLinks = document.getElementById('navLinks');
    const blogContent = document.getElementById('blogContent');
    const progressBar = document.getElementById('progressBar');
    const hero = document.getElementById('hero');

    // Setup hero background
    hero.style.backgroundImage = `linear-gradient(rgba(26, 58, 95, 0.4), rgba(26, 58, 95, 0.6)), url('hero.png')`;

    function renderTerm(termIndex) {
        const term = blogData[termIndex];
        if (!term) return;

        // Clear contents
        blogContent.innerHTML = '';
        
        // Add Term Header
        const h2 = document.createElement('h2');
        h2.className = 'term-title';
        h2.textContent = term.name;
        blogContent.appendChild(h2);

        // Add Posts
        term.posts.forEach((post, i) => {
            const postEl = document.createElement('article');
            postEl.className = 'post';
            postEl.innerHTML = `
                <header class="post-header">
                    <span class="post-date">${post.date}</span>
                    ${post.title ? `<h3 class="post-title">${post.title}</h3>` : ''}
                </header>
                <div class="post-content">
                    <p>${post.content}</p>
                </div>
            `;
            blogContent.appendChild(postEl);
        });

        // Scroll to top of content
        window.scrollTo({ top: hero.offsetHeight - 50, behavior: 'smooth' });
        
        // Update active nav
        document.querySelectorAll('.nav-link').forEach((link, i) => {
            link.classList.toggle('active', i === termIndex);
        });
    }

    // Build Navigation
    blogData.forEach((term, index) => {
        const link = document.createElement('a');
        link.className = 'nav-link';
        link.textContent = term.name;
        link.onclick = () => renderTerm(index);
        navLinks.appendChild(link);
    });

    // Initial render
    if (blogData.length > 0) {
        renderTerm(0);
    }

    // Progress Bar Logic
    window.onscroll = () => {
        const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (winScroll / height) * 100;
        progressBar.style.width = scrolled + "%";
    };

    // Initialize Lucide Icons
    if (window.lucide) {
        window.lucide.createIcons();
    }
});
