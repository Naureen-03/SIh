import React from 'react';
import { UserCheck } from 'lucide-react';
import { useApp } from '../../context/AppContext';

export const ContractorCompliancePage: React.FC = () => {
  const { contractors } = useApp();

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
          <UserCheck className="w-4 h-4 text-[#0B2545]" />
          <span>Statutory Labour & Training Verification</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Contractor Compliance & Risk</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Vocational Training Centre (VTC) compliance, Form B registers, and Periodic Medical Examination (PME) records.
        </p>
      </div>

      <div className="gov-card overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="bg-slate-50 border-b border-slate-200 text-slate-700 font-bold uppercase tracking-wider text-[10px]">
              <tr>
                <th className="p-3">Contractor Name</th>
                <th className="p-3">Service Area</th>
                <th className="p-3">Deployed Workers</th>
                <th className="p-3">VTC Trained</th>
                <th className="p-3">PME Medical Fit</th>
                <th className="p-3">Open Violations</th>
                <th className="p-3">Compliance Score</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-200">
              {contractors.map(c => (
                <tr key={c.id} className="hover:bg-slate-50/80 transition-colors">
                  <td className="p-3 font-bold text-slate-900">{c.name}</td>
                  <td className="p-3 text-slate-700 font-mono">{c.serviceType}</td>
                  <td className="p-3 font-mono text-slate-900">{c.stats.totalDeployed}</td>
                  <td className="p-3 font-mono text-emerald-800 font-bold">{c.stats.trainedVTC} / {c.stats.totalDeployed}</td>
                  <td className="p-3 font-mono text-slate-700">{c.stats.medicalFitPME}</td>
                  <td className="p-3 font-mono font-bold text-red-700">{c.openViolations}</td>
                  <td className="p-3 font-mono font-bold text-slate-900">{c.complianceScore}%</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
