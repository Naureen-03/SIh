const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');

// 1. tailwind.config.js
fs.writeFileSync(path.join(root, 'tailwind.config.js'), `/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        coal: {
          950: '#07090E',
          900: '#0E131F',
          850: '#141B2D',
          800: '#1B243B',
          750: '#232E4A',
          700: '#2D3B5E',
          600: '#41537F',
          500: '#5C72A8',
          400: '#859BC9',
          300: '#B2C2E4',
          200: '#D6E0F5',
          100: '#EEF3FD',
          50: '#F8FAFD',
        },
        safety: {
          orange: '#FF6B00',
          amber: '#F59E0B',
          yellow: '#EAB308',
          red: '#EF4444',
          green: '#10B981',
          cyan: '#06B6D4',
          blue: '#3B82F6',
          purple: '#8B5CF6',
        },
        govt: {
          navy: '#0B2545',
          gold: '#C59B27',
          ash: '#4A5568',
        }
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
        mono: ['JetBrains Mono', 'Fira Code', 'Courier New', 'monospace'],
      },
      animation: {
        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'scan': 'scan 2.5s linear infinite',
        'fade-in': 'fadeIn 0.25s ease-out forwards',
        'slide-up': 'slideUp 0.3s ease-out forwards',
      },
      keyframes: {
        scan: {
          '0%': { top: '0%' },
          '50%': { top: '92%' },
          '100%': { top: '0%' },
        },
        fadeIn: {
          '0%': { opacity: '0', transform: 'translateY(4px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        slideUp: {
          '0%': { opacity: '0', transform: 'translateY(16px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
      },
    },
  },
  plugins: [],
}
`);

// 2. postcss.config.js
fs.writeFileSync(path.join(root, 'postcss.config.js'), `export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
`);

// 3. src/index.css
fs.writeFileSync(path.join(root, 'src', 'index.css'), `@import "tailwindcss/base";
@import "tailwindcss/components";
@import "tailwindcss/utilities";

@layer base {
  body {
    @apply bg-coal-950 text-slate-100 font-sans antialiased selection:bg-safety-orange selection:text-white;
    overflow-x: hidden;
  }
}

/* Custom Scrollbar */
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}
::-webkit-scrollbar-track {
  background: rgba(16, 21, 34, 0.6);
}
::-webkit-scrollbar-thumb {
  background: rgba(92, 114, 168, 0.4);
  border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover {
  background: rgba(255, 107, 0, 0.7);
}

/* Leaflet container fixes */
.leaflet-container {
  width: 100%;
  height: 100%;
  border-radius: 0.75rem;
  z-index: 10;
}

.glass-panel {
  background: rgba(20, 27, 45, 0.75);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.glass-panel-hover {
  transition: all 0.2s ease-in-out;
}
.glass-panel-hover:hover {
  background: rgba(27, 36, 59, 0.85);
  border-color: rgba(255, 107, 0, 0.3);
  transform: translateY(-2px);
}

.industrial-border {
  border: 1px solid rgba(65, 83, 127, 0.3);
}

.hazard-stripe {
  background: repeating-linear-gradient(
    45deg,
    rgba(255, 107, 0, 0.15),
    rgba(255, 107, 0, 0.15) 10px,
    rgba(20, 27, 45, 0.4) 10px,
    rgba(20, 27, 45, 0.4) 20px
  );
}
`);

console.log('Configs created successfully!');
