import json, glob, os, collections, gzip
base="/root/.claude/projects/-home-user-RF-Stuff/"
files=[("main",base+"e2c1133f-7df8-5a27-93b4-4d781de9e32f.jsonl")]+[(os.path.basename(f)[:-6],f) for f in sorted(glob.glob(base+"e2c1133f-7df8-5a27-93b4-4d781de9e32f/subagents/*.jsonl"))]
out=[]; 
def text_of(c):
    if isinstance(c,str): return c
    if isinstance(c,list):
        parts=[]
        for x in c:
            if isinstance(x,dict):
                if x.get("type")=="text": parts.append(x.get("text",""))
                elif x.get("type")=="image": parts.append("[image]")
                else: parts.append(json.dumps(x)[:2000])
            else: parts.append(str(x))
        return "\n".join(parts)
    return json.dumps(c)
agent_desc={}
for label,f in files:
    uses={}; first_prompt=None
    with open(f) as fh:
        for line in fh:
            try: ev=json.loads(line)
            except: continue
            msg=ev.get("message") or {}
            content=msg.get("content")
            ts=ev.get("timestamp")
            if ev.get("type")=="user" and first_prompt is None and isinstance(content,(str,list)):
                t=text_of(content)
                if t and not t.startswith("[{"): first_prompt=t[:400]
            if isinstance(content,list):
                for b in content:
                    if not isinstance(b,dict): continue
                    if b.get("type")=="tool_use" and str(b.get("name","")).startswith("mcp__"):
                        uses[b["id"]]={"agent":label,"ts":ts,"tool":b["name"],"input":b.get("input")}
                    if b.get("type")=="tool_result" and b.get("tool_use_id") in uses:
                        r=text_of(b.get("content"))
                        u=uses[b["tool_use_id"]]; u["result"]=r; u["result_chars"]=len(r); u["is_error"]=bool(b.get("is_error"))
    agent_desc[label]=first_prompt
    out.extend(uses.values())
out.sort(key=lambda u:(u["ts"] or ""))
for i,u in enumerate(out,1): u["seq"]=i
P="/tmp/claude-0/-home-user-RF-Stuff/e2c1133f-7df8-5a27-93b4-4d781de9e32f/scratchpad/cpng/prov/"
with gzip.open(P+"mcp_calls_full.jsonl.gz","wt") as g:
    for u in out: g.write(json.dumps(u)+"\n")
c=collections.Counter((u["agent"],u["tool"].split("__")[1],u["tool"].split("__")[2]) for u in out)
for k,v in sorted(c.items()): print(k,v)
print("total",len(out),"errors",sum(1 for u in out if u.get("is_error")),"result chars",sum(u.get("result_chars",0) for u in out))
print("first ts",out[0]["ts"],"last ts",out[-1]["ts"])
json.dump(agent_desc,open(P+"agent_prompts.json","w"),indent=1)
for k,v in agent_desc.items(): print(k, (v or "")[:160].replace("\n"," "))
