from flask import Flask, render_template_string, send_from_directory
import json
import os

app = Flask(__name__)

# Configuration
PORTFOLIO_IMAGE = 'image.png'
STATIC_FOLDER = 'static'

# Create static folder if it doesn't exist
if not os.path.exists(STATIC_FOLDER):
    os.makedirs(STATIC_FOLDER)

# Portfolio data
portfolio_data = {
    "name": "NAMRATHA N R",
    "title": "Web Developer & Aspiring ML Engineer",
    "location": "Bangalore, India",
    "email": "namrathanrpetemane18@gmail.com",
    "github": "https://github.com/NamrathaNRpetemane",
    "linkedin": "https://www.linkedin.com/in/namratha-nr-2ab271337/",
    "profile_image": PORTFOLIO_IMAGE,
    "bio": "Dynamic and ambitious engineering student with a focus on web development and machine learning, aiming to leverage strong adaptability, communication, and computer skills.",
    "education": [
        {
            "degree": "Bachelor of Engineering - Computer Science",
            "institution": "Channabasaveshwara Institute of Technology",
            "location": "Tumkur, Karnataka",
            "duration": "Nov 2022 – Jun 2026",
            "status": "3rd Year Student"
        },
        {
            "degree": "CBSE - PCMB",
            "institution": "Govt Boys College, Tiptur",
            "location": "Tiptur, Karnataka",
            "duration": "Aug 2020 – Apr 2022",
            "grade": "91.8%"
        }
    ],
    "skills": {
        "technical": ["Web Development", "Machine Learning", "SQL", "Tableau"],
        "soft": ["Team Collaboration", "Problem-Solving", "Communication"]
    },
    "languages": ["Kannada (Native)", "English (Highly Proficient)", "Hindi (Working Proficiency)"],
    "projects": [
        {
            "title": "AI-Powered Auto-Debugger",
            "description": "Using Gemini LLM to detect, explain, and fix code errors in real time with React frontend, FastAPI backend, and VS Code plugin",
            "tech": ["React", "FastAPI", "Gemini LLM", "VS Code"]
        },
        {
            "title": "Student Dashboard",
            "description": "Responsive dashboard using Bootstrap for seamless UX and real-time academic data visualization",
            "tech": ["Bootstrap", "JavaScript", "Data Visualization"]
        },
        {
            "title": "AI Phishing Email Detection",
            "description": "Detection system using NLP and Machine Learning to identify AI-generated phishing emails",
            "tech": ["NLP", "Machine Learning", "Python"]
        },
        {
            "title": "Medication Adherence App",
            "description": "Cross-platform app using React Native, Firebase, and TensorFlow Lite for pill identification and face recognition",
            "tech": ["React Native", "Firebase", "TensorFlow Lite"]
        }
    ],
    "achievements": [
        "Top 5 Finalist - National Buildathon 2025 (100+ teams)",
        "Participated in IDEATHON 2024 - ISTE Karnataka Section",
        "Contributed in START-A-THON 2.0 - MERN Stack Development"
    ],
    "hobbies": ["Problem Solving", "Reading about Quantum Computing"]
}

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, data=portfolio_data)

