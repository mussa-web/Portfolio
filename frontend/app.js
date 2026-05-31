const API = (window.API_ORIGIN || '').replace(/\/$/, '');

async function fetchJSON(path){
  const url = path.startsWith('http') ? path : (API + path);
  const res = await fetch(url);
  if(!res.ok) throw new Error('Network error');
  return res.json();
}

function profileImgUrl(p){
  const defaultImage = 'profile.jpg';
  if(!p || !p.picture_path) return defaultImage;
  return p.picture_path;
}

function renderHero(p){
  const title = document.getElementById('hero-title');
  const subtitle = document.getElementById('hero-subtitle');
  const image = document.querySelector('.hero-card .avatar');
  if(title) title.textContent = p.full_name || 'Portfolio';
  if(subtitle) subtitle.textContent = p.bio || 'Building modern data products and network marketing growth.';
  if(image) image.src = profileImgUrl(p);
}

function renderAbout(p){
  const el = document.getElementById('about');
  el.innerHTML = `
    <div class="section-header reveal">
      <span class="eyebrow">About</span>
      <h2>About ${p.full_name}</h2>
    </div>
    <div class="about-grid reveal">
      <div class="about-copy">
        <p>${p.bio || 'A dedicated professional with experience in data science, analytics, and network marketing.'}</p>
        <ul>
          <li><strong>Location:</strong> Remote / Global</li>
          <li><strong>Instagram:</strong> <span>${p.twitter || '@mussa_bbo'}</span></li>
        </ul>
      </div>
      <div class="about-stats">
        <div class="stat-card reveal-delay-0"><strong>2</strong><span>Years experience</span></div>
        <div class="stat-card reveal-delay-1"><strong>4</strong><span>Projects delivered</span></div>
        <div class="stat-card reveal-delay-2"><strong>2</strong><span>Skills domains</span></div>
      </div>
    </div>
  `;
}

function renderSkills(list){
  const el = document.getElementById('skills');
  const categories = {};
  list.forEach(skill => {
    const key = skill.category || 'General';
    if(!categories[key]) categories[key] = [];
    categories[key].push(skill);
  });

  el.innerHTML = '<div class="section-header reveal"><span class="eyebrow">Expertise</span><h2>Core skills</h2></div>' + Object.entries(categories).map(([category, skills]) => `
    <div class="skill-section reveal">
      <h3>${category.replace(/-/g, ' ')}</h3>
      <div class="skills-grid">${skills.map(s => `<div class="skill-pill"><strong>${s.name}</strong><span>${s.level || 'Experienced'}</span></div>`).join('')}</div>
    </div>
  `).join('');
}

function renderProjects(list){
  const el = document.getElementById('projects');
  el.innerHTML = `
    <div class="section-header reveal"><span class="eyebrow">Projects</span><h2>Recent work</h2></div>
    <div class="projects-grid">${list.map((p, index) => `
      <article class="project-card reveal-delay-${index % 3}">
        <div class="project-card-copy">
          <h3>${p.title}</h3>
          <p>${p.description || 'High-impact project with measurable outcomes.'}</p>
        </div>
        <div class="project-card-meta">
          <a class="btn btn-secondary" href="/project.html?id=${p.id}">Explore</a>
        </div>
      </article>
    `).join('')}</div>
  `;
}

function renderContact(){
  const el = document.getElementById('contact');
  el.innerHTML = `
    <div class="section-header reveal">
      <span class="eyebrow">Contact</span>
      <h2>Let's build something together</h2>
    </div>
    <div class="contact-panel reveal">
      <p>Reach out to discuss a project, collaboration, or a new data-driven strategy.</p>
      <p class="contact-email"><strong>Email:</strong> <a href="mailto:mussarutta4@gmail.com">mussarutta4@gmail.com</a></p>
      <div class="contact-actions">
        <a class="btn btn-primary" href="mailto:mussarutta4@gmail.com">Email me</a>
        <a class="btn btn-secondary" href="/project.html?id=1">See work</a>
      </div>
    </div>
  `;
}

function revealElement(el, delay = 0){
  if(!el) return;
  setTimeout(() => el.classList.add('is-visible'), delay);
}

function setupRevealAnimations(){
  document.querySelectorAll('.reveal').forEach((el, index) => {
    const delay = parseInt(el.className.match(/reveal-delay-(\d+)/)?.[1] || '0', 10) * 120;
    revealElement(el, 120 + delay);
  });
}

async function init(){
  const heroCard = document.querySelector('.hero-card');
  heroCard?.classList.add('animate-in');

  try{
    const profile = await fetchJSON('/profile/');
    renderHero(profile);
    renderAbout(profile);
  }catch(e){ console.warn('profile not found', e) }

  try{
    const skills = await fetchJSON('/skills/');
    renderSkills(skills);
  }catch(e){ console.warn('skills not found', e) }

  try{
    const projects = await fetchJSON('/projects/');
    renderProjects(projects);
  }catch(e){ console.warn('projects not found', e) }

  renderContact();
  setupRevealAnimations();
}

window.addEventListener('DOMContentLoaded', init);
