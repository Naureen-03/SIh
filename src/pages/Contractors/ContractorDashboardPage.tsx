import React from 'react';
import { HardHat, UserCheck, ShieldCheck, AlertTriangle } from 'lucide-react';
import { useApp } from '../../context/AppContext';

export const ContractorDashboardPage: React.FC = () => {
  const { contractors } = useApp();

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
          <HardHat className="w-4 h-4 text-[#0B2545]" />
          <span>Outsourced Workforce Governance</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Contractor Management Hub</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Contractor safety index, mandatory VTC refresher tracking, Form B register verification, and statutory audit ranking.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {contractors.map(c => (
          <div
            key={c.id}
            className={`gov-card p-4 space-y-3 ${
              c.status === 'High Risk' ? 'border-l-4 border-l-red-700 bg-red-50/20' : 'border-slate-200'
            }`}
          >
            <div className="flex items-start justify-between">
              <div>
                <span className="text-[10px] font-bold bg-slate-100 text-slate-700 px-2 py-0.5 rounded font-mono">
                  {c.serviceType}
                </span>
                <h3 className="text-sm font-extrabold text-slate-900 mt-1">{c.name}</h3>
                <p className="text-[11px] text-slate-500">{c.mineName} ({c.subsidiary})</p>
              </div>

              <span className={`text-[10px] font-extrabold px-2 py-0.5 rounded uppercase ${
                c.status === 'High Risk' ? 'bg-red-700 text-white' : 'bg-emerald-50 text-emerald-800 border border-emerald-300'
              }`}>
                {c.status}
              </span>
            </div>

            <div className="grid grid-cols-3 gap-2 text-center text-xs">
              <div className="p-2 bg-slate-50 rounded border border-slate-200">
                <span className="text-[9px] text-slate-500 uppercase">Compliance</span>
                <div className="font-mono font-bold text-slate-900 text-base mt-0.5">{c.complianceScore}%</div>
              </div>
              <div className="p-2 bg-slate-50 rounded border border-slate-200">
                <span className="text-[9px] text-slate-500 uppercase">Risk Index</span>
                <div className={`font-mono font-bold text-base mt-0.5 ${c.riskScore > 60 ? 'text-red-700' : 'text-emerald-800'}`}>
                  {c.riskScore}/100
                </div>
              </div>
              <div className="p-2 bg-slate-50 rounded border border-slate-200">
                <span className="text-[9px] text-slate-500 uppercase">Deployed</span>
                <div className="font-mono font-bold text-[#0B2545] text-base mt-0.5">{c.activeWorkers}</div>
              </div>
            </div>

            <div className="p-2.5 bg-slate-50 rounded border border-slate-200 text-xs space-y-0.5">
              <span className="font-bold text-[#0B2545] text-[10px] uppercase">AI Audit Directive:</span>
              <p className="text-slate-700 text-[11px]">{c.auditRecommendation}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
