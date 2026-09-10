import React from 'react';
import {
  LayoutDashboard,
  ClipboardList,
  Flame,
  CheckCircle2,
  Bot
} from 'lucide-react';

interface BottomNavProps {
  activeTab: string;
  setActiveTab: (tab: string) => void;
}

export const BottomNav: React.FC<BottomNavProps> = ({ activeTab, setActiveTab }) => {
  const tabs = [
    { id: 'dashboard', label: 'Dashboard', icon: LayoutDashboard },
    { id: 'new-inspection', label: 'Inspection', icon: ClipboardList },
    { id: 'critical-issues', label: 'Critical SLAs', icon: Flame },
    { id: 'evidence-verification', label: 'Verify', icon: CheckCircle2 },
    { id: 'ai-copilot', label: 'Copilot', icon: Bot },
  ];

  return (
    <nav className="md:hidden fixed bottom-0 left-0 right-0 z-40 bg-[#0B2545] border-t border-[#0F3057] px-2 py-1.5 flex items-center justify-around shadow-gov-lg text-slate-300">
      {tabs.map(t => {
        const Icon = t.icon;
        const isActive = activeTab === t.id;
        return (
          <button
            key={t.id}
            onClick={() => setActiveTab(t.id)}
            className={`flex flex-col items-center justify-center p-1.5 rounded transition-all ${
              isActive ? 'text-amber-400 font-bold' : 'text-slate-400 hover:text-white'
            }`}
          >
            <Icon className="w-4 h-4 mb-0.5" />
            <span className="text-[10px]">{t.label}</span>
          </button>
        );
      })}
    </nav>
  );
};
