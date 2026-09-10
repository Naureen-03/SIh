import React, { useState } from 'react';
import { ShieldAlert, Plus } from 'lucide-react';

export const IncidentManagementPage: React.FC = () => {
  const incidents = [
    { id: 'INC-2026-081', title: 'Hydraulic Hose Rupture on Dumper #14', location: 'Gevra Bench 4', date: '29 Aug 2026 11:30', reporter: 'P. K. Verma', status: 'Contained' },
    { id: 'INC-2026-080', title: 'Localized Water Logging near Pit Sump', location: 'Kusmunda Pit Face', date: '28 Aug 2026 15:40', reporter: 'R. S. Sahu', status: 'Resolved' }
  ];

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2 text-xs text-red-700 font-extrabold uppercase tracking-wider">
            <ShieldAlert className="w-4 h-4 text-red-700" />
            <span>Emergency Incident Reporting</span>
          </div>
          <h1 className="text-2xl font-black text-slate-900 mt-1">Incident Management Register</h1>
          <p className="text-xs text-slate-600 mt-0.5">
            Real-time hazard containment and automatic generation of closed-loop corrective actions.
          </p>
        </div>

        <button className="gov-btn-danger">
          <Plus className="w-4 h-4" />
          <span>Report Safety Incident</span>
        </button>
      </div>

      <div className="space-y-3">
        {incidents.map(inc => (
          <div key={inc.id} className="gov-card p-4 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3">
            <div>
              <div className="flex items-center space-x-2">
                <span className="font-mono font-bold text-slate-900 text-xs">{inc.id}</span>
                <span className="text-[10px] bg-slate-100 text-slate-700 px-2 py-0.5 rounded">{inc.location}</span>
              </div>
              <h3 className="text-xs font-bold text-slate-900 mt-1">{inc.title}</h3>
              <p className="text-[11px] text-slate-500">Reported by {inc.reporter} &bull; {inc.date}</p>
            </div>

            <span className="text-[10px] font-extrabold px-2.5 py-1 rounded bg-emerald-50 text-emerald-800 border border-emerald-300">
              {inc.status} (Corrective Action Active)
            </span>
          </div>
        ))}
      </div>
    </div>
  );
};
