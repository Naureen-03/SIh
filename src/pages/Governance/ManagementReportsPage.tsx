import React from 'react';
import { BarChart3, Download, Sparkles } from 'lucide-react';
import { useApp } from '../../context/AppContext';

export const ManagementReportsPage: React.FC = () => {
  const { stats } = useApp();

  return (
    <div className="space-y-6 pb-12 max-w-4xl mx-auto">
      <div className="gov-card p-5 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
            <BarChart3 className="w-4 h-4 text-[#0B2545]" />
            <span>Automated Governance Intelligence</span>
          </div>
          <h1 className="text-2xl font-black text-slate-900 mt-1">Official Management Reports</h1>
          <p className="text-xs text-slate-600 mt-0.5">
            Auto-compiled executive briefs, DGMS safety returns, and compliance audits with instant PDF export.
          </p>
        </div>

        <button className="gov-btn-primary">
          <Download className="w-4 h-4 text-amber-400" />
          <span>Export Monthly Governance PDF</span>
        </button>
      </div>

      <div className="gov-card p-6 space-y-4 border-l-4 border-l-[#0B2545]">
        <div className="flex items-center space-x-2">
          <Sparkles className="w-5 h-5 text-amber-600" />
          <h3 className="text-sm font-black text-slate-900 uppercase tracking-wider">
            AI Executive Governance Summary
          </h3>
        </div>
        <p className="text-xs text-slate-700 leading-relaxed">
          &ldquo;Overall coal mine governance compliance improved by <strong>+8.0% compared to last month</strong> across the Korba operational cluster. However, mechanical conveyor safety violations increased in Zone 4 due to recurring equipment protection lapses. 17 corrective actions are currently under active SLA countdown, with 1 critical hazard verified and ready for closure.&rdquo;
        </p>

        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-3 border-t border-slate-200">
          <div className="p-3 bg-slate-50 rounded border border-slate-200 text-center">
            <span className="text-[10px] text-slate-500 uppercase font-bold">Overall Compliance</span>
            <div className="text-xl font-black text-emerald-800 font-mono mt-0.5">{stats.overallCompliance}%</div>
          </div>
          <div className="p-3 bg-slate-50 rounded border border-slate-200 text-center">
            <span className="text-[10px] text-slate-500 uppercase font-bold">Open Issues</span>
            <div className="text-xl font-black text-amber-800 font-mono mt-0.5">{stats.openIssues}</div>
          </div>
          <div className="p-3 bg-slate-50 rounded border border-slate-200 text-center">
            <span className="text-[10px] text-slate-500 uppercase font-bold">Critical Risks</span>
            <div className="text-xl font-black text-red-700 font-mono mt-0.5">{stats.criticalIssues}</div>
          </div>
          <div className="p-3 bg-slate-50 rounded border border-slate-200 text-center">
            <span className="text-[10px] text-slate-500 uppercase font-bold">Field Audits</span>
            <div className="text-xl font-black text-[#0B2545] font-mono mt-0.5">{stats.inspectionsThisMonth}</div>
          </div>
        </div>
      </div>
    </div>
  );
};
