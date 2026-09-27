"""Read the existing authoritative PDF links; do not invent or download replacements."""
import json,urllib.request,concurrent.futures,collections
from pathlib import Path
root=Path(__file__).resolve().parents[1]
urls=sorted({p['pmc_pdf_url'] for p in json.loads((root/'data/publications.json').read_text()) if p.get('pmc_pdf_url')})
def check(url):
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (scholarly website link validation)'})
  with urllib.request.urlopen(req,timeout=30) as r:
   first=r.read(4096);return {'url':url,'status':r.status,'resolved_url':r.url,'content_type':r.headers.get('Content-Type'),'pdf_confirmed':first.startswith(b'%PDF'),'challenge':b'captcha' in first.lower() or b'checking your browser' in first.lower() or b'recaptcha' in first.lower() or b'pow_challenge' in first.lower()}
 except Exception as e:return {'url':url,'error':str(e),'pdf_confirmed':False}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:results=list(pool.map(check,urls))
(root/'reports/pdf-validation.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps({'checked':len(results),'confirmed_pdfs':sum(x['pdf_confirmed'] for x in results),'statuses':dict(collections.Counter(str(x.get('status',x.get('error'))) for x in results))},indent=2))
