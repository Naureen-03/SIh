import React from 'react';
import { Calendar, Clock, AlertTriangle, CheckCircle2 } from 'lucide-react';
import { INITIAL_STATUTORY_RULES } from '../../data/mockData';

export const ComplianceCalendarPage: React.FC = () => {
  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
          <Calendar className="w-4 h-4 text-[#0B2545]" />
          <span>Statutory Filing & Return Calendar</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Compliance Filing Calendar</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Upcoming deadlines for DGMS Form IV safety returns, MoEFCC six-monthly compliance reports, and Consent to Operate renewals.
        </p>
      </div>

      <div className="space-y-3">
        {INITIAL_STATUTORY_RULES.map(rule => (
          <div
            key={rule.id}
            className="gov-card p-4 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3"
          >
            <div className="space-y-1">
              <div className="flex items-center space-x-2">
                <span className="font-mono font-bold text-slate-900 text-xs">{rule.ruleCode}</span>
                <span className="text-[10px] bg-slate-100 text-slate-700 px-2 py-0.5 rounded">{rule.authority}</span>
              </div>
              <h3 className="text-xs font-bold text-slate-900">{rule.title}</h3>
              <p className="text-[11px] text-slate-500">Statutory Frequency: {rule.frequency}</p>
            </div>

            <div className="flex items-center space-x-3 self-end sm:self-auto">
              <div className="text-right">
                <span className="text-[10px] text-slate-500 block">Due Date</span>
                <span className="font-mono font-bold text-slate-900 text-xs">15 Sep 2026</span>
              </div>
              <button className="gov-btn-primary text-xs py-1 px-3">
                File Docket
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
