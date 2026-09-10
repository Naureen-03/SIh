/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        gov: {
          navy: {
            950: '#061325',
            900: '#0B2545',
            850: '#0F3057',
            800: '#134074',
            700: '#1D4E89',
            600: '#2A6F97',
            500: '#468FAF',
            100: '#EEF4F8',
            50: '#F5F8FA',
          },
          saffron: {
            DEFAULT: '#F97316',
            dark: '#C2410C',
            muted: '#D97706',
            light: '#FFEDD5',
          },
          green: {
            DEFAULT: '#15803D',
            dark: '#166534',
            light: '#DCFCE7',
          },
          red: {
            DEFAULT: '#B91C1C',
            dark: '#991B1B',
            light: '#FEE2E2',
          },
          amber: {
            DEFAULT: '#D97706',
            dark: '#B45309',
            light: '#FEF3C7',
          },
          slate: {
            900: '#0F172A',
            800: '#1E293B',
            700: '#334155',
            600: '#475569',
            500: '#64748B',
            400: '#94A3B8',
            300: '#CBD5E1',
            200: '#E2E8F0',
            100: '#F1F5F9',
            50: '#F8FAFC',
          }
        }
      },
      fontFamily: {
        sans: ['Inter', 'Noto Sans', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
        mono: ['JetBrains Mono', 'Fira Code', 'monospace'],
      },
      boxShadow: {
        'gov': '0 1px 3px 0 rgba(11, 37, 69, 0.08), 0 1px 2px -1px rgba(11, 37, 69, 0.04)',
        'gov-md': '0 4px 6px -1px rgba(11, 37, 69, 0.1), 0 2px 4px -2px rgba(11, 37, 69, 0.06)',
        'gov-lg': '0 10px 15px -3px rgba(11, 37, 69, 0.1), 0 4px 6px -4px rgba(11, 37, 69, 0.05)',
      }
    },
  },
  plugins: [],
}
