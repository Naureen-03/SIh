import os

alerts_escalations = """import React from 'react';
import { Bell } from 'lucide-react';
import { useApp } from '../../context/AppContext';

export const AlertsEscalationsPage: React.FC = () => {
  const { notifications, markNotificationRead } = useApp();

  const escalationTiers = [
    { level: 'Level 1 (0-24 Hours)', target: 'Assigned Field Officer', action: 'Direct on-site hazard containment' },
    { level: 'Level 2 (24-48 Hours)', target: 'Department Head', action: 'Resource reallocation & secondary audit' },
    { level: 'Level 3 (48-72 Hours)', target: 'Mine General Manager', action: 'Statutory stoppage notice warning' },
    { level: 'Level 4 (>72 Hours)', target: 'Corporate Director & Ministry', action: 'High-level inquiry & disciplinary notice' }
  ];

  return (
    <div className="space-y-6 pb-12">
      <div className="glass-panel p-5 rounded-2xl border border-slate-800">
        <div className="flex items-center space-x-2 text-xs text-amber-500 font-bold uppercase tracking-wider">
          <Bell className="w-4 h-4 text-amber-500" />
          <span>SLA Countdown & 4-Tier Hierarchy</span>
        </div>
        <h1 className="text-2xl font-black text-white mt-1">Alerts & Escalation Center</h1>
        <p className="text-xs text-slate-400 mt-0.5">
          Automated escalation timeline notifying responsible officers, department heads, mine managers, and corporate leadership.
        </p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
        {escalationTiers.map((t, idx) => (
          <div key={idx} className="glass-panel p-4 rounded-xl border border-slate-800 space-y-2">
            <span className="text-[10px] font-extrabold text-safety-orange uppercase font-mono">{t.level}</span>
            <h4 className="text-xs font-bold text-white">{t.target}</h4>
            <p className="text-[11px] text-slate-400">{t.action}</p>
          </div>
        ))}
      </div>

      <div className="space-y-3">
        {notifications.map(n => (
          <div
            key={n.id}
            className={`glass-panel p-4 rounded-xl border flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 ${
              n.severity === 'Critical' ? 'border-red-500/40 bg-red-950/20' : 'border-slate-800'
            }`}
          >
            <div className="space-y-1">
              <div className="flex items-center space-x-2">
                <span className={`text-[10px] font-bold px-2 py-0.5 rounded ${
                  n.severity === 'Critical' ? 'bg-red-500 text-white' : 'bg-amber-500 text-black'
                }`}>
                  {n.severity}
                </span>
                <h3 className="text-xs font-bold text-white">{n.title}</h3>
              </div>
              <p className="text-xs text-slate-300">{n.message}</p>
              <span className="text-[10px] text-slate-500 font-mono">{n.timestamp}</span>
            </div>

            <button
              onClick={() => markNotificationRead(n.id)}
              className="px-3 py-1.5 rounded-lg bg-coal-800 text-xs text-slate-300 hover:text-white font-bold border border-slate-700 self-end sm:self-center"
            >
              {n.read ? 'Acknowledged' : 'Acknowledge & Dismiss'}
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

management_reports = """import React from 'react';
import { BarChart3, Download, Sparkles } from 'lucide-react';
import { useApp } from '../../context/AppContext';

