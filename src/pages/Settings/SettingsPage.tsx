import React from 'react';
import { Settings } from 'lucide-react';
import { useAuth } from '../../context/AuthContext';
import { useLanguage } from '../../context/LanguageContext';

export const SettingsPage: React.FC = () => {
  const { currentUser } = useAuth();
  const { language, setLanguage } = useLanguage();

  return (
    <div className="max-w-4xl mx-auto space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-slate-600 font-extrabold uppercase tracking-wider">
          <Settings className="w-4 h-4 text-slate-600" />
          <span>System Configuration</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Platform Settings</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          User profile, escalation SLA timers, neural risk sensitivity thresholds, and language preferences.
        </p>
      </div>

      <div className="gov-card p-5 space-y-4">
        <h3 className="text-xs font-extrabold text-slate-900 uppercase tracking-wider">Active User Profile</h3>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
          <div>
            <span className="text-slate-500 block">Full Name:</span>
            <p className="font-bold text-slate-900 mt-0.5">{currentUser.name}</p>
          </div>
          <div>
            <span className="text-slate-500 block">Designation & Role:</span>
            <p className="font-bold text-[#0B2545] mt-0.5">{currentUser.roleTitle}</p>
          </div>
          <div>
            <span className="text-slate-500 block">Official Email:</span>
            <p className="font-mono text-slate-900 mt-0.5">{currentUser.email}</p>
          </div>
          <div>
            <span className="text-slate-500 block">Department:</span>
            <p className="font-bold text-slate-900 mt-0.5">{currentUser.department}</p>
          </div>
        </div>
      </div>

      <div className="gov-card p-5 space-y-4">
        <h3 className="text-xs font-extrabold text-slate-900 uppercase tracking-wider">Language & Regionalization</h3>
        <div className="flex items-center space-x-4">
          <button
            onClick={() => setLanguage('en')}
            className={`px-4 py-2 rounded text-xs font-bold border transition-all ${
              language === 'en' ? 'bg-[#0B2545] text-white border-[#0B2545]' : 'bg-slate-50 text-slate-800 border-slate-300'
            }`}
          >
            English (Standard)
          </button>
          <button
            onClick={() => setLanguage('hi')}
            className={`px-4 py-2 rounded text-xs font-bold border transition-all ${
              language === 'hi' ? 'bg-[#0B2545] text-white border-[#0B2545]' : 'bg-slate-50 text-slate-800 border-slate-300'
            }`}
          >
            हिंदी (Hindi)
          </button>
        </div>
      </div>
    </div>
  );
};
