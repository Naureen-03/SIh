import React from 'react';
import { Users } from 'lucide-react';

export const LabourCompliancePage: React.FC = () => {
  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
          <Users className="w-4 h-4 text-[#0B2545]" />
          <span>Worker Health & Statutory Registers</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Labour & Worker Compliance</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Tracking Form B worker master registry, Vocational Training Centre (VTC) attendance, and Periodic Medical Examination (PME).
        </p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
        <div className="gov-card p-4 space-y-2">
          <span className="text-xs font-bold text-slate-600 uppercase">Form B Register Status</span>
          <div className="text-xl font-black text-emerald-800 font-mono">96.4% Verified</div>
          <p className="text-xs text-slate-500">Biometric fingerprint sync</p>
        </div>

        <div className="gov-card p-4 space-y-2">
          <span className="text-xs font-bold text-slate-600 uppercase">Annual VTC Safety Refresher</span>
          <div className="text-xl font-black text-amber-800 font-mono">89.2% Completed</div>
          <p className="text-xs text-slate-500">18 operators pending batch</p>
        </div>

        <div className="gov-card p-4 space-y-2">
          <span className="text-xs font-bold text-slate-600 uppercase">PME Medical Fitness</span>
          <div className="text-xl font-black text-slate-900 font-mono">98.1% Current</div>
          <p className="text-xs text-slate-500">DGMS Standard Audiometry/Chest</p>
        </div>
      </div>
    </div>
  );
};
