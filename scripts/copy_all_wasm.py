import os
import shutil

wasm_dir = 'node_modules/@rollup/wasm-node/dist'
rollup_dir = 'node_modules/rollup/dist'

if os.path.exists(wasm_dir) and os.path.exists(rollup_dir):
    shutil.copytree(wasm_dir, rollup_dir, dirs_exist_ok=True)
    print("Entire WASM rollup distribution copied into rollup/dist!")
