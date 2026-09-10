import React from 'react';
import { History, Eye, Download, Search } from 'lucide-react';
import { useApp } from '../../context/AppContext';

export const InspectionHistoryPage: React.FC = () => {
  const { inspections } = useApp();

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
          <History className="w-4 h-4 text-[#0B2545]" />
          <span>Statutory Audit Logs Archive</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Digital Field Inspection History</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Archival log of all on-site inspections, GPS coordinates, voice transcriptions, and generated corrective cases.
        </p>
      </div>

      <div className="gov-card overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="bg-slate-50 border-b border-slate-200 text-slate-700 font-bold uppercase tracking-wider text-[10px]">
              <tr>
                <th className="p-3">Inspection ID</th>
                <th className="p-3">Mine & Sector</th>
                <th className="p-3">Inspector Officer</th>
                <th className="p-3">Date & Timestamp</th>
                <th className="p-3">Findings Recorded</th>
                <th className="p-3">Status</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-200">
              {inspections.map(insp => (
                <tr key={insp.id} className="hover:bg-slate-50/80 transition-colors">
                  <td className="p-3 font-mono font-bold text-slate-900">{insp.inspectionCode}</td>
                  <td className="p-3 font-bold text-slate-900">
                    <div>{insp.mineName}</div>
                    <div className="text-[10px] text-slate-500 font-normal">{insp.zone}</div>
                  </td>
                  <td className="p-3 text-slate-700">{insp.inspectorName}</td>
                  <td className="p-3 font-mono text-slate-600">{insp.date} {insp.time}</td>
                  <td className="p-3 text-slate-700 max-w-xs truncate">{insp.notes}</td>
                  <td className="p-3">
                    <span className="bg-emerald-50 text-emerald-800 border border-emerald-300 text-[10px] font-bold px-2 py-0.5 rounded uppercase">
                      {insp.status}
                    </span>
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
