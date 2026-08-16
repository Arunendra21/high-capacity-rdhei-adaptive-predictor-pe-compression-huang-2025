import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "_toolkit"))
import run_rdhei_paper as R
R.run(24, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
print("built paper 24")
