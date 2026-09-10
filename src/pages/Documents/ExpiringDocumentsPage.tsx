import React from 'react';
import { ClockAlert } from 'lucide-react';
import { useApp } from '../../context/AppContext';

export const ExpiringDocumentsPage: React.FC = () => {
  const { documents } = useApp();
  const expiring = documents.filter(d => d.daysToExpiry < 30);

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5 border-l-4 border-l-red-700">
        <div className="flex items-center space-x-2 text-xs text-red-700 font-extrabold uppercase tracking-wider">
          <ClockAlert className="w-4 h-4 text-red-700" />
          <span>Statutory Permit Expirations</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Expiring Documents & Licenses</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Proactive renewal alerts for Environmental Clearances, PESO explosive magazine licenses, and Consent to Operate (CTO).
        </p>
      </div>

      <div className="space-y-3">
        {expiring.map(doc => (
          <div
            key={doc.id}
            className="gov-card p-4 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 border-l-4 border-l-red-700"
          >
            <div className="space-y-1">
              <div className="flex items-center space-x-2">
                <span className="bg-red-700 text-white font-mono font-bold text-[10px] px-2 py-0.5 rounded">
                  EXPIRES IN {doc.daysToExpiry} DAYS
                </span>
                <span className="font-mono font-bold text-slate-900 text-xs">{doc.documentNo}</span>
              </div>
              <h3 className="text-sm font-extrabold text-slate-900">{doc.title}</h3>
              <p className="text-xs text-slate-600">Authority: <strong>{doc.authority}</strong> &bull; Mine: <strong>{doc.mineName}</strong></p>
            </div>

            <button className="gov-btn-primary text-xs py-2 px-4 self-end sm:self-center">
              Initiate Renewal Docket
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
