import React from 'react';
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
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-amber-800 font-extrabold uppercase tracking-wider">
          <Bell className="w-4 h-4 text-amber-700" />
          <span>SLA Countdown & 4-Tier Hierarchy</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Alerts & Escalation Center</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Automated escalation timeline notifying responsible officers, department heads, mine managers, and corporate leadership.
        </p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
        {escalationTiers.map((t, idx) => (
          <div key={idx} className="gov-card p-3.5 space-y-1.5 border-t-4 border-t-[#0B2545]">
            <span className="text-[10px] font-extrabold text-[#0B2545] uppercase font-mono">{t.level}</span>
            <h4 className="text-xs font-bold text-slate-900">{t.target}</h4>
            <p className="text-[11px] text-slate-600">{t.action}</p>
          </div>
        ))}
      </div>

      <div className="space-y-3">
        {notifications.map(n => (
          <div
            key={n.id}
            className={`gov-card p-4 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 ${
              n.severity === 'Critical' ? 'border-l-4 border-l-red-700 bg-red-50/20' : 'border-slate-200'
            }`}
          >
            <div className="space-y-1">
              <div className="flex items-center space-x-2">
                <span className={`text-[10px] font-bold px-2 py-0.5 rounded ${
                  n.severity === 'Critical' ? 'bg-red-700 text-white' : 'bg-amber-600 text-white'
                }`}>
                  {n.severity}
                </span>
                <h3 className="text-xs font-bold text-slate-900">{n.title}</h3>
              </div>
              <p className="text-xs text-slate-700">{n.message}</p>
              <span className="text-[10px] text-slate-500 font-mono">{n.timestamp}</span>
            </div>

            <button
              onClick={() => markNotificationRead(n.id)}
              className="gov-btn-secondary text-xs py-1 px-3 self-end sm:self-center"
            >
              {n.read ? 'Acknowledged' : 'Acknowledge & Dismiss'}
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
