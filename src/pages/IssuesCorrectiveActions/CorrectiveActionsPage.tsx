import React from 'react';
import { Wrench, CheckCircle2, Clock } from 'lucide-react';
import { useApp } from '../../context/AppContext';

interface Props {
  setActiveTab: (tab: string) => void;
}

export const CorrectiveActionsPage: React.FC<Props> = ({ setActiveTab }) => {
  const { issues } = useApp();
  const list = issues.filter(i => i.correctiveAction);

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
          <Wrench className="w-4 h-4 text-[#0B2545]" />
          <span>Remediation Dispatch Hub</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Corrective Action Workflow Center</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Case management center tracking work orders from assignment, rectification, before/after verification, to final case closure.
        </p>
      </div>

      <div className="space-y-3">
        {list.map(item => {
          const ca = item.correctiveAction!;
          return (
            <div key={item.id} className="gov-card p-4 space-y-3">
              <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2 border-b border-slate-200 pb-2">
                <div>
                  <span className="text-[10px] font-bold bg-slate-100 text-slate-700 px-2 py-0.5 rounded font-mono">
                    Docket #{item.issueCode}
                  </span>
                  <h3 className="text-sm font-extrabold text-slate-900 mt-0.5">{ca.title}</h3>
                </div>

                <span className="bg-blue-50 text-blue-800 border border-blue-300 text-[10px] font-bold px-2 py-0.5 rounded uppercase">
                  {ca.status}
                </span>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
                <div>
                  <span className="text-slate-500 block text-[10px] uppercase">Assigned Officer</span>
                  <p className="font-bold text-slate-900">{ca.assignedTo}</p>
                </div>
                <div>
                  <span className="text-slate-500 block text-[10px] uppercase">Responsible Department</span>
                  <p className="font-bold text-slate-900">{ca.assignedDepartment}</p>
                </div>
                <div>
                  <span className="text-slate-500 block text-[10px] uppercase">SLA Deadline</span>
                  <p className="font-mono font-bold text-red-700">{ca.deadline}</p>
                </div>
              </div>

              <div className="flex justify-end pt-2 border-t border-slate-200">
                <button
                  onClick={() => setActiveTab('evidence-verification')}
                  className="gov-btn-primary text-xs py-1.5 px-3"
                >
                  Verify Rectification Evidence
                </button>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
