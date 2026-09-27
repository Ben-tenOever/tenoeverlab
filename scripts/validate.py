"""Validate the generated corpus, all internal links, fragments, metadata and JSON."""
from pathlib import Path
from urllib.parse import urlsplit,unquote
import json,xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1];SITE=ROOT/'docs';BASE='https://tenoeverlab.us'
errors=[];count=0;anchors={};documents={}
for f in SITE.rglob('*.html'):
 s=BeautifulSoup(f.read_text(),'html.parser');documents[f]=s;anchors[f]={n['id'] for n in s.find_all(id=True)}
for f,s in documents.items():
 count+=1
 def check(ok,msg):
  if not ok:errors.append(f'{f.relative_to(SITE)}: {msg}')
 check(len(s.find_all('h1'))==1,'exactly one h1 required')
 check(s.html.get('lang')=='en','language missing')
 check(bool(s.title and s.title.text),'title missing')
 check(bool(s.find('meta',attrs={'name':'description'})),'description missing')
 canonical=s.find('link',rel='canonical')['href'];check(canonical.startswith(BASE+'/'),'canonical origin incorrect')
 check('localhost' not in str(s) and '127.0.0.1' not in str(s),'local address leaked')
 for script in s.find_all('script',type='application/ld+json'):
  d=json.loads(script.string);check(d['@context']=='https://schema.org','schema context incorrect')
  people=[x for x in d['@graph'] if x['@type']=='Person'];check(all(p['@id']=='https://benjamintenoever.com/#person' for p in people),'inconsistent person entity')
  for n in d['@graph']:
   if n.get('@type')=='ScholarlyArticle':check(any(a.get('@id')=='https://benjamintenoever.com/#person' for a in n['author']),'article not linked to canonical person')
 for a in s.select('[href],[src]'):
  url=a.get('href',a.get('src'));u=urlsplit(url)
  if u.scheme or u.netloc:continue
  target=SITE/unquote(u.path.lstrip('/')) if u.path.startswith('/') else f.parent/unquote(u.path)
  if not u.path:target=f
  elif target.is_dir():target=target/'index.html'
  check(target.exists(),f'broken internal link: {url}')
  if u.fragment and target.suffix=='.html' and target in anchors:check(unquote(u.fragment) in anchors[target],f'broken fragment: {url}')
for f in (SITE/'data').glob('*.json'):json.loads(f.read_text())
ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
urls=[n.text for n in ET.parse(SITE/'sitemap.xml').findall('.//s:loc',ns)]
assert len(urls)==len(set(urls))
for url in urls:
 assert url.startswith(BASE+'/');assert (SITE/url.removeprefix(BASE).strip('/')/'index.html').exists()
expected={s.find('link',rel='canonical')['href'] for f,s in documents.items() if '404' not in str(f.relative_to(SITE))}
assert set(urls)==expected
assert 'Sitemap: '+BASE+'/sitemap.xml' in (SITE/'robots.txt').read_text()
assert (SITE/'CNAME').read_text().strip()=='tenoeverlab.us'
pubs=json.loads((SITE/'data/publications.json').read_text());assert len(pubs)==63
assert all({'Citation','Executive summary','Key findings','Limitations and boundaries'}.issubset(p['sections']) for p in pubs)
assert len(json.loads((SITE/'data/discoveries.json').read_text()))==14
assert len(json.loads((SITE/'data/research-areas.json').read_text()))==6
report={'html_files':count,'sitemap_urls':len(urls),'publication_records':len(pubs),'errors':errors}
(ROOT/'reports/static-validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2));raise SystemExit(bool(errors))
