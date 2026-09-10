import React from 'react';
import { ScanEye, AlertTriangle, ArrowRight } from 'lucide-react';
import { useApp } from '../../context/AppContext';

interface Props {
  setActiveTab: (tab: string) => void;
}

export const AIFindingsPage: React.FC<Props> = ({ setActiveTab }) => {
  const { issues } = useApp();
  const criticalFindings = issues.filter(i => i.severity === 'Critical');

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
          <ScanEye className="w-4 h-4 text-[#0B2545]" />
          <span>AI Computer Vision & NLP Findings</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Identified Hazards & Risk Findings</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Automatic risk classifications synthesized from field audits, raster comparison, and historical clusters.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {criticalFindings.map(item => (
          <div key={item.id} className="gov-card p-4 space-y-3 border-l-4 border-l-red-700">
            <div className="flex items-start justify-between">
              <div>
                <span className="text-[10px] font-bold bg-slate-100 text-slate-700 px-2 py-0.5 rounded font-mono">
                  {item.issueCode}
                </span>
                <h3 className="text-sm font-extrabold text-slate-900 mt-1">{item.title}</h3>
                <p className="text-[11px] text-slate-500">{item.mineName} &bull; {item.zone}</p>
              </div>
              <span className="text-[10px] font-black px-2 py-0.5 rounded bg-red-50 text-red-800 border border-red-300 font-mono">
                RISK {item.riskScore}/100
              </span>
            </div>

            <p className="text-xs text-slate-700 leading-relaxed">{item.description}</p>

            <div className="flex items-center justify-between pt-2 border-t border-slate-200 text-xs">
              <span className="text-slate-500 font-mono">SLA: {item.slaRemainingHours}h Left</span>
              <button
                onClick={() => setActiveTab('evidence-verification')}
                className="gov-btn-secondary text-[11px] py-1 px-3"
              >
                <span>Verify Remediation</span>
                <ArrowRight className="w-3 h-3" />
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
