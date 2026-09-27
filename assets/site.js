'use strict';
const form=document.querySelector('#publication-filters');
if(form){
 const cards=[...document.querySelectorAll('.publication')];
 const q=form.querySelector('[name=q]'),area=form.querySelector('[name=area]'),role=form.querySelector('[name=role]'),year=form.querySelector('[name=year]');
 const status=document.querySelector('#result-count'),empty=document.querySelector('#empty-results');
 function update(){const terms=q.value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);let count=0;
 cards.forEach(card=>{const show=terms.every(t=>card.dataset.search.includes(t))&&(!area.value||card.dataset.areas.split(' ').includes(area.value))&&(!role.value||role.value===card.dataset.role)&&(!year.value||year.value===card.dataset.year);card.hidden=!show;if(show)count++;});
 status.textContent=`${count} of ${cards.length} publications`;empty.hidden=count!==0;
 const params=new URLSearchParams();[q,area,role,year].forEach(el=>{if(el.value)params.set(el.name,el.value)});history.replaceState(null,'',location.pathname+(params.size?'?'+params:''));}
 const params=new URLSearchParams(location.search);[q,area,role,year].forEach(el=>{el.value=params.get(el.name)||''});
 form.addEventListener('submit',e=>e.preventDefault());form.addEventListener('input',update);form.addEventListener('reset',()=>setTimeout(update,0));update();
}