@app.route('/api/data')
def api_data():
    return json.dumps(portfolio_data)

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(STATIC_FOLDER, filename)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ data.name }} - Portfolio</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        :root {
            --primary: #00f5ff;
            --secondary: #ff006e;
            --accent: #8338ec;
            --dark: #0a0a0a;
            --light: #ffffff;
            --gradient: linear-gradient(135deg, var(--primary), var(--secondary), var(--accent));
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: var(--dark);
            color: var(--light);
            overflow-x: hidden;
            line-height: 1.6;
        }

        /* Animated Background */
        .bg-animation {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            background: radial-gradient(circle at 20% 80%, rgba(0, 245, 255, 0.1) 0%, transparent 50%),
                        radial-gradient(circle at 80% 20%, rgba(255, 0, 110, 0.1) 0%, transparent 50%),
                        radial-gradient(circle at 40% 40%, rgba(131, 56, 236, 0.1) 0%, transparent 50%);
            animation: bgShift 20s ease-in-out infinite;
        }

        @keyframes bgShift {
            0%, 100% { transform: rotate(0deg) scale(1); }
            50% { transform: rotate(180deg) scale(1.1); }
        }

        /* Floating particles */
        .particle {
            position: fixed;
            width: 4px;
            height: 4px;
            background: var(--primary);
            border-radius: 50%;
            animation: float 8s infinite ease-in-out;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0px) rotate(0deg); opacity: 0; }
            50% { transform: translateY(-100px) rotate(180deg); opacity: 1; }
        }

        /* Navigation */
        nav {
            position: fixed;
            top: 0;
            width: 100%;
            background: rgba(10, 10, 10, 0.95);
            backdrop-filter: blur(20px);
            z-index: 1000;
            padding: 1rem 0;
            transition: all 0.3s ease;
        }

        nav.scrolled {
            background: rgba(10, 10, 10, 0.98);
            box-shadow: 0 4px 20px rgba(0, 245, 255, 0.3);
        }

        .nav-container {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 2rem;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
            background: var(--gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .nav-links {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        .nav-links a {
            color: var(--light);
            text-decoration: none;
            transition: all 0.3s ease;
            position: relative;
        }

        .nav-links a:hover {
            color: var(--primary);
            transform: translateY(-2px);
        }

        .nav-links a::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 2px;
            background: var(--gradient);
            transition: width 0.3s ease;
        }

        .nav-links a:hover::after {
            width: 100%;
        }

        /* Hero Section */
        .hero {
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            background: linear-gradient(135deg, rgba(0, 245, 255, 0.1), rgba(255, 0, 110, 0.1));
            padding-top: 70px;
        }

        .hero-content {
            text-align: center;
            max-width: 800px;
            padding: 2rem;
            animation: fadeInUp 1s ease-out;
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Profile Photo Styles */
        .profile-photo-container {
            position: relative;
            width: 220px;
            height: 220px;
            margin: 0 auto 2rem;
            animation: photoFloat 8s ease-in-out infinite;
        }
        
        .profile-photo {
            width: 100%;
            height: 100%;
            border-radius: 50%;
            object-fit: cover;
            border: 5px solid transparent;
            background: 
                linear-gradient(var(--dark), var(--dark)) padding-box,
                var(--gradient) border-box;
            box-shadow: 0 0 30px rgba(0, 245, 255, 0.3);
            transition: all 0.3s ease;
        }
        
        .profile-photo:hover {
            transform: scale(1.05);
            box-shadow: 0 0 40px rgba(0, 245, 255, 0.5);
        }

        .profile-photo-container::after {
            content: '';
            position: absolute;
            top: -8px;
            left: -8px;
            right: -8px;
            bottom: -8px;
            border-radius: 50%;
            background: var(--gradient);
            z-index: -1;
            opacity: 0.5;
            animation: pulse 3s ease-in-out infinite;
        }

        @keyframes photoFloat {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-15px); }
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); opacity: 0.5; }
            50% { transform: scale(1.05); opacity: 0.8; }
        }

        .hero h1 {
            font-size: 4rem;
            margin-bottom: 1rem;
            background: var(--gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: textGlow 2s ease-in-out infinite alternate;
        }

        @keyframes textGlow {
            from { filter: brightness(1); }
            to { filter: brightness(1.3); }
        }

        .hero .subtitle {
            font-size: 1.5rem;
            margin-bottom: 2rem;
            color: rgba(255, 255, 255, 0.8);
        }

        .hero .bio {
            font-size: 1.1rem;
            margin-bottom: 3rem;
            color: rgba(255, 255, 255, 0.7);
            line-height: 1.8;
        }

        .cta-buttons {
            display: flex;
            gap: 1rem;
            justify-content: center;
            flex-wrap: wrap;
        }

        .btn {
            padding: 1rem 2rem;
            border: none;
            border-radius: 50px;
            font-size: 1rem;
            font-weight: bold;
            text-decoration: none;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            cursor: pointer;
        }

        .btn-primary {
            background: var(--gradient);
            color: var(--dark);
        }

        .btn-secondary {
            background: transparent;
            color: var(--light);
            border: 2px solid var(--primary);
        }

        .btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 30px rgba(0, 245, 255, 0.4);
        }

        .btn::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
            transition: left 0.5s;
        }

        .btn:hover::before {
            left: 100%;
        }

        /* Sections */
        .section {
            padding: 5rem 0;
            max-width: 1200px;
            margin: 0 auto;
        }

        .section-title {
            font-size: 3rem;
            text-align: center;
            margin-bottom: 3rem;
            background: var(--gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        /* Skills Section */
        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            padding: 0 2rem;
        }

        .skill-card {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 20px;
            padding: 2rem;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(0, 245, 255, 0.2);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .skill-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: var(--gradient);
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .skill-card:hover::before {
            opacity: 0.1;
        }

        .skill-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0, 245, 255, 0.3);
        }

        .skill-card h3 {
            color: var(--primary);
            margin-bottom: 1rem;
            font-size: 1.5rem;
        }

        .skill-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }

        .skill-tag {
            background: rgba(0, 245, 255, 0.2);
            color: var(--primary);
            padding: 0.5rem 1rem;
            border-radius: 25px;
            font-size: 0.9rem;
            border: 1px solid var(--primary);
        }

        /* Projects Section */
        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 2rem;
            padding: 0 2rem;
        }

        .project-card {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 20px;
            padding: 2rem;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 0, 110, 0.2);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .project-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, var(--secondary), var(--accent));
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .project-card:hover::before {
            opacity: 0.1;
        }

        .project-card:hover {
            transform: translateY(-10px) scale(1.02);
            box-shadow: 0 20px 40px rgba(255, 0, 110, 0.3);
        }

        .project-card h3 {
            color: var(--secondary);
            margin-bottom: 1rem;
            font-size: 1.5rem;
        }

        .project-card p {
            color: rgba(255, 255, 255, 0.8);
            margin-bottom: 1rem;
            line-height: 1.6;
        }

        .tech-stack {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }

        .tech-tag {
            background: rgba(255, 0, 110, 0.2);
            color: var(--secondary);
            padding: 0.3rem 0.8rem;
            border-radius: 15px;
            font-size: 0.8rem;
            border: 1px solid var(--secondary);
        }

        /* Achievements Section */
        .achievements-list {
            padding: 0 2rem;
        }

        .achievement-item {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            border-left: 4px solid var(--accent);
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
        }

        .achievement-item:hover {
            transform: translateX(10px);
            background: rgba(131, 56, 236, 0.1);
        }

        .achievement-item i {
            color: var(--accent);
            margin-right: 1rem;
            font-size: 1.2rem;
        }

        /* Contact Section */
        .contact-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            padding: 0 2rem;
        }

        .contact-item {
            text-align: center;
            padding: 2rem;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 20px;
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
            border: 1px solid rgba(0, 245, 255, 0.2);
        }

        .contact-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 30px rgba(0, 245, 255, 0.2);
        }

        .contact-item i {
            font-size: 3rem;
            color: var(--primary);
            margin-bottom: 1rem;
        }

        .contact-item a {
            color: var(--light);
            text-decoration: none;
            transition: color 0.3s ease;
            word-break: break-all;
            overflow-wrap: break-word;
            display: block;
            padding: 0 0.5rem;
            font-size: 0.9rem;
            line-height: 1.4;
        }

        .contact-item a:hover {
            color: var(--primary);
        }

        .contact-item p {
            word-break: break-word;
            overflow-wrap: break-word;
            padding: 0 0.5rem;
        }

        /* Footer */
        footer {
            background: rgba(10, 10, 10, 0.9);
            padding: 2rem 0;
            text-align: center;
            border-top: 1px solid rgba(0, 245, 255, 0.2);
        }

        /* Mobile Responsiveness */
        @media (max-width: 768px) {
            .hero h1 {
                font-size: 2.5rem;
            }
            
            .hero .subtitle {
                font-size: 1.2rem;
            }
            
            .profile-photo-container {
                width: 180px;
                height: 180px;
            }
            
            .cta-buttons {
                flex-direction: column;
                align-items: center;
            }
            
            .nav-links {
                display: none;
            }
            
            .section-title {
                font-size: 2rem;
            }
        }

        /* Scroll reveal animation */
        .reveal {
            opacity: 0;
            transform: translateY(50px);
            transition: all 0.6s ease;
        }

        .reveal.active {
            opacity: 1;
            transform: translateY(0);
        }
    </style>
