import os
import shutil

wasm_dir = 'node_modules/@rollup/wasm-node/dist'
rollup_dir = 'node_modules/rollup/dist'

if os.path.exists(wasm_dir) and os.path.exists(rollup_dir):
    for item in os.listdir(wasm_dir):
        s = os.path.join(wasm_dir, item)
        d = os.path.join(rollup_dir, item)
        if os.path.isfile(s):
            shutil.copy2(s, d)
    print("WASM rollup files copied into rollup/dist!")
else:
    print("Paths not found:", wasm_dir, rollup_dir)
