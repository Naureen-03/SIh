import React from 'react';
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
