from playwright.sync_api import sync_playwright, expect
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1];base='http://127.0.0.1:8765'
paths=['/','/publications/','/research/programmable-virology/','/research/small-rna-antiviral-defense/','/discoveries/drosha-antiviral-restriction/','/publications/2015-benitez-engineered-mammalian-rnai-can-elic/','/publications/2020-blanco-melo-imbalanced-host-response-to-sars-c/','/about/']
results=[];errors=[]
with sync_playwright() as pw:
 browser=pw.chromium.launch(executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless=True)
 for width in [1440,390,320]:
  page=browser.new_page(viewport={'width':width,'height':960},device_scale_factor=1)
  page.on('pageerror',lambda e:errors.append(str(e)))
  for path in paths:
   r=page.goto(base+path);assert r.status==200
   assert page.locator('h1').count()==1
   overflow=page.evaluate('document.documentElement.scrollWidth > innerWidth')
   if overflow:
    print(page.evaluate("[...document.querySelectorAll('body *')].filter(e=>e.getBoundingClientRect().right>innerWidth).map(e=>[e.tagName,e.className,e.getBoundingClientRect().width,e.textContent.slice(0,50)]).slice(0,25)"))
   assert not overflow,(width,path,'horizontal overflow')
   results.append({'width':width,'path':path,'status':r.status,'horizontal_overflow':overflow})
   if path=='/' and width in [1440,390]:page.screenshot(path=str(root/f'reports/home-{width}.png'),full_page=True)
  page.goto(base+'/publications/')
  page.locator('[name=q]').fill('Drosha');assert page.locator('.publication:visible').count()>0
  page.locator('[name=role]').select_option('lab-led');assert page.locator('.publication:visible').count()>0
  page.reload();assert page.locator('[name=q]').input_value()=='Drosha'
  page.locator('[name=q]').fill('unmatchablezzz');assert page.locator('.publication:visible').count()==0
  assert page.locator('#empty-results').is_visible()
  page.get_by_role('button',name='Reset',exact=True).click();expect(page.locator('.publication:visible')).to_have_count(63)
  page.close()
 context=browser.new_context(java_script_enabled=False);page=context.new_page();page.goto(base+'/publications/');assert page.locator('.publication').count()==63
 page.goto(base+paths[5]);assert 'Limitations and boundaries' in page.inner_text('main')
 browser.close()
assert not errors,errors
(root/'reports/browser-validation.json').write_text(json.dumps({'pages':results,'search_filters_reset_url_state':'passed','javascript_disabled_content':'passed','console_errors':errors},indent=2)+'\n')
print('Passed: 24 viewport/page checks; search, attribution filter, URL state, empty result, reset, and JavaScript-disabled content.')
