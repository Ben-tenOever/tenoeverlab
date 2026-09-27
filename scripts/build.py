"""Build a complete, JavaScript-optional scholarly website from the reviewed corpus."""
from pathlib import Path
import json, re, html, shutil, hashlib
import markdown
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs'
BASE='https://tenoeverlab.us'
# Benjamin tenOever's canonical identity lives on benjamintenoever.com; this site refers to it rather than minting a second Person.
PERSON='https://benjamintenoever.com/#person'
LAB=BASE+'/#lab'
ORCID='https://orcid.org/0000-0003-0324-3078'
PERSON_NODE={'@type':'Person','@id':PERSON,'name':'Benjamin tenOever','alternateName':['Benjamin R. tenOever','Ben tenOever'],'honorificSuffix':'PhD',
 'url':'https://benjamintenoever.com/','jobTitle':['Jan T. Vilcek Professor of Molecular Pathogenesis','Chair, Department of Microbiology','Director, NYU Langone Virology Institute','Professor, Department of Medicine'],
 'worksFor':{'@type':'CollegeOrUniversity','name':'NYU Grossman School of Medicine','url':'https://med.nyu.edu/','parentOrganization':{'@type':'Organization','name':'NYU Langone Health','url':'https://nyulangone.org/'}},
 'affiliation':{'@type':'Organization','name':'Department of Microbiology, NYU Grossman School of Medicine','url':'https://med.nyu.edu/departments-institutes/microbiology/'},
 'identifier':{'@type':'PropertyValue','propertyID':'ORCID','value':'0000-0003-0324-3078','url':ORCID},
 'sameAs':[ORCID,'https://med.nyu.edu/faculty/benjamin-tenoever','https://scholar.google.com/citations?user=xKrzXtoAAAAJ','https://www.semanticscholar.org/author/5462120','https://openalex.org/A5060623081','https://www.wikidata.org/wiki/Q88822127','https://github.com/Ben-tenOever']}
LAB_NODE={'@type':'ResearchOrganization','@id':LAB,'name':'tenOever Laboratory','url':'https://tenoeverlab.com/','sameAs':[BASE+'/'],
 'parentOrganization':{'@type':'Organization','name':'Department of Microbiology, NYU Grossman School of Medicine','url':'https://med.nyu.edu/departments-institutes/microbiology/'},
 'founder':{'@id':PERSON},'member':{'@id':PERSON}}
E=lambda x:html.escape(str(x),quote=True)
def read(path): return (ROOT/path).read_text()
def load(path): return json.loads(read(path))
def write(path,text):
 p=OUT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
