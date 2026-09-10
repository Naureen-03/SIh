import React from 'react';
import { FileCheck2, BookOpen, ExternalLink, ShieldCheck } from 'lucide-react';
import { INITIAL_STATUTORY_RULES } from '../../data/mockData';

export const StatutoryReqsPage: React.FC = () => {
  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
          <BookOpen className="w-4 h-4 text-[#0B2545]" />
          <span>Regulatory Rulebook & Legal Citations</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Statutory Requirements & Mandates</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Official statutory citations across DGMS (Directorate General of Mines Safety), MoEFCC, and Central Pollution Control Board (CPCB).
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {INITIAL_STATUTORY_RULES.map(rule => (
          <div key={rule.id} className="gov-card p-4 space-y-3">
            <div className="flex items-start justify-between">
              <div>
                <span className="text-[10px] font-bold bg-[#0B2545] text-white px-2 py-0.5 rounded font-mono">
                  {rule.ruleCode}
                </span>
                <h3 className="text-sm font-extrabold text-slate-900 mt-1">{rule.title}</h3>
                <p className="text-[11px] text-slate-500">{rule.act} &bull; {rule.authority}</p>
              </div>
              <span className="text-[10px] font-bold px-2 py-0.5 rounded bg-emerald-50 text-emerald-800 border border-emerald-300">
                {rule.penaltyClause ? 'Strict Liability' : 'Standard Mandate'}
              </span>
            </div>

            <p className="text-xs text-slate-700 leading-relaxed">{rule.description}</p>

            <div className="p-2.5 bg-slate-50 rounded border border-slate-200 text-xs">
              <span className="font-bold text-red-800">Statutory Non-Compliance Penalty:</span>
              <p className="text-slate-700 text-[11px] mt-0.5">{rule.penaltyClause}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
