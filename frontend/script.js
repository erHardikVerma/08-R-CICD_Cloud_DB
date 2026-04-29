// Switch between local and production:
const API_URL = 'https://ebg-backend.onrender.com';  // Production (Render)
// const API_URL = 'http://localhost:5000';  // Local Development

// ═══════ State ═══════
let currentUser = null;

// ═══════ Tab Switching ═══════
function switchTab(tab) {
    const loginTab = document.getElementById('login-tab');
    const signupTab = document.getElementById('signup-tab');
    const loginForm = document.getElementById('login-form');
    const signupForm = document.getElementById('signup-form');
    const slider = document.querySelector('.tab-slider');
    const message = document.getElementById('auth-message');

    message.className = 'message';
    message.style.display = 'none';

    if (tab === 'login') {
        loginTab.classList.add('active');
        signupTab.classList.remove('active');
        loginForm.classList.add('active');
        signupForm.classList.remove('active');
        slider.style.left = '4px';
    } else {
        signupTab.classList.add('active');
        loginTab.classList.remove('active');
        signupForm.classList.add('active');
        loginForm.classList.remove('active');
        slider.style.left = 'calc(50%)';
    }
}

// ═══════ Show Message ═══════
function showMessage(text, type) {
    const msg = document.getElementById('auth-message');
    msg.textContent = text;
    msg.className = `message ${type}`;
}

// ═══════ Login ═══════
async function handleLogin(e) {
    e.preventDefault();
    const btn = document.getElementById('login-btn');
    btn.classList.add('loading');

    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;

    try {
        const res = await fetch(`${API_URL}/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password })
        });

        const data = await res.json();

        if (res.ok) {
            currentUser = data.user;
            showAppScreen();
        } else {
            showMessage(data.error || 'Login failed', 'error');
        }
    } catch (err) {
        showMessage('Server is waking up... try again in 30s', 'error');
    }

    btn.classList.remove('loading');
}

// ═══════ Signup ═══════
async function handleSignup(e) {
    e.preventDefault();
    const btn = document.getElementById('signup-btn');
    btn.classList.add('loading');

    const name = document.getElementById('signup-name').value;
    const username = document.getElementById('signup-username').value;
    const password = document.getElementById('signup-password').value;

    try {
        const res = await fetch(`${API_URL}/signup`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, username, password })
        });

        const data = await res.json();

        if (res.ok) {
            showMessage('Account created! Please login.', 'success');
            setTimeout(() => switchTab('login'), 1500);
        } else {
            showMessage(data.error || 'Signup failed', 'error');
        }
    } catch (err) {
        showMessage('Server is waking up... try again in 30s', 'error');
    }

    btn.classList.remove('loading');
}

// ═══════ Show App Screen ═══════
function showAppScreen() {
    document.getElementById('auth-screen').classList.remove('active');
    document.getElementById('app-screen').classList.add('active');

    // Set user info
    document.getElementById('display-name').textContent = currentUser.name;
    const roleTag = document.getElementById('role-tag');
    roleTag.textContent = currentUser.role;
    roleTag.className = `role-tag ${currentUser.role}`;

    // Welcome text
    document.getElementById('welcome-text').textContent = `Welcome back, ${currentUser.name}!`;

    // Show admin panel if admin
    if (currentUser.role === 'admin') {
        document.getElementById('admin-panel').style.display = 'block';
    } else {
        document.getElementById('admin-panel').style.display = 'none';
    }

    // Load notes
    loadNotes();
}

// ═══════ Load Notes ═══════
async function loadNotes() {
    const feed = document.getElementById('notes-feed');
    const emptyState = document.getElementById('empty-state');

    feed.innerHTML = '<div class="loading-notes"><div class="spinner"></div><p>Loading notes...</p></div>';

    try {
        const res = await fetch(`${API_URL}/notes`);
        const notes = await res.json();

        if (notes.length === 0) {
            feed.innerHTML = '';
            emptyState.style.display = 'block';
            return;
        }

        emptyState.style.display = 'none';
        feed.innerHTML = notes.map((note, i) => `
            <div class="note-card" style="animation-delay: ${i * 0.1}s">
                <div class="note-content">${escapeHtml(note.content)}</div>
                <div class="note-meta">
                    <span class="note-author">✍️ ${escapeHtml(note.created_by)}</span>
                    <span>${formatDate(note.created_at)}</span>
                </div>
            </div>
        `).join('');
    } catch (err) {
        feed.innerHTML = '<p style="text-align:center; color: var(--danger);">Failed to load notes</p>';
    }
}

// ═══════ Add Note (Admin) ═══════
async function addNote() {
    const input = document.getElementById('note-input');
    const content = input.value.trim();

    if (!content) return;

    try {
        const res = await fetch(`${API_URL}/notes`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                content,
                username: currentUser.username,
                role: currentUser.role
            })
        });

        const data = await res.json();

        if (res.ok) {
            input.value = '';
            loadNotes();
        } else {
            alert(data.error || 'Failed to add note');
        }
    } catch (err) {
        alert('Failed to connect to server');
    }
}

// ═══════ Logout ═══════
function logout() {
    currentUser = null;
    document.getElementById('app-screen').classList.remove('active');
    document.getElementById('auth-screen').classList.add('active');
    document.getElementById('login-form').reset();
    document.getElementById('signup-form').reset();
    document.getElementById('auth-message').style.display = 'none';
}

// ═══════ Helpers ═══════
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function formatDate(dateStr) {
    if (!dateStr) return '';
    const date = new Date(dateStr);
    return date.toLocaleDateString('en-IN', {
        day: 'numeric',
        month: 'short',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
}