export const ManagementReportsPage: React.FC = () => {
  const { stats } = useApp();

  return (
    <div className="space-y-6 pb-12 max-w-4xl mx-auto">
      <div className="glass-panel p-5 rounded-2xl border border-slate-800 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2 text-xs text-cyan-400 font-bold uppercase tracking-wider">
            <BarChart3 className="w-4 h-4 text-cyan-400" />
            <span>Automated Governance Intelligence</span>
          </div>
          <h1 className="text-2xl font-black text-white mt-1">Management Reports</h1>
          <p className="text-xs text-slate-400 mt-0.5">
            Auto-compiled executive briefs, DGMS safety returns, and compliance audits with instant export.
          </p>
        </div>

        <button className="flex items-center space-x-2 px-5 py-2.5 rounded-xl bg-gradient-to-r from-safety-orange to-amber-500 hover:from-safety-orange/90 text-white font-bold text-xs shadow-lg shadow-safety-orange/20">
          <Download className="w-4 h-4" />
          <span>Export Monthly Governance PDF</span>
        </button>
      </div>

      <div className="glass-panel p-6 rounded-2xl border border-safety-orange/40 bg-coal-900/90 space-y-3 shadow-2xl">
        <div className="flex items-center space-x-2">
          <Sparkles className="w-5 h-5 text-safety-orange" />
          <h3 className="text-sm font-black text-white uppercase tracking-wider">AI Executive Governance Summary</h3>
        </div>
        <p className="text-xs text-slate-300 leading-relaxed">
          &ldquo;Overall coal mine governance compliance improved by <strong>+8.0% compared to last month</strong> across the Korba operational cluster. However, mechanical conveyor safety violations increased in Zone 4 due to recurring equipment protection lapses. 17 corrective actions are currently under active SLA countdown, with 1 critical hazard verified and ready for closure.&rdquo;
        </p>

        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-3 border-t border-slate-800">
          <div className="p-3 bg-coal-950 rounded-lg text-center">
            <span className="text-[10px] text-slate-400 uppercase font-bold">Overall Compliance</span>
            <div className="text-xl font-black text-emerald-400 font-mono mt-0.5">{stats.overallCompliance}%</div>
          </div>
          <div className="p-3 bg-coal-950 rounded-lg text-center">
            <span className="text-[10px] text-slate-400 uppercase font-bold">Open Issues</span>
            <div className="text-xl font-black text-amber-400 font-mono mt-0.5">{stats.openIssues}</div>
          </div>
          <div className="p-3 bg-coal-950 rounded-lg text-center">
            <span className="text-[10px] text-slate-400 uppercase font-bold">Critical Risks</span>
            <div className="text-xl font-black text-red-400 font-mono mt-0.5">{stats.criticalIssues}</div>
          </div>
          <div className="p-3 bg-coal-950 rounded-lg text-center">
            <span className="text-[10px] text-slate-400 uppercase font-bold">Field Audits</span>
            <div className="text-xl font-black text-cyan-400 font-mono mt-0.5">{stats.inspectionsThisMonth}</div>
          </div>
        </div>
      </div>
    </div>
  );
};
"""

audit_trail = """import React, { useState } from 'react';
import { Lock, CheckCircle2, RefreshCw } from 'lucide-react';
import { useApp } from '../../context/AppContext';

