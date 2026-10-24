"""Refresh print diagrams with Mermaid CLI 12.0.0; review the resulting SVGs."""
import hashlib,json,os,re,subprocess,tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
BOOK=ROOT/'tools/book'

def render():
    destination=BOOK/'diagrams';destination.mkdir(exist_ok=True)
    catalog=json.loads((ROOT/'docs/course/catalog.json').read_text())
    manifest={}
    with tempfile.TemporaryDirectory(prefix='book-diagrams-') as directory:
        temp=Path(directory)
        config={'htmlLabels':False,'look':'classic','theme':'base','fontFamily':'Noto Sans CJK SC, PingFang SC, Microsoft YaHei, sans-serif','themeVariables':{'fontSize':'18px','primaryColor':'#edf4ef','primaryTextColor':'#253c32','primaryBorderColor':'#719984','lineColor':'#557766','secondaryColor':'#f5f6f8','tertiaryColor':'#f8f3e8'},'flowchart':{'htmlLabels':False,'curve':'linear','nodeSpacing':22,'rankSpacing':30,'padding':12},'securityLevel':'strict'}
        (temp/'config.json').write_text(json.dumps(config))
        puppet={'args':['--no-sandbox']}
        if os.environ.get('CHROME_PATH'):puppet['executablePath']=os.environ['CHROME_PATH']
        (temp/'puppeteer.json').write_text(json.dumps(puppet))
        cli=os.environ.get('MMDC','mmdc')
        for row in catalog['chapters']:
            raw=(ROOT/row['path']).read_text();counter=0
            for match in re.finditer(r'^```mermaid\s*\n(.*?)^```\s*$',raw,re.M|re.S):
                counter+=1;key=f'{row["id"]}-{counter}';code=match[1].rstrip()
                # A vertical reading direction suits the narrow printed page; edges and labels are unchanged.
                paper=re.sub(r'^(flowchart|graph) LR',r'\1 TB',code)
                paper=paper.replace('\\n','<br/>')
                source=temp/(key+'.mmd');source.write_text(paper)
                headings=re.findall(r'^#{2,3} (.+)',raw[:match.start()],re.M)
                caption=re.sub(r'^[一二三四五六七八九十]+、','',headings[-1]) if headings else row['title']
                out=destination/(key+'.svg')
                subprocess.run([cli,'-i',str(source),'-o',str(out),'-c',str(temp/'config.json'),'-p',str(temp/'puppeteer.json'),'-b','transparent','-q'],check=True)
                manifest[key]={'file':out.name,'caption':caption,'source_sha256':hashlib.sha256(code.encode()).hexdigest()}
                print(key,flush=True)
        (destination/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')

if __name__=='__main__':render()