def dump(path,value):write(path,json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def body(path):return re.sub(r'\A---\n.*?\n---\n','',read(path),flags=re.S).strip()
def sections(text):return {m[0]:m[1].strip() for m in re.findall(r'^## ([^\n]+)\n(.*?)(?=^## |\Z)',text,re.M|re.S)}
pubs=load('data/publications.json');pubmap={p['id']:p for p in pubs}
tax=load('data/themes.json');areas={a['id']:a for a in tax['areas']};themes={t['id']:t for t in tax['themes']}
claims=load('data/claims.json');edges=load('data/connections.json');vocab=load('data/vocabulary.json')
labels={**{k:v['name'] for k,v in areas.items()},**{k:v['name'] for k,v in themes.items()}}
links={k:'/research/'+k+'/' for k in areas}|{k:'/themes/'+k+'/' for k in themes}|{k:v['url'] for k,v in pubmap.items()}
labels.update({k:v['title'] for k,v in pubmap.items()})
slug_pattern=re.compile(r'(?<![\w/-])('+ '|'.join(re.escape(x) for x in sorted(links,key=len,reverse=True))+r')(?![\w-])')
def rich(text):
 text=re.sub(r'^# .+\n','',text,count=1)
 soup=BeautifulSoup(markdown.markdown(text,extensions=['tables','toc','sane_lists']), 'html.parser')
 for node in list(soup.find_all(string=True)):
  if node.parent.name in ['a','code','script','style']:continue
  s=str(node);parts=[];pos=0
  for m in slug_pattern.finditer(s):
   parts.append(s[pos:m.start()]);a=soup.new_tag('a',href=links[m[0]]);a.string=labels[m[0]];parts.append(a);pos=m.end()
  if parts:
   parts.append(s[pos:]);node.replace_with(*parts)
 for a in soup.find_all('a',href='controlled-vocabulary.md'):a['href']='/methods/'
 return str(soup)
def link(url,label,cls=''):return f'<a href="{E(url)}"'+(f' class="{cls}"' if cls else '')+f'>{E(label)}</a>'
def chips(items):return '<div class="chips">'+''.join(link(links[x],labels[x]) for x in items)+'</div>'
def collection(items,kind):
 return '<div class="grid">'+''.join(f'<article class="card"><span class="eyebrow">{E(kind)}</span><h3>{link(i["url"],i["name"])}</h3><p>{E(i.get("description",""))}</p></article>' for i in items)+'</div>'
def publist(ids,heading=3,search=False):
 result=''
 for p in sorted([pubmap[i] for i in set(ids)],key=lambda p:(-p['year'],p['title'])):
  searchtext=' '.join(str(p.get(k,'')) for k in ['title','authors','journal','year','doi','pmid','themes','pathogens','technologies','keywords','one_sentence_contribution']).lower()
  result+=f'<article class="publication"'+(f' data-search="{E(searchtext)}" data-areas="{E(" ".join(p["research_areas"]))}" data-role="{E(p["contribution_character"])}" data-year="{p["year"]}"' if search else '')+f'><div class="meta">{p["year"]} · {E(p["journal"])} · <span class="badge">{E(p["contribution_character"])}</span></div><h{heading}>{link(p["url"],p["title"])}</h{heading}><p>{E(p["one_sentence_contribution"])}</p></article>'
 return result
pages=[]
nav=[('/','Home'),('/research/','Research'),('/discoveries/','Discoveries'),('/publications/','Publications'),('/trajectory/','Scientific trajectory'),('/about/','About')]
def page(path,title,description,content,kind='Research resource',schema=None,meta='',reading=False):
 url=BASE+path
 primary=''.join(f'<a href="{p}"'+(' aria-current="page"' if (path==p or p!='/' and path.startswith(p)) else '')+f'>{t}</a>' for p,t in nav)
 breadcrumb=[{'@type':'ListItem','position':1,'name':'Home','item':BASE+'/'}]
 if path!='/':breadcrumb.append({'@type':'ListItem','position':2,'name':title,'item':url})
 graph=[{'@type':'WebSite','@id':BASE+'/#website','url':BASE+'/','name':'tenOever Laboratory research resource','inLanguage':'en','publisher':{'@id':LAB},'about':[{'@id':LAB},{'@id':PERSON}]},
 PERSON_NODE,LAB_NODE,
 {'@type':'WebPage','@id':url+'#webpage','url':url,'name':title,'description':description,'isPartOf':{'@id':BASE+'/#website'},'inLanguage':'en','breadcrumb':{'@id':url+'#breadcrumb'}},
 {'@type':'BreadcrumbList','@id':url+'#breadcrumb','itemListElement':breadcrumb}]
 if schema:graph.append(schema)
 structured=json.dumps({'@context':'https://schema.org','@graph':graph},ensure_ascii=False).replace('<','\\u003c')
 toc=''
 if reading:
  soup=BeautifulSoup(content,'html.parser');heads=soup.find_all('h2',id=True)
  if heads:toc='<aside class="toc" aria-label="On this page"><strong>On this page</strong><ul>'+''.join('<li>'+link('#'+h['id'],h.get_text())+'</li>' for h in heads)+'</ul></aside>'
  content='<div class="layout"><div class="reading">'+content+'</div>'+toc+'</div>'
 heading='' if path=='/' else f'<div class="breadcrumbs">{link("/","Home")} / {E(kind)}</div><span class="eyebrow">{E(kind)}</span><h1>{E(title)}</h1>'
 document=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{E(title)} | tenOever Laboratory</title><meta name="description" content="{E(description)}"><link rel="canonical" href="{url}"><meta property="og:type" content="{'article' if schema and schema.get('@type')=='ScholarlyArticle' else 'website'}"><meta property="og:site_name" content="tenOever Laboratory"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(description)}"><meta property="og:url" content="{url}"><meta name="twitter:card" content="summary"><meta name="twitter:title" content="{E(title)}"><meta name="twitter:description" content="{E(description)}"><meta name="theme-color" content="#4f2c85"><link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/site.css"><script src="/assets/site.js" defer></script>{meta}<script type="application/ld+json">{structured}</script></head>
