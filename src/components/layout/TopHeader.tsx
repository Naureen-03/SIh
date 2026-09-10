import React, { useState } from 'react';
import {
  Bell,
  Globe,
  Radio,
  Menu,
  ChevronDown,
  CheckCircle2,
  RefreshCw,
  UserCheck,
  Award,
  HelpCircle,
  Building2,
  FileCheck2
} from 'lucide-react';
import { useAuth } from '../../context/AuthContext';
import { useLanguage } from '../../context/LanguageContext';
import { useApp } from '../../context/AppContext';

interface TopHeaderProps {
  sidebarCollapsed: boolean;
  setSidebarCollapsed: (c: boolean) => void;
  onOpenHeroDemo: () => void;
  setActiveTab: (tab: string) => void;
}

export const TopHeader: React.FC<TopHeaderProps> = ({
  sidebarCollapsed,
  setSidebarCollapsed,
  onOpenHeroDemo,
  setActiveTab
}) => {
  const { currentUser, switchRole, availableRoles } = useAuth();
  const { language, setLanguage, t } = useLanguage();
  const { offlineQueueCount, syncOfflineQueue, notifications, markNotificationRead } = useApp();
  const [showRoleModal, setShowRoleModal] = useState(false);
  const [showNotifModal, setShowNotifModal] = useState(false);
  const [syncing, setSyncing] = useState(false);

  const unreadNotifs = notifications.filter(n => !n.read);

  const handleSync = () => {
    setSyncing(true);
    setTimeout(() => {
      syncOfflineQueue();
      setSyncing(false);
    }, 1000);
  };

  return (
    <header className={`fixed top-0 right-0 z-30 bg-white border-b border-slate-200 shadow-sm transition-all duration-300 ${sidebarCollapsed ? 'left-20' : 'left-72'}`}>
      <div className="gov-tricolor-strip" />

      <div className="h-16 px-4 lg:px-6 flex items-center justify-between">
        <div className="flex items-center space-x-3.5">
          <button
            onClick={() => setSidebarCollapsed(!sidebarCollapsed)}
            className="p-1.5 rounded bg-slate-100 text-slate-700 hover:bg-slate-200 border border-slate-300 transition-colors"
            title="Toggle Navigation Menu"
          >
            <Menu className="w-5 h-5" />
          </button>

          <div className="flex items-center space-x-3">
            <div className="w-9 h-9 rounded bg-[#0B2545] border border-slate-300 flex flex-col items-center justify-center text-white shadow-xs">
              <span className="text-[10px] font-extrabold tracking-tighter leading-none">GOI</span>
              <span className="text-[7px] text-amber-400 font-bold uppercase leading-none mt-0.5">Coal</span>
            </div>

            <div>
              <div className="flex items-center space-x-2">
                <span className="text-[11px] font-extrabold text-[#0B2545] uppercase tracking-wider">
                  Ministry of Coal
                </span>
                <span className="text-[10px] text-slate-500 font-medium">| Government of India</span>
              </div>
              <div className="flex items-center space-x-2">
                <span className="text-xs font-black text-slate-900 tracking-tight">
                  MINEGUARD AI
                </span>
                <span className="text-[9px] bg-slate-100 text-slate-700 font-semibold px-1.5 py-0.2 rounded border border-slate-300">
                  SIH 2026 Prototype
                </span>
              </div>
            </div>
          </div>
        </div>

        <div className="flex items-center space-x-2.5 sm:space-x-3">
          <div className="hidden lg:flex items-center space-x-1.5 bg-emerald-50 text-emerald-800 border border-emerald-300 px-2.5 py-1 rounded text-[11px] font-bold font-mono">
            <span className="w-2 h-2 rounded-full bg-emerald-600 animate-pulse" />
            <span>LIVE SYNC</span>
          </div>

          <button
            onClick={onOpenHeroDemo}
            className="gov-btn-primary text-xs"
            title="Launch the 17-Step Closed-Loop Governance Tour"
          >
            <Award className="w-3.5 h-3.5 text-amber-400" />
            <span className="hidden sm:inline">SIH 2026 Hero Demo</span>
            <span className="sm:hidden">Demo</span>
          </button>

          {offlineQueueCount > 0 && (
            <button
              onClick={handleSync}
              disabled={syncing}
              className="flex items-center space-x-1.5 bg-amber-50 border border-amber-300 text-amber-900 text-xs px-2.5 py-1.5 rounded hover:bg-amber-100 font-semibold transition-all"
              title="Sync field inspection drafts"
            >
              <RefreshCw className={`w-3.5 h-3.5 ${syncing ? 'animate-spin' : ''}`} />
              <span className="hidden md:inline font-mono">{offlineQueueCount} Drafts</span>
            </button>
          )}

          <button
            onClick={() => setLanguage(language === 'en' ? 'hi' : 'en')}
            className="flex items-center space-x-1 px-2.5 py-1.5 rounded border border-slate-300 bg-slate-50 hover:bg-slate-100 text-xs font-bold text-slate-800"
          >
            <Globe className="w-3.5 h-3.5 text-[#0B2545]" />
            <span>{language === 'en' ? 'English' : 'हिन्दी'}</span>
          </button>

          <div className="relative">
            <button
              onClick={() => setShowNotifModal(!showNotifModal)}
              className="relative p-2 rounded border border-slate-300 bg-slate-50 hover:bg-slate-100 text-slate-700"
              title="Official Alert Center"
            >
              <Bell className="w-4 h-4" />
              {unreadNotifs.length > 0 && (
                <span className="absolute -top-1 -right-1 w-4 h-4 rounded-full bg-red-700 text-white text-[9px] font-bold flex items-center justify-center">
                  {unreadNotifs.length}
                </span>
              )}
            </button>

            {showNotifModal && (
              <div className="absolute right-0 mt-2 w-80 sm:w-96 bg-white border border-slate-300 rounded-lg shadow-gov-lg z-50 p-3 animate-fade-in text-xs">
                <div className="flex items-center justify-between pb-2 border-b border-slate-200">
                  <span className="font-extrabold text-slate-800 uppercase tracking-wider text-[11px]">
                    Official Notification Center
                  </span>
                  <span className="bg-red-50 text-red-800 border border-red-200 font-bold px-2 py-0.5 rounded text-[10px]">
                    {unreadNotifs.length} Critical
                  </span>
                </div>
                <div className="space-y-2 mt-2 max-h-72 overflow-y-auto">
                  {notifications.map(n => (
                    <div
                      key={n.id}
                      onClick={() => { markNotificationRead(n.id); setShowNotifModal(false); setActiveTab('alerts-escalations'); }}
                      className={`p-2.5 rounded border cursor-pointer transition-all ${
                        n.severity === 'Critical' ? 'bg-red-50/70 border-red-300' : 'bg-slate-50 border-slate-200 hover:bg-slate-100'
                      }`}
                    >
                      <div className="flex items-center justify-between">
                        <span className={`text-[9px] font-extrabold px-1.5 py-0.2 rounded ${
                          n.severity === 'Critical' ? 'bg-red-700 text-white' : 'bg-amber-600 text-white'
                        }`}>
                          {n.severity}
                        </span>
                        <span className="text-[10px] text-slate-500 font-mono">{n.timestamp}</span>
                      </div>
                      <p className="font-bold text-slate-900 mt-1">{n.title}</p>
                      <p className="text-[11px] text-slate-600 mt-0.5 line-clamp-2">{n.message}</p>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>

          <div className="relative">
            <button
              onClick={() => setShowRoleModal(!showRoleModal)}
              className="flex items-center space-x-2 bg-slate-50 hover:bg-slate-100 text-slate-900 px-3 py-1.5 rounded border border-slate-300 text-xs font-semibold transition-all"
            >
              <UserCheck className="w-3.5 h-3.5 text-[#0B2545]" />
              <span className="max-w-[120px] sm:max-w-[170px] truncate">
                {currentUser.name} ({currentUser.role.replace('_', ' ')})
              </span>
              <ChevronDown className="w-3.5 h-3.5 text-slate-500" />
            </button>

            {showRoleModal && (
              <div className="absolute right-0 mt-2 w-72 bg-white border border-slate-300 rounded-lg shadow-gov-lg z-50 p-2 animate-fade-in text-xs">
                <div className="px-2 py-1 text-[10px] font-bold uppercase tracking-wider text-slate-500 border-b border-slate-200 mb-1">
                  Select User Perspective (6 Roles)
                </div>
                <div className="space-y-1">
                  {availableRoles.map(item => (
                    <button
                      key={item.role}
                      onClick={() => { switchRole(item.role); setShowRoleModal(false); }}
                      className={`w-full text-left p-2 rounded text-xs transition-all flex items-center justify-between ${
                        currentUser.role === item.role
                          ? 'bg-[#0B2545]/10 border border-[#0B2545]/30 text-[#0B2545] font-bold'
                          : 'text-slate-700 hover:bg-slate-100'
                      }`}
                    >
                      <div>
                        <p className="font-bold text-slate-900">{item.title}</p>
                        <p className="text-[10px] text-slate-500">{item.desc}</p>
                      </div>
                      {currentUser.role === item.role && <CheckCircle2 className="w-4 h-4 text-[#0B2545]" />}
                    </button>
                  ))}
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </header>
  );
};
