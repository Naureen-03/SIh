import React from 'react';
import { FileText, Download, CheckCircle2, Building2 } from 'lucide-react';

export const StatutoryReportsPage: React.FC = () => {
  const reports = [
    { code: 'FORM-IV', title: 'DGMS Annual Safety Return (Mines Act 1952)', period: 'Annual 2025-26', status: 'Submitted & Acknowledged' },
    { code: 'FORM-VI', title: 'Notice of Accident / Serious Bodily Injury Register', period: 'August 2026', status: 'Up to date' },
    { code: 'EC-RETURNS', title: 'MoEFCC Six-Monthly Environmental Compliance Return', period: 'Apr - Sep 2026', status: 'Draft Ready' },
    { code: 'FORM-B', title: 'Register of Employees (Contract Labour Act, 1970)', period: 'August 2026', status: 'Biometric Verified' },
  ];

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
          <FileText className="w-4 h-4 text-[#0B2545]" />
          <span>Statutory Returns & Form Submissions</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Official Statutory Reports Archive</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Standardized digital forms complying with Directorate General of Mines Safety and MoEFCC formats.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {reports.map(rep => (
          <div key={rep.code} className="gov-card p-4 space-y-3">
            <div className="flex items-start justify-between">
              <div>
                <span className="text-[10px] font-bold bg-[#0B2545] text-white px-2 py-0.5 rounded font-mono">
                  {rep.code}
                </span>
                <h3 className="text-sm font-extrabold text-slate-900 mt-1">{rep.title}</h3>
                <p className="text-[11px] text-slate-500 font-mono">Period: {rep.period}</p>
              </div>
              <span className="text-[10px] font-bold px-2 py-0.5 rounded bg-emerald-50 text-emerald-800 border border-emerald-300">
                {rep.status}
              </span>
            </div>

            <div className="flex justify-end space-x-2 pt-2 border-t border-slate-200">
              <button className="gov-btn-secondary text-xs py-1 px-3">
                Preview Form
              </button>
              <button className="gov-btn-primary text-xs py-1 px-3">
                <Download className="w-3.5 h-3.5" />
                <span>Download Signed PDF</span>
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
