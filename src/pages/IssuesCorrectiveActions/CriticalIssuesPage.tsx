import React from 'react';
import { Flame, ClockAlert, ArrowRight, AlertTriangle } from 'lucide-react';
import { useApp } from '../../context/AppContext';

interface Props {
  setActiveTab: (tab: string) => void;
}

export const CriticalIssuesPage: React.FC<Props> = ({ setActiveTab }) => {
  const { issues } = useApp();
  const critical = issues.filter(i => i.severity === 'Critical' && i.status !== 'CLOSED');

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5 border-l-4 border-l-red-700">
        <div className="flex items-center space-x-2 text-xs text-red-700 font-extrabold uppercase tracking-wider">
          <Flame className="w-4 h-4 text-red-700" />
          <span>Priority Emergency SLAs</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Critical Issues & Escalation Register</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          High-risk statutory non-conformances subject to automated 4-tier management escalation and DGMS notification rules.
        </p>
      </div>

      <div className="space-y-3">
        {critical.map(item => (
          <div
            key={item.id}
            className="gov-card p-4 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 border-l-4 border-l-red-700"
          >
            <div className="space-y-1">
              <div className="flex items-center space-x-2">
                <span className="bg-red-700 text-white font-mono font-bold text-[10px] px-2 py-0.5 rounded">
                  SLA: {item.slaRemainingHours}H REMAINING
                </span>
                <span className="font-mono font-bold text-slate-900 text-xs">{item.issueCode}</span>
              </div>
              <h3 className="text-sm font-extrabold text-slate-900">{item.title}</h3>
              <p className="text-xs text-slate-600">
                Location: <strong>{item.mineName} ({item.zone})</strong> &bull; Assignee: <strong>{item.assignedTo}</strong>
              </p>
            </div>

            <button
              onClick={() => setActiveTab('evidence-verification')}
              className="gov-btn-primary text-xs py-2 px-4 self-end sm:self-center"
            >
              <span>Inspect & Verify Evidence</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