export const AuditTrailPage: React.FC = () => {
  const { auditLogs } = useApp();
  const [verifying, setVerifying] = useState(false);

  const handleVerifyLedger = () => {
    setVerifying(true);
    setTimeout(() => {
      setVerifying(false);
    }, 1200);
  };

  return (
    <div className="space-y-6 pb-12">
      <div className="glass-panel p-5 rounded-2xl border border-slate-800 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2 text-xs text-emerald-400 font-bold uppercase tracking-wider">
            <Lock className="w-4 h-4 text-emerald-400" />
            <span>Cryptographic Digital Ledger</span>
          </div>
          <h1 className="text-2xl font-black text-white mt-1">Immutable Digital Audit Trail</h1>
          <p className="text-xs text-slate-400 mt-0.5">
            Every inspection, classification, assignment, and manager signoff is secured in a SHA-256 hash-chained block.
          </p>
        </div>

        <button
          onClick={handleVerifyLedger}
          disabled={verifying}
          className="flex items-center space-x-2 px-4 py-2.5 rounded-xl bg-coal-800 text-emerald-400 border border-emerald-500/40 text-xs font-bold hover:bg-coal-750 transition-all"
        >
          <RefreshCw className={`w-3.5 h-3.5 ${verifying ? 'animate-spin' : ''}`} />
          <span>{verifying ? 'Verifying Block Hashes...' : 'Verify Ledger Integrity'}</span>
        </button>
      </div>

      <div className="space-y-3">
        {auditLogs.map(log => (
          <div
            key={log.blockNumber}
            className="glass-panel p-4 rounded-xl border border-slate-800 space-y-2 hover:border-slate-700 transition-all font-mono"
          >
            <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between text-xs pb-2 border-b border-slate-800 gap-2">
              <div className="flex items-center space-x-2">
                <span className="bg-coal-950 text-safety-orange font-black px-2 py-0.5 rounded text-[11px] border border-safety-orange/30">
                  BLOCK #{log.blockNumber}
                </span>
                <span className="font-bold text-white text-xs">{log.action}</span>
                <span className="text-[10px] text-slate-400">({log.module})</span>
              </div>
              <div className="flex items-center space-x-2 text-[10px] text-slate-400">
                <span>{log.timestamp}</span>
                <span className="text-emerald-400 font-bold flex items-center space-x-1">
                  <CheckCircle2 className="w-3 h-3" />
                  <span>Verified</span>
                </span>
              </div>
            </div>

            <p className="text-xs text-slate-300 font-sans">{log.details}</p>

            <div className="pt-2 text-[10px] text-slate-400 space-y-0.5 bg-coal-950 p-2.5 rounded-lg border border-slate-800/80">
              <p className="truncate">Hash: <strong className="text-emerald-400">{log.blockHash}</strong></p>
              <p className="truncate">Prev: <span className="text-slate-500">{log.previousHash}</span></p>
              <p>Signer: <strong className="text-slate-200 font-sans">{log.user} ({log.role})</strong> • IP: {log.ipAddress}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

settings_page = """import React from 'react';
import { Settings } from 'lucide-react';
import { useAuth } from '../../context/AuthContext';
import { useLanguage } from '../../context/LanguageContext';

export const SettingsPage: React.FC = () => {
  const { currentUser } = useAuth();
  const { language, setLanguage } = useLanguage();

  return (
    <div className="max-w-4xl mx-auto space-y-6 pb-12">
      <div className="glass-panel p-5 rounded-2xl border border-slate-800">
        <div className="flex items-center space-x-2 text-xs text-slate-400 font-bold uppercase tracking-wider">
          <Settings className="w-4 h-4 text-slate-400" />
          <span>System Configuration</span>
        </div>
        <h1 className="text-2xl font-black text-white mt-1">Platform Settings</h1>
        <p className="text-xs text-slate-400 mt-0.5">
          User profile, escalation SLA timers, neural risk sensitivity thresholds, and language preferences.
        </p>
      </div>

      <div className="glass-panel p-5 rounded-xl border border-slate-800 space-y-4">
        <h3 className="text-sm font-extrabold text-white uppercase tracking-wider">Active User Profile</h3>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
          <div>
            <span className="text-slate-400">Full Name:</span>
            <p className="font-bold text-white mt-0.5">{currentUser.name}</p>
          </div>
          <div>
            <span className="text-slate-400">Designation & Role:</span>
            <p className="font-bold text-safety-orange mt-0.5">{currentUser.roleTitle}</p>
          </div>
          <div>
            <span className="text-slate-400">Official Email:</span>
            <p className="font-mono text-slate-200 mt-0.5">{currentUser.email}</p>
          </div>
          <div>
            <span className="text-slate-400">Department:</span>
            <p className="font-bold text-slate-200 mt-0.5">{currentUser.department}</p>
          </div>
        </div>
      </div>

      <div className="glass-panel p-5 rounded-xl border border-slate-800 space-y-4">
        <h3 className="text-sm font-extrabold text-white uppercase tracking-wider">Language & Regionalization</h3>
        <div className="flex items-center space-x-4">
          <button
            onClick={() => setLanguage('en')}
            className={`px-4 py-2 rounded-xl text-xs font-bold border transition-all ${
              language === 'en' ? 'bg-safety-orange text-white border-safety-orange' : 'bg-coal-800 text-slate-300 border-slate-700'
            }`}
          >
            English (Standard)
          </button>
          <button
            onClick={() => setLanguage('hi')}
            className={`px-4 py-2 rounded-xl text-xs font-bold border transition-all ${
              language === 'hi' ? 'bg-safety-orange text-white border-safety-orange' : 'bg-coal-800 text-slate-300 border-slate-700'
            }`}
          >
            हिंदी (Hindi)
          </button>
        </div>
      </div>
    </div>
  );
};
"""

with open('src/pages/Governance/AlertsEscalationsPage.tsx', 'w', encoding='utf-8') as f:
    f.write(alerts_escalations)

with open('src/pages/Governance/ManagementReportsPage.tsx', 'w', encoding='utf-8') as f:
    f.write(management_reports)

with open('src/pages/Governance/AuditTrailPage.tsx', 'w', encoding='utf-8') as f:
    f.write(audit_trail)

with open('src/pages/Settings/SettingsPage.tsx', 'w', encoding='utf-8') as f:
    f.write(settings_page)

print("Governance and Settings pages written successfully!")
