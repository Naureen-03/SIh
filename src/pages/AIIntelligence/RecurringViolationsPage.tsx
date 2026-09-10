import React from 'react';
import { RefreshCw, AlertTriangle } from 'lucide-react';
import { useApp } from '../../context/AppContext';

interface Props {
  setActiveTab: (tab: string) => void;
}

export const RecurringViolationsPage: React.FC<Props> = ({ setActiveTab }) => {
  const recurring = [
    { title: 'Conveyor Trunk Pinch-Point Guard Absence', occurrences: 4, cluster: 'Korba Area (SECL)', risk: 'Critical', dgmsClause: 'CMR 2017 Reg 184(2)', action: 'Mandatory structural audit of all conveyor flanks' },
    { title: 'Contractor Dump Truck Rear Optical Camera Failure', occurrences: 6, cluster: 'Singrauli Area (NCL)', risk: 'High', dgmsClause: 'DGMS Tech Circular 04/2019', action: 'Blacklist non-compliant transport vendor ABC Haulage' },
    { title: 'Excess Ambient PM10 Dust at Coal Loading Hopper', occurrences: 5, cluster: 'Kusmunda Area (SECL)', risk: 'High', dgmsClause: 'MoEFCC EC Condition IV(b)', action: 'Automate dry-fog dust suppression with CAAQMS link' }
  ];

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
          <RefreshCw className="w-4 h-4 text-[#0B2545]" />
          <span>Systemic Pattern Recognition</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Recurring Statutory Violations</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          AI pattern detection isolating chronic safety and environmental non-compliances repeating across mining clusters.
        </p>
      </div>

      <div className="space-y-3">
        {recurring.map((item, idx) => (
          <div key={idx} className="gov-card p-4 space-y-3 border-l-4 border-l-amber-600">
            <div className="flex items-start justify-between">
              <div>
                <span className="text-[10px] font-bold bg-slate-100 text-slate-700 px-2 py-0.5 rounded font-mono">
                  Cluster: {item.cluster} &bull; {item.dgmsClause}
                </span>
                <h3 className="text-sm font-extrabold text-slate-900 mt-1">{item.title}</h3>
              </div>
              <span className="bg-red-50 text-red-800 border border-red-300 text-xs font-mono font-bold px-2 py-0.5 rounded">
                {item.occurrences} Recurring Events
              </span>
            </div>

            <div className="p-2.5 bg-slate-50 rounded border border-slate-200 text-xs">
              <span className="font-bold text-[#0B2545]">Statutory Systemic Directive:</span>
              <p className="text-slate-700 text-[11px] mt-0.5">{item.action}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
