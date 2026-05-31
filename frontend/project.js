const API = (window.API_ORIGIN || '').replace(/\/$/, '');

async function fetchJSON(path){
  const url = path.startsWith('http') ? path : (API + path);
  const res = await fetch(url);
  if(!res.ok) throw new Error('Network error');
  return res.json();
}

function buildBackLink(){
  return `<a class="btn btn-secondary" href="/project.html">Back to projects</a>`;
}

function renderProject(p){
  const el = document.getElementById('project-detail');
  el.innerHTML = `
    <div class="project-detail-card">
      <div class="project-detail-copy">
        <span class="eyebrow">Project</span>
        <h1>${p.title}</h1>
        <p>${p.description || 'Detailed project summary will appear here.'}</p>
      </div>
      <div class="project-detail-actions">
        ${p.url ? `<a class="btn btn-primary" href="${p.url}" target="_blank">Open project</a>` : ''}
        ${buildBackLink()}
      </div>
    </div>
  `;
}

function getParam(name){
  return new URLSearchParams(window.location.search).get(name);
}

async function init(){
  const id = getParam('id');
  const el = document.getElementById('project-detail');
  if(!id){ el.innerHTML = '<p>No project id provided.</p>';
    return;
  }
  try{
    const proj = await fetchJSON(`/projects/${id}`);
    renderProject(proj);
  }catch(e){
    el.innerHTML = '<p>Project not found. Please return to projects.</p>' + buildBackLink();
  }
}

window.addEventListener('DOMContentLoaded', init);