<body><a class="skip" href="#main">Skip to content</a><header><div class="masthead"><a class="brand" href="/">tenOever <span>Laboratory</span></a><span class="identity">Virology · Host defense · RNA biology</span></div></header><div class="navwrap"><nav class="primary" aria-label="Main navigation">{primary}</nav></div><main id="main">{heading}{content}</main><footer><div><strong>tenOever Laboratory</strong><p>A source-grounded account of a research program. The reviewed collection contains 63 publications from 2003–2025; it is not a complete or continuously updated bibliography. Attribution distinguishes lab-led, co-led, collaborative, and training-period work.</p><p>{link('/methods/','Sources & editorial method')}{link('/data/','Open data')}{link('/themes/','Themes')}{link('/technologies/','Technologies')}{link('/pathogens/','Pathogens')}{link('/llms.txt','Machine-reader guide')}</p><p>{link('https://benjamintenoever.com/','Benjamin tenOever · profile')}{link('https://tenoeverlab.com/','Laboratory team & news')}{link('https://orcid.org/0000-0003-0324-3078','ORCID')}{link('https://med.nyu.edu/faculty/benjamin-tenoever','NYU faculty page')}</p></div></footer></body></html>'''
 file=path.strip('/')+'/index.html' if path!='/' else 'index.html'
 write(file,document);pages.append(url)

# Every source is read in full; preserve a reproducible content inventory.
audit=[]
for p in sorted(ROOT.rglob('*')):
 if p.is_file() and (p.parent==ROOT and (p.name.endswith('_1.md') or p.name=='REVIEW_2.md') or p.is_relative_to(ROOT/'content') or p.is_relative_to(ROOT/'data')):
  raw=p.read_bytes();audit.append({'path':str(p.relative_to(ROOT)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
(ROOT/'reports/source-inventory.json').write_text(json.dumps(audit,indent=2)+'\n')
if OUT.exists(): shutil.rmtree(OUT)  # docs is exclusively generated output.
OUT.mkdir(exist_ok=True);shutil.copytree(ROOT/'assets',OUT/'assets',dirs_exist_ok=True)
write('assets/favicon.svg','<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#4f2c85"/><text x="32" y="44" font-family="Georgia,serif" font-size="38" fill="white" text-anchor="middle">tO</text></svg>')
(OUT/'data').mkdir(exist_ok=True)
# Copy independently of initial directory creation.
for p in (ROOT/'data').glob('*.json'):shutil.copy2(p,OUT/'data'/p.name)
claimsections=sections(body('content/synthesis/key-discoveries.md'))
discovery_slugs=['influenza-small-viral-rnas','influenza-splicing-timer','nucleoprotein-and-immune-sensing','interferon-transcriptional-selectivity','homeostatic-repression','costs-of-antiviral-defense','drosha-antiviral-restriction','reconstructing-antiviral-rnai','recombination-and-rna-editing','viruses-as-experimental-tools','influenza-transmission-bottlenecks','sars-cov-2-inflammatory-dependency','airway-interferon-and-systemic-protection','persistent-inflammation-and-olfactory-loss']
for c, discovery_slug in zip(claims,discovery_slugs,strict=True):
 assert c['statement'] in claimsections,c['id']
 c['url']='/discoveries/'+discovery_slug+'/'
 c['narrative_markdown']=claimsections[c['statement']]
 c['supporting_publications']=[{'id':x['slug'],'url':BASE+pubmap[x['slug']]['url'],'evidence':x['contributes']} for x in c['substantiated_by']]

def discoverycards(cs):return collection([{'url':c['url'],'name':c['statement'],'description':c['status']} for c in cs],'Discovery')
for p in pubs:
 narrative=body('content/publications/'+p['id']+'.md')
 p['sections']=sections(narrative)
 p['discoveries']=[c['id'] for c in claims if any(x['slug']==p['id'] for x in c['substantiated_by'])]
 p['relationships']=[x for x in edges if p['id'] in (x['from'],x['to'])]
 p['canonical_url']=BASE+p['url']
 p['controlled_vocabulary']={k:[v['id'] for v in vocab[k] if p['id'] in v['publications']] for k in ['pathogens','technologies']}
 metadata=f'<span class="badge">{E(p["contribution_character"])}</span><p class="lead">{E(p["one_sentence_contribution"])}</p><p class="byline">{E("; ".join(p["authors"]))}</p><p class="meta">{p["year"]} · {E(p["journal"])} · {E(p["publication_type"])}</p><div class="chips">'
 for key,label in [('doi_url','DOI'),('pmid_url','PubMed'),('pmc_url','Open-access full text'),('pmc_pdf_url','PDF · PubMed Central')]:
  if p.get(key):metadata+=link(p[key],label,'button' if key=='pmc_pdf_url' else '')
 metadata+='</div><dl><dt>Senior authors</dt><dd>'+E('; '.join(p['senior_authors']))+'</dd><dt>Correspondence</dt><dd>'+E('; '.join(p['corresponding_authors']))+'</dd></dl>'
 metadata+='<h2>Research areas & themes</h2>'+chips(p['research_areas']+p['themes'])
 text=metadata+rich(narrative)
 if p['discoveries']:text+='<h2 id="discoveries">Discoveries supported by this paper</h2>'+discoverycards([c for c in claims if c['id'] in p['discoveries']])
 text+='<h2 id="graph">Documented publication relationships</h2>'
 if p['relationships']:
  text+='<ul>'+''.join('<li>'+link(pubmap[e['to'] if e['from']==p['id'] else e['from']]['url'],pubmap[e['to'] if e['from']==p['id'] else e['from']]['title'])+f' — {E(e["relationship"])}. <span class="meta">Direction: {"this paper → linked paper" if e["from"]==p["id"] else "linked paper → this paper"}. {E(e["evidence"])}</span></li>' for e in p['relationships'])+'</ul>'
 else:text+='<p>No explicit publication relationship was recorded in the reviewed graph.</p>'
 for k in ['pathogens','technologies']:
  text+=f'<h2 id="{k}">{k.title()}</h2><div class="chips">'+''.join(link('/'+k+'/'+v['id']+'/',v['label']) for v in vocab[k] if p['id'] in v['publications'])+'</div>'
 schema={'@type':'ScholarlyArticle','@id':BASE+p['url']+'#article','url':BASE+p['url'],'headline':p['title'],'name':p['title'],'datePublished':str(p['year']),'author':[{'@id':PERSON} if 'tenoever' in a.lower() else {'@type':'Person','name':a} for a in p['authors']], 'isPartOf':{'@type':'Periodical','name':p['journal']},'abstract':p['summary_150'],'identifier':[{'@type':'PropertyValue','propertyID':key.upper(),'value':p[key]} for key in ['doi','pmid','pmcid'] if p.get(key)],'sameAs':[p[key] for key in ['doi_url','pmid_url','pmc_url'] if p.get(key)],'about':[{'@id':BASE+links[a]+'#project'} for a in p['research_areas']],'keywords':list(dict.fromkeys((p.get('keywords') or [])+[labels[x] for x in p['research_areas']+p['themes']])),'mainEntityOfPage':{'@id':BASE+p['url']+'#webpage'},'inLanguage':'en'}
 if p.get('volume') or p.get('issue') or p.get('pages'):
  schema['pagination']=p.get('pages') or None
  schema['isPartOf']={'@type':'PublicationIssue','issueNumber':p.get('issue') or None,'isPartOf':{'@type':'PublicationVolume','volumeNumber':p.get('volume') or None,'isPartOf':{'@type':'Periodical','name':p['journal']}}}
 if p.get('pmc_pdf_url'):schema['associatedMedia']={'@type':'MediaObject','contentUrl':p['pmc_pdf_url'],'encodingFormat':'application/pdf','provider':{'@type':'Organization','name':'PubMed Central'}}
 schema={k:v for k,v in schema.items() if v not in (None,[],'')}
 if isinstance(schema.get('isPartOf'),dict):
  def prune(d):return {k:(prune(v) if isinstance(v,dict) else v) for k,v in d.items() if v not in (None,'')}
  schema['isPartOf']=prune(schema['isPartOf'])
 scholarmeta={'citation_title':[p['title']],'citation_author':p['authors'],'citation_publication_date':[str(p['year'])],'citation_journal_title':[p['journal']],'citation_doi':[p['doi']],'citation_pmid':[p['pmid']],'citation_volume':[p['volume']],'citation_issue':[p['issue']]}
 meta=''.join(f'<meta name="{k}" content="{E(v)}">' for k,vs in scholarmeta.items() for v in vs if v)
 page(p['url'],p['title'],p['summary_25'],text,'Publication',schema,meta,True)

for c in claims:
 page(c['url'],c['statement'],'Evidence, attribution, and limitations for a discovery in the tenOever research corpus.',rich(c['narrative_markdown'])+'<h2>Research areas</h2>'+chips(c['research_areas'])+'<h2>Supporting publications</h2>'+publist([x['slug'] for x in c['substantiated_by']]),'Discovery',reading=True)
page('/discoveries/','Discoveries','Fourteen source-grounded discoveries with supporting publications, attribution, and scientific limitations.',rich(claimsections['How to read this document'])+discoverycards(claims),'Discoveries')

for a in areas.values():
 cs=[c for c in claims if a['id'] in c['research_areas']]
 text=f'<p class="lead">{E(a["question"])}</p>'+rich(body('content/areas/'+a['id']+'.md'))+'<h2 id="themes">Explore the themes</h2>'+chips(a['themes'])+'<h2 id="discoveries">Connected discoveries</h2>'+discoverycards(cs)+'<h2 id="publications">Publications in this area</h2>'+publist(a['publications'])
 page('/research/'+a['id']+'/',a['name'],a['question'],text,'Research area',{'@type':'ResearchProject','@id':BASE+'/research/'+a['id']+'/#project','name':a['name'],'description':a['question'],'url':BASE+'/research/'+a['id']+'/'},reading=True)
for t in themes.values():
 page('/themes/'+t['id']+'/',t['name'],t['question'],f'<p class="lead">{E(t["question"])}</p>'+chips([t['area']])+rich(body('content/themes/'+t['id']+'.md'))+'<h2 id="publications">Publications in this theme</h2>'+publist(t['publications']),'Research theme',reading=True)
areacards=collection([{'url':'/research/'+a['id']+'/','name':a['name'],'description':a['question']} for a in areas.values()],'Research area')
page('/research/program/','The research program','A detailed source-grounded overview of the tenOever research program and its unresolved scientific questions.',rich(sections(body('content/synthesis/program-overview.md'))['2000 words']),'Program overview',reading=True)
page('/research/','Six questions, one connected program','Explore six research areas spanning antiviral immunity, RNA biology, programmable virology, influenza, pandemic response, and viral evolution.',f'<p class="lead">The research is organized around scientific questions. Each area connects its intellectual history to themes, discoveries, and the publications that support them.</p><p>'+link('/research/program/','Read the full program overview →')+'</p>'+areacards,'Research')
page('/themes/','Research themes','Thirty-four scientific themes connecting publications across six areas of virology and host defense.',collection([{'url':'/themes/'+t['id']+'/','name':t['name'],'description':t['question']} for t in themes.values()],'Theme'),'Themes')
for k in ['pathogens','technologies']:
 overview_file='pathogens-and-systems' if k=='pathogens' else 'technologies-and-platforms'
 page('/'+k+'/overview/',k.title()+' across the research program','Cross-cutting synthesis of '+k+' in the reviewed publication corpus.',rich(body('content/synthesis/'+overview_file+'.md')),k.title(),reading=True)
 page('/'+k+'/',k.title(),'Browse the publication corpus by '+k+'.','<p class="lead">Controlled terms connect methods and biological systems across the research program.</p><p>'+link('/'+k+'/overview/','Read the cross-cutting overview →')+'</p><ul class="resource-list">'+''.join('<li>'+link('/'+k+'/'+v['id']+'/',v['label'])+f' <span class="meta">({len(v["publications"])})</span></li>' for v in vocab[k])+'</ul>',k.title())
 for v in vocab[k]:
  page('/'+k+'/'+v['id']+'/',v['label'],'Research publications associated with '+v['label']+'.',f'<p class="lead">{E(v.get("family", ""))}</p><p>Recorded terms: {E("; ".join(v.get("aliases",[])))}</p>'+publist(v['publications'],2),k.title())

overview=sections(body('content/synthesis/program-overview.md'))
home=f'<section class="hero"><div class="hero-grid"><div><span class="eyebrow">Benjamin tenOever & the tenOever laboratory</span><h1>Viruses, host defense, and the biology between them.</h1><p class="lead">{E(overview["50 words"])}</p>{link("/research/","Explore the research →","button")}</div><aside class="hero-aside"><span class="eyebrow">Pathways into the work</span>'+''.join(link('/research/'+a+'/',label+' →') for a,label in [('programmable-virology','Programmable virology'),('influenza-genome-regulation','Influenza'),('innate-immune-signaling','Antiviral immunity / interferon'),('small-rna-antiviral-defense','Small RNA / RNAi'),('pandemic-host-response','SARS-CoV-2 / pandemic response'),('viral-populations-evolution','Viral evolution & transmission')])+'</aside></div></section>'
home+='<div class="stats"><div><strong>63</strong><span>Reviewed publications</span></div><div><strong>6</strong><span>Research areas</span></div><div><strong>14</strong><span>Discoveries with evidence</span></div><div><strong>2003–2025</strong><span>Corpus coverage</span></div></div><h2>A program built around questions</h2>'+areacards
home+='<h2>Selected discoveries</h2>'+discoverycards([claims[i] for i in [9,7,11]])+'<p>'+link('/discoveries/','Read all fourteen discoveries →')+'</p><section class="note"><h2>How to read the evidence</h2><p>Individual studies, cross-paper synthesis, and unresolved questions are kept distinct. Each publication identifies the laboratory’s role; collaborative discoveries retain credit to the groups that led them.</p>'+link('/methods/','Sources, attribution & scope →')+'</section><h2>Find your starting point</h2>'+collection([{'url':'/publications/','name':'For scientists & collaborators','description':'Search the corpus and follow the evidence into individual publication records.'},{'url':'/trajectory/','name':'For trainees','description':'Follow how questions, methods, and interpretations developed over two decades.'},{'url':'/discoveries/','name':'For journalists & readers','description':'Start with the discoveries, their experimental support, and the limits of each claim.'}],'Reading guide')
page('/','Virology, antiviral immunity & programmable biology',overview['50 words'],home)
filters='<form id="publication-filters" class="filters"><label>Search publications<input name="q" type="search" placeholder="Title, author, DOI, method…"></label><label>Research area<select name="area"><option value="">All areas</option>'+''.join(f'<option value="{a["id"]}">{E(a["name"])}</option>' for a in areas.values())+'</select></label><label>Attribution<select name="role"><option value="">All contributions</option>'+''.join(f'<option>{r}</option>' for r in ['lab-led','co-led','collaborative','training period'])+'</select></label><label>Year<select name="year"><option value="">All years</option>'+''.join(f'<option>{y}</option>' for y in sorted({p['year'] for p in pubs},reverse=True))+'</select></label><button type="reset">Reset</button></form><p id="result-count" role="status" aria-live="polite">63 publications</p><noscript><p>All publications are shown below. Enable JavaScript to use search and filters.</p></noscript><p id="empty-results" class="empty" hidden>No publications match these filters. Try fewer terms or reset the filters.</p>'
page('/publications/','Publications','Search 63 reviewed publications by title, author, DOI, research area, year, pathogen, technology, and attribution.','<p class="lead">A curated scholarly corpus, with full citations, scientific summaries, limitations, and connections between studies.</p><p>Coverage: 2003–2025. This collection is not the complete laboratory bibliography.</p>'+filters+publist(pubmap,2,True),'Publication corpus')
page('/trajectory/','How the research program developed','An intellectual history of interferon signaling, RNA biology, synthetic virology, and pandemic host response.',rich(body('content/synthesis/trajectory-public.md'))+'<p>'+link('/trajectory/detailed/','Read the detailed intellectual history →')+'</p>','Scientific trajectory',reading=True)
page('/trajectory/detailed/','The intellectual history of the program','A detailed account of scientific foundations, mechanistic advances, revisions, and unresolved questions.',rich(body('content/synthesis/trajectory-detailed.md')),'Scientific trajectory',reading=True)
profile='''<p class="lead">Benjamin tenOever studies virus–host interactions, antiviral defense, and the use of engineered viruses as tools for biological inquiry.</p><h2 id="profile">Academic profile</h2><p>Benjamin tenOever, PhD, is Chair of the Department of Microbiology, Director of the NYU Langone Virology Institute, Jan T. Vilcek Professor of Molecular Pathogenesis, and Professor in the Department of Medicine at NYU Grossman School of Medicine. His graduate training was at McGill University and his postdoctoral training was at Harvard University.</p><p>Positions and education are sourced to the <a href="https://med.nyu.edu/faculty/benjamin-tenoever">NYU faculty profile</a>, checked September 26, 2026. The institutional profile also provides current contact information.</p><h2 id="program">The scientific program</h2>'''+rich(overview['100 words'])+'''<h2 id="attribution">Foundations and attribution</h2><p>The reviewed corpus includes two training-period studies: Sharma 2003 in the Hiscott laboratory and tenOever 2007 in the Maniatis laboratory. These are part of the intellectual history and are identified separately from the independent laboratory’s work.</p><p>The remaining records distinguish lab-led, co-led, and collaborative studies. The site describes contributions using the reviewed source records rather than inferring leadership from authorship order.</p><h2 id="identity">Canonical profile and scholarly identifiers</h2><p>This page describes the research program. The canonical biography of Benjamin tenOever is at <a href="https://benjamintenoever.com/">benjamintenoever.com</a>, and the laboratory’s team, news and contact pages are at <a href="https://tenoeverlab.com/">tenoeverlab.com</a>.</p><ul><li>ORCID: <a href="https://orcid.org/0000-0003-0324-3078">0000-0003-0324-3078</a></li><li><a href="https://med.nyu.edu/faculty/benjamin-tenoever">NYU Grossman School of Medicine faculty profile</a></li><li><a href="https://scholar.google.com/citations?user=xKrzXtoAAAAJ">Google Scholar</a> · <a href="https://www.semanticscholar.org/author/5462120">Semantic Scholar</a> · <a href="https://openalex.org/A5060623081">OpenAlex</a> · <a href="https://pubmed.ncbi.nlm.nih.gov/?term=tenOever+B%5BAuthor%5D">PubMed author search</a></li><li><a href="https://www.wikidata.org/wiki/Q88822127">Wikidata Q88822127</a> · <a href="https://github.com/Ben-tenOever">GitHub</a></li></ul><h2 id="trainees">For prospective trainees and collaborators</h2><p>Start with the <a href="/trajectory/">scientific trajectory</a> and <a href="/research/">research questions</a> to understand the program’s methods and intellectual development. For current opportunities and inquiries, use the contact details on the <a href="https://med.nyu.edu/faculty/benjamin-tenoever">institutional profile</a>.</p>'''
page('/about/','Benjamin tenOever','A factual scholarly profile of Benjamin tenOever and the research program in virology, innate immunity, and RNA biology.',profile,'About',{'@type':'AboutPage','@id':BASE+'/about/#aboutpage','url':BASE+'/about/','about':[{'@id':PERSON},{'@id':LAB}]},reading=True)
method='''<p class="lead">This site exposes the reviewed knowledge base as a connected scholarly resource.</p><h2 id="scope">Corpus and scope</h2><p>The collection contains 63 publication records, six research areas, 34 themes, 14 discoveries, and 129 explicit publication relationships. It spans 2003–2025 and is a selected corpus, not a complete bibliography or a statement about all current laboratory activity.</p><p>The supplied review reports full-text assessment and identifier verification against Crossref and NCBI. This website preserves those records and their source mappings. No original publication PDFs were included in the supplied archive. Open-access links point to PubMed Central where recorded; publisher access and PDF delivery are controlled by the source.</p><h2 id="attribution">Attribution and evidence</h2><p>The corpus classifies 37 papers as lab-led, 10 as co-led, 14 as collaborative, and two as training-period work. These classifications follow contribution statements in the reviewed records. Discovery pages distinguish demonstrated findings, interpretation, cross-paper synthesis, and limitations.</p><p>Publication relationships are included only when documented in the reviewed records. Sharing a pathogen or a method creates a browsing connection, not a claim of scientific derivation. Directed edges retain their original direction and evidence.</p><h2 id="history">Historical boundaries</h2><p>Statements that a line of work stopped or was not revisited refer only to the supplied corpus. They do not establish the present status of unpublished or later research. The RNAi and Drosha accounts retain both negative and positive findings and the laboratory’s revisions.</p><h2 id="reuse">Sources and machine-readable access</h2><p>Each publication page includes its citation and authoritative identifiers. The <a href="/data/">data catalog</a> exposes original records, source mappings, controlled vocabulary, and derived relationships. Scientific articles retain their original rights; this site does not redistribute publisher PDFs or grant rights to their contents.</p><h2 id="vocabulary">Controlled vocabulary</h2>'''+rich(body('content/synthesis/controlled-vocabulary.md'))
page('/methods/','Sources, attribution & editorial method','How this resource preserves evidence, attribution, source relationships, and the boundaries of its curated publication corpus.',method,'Editorial method',reading=True)
for a in areas.values():a['url']=BASE+'/research/'+a['id']+'/';a['discoveries']=[c['id'] for c in claims if a['id'] in c['research_areas']]
dump('data/publications.json',pubs);dump('data/discoveries.json',claims);dump('data/research-areas.json',list(areas.values()))
dump('data/provenance.json',{'canonical_origin':BASE,'corpus_years':[2003,2025],'publication_count':len(pubs),'source_inventory':audit,'profile_source':{'url':'https://med.nyu.edu/faculty/benjamin-tenoever','checked':'2026-09-26'},'relationships':'Directed edges as supplied, not inferred from subject similarity.'})
files=[('publications','Publication metadata, full narrative sections, attribution, identifiers, and relationships'),('discoveries','Discovery statements, full narratives, and evidence-to-publication mappings'),('research-areas','Six research areas with themes, publications, and discoveries'),('themes','Research area and theme membership'),('connections','129 documented directed publication relationships'),('claims','Original claim-to-source mappings'),('vocabulary','Controlled terms and publication memberships'),('timeline','Chronology and scientific transitions'),('publication_inventory','Source inventory, including an inventory-only entry; the 63 reviewed records define site coverage'),('search_index','Original search index'),('provenance','Source checksums and scope')]
page('/data/','Open scholarly data','Download publication records, discovery evidence, research areas, controlled vocabulary, and the documented relationship graph.','<p class="lead">Structured companions to the human-readable pages. Identifiers and relationships retain their provenance in the reviewed corpus.</p><ul>'+''.join('<li>'+link('/data/'+f+'.json',f+'.json')+' — '+d+'</li>' for f,d in files)+'</ul><h2>Conventions</h2><p>Publication IDs are stable slugs. Discovery IDs follow the original claim IDs. Publication canonical_url fields are absolute; original url fields are site-relative. Research-area URLs are absolute. Graph from/to fields reference publication IDs; substantiated_by references supporting papers. Missing identifiers are null, not inferred.</p>','Data catalog')
page('/404/','Page not found','Find research, publications, and discoveries in the tenOever Laboratory scholarly resource.','<p class="lead">This address does not match a page in the resource.</p><p>'+link('/publications/','Search publications')+' or '+link('/research/','browse research areas')+'.</p>','Navigation')
shutil.copy2(OUT/'404/index.html',OUT/'404.html')
write('CNAME','tenoeverlab.us');write('.nojekyll','')
write('robots.txt','User-agent: *\nAllow: /\n\nSitemap: '+BASE+'/sitemap.xml\n')
write('sitemap.xml','<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join('<url><loc>'+E(u)+'</loc></url>\n' for u in sorted(pages) if '/404/' not in u)+'</urlset>\n')
write('llms.txt','# tenOever Laboratory\n\n> A source-grounded scholarly resource on Benjamin tenOever and the tenOever laboratory: virology, antiviral immunity, RNA biology, programmable virology, influenza, viral evolution, and pandemic host response.\n\nThe curated corpus covers 63 publications from 2003–2025, not a complete or current bibliography. Preserve lab-led, co-led, collaborative, and training-period attribution. Distinguish demonstrated findings, interpretation, synthesis, and limitations. Historical statements about stopped work are bounded by this corpus. Cite original publications through their DOIs when using scientific findings.\n\n## Identity\n- Canonical person page: https://benjamintenoever.com/\n- ORCID: https://orcid.org/0000-0003-0324-3078\n- Institutional profile: https://med.nyu.edu/faculty/benjamin-tenoever\n- Laboratory main site (team, news, contact): https://tenoeverlab.com/\n\n## Human-readable resources\n'+''.join('- ['+t+']('+BASE+p+')\n' for p,t in nav)+'- [Editorial method]('+BASE+'/methods/)\n\n## Structured resources\n'+''.join('- ['+f+']('+BASE+'/data/'+f+'.json): '+d+'\n' for f,d in files))
print(f'Built {len(pages)} pages, {len(pubs)} publications, {len(claims)} discoveries into {OUT}')