</head>
<body>
    <div class="bg-animation"></div>
    
    <!-- Floating Particles -->
    <div class="particle" style="left: 10%; animation-delay: 0s;"></div>
    <div class="particle" style="left: 20%; animation-delay: 2s;"></div>
    <div class="particle" style="left: 30%; animation-delay: 4s;"></div>
    <div class="particle" style="left: 40%; animation-delay: 1s;"></div>
    <div class="particle" style="left: 50%; animation-delay: 3s;"></div>
    <div class="particle" style="left: 60%; animation-delay: 5s;"></div>
    <div class="particle" style="left: 70%; animation-delay: 2.5s;"></div>
    <div class="particle" style="left: 80%; animation-delay: 4.5s;"></div>
    <div class="particle" style="left: 90%; animation-delay: 1.5s;"></div>

    <!-- Navigation -->
    <nav id="navbar">
        <div class="nav-container">
            <div class="logo">{{ data.name }}</div>
            <ul class="nav-links">
                <li><a href="#home">Home</a></li>
                <li><a href="#skills">Skills</a></li>
                <li><a href="#projects">Projects</a></li>
                <li><a href="#achievements">Achievements</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </div>
    </nav>

    <!-- Hero Section -->
    <section id="home" class="hero">
        <div class="hero-content">
            <div class="profile-photo-container">
                <img src="{{ url_for('static', filename=data.profile_image) if data.profile_image.startswith('static/') else data.profile_image }}" alt="{{ data.name }}" class="profile-photo">
            </div>
            <h1>{{ data.name }}</h1>
            <p class="subtitle">{{ data.title }}</p>
            <p class="bio">{{ data.bio }}</p>
            <div class="cta-buttons">
                <a href="#projects" class="btn btn-primary">View My Work</a>
                <a href="#contact" class="btn btn-secondary">Get In Touch</a>
            </div>
        </div>
    </section>

    <!-- Skills Section -->
    <section id="skills" class="section">
        <h2 class="section-title reveal">Skills & Expertise</h2>
        <div class="skills-grid">
            <div class="skill-card reveal">
                <h3><i class="fas fa-code"></i> Technical Skills</h3>
                <div class="skill-tags">
                    {% for skill in data.skills.technical %}
                    <span class="skill-tag">{{ skill }}</span>
                    {% endfor %}
                </div>
            </div>
            <div class="skill-card reveal">
                <h3><i class="fas fa-users"></i> Soft Skills</h3>
                <div class="skill-tags">
                    {% for skill in data.skills.soft %}
                    <span class="skill-tag">{{ skill }}</span>
                    {% endfor %}
                </div>
            </div>
            <div class="skill-card reveal">
                <h3><i class="fas fa-language"></i> Languages</h3>
                <div class="skill-tags">
                    {% for lang in data.languages %}
                    <span class="skill-tag">{{ lang }}</span>
                    {% endfor %}
                </div>
            </div>
        </div>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="section">
        <h2 class="section-title reveal">Featured Projects</h2>
        <div class="projects-grid">
            {% for project in data.projects %}
            <div class="project-card reveal">
                <h3>{{ project.title }}</h3>
                <p>{{ project.description }}</p>
                <div class="tech-stack">
                    {% for tech in project.tech %}
                    <span class="tech-tag">{{ tech }}</span>
                    {% endfor %}
                </div>
            </div>
            {% endfor %}
        </div>
    </section>

    <!-- Achievements Section -->
    <section id="achievements" class="section">
        <h2 class="section-title reveal">Achievements & Recognition</h2>
        <div class="achievements-list">
            {% for achievement in data.achievements %}
            <div class="achievement-item reveal">
                <i class="fas fa-trophy"></i>
                {{ achievement }}
            </div>
            {% endfor %}
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="section">
        <h2 class="section-title reveal">Let's Connect</h2>
        <div class="contact-grid">
            <div class="contact-item reveal">
                <i class="fas fa-envelope"></i>
                <h3>Email</h3>
                <a href="mailto:{{ data.email }}">{{ data.email }}</a>
            </div>
            <div class="contact-item reveal">
                <i class="fab fa-github"></i>
                <h3>GitHub</h3>
                <a href="{{ data.github }}" target="_blank">View Profile</a>
            </div>
            <div class="contact-item reveal">
                <i class="fab fa-linkedin"></i>
                <h3>LinkedIn</h3>
                <a href="{{ data.linkedin }}" target="_blank">Connect</a>
            </div>
            <div class="contact-item reveal">
                <i class="fas fa-map-marker-alt"></i>
                <h3>Location</h3>
                <p>{{ data.location }}</p>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <p>&copy; 2025 {{ data.name }}. Crafted with passion and innovation.</p>
    </footer>

    <script>
        // Smooth scrolling
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });

        // Navbar scroll effect
        window.addEventListener('scroll', () => {
            const navbar = document.getElementById('navbar');
            if (window.scrollY > 100) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });

        // Reveal animation on scroll
        function reveal() {
            const reveals = document.querySelectorAll('.reveal');
            reveals.forEach(element => {
                const windowHeight = window.innerHeight;
                const elementTop = element.getBoundingClientRect().top;
                const elementVisible = 150;

                if (elementTop < windowHeight - elementVisible) {
                    element.classList.add('active');
                }
            });
        }

        window.addEventListener('scroll', reveal);
        reveal(); // Initial call

        // Add more dynamic particles
        function createParticle() {
            const particle = document.createElement('div');
            particle.className = 'particle';
            particle.style.left = Math.random() * 100 + '%';
            particle.style.animationDelay = Math.random() * 8 + 's';
            particle.style.animationDuration = (Math.random() * 8 + 4) + 's';
            document.body.appendChild(particle);

            setTimeout(() => {
                particle.remove();
            }, 12000);
        }

        setInterval(createParticle, 2000);

        // Typing effect for hero title
        function typeWriter(element, text, speed = 100) {
            let i = 0;
            element.innerHTML = '';
            function type() {
                if (i < text.length) {
                    element.innerHTML += text.charAt(i);
                    i++;
                    setTimeout(type, speed);
                }
            }
            type();
        }

        // Profile photo hover effects
        const profilePhoto = document.querySelector('.profile-photo-container');
        if (profilePhoto) {
            profilePhoto.addEventListener('mouseenter', function() {
                this.style.animation = 'photoFloat 4s ease-in-out infinite';
            });
            
            profilePhoto.addEventListener('mouseleave', function() {
                this.style.animation = 'photoFloat 8s ease-in-out infinite';
            });
        }

        // Initialize typing effect
        window.addEventListener('load', () => {
            const heroTitle = document.querySelector('.hero h1');
            if (heroTitle) {
                const originalText = heroTitle.textContent;
                typeWriter(heroTitle, originalText, 150);
            }
        });

        // Add interactive cursor trail
        document.addEventListener('mousemove', (e) => {
            if (Math.random() > 0.9) {
                const trail = document.createElement('div');
                trail.className = 'particle';
                trail.style.left = e.clientX + 'px';
                trail.style.top = e.clientY + 'px';
                trail.style.position = 'fixed';
                trail.style.pointerEvents = 'none';
                trail.style.zIndex = '9999';
                document.body.appendChild(trail);

                setTimeout(() => {
                    trail.remove();
                }, 1000);
            }
        });
    </script>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)