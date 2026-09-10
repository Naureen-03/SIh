import glob

for fpath in glob.glob("src/pages/Compliance/*.tsx"):
    with open(fpath, "r", encoding="utf-8") as f:
        c = f.read()
    if "STATUTORY_COMPLIANCE_RULES" in c:
        c = c.replace("STATUTORY_COMPLIANCE_RULES", "INITIAL_STATUTORY_RULES")
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(c)
        print("Updated:", fpath)

# Also check mockData.ts export
with open("src/data/mockData.ts", "r", encoding="utf-8") as f:
    mc = f.read()

if "export const STATUTORY_COMPLIANCE_RULES" not in mc:
    mc += "\nexport const STATUTORY_COMPLIANCE_RULES = INITIAL_STATUTORY_RULES;\n"
    with open("src/data/mockData.ts", "w", encoding="utf-8") as f:
        f.write(mc)
    print("Export alias added to mockData.ts")

