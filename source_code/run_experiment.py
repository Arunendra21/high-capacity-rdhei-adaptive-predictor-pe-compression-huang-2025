import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "_toolkit"))
import build_rdhei_paper as B, rdhei_papers_content as RC, rdhei_msb as MSB, rdhei_variants as V
c=RC.CONTENT[24]; engine=V.ChaosEngine if c.get("engine")=="Chaos" else MSB
B._run(os.path.join(os.path.dirname(__file__),"..","figures"),
       os.path.join(os.path.dirname(__file__),"..","outputs"), engine, "lena")
print("experiment done paper 24")
