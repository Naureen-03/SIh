import json

tsconfig_content = """{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",

    /* Linting */
    "strict": false,
    "noUnusedLocals": false,
    "noUnusedParameters": false,
    "noFallthroughCasesInSwitch": false,
    "verbatimModuleSyntax": false
  },
  "include": ["src"]
}
"""

with open('tsconfig.app.json', 'w', encoding='utf-8') as f:
    f.write(tsconfig_content)

with open('tsconfig.json', 'w', encoding='utf-8') as f:
    f.write(tsconfig_content)

print("tsconfigs updated successfully!")
