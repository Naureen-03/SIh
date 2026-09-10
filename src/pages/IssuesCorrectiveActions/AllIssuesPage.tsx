import React, { useState } from 'react';
import { AlertTriangle, Flame, CheckCircle2, Wrench, Search, Filter } from 'lucide-react';
import { useApp } from '../../context/AppContext';

interface Props {
  setActiveTab: (tab: string) => void;
}

export const AllIssuesPage: React.FC<Props> = ({ setActiveTab }) => {
  const { issues } = useApp();
  const [searchTerm, setSearchTerm] = useState('');

  const filtered = issues.filter(i => i.title.toLowerCase().includes(searchTerm.toLowerCase()) || i.issueCode.toLowerCase().includes(searchTerm.toLowerCase()));

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
            <AlertTriangle className="w-4 h-4 text-[#0B2545]" />
            <span>Official Non-Compliance & Safety Docket</span>
          </div>
          <h1 className="text-2xl font-black text-slate-900 mt-1">Open Issues Register</h1>
          <p className="text-xs text-slate-600 mt-0.5">
            Master register of all open statutory violations, safety observations, and environmental notices.
          </p>
        </div>

        <input
          type="text"
          placeholder="Search issue code, title..."
          value={searchTerm}
          onChange={e => setSearchTerm(e.target.value)}
          className="bg-slate-50 border border-slate-300 rounded px-3 py-1.5 text-xs text-slate-900 placeholder-slate-400 focus:outline-none focus:border-[#0B2545] w-64"
        />
      </div>

      <div className="gov-card overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="bg-slate-50 border-b border-slate-200 text-slate-700 font-bold uppercase tracking-wider text-[10px]">
              <tr>
                <th className="p-3">Docket No</th>
                <th className="p-3">Mine Location</th>
                <th className="p-3">Category</th>
                <th className="p-3">Severity</th>
                <th className="p-3">Risk Score</th>
                <th className="p-3">Assignee</th>
                <th className="p-3">Status</th>
                <th className="p-3 text-right">Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-200">
              {filtered.map(item => (
                <tr key={item.id} className="hover:bg-slate-50/80 transition-colors">
                  <td className="p-3 font-mono font-bold text-slate-900">
                    <div>{item.issueCode}</div>
                    <div className="text-[10px] text-slate-500 font-sans font-normal truncate max-w-xs">{item.title}</div>
                  </td>
                  <td className="p-3 font-bold text-slate-900">{item.mineName}</td>
                  <td className="p-3">
                    <span className="bg-slate-100 text-slate-800 border border-slate-300 text-[10px] font-bold px-2 py-0.5 rounded uppercase">
                      {item.category}
                    </span>
                  </td>
                  <td className="p-3">
                    <span className={`text-[10px] font-bold px-2 py-0.5 rounded uppercase ${
                      item.severity === 'Critical' ? 'bg-red-50 text-red-800 border border-red-300' : 'bg-amber-50 text-amber-800 border border-amber-300'
                    }`}>
                      {item.severity}
                    </span>
                  </td>
                  <td className="p-3 font-mono font-bold text-slate-900">{item.riskScore}</td>
                  <td className="p-3 text-slate-700">{item.assignedTo || 'Unassigned'}</td>
                  <td className="p-3">
                    <span className="bg-blue-50 text-blue-800 border border-blue-300 text-[10px] font-bold px-2 py-0.5 rounded uppercase">
                      {item.status}
                    </span>
                  </td>
                  <td className="p-3 text-right">
                    <button
                      onClick={() => setActiveTab('evidence-verification')}
                      className="gov-btn-secondary text-[11px] py-1 px-2.5"
                    >
                      Inspect
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
