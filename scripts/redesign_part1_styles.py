import os

# 1. tailwind.config.js - Government / Public Sector Palette
tailwind_config = """/** @type {import('tailwindcss').Config} */
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
"""

with open('tailwind.config.js', 'w', encoding='utf-8') as f:
    f.write(tailwind_config)

# 2. src/index.css - Government Typography, crisp borders, clean cards
index_css = """@import "tailwindcss/base";
@import "tailwindcss/components";
@import "tailwindcss/utilities";

@layer base {
  body {
    @apply bg-[#F4F6F9] text-slate-900 font-sans antialiased;
    overflow-x: hidden;
  }
}

/* Official Government Tricolor Ribbon */
.gov-tricolor-strip {
  height: 4px;
  background: linear-gradient(90deg, #FF9933 0%, #FF9933 33.3%, #FFFFFF 33.3%, #FFFFFF 66.6%, #138808 66.6%, #138808 100%);
  width: 100%;
}

.gov-card {
  @apply bg-white border border-slate-200 rounded-lg shadow-gov;
}

.gov-card-header {
  @apply px-4 py-3 border-b border-slate-200 bg-slate-50/80 font-bold text-slate-800 text-xs uppercase tracking-wider flex items-center justify-between;
}

.gov-btn-primary {
  @apply bg-[#0B2545] hover:bg-[#134074] text-white font-bold text-xs px-4 py-2 rounded-md shadow-sm transition-all inline-flex items-center justify-center space-x-1.5 uppercase tracking-wide;
}

.gov-btn-secondary {
  @apply bg-white hover:bg-slate-50 text-[#0B2545] border border-slate-300 font-bold text-xs px-4 py-2 rounded-md shadow-sm transition-all inline-flex items-center justify-center space-x-1.5 uppercase tracking-wide;
}

.gov-btn-success {
  @apply bg-[#15803D] hover:bg-[#166534] text-white font-bold text-xs px-4 py-2 rounded-md shadow-sm transition-all inline-flex items-center justify-center space-x-1.5 uppercase tracking-wide;
}

.gov-btn-danger {
  @apply bg-[#B91C1C] hover:bg-[#991B1B] text-white font-bold text-xs px-4 py-2 rounded-md shadow-sm transition-all inline-flex items-center justify-center space-x-1.5 uppercase tracking-wide;
}

.gov-badge-compliant {
  @apply bg-emerald-50 text-emerald-800 border border-emerald-300 text-[10px] font-bold px-2 py-0.5 rounded uppercase;
}

.gov-badge-critical {
  @apply bg-red-50 text-red-800 border border-red-300 text-[10px] font-bold px-2 py-0.5 rounded uppercase;
}

.gov-badge-high {
  @apply bg-amber-50 text-amber-900 border border-amber-300 text-[10px] font-bold px-2 py-0.5 rounded uppercase;
}

.gov-badge-info {
  @apply bg-blue-50 text-blue-800 border border-blue-300 text-[10px] font-bold px-2 py-0.5 rounded uppercase;
}

/* Custom Scrollbar */
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}
::-webkit-scrollbar-track {
  background: #E2E8F0;
}
::-webkit-scrollbar-thumb {
  background: #94A3B8;
  border-radius: 3px;
}
::-webkit-scrollbar-thumb:hover {
  background: #0B2545;
}

.leaflet-container {
  width: 100%;
  height: 100%;
  border-radius: 0.5rem;
  z-index: 10;
}
"""

with open('src/index.css', 'w', encoding='utf-8') as f:
    f.write(index_css)

# 3. Footer Component (`src/components/layout/Footer.tsx`)
footer_tsx = """import React from 'react';
import { ShieldCheck, ExternalLink, Award } from 'lucide-react';

export const Footer: React.FC = () => {
  return (
    <footer className="mt-12 border-t border-slate-300 bg-[#0B2545] text-slate-200">
      <div className="gov-tricolor-strip" />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8 text-xs">
          {/* Col 1 */}
          <div className="space-y-2 md:col-span-2">
            <div className="flex items-center space-x-2">
              <div className="w-7 h-7 rounded bg-white/10 border border-white/20 flex items-center justify-center font-bold text-white text-xs">
                GOI
              </div>
              <div>
                <h4 className="font-extrabold text-white text-sm tracking-wide">MINEGUARD AI</h4>
                <p className="text-[11px] text-slate-300">Smart Governance & Compliance Monitoring System</p>
              </div>
            </div>
            <p className="text-slate-300 leading-relaxed text-[11px] pt-2">
              Developed as an AI-powered smart automation prototype for <strong>Smart India Hackathon (SIH 2026)</strong> under <strong>Problem Statement ID 26024</strong>.
              Institutional Partner: <strong>Ministry of Coal • Coal India Limited (CIL)</strong>.
            </p>
            <p className="text-[10px] text-amber-300 font-mono pt-1">
              * Prototype System for Demonstration & Evaluation Purposes
            </p>
          </div>

          {/* Col 2 */}
          <div className="space-y-2">
            <h5 className="font-bold text-white uppercase tracking-wider text-[11px] border-b border-slate-700 pb-1">
              Governance Framework
            </h5>
            <ul className="space-y-1.5 text-slate-300 text-[11px]">
              <li>Mines Act, 1952</li>
              <li>Coal Mines Regulations, 2017</li>
              <li>MoEFCC EC Guidelines</li>
              <li>DGMS Safety Standards</li>
              <li>Contract Labour (R&A) Act, 1970</li>
            </ul>
          </div>

          {/* Col 3 */}
          <div className="space-y-2">
            <h5 className="font-bold text-white uppercase tracking-wider text-[11px] border-b border-slate-700 pb-1">
              Official Portals
            </h5>
            <ul className="space-y-1.5 text-slate-300 text-[11px]">
              <li><a href="https://coal.gov.in" target="_blank" rel="noreferrer" className="hover:text-white flex items-center space-x-1"><span>Ministry of Coal</span><ExternalLink className="w-2.5 h-2.5" /></a></li>
              <li><a href="https://coalindia.in" target="_blank" rel="noreferrer" className="hover:text-white flex items-center space-x-1"><span>Coal India Limited</span><ExternalLink className="w-2.5 h-2.5" /></a></li>
              <li><a href="https://dgms.gov.in" target="_blank" rel="noreferrer" className="hover:text-white flex items-center space-x-1"><span>DGMS Portal</span><ExternalLink className="w-2.5 h-2.5" /></a></li>
              <li><a href="https://parivesh.nic.in" target="_blank" rel="noreferrer" className="hover:text-white flex items-center space-x-1"><span>PARIVESH (MoEFCC)</span><ExternalLink className="w-2.5 h-2.5" /></a></li>
            </ul>
          </div>
        </div>

        <div className="mt-8 pt-4 border-t border-slate-700/80 flex flex-col sm:flex-row items-center justify-between text-[11px] text-slate-400 gap-2">
          <p>© 2026 Government of India • Ministry of Coal. Prototype Version 2.4.0 (SIH 26024)</p>
          <div className="flex items-center space-x-4">
            <span>Website Policies</span>
            <span>Accessibility Statement</span>
            <span>Helpdesk: support-mineguard@nic.in</span>
          </div>
        </div>
      </div>
    </footer>
  );
};
"""

with open('src/components/layout/Footer.tsx', 'w', encoding='utf-8') as f:
    f.write(footer_tsx)

print("Part 1: tailwind, index.css, and Footer.tsx written successfully!")
