import os

top_header = """import React, { useState } from 'react';
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
"""

sidebar = """import React, { useState } from 'react';
import {
  LayoutDashboard,
  Pickaxe,
  MapPin,
  AlertTriangle,
  ShieldCheck,
  Calendar,
  FileCheck2,
  ClipboardList,
  History,
  ScanEye,
  CheckCircle2,
  Flame,
  Wrench,
  Sparkles,
  BrainCircuit,
  TrendingUp,
  Bot,
  RefreshCw,
  Share2,
  FolderOpen,
  FileText,
  ClockAlert,
  Users,
  HardHat,
  Bell,
  BarChart3,
  ScrollText,
  Settings,
  ChevronDown,
  ChevronRight,
  ShieldAlert,
  Activity,
  Leaf,
  Layers,
  UserCheck
} from 'lucide-react';
import { useAuth } from '../../context/AuthContext';
import { useApp } from '../../context/AppContext';

interface SidebarProps {
  activeTab: string;
  setActiveTab: (tab: string) => void;
  collapsed: boolean;
  setCollapsed: (collapsed: boolean) => void;
}

interface NavGroup {
  title: string;
  items: {
    id: string;
    label: string;
    icon: React.ElementType;
    badge?: number;
    badgeColor?: string;
  }[];
}

export const Sidebar: React.FC<SidebarProps> = ({
  activeTab,
  setActiveTab,
  collapsed,
  setCollapsed
}) => {
  const { currentUser } = useAuth();
  const { stats, issues } = useApp();
  const [openSections, setOpenSections] = useState<Record<string, boolean>>({
    'COMMAND CENTER': true,
    'MINE OPERATIONS': true,
    'COMPLIANCE MANAGEMENT': true,
    'INSPECTIONS': true,
    'ISSUES & ACTIONS': true,
    'AI INTELLIGENCE': true,
    'RECORDS & DOCUMENTS': false,
    'GOVERNANCE & AUDIT': false
  });

  const toggleSection = (title: string) => {
    setOpenSections(prev => ({ ...prev, [title]: !prev[title] }));
  };

  const navGroups: NavGroup[] = [
    {
      title: 'MINE OPERATIONS',
      items: [
        { id: 'mine-overview', label: 'Mine Overview', icon: Pickaxe },
        { id: 'gis-map', label: 'GIS Monitoring', icon: MapPin },
        { id: 'risk-zones', label: 'Risk Zones', icon: AlertTriangle }
      ]
    },
    {
      title: 'COMPLIANCE MANAGEMENT',
      items: [
        { id: 'compliance-tracker', label: 'Compliance Dashboard', icon: ShieldCheck, badge: 2, badgeColor: 'bg-amber-600' },
        { id: 'statutory-reqs', label: 'Statutory Requirements', icon: FileCheck2 },
        { id: 'compliance-calendar', label: 'Compliance Calendar', icon: Calendar },
        { id: 'statutory-reports', label: 'Statutory Reports', icon: FileText }
      ]
    },
    {
      title: 'INSPECTIONS',
      items: [
        { id: 'new-inspection', label: 'Field Inspection', icon: ClipboardList, badgeColor: 'bg-amber-600' },
        { id: 'inspection-history', label: 'Inspection History', icon: History },
        { id: 'ai-findings', label: 'AI Findings', icon: ScanEye }
      ]
    },
    {
      title: 'ISSUES & ACTIONS',
      items: [
        { id: 'all-issues', label: 'Open Issues', icon: AlertTriangle, badge: stats.openIssues },
        { id: 'critical-issues', label: 'Critical Issues', icon: Flame, badge: stats.criticalIssues, badgeColor: 'bg-red-700' },
        { id: 'corrective-actions', label: 'Corrective Actions', icon: Wrench },
        { id: 'evidence-verification', label: 'Evidence Verification', icon: CheckCircle2, badge: issues.filter(i => i.status === 'VERIFIED' || i.status === 'OPEN').length, badgeColor: 'bg-emerald-700' }
      ]
    },
    {
      title: 'AI INTELLIGENCE',
      items: [
        { id: 'ai-risk-analytics', label: 'Risk Analytics', icon: BrainCircuit },
        { id: 'ai-predictions', label: 'Predictions', icon: TrendingUp },
        { id: 'ai-copilot', label: 'Compliance Copilot', icon: Bot },
        { id: 'recurring-violations', label: 'Recurring Violations', icon: RefreshCw, badge: 4, badgeColor: 'bg-amber-600' },
        { id: 'cross-mine-learning', label: 'Cross-Mine Learning', icon: Share2 }
      ]
    },
    {
      title: 'RECORDS & DOCUMENTS',
      items: [
        { id: 'ocr-digitization', label: 'OCR Digitization', icon: ScanEye },
        { id: 'doc-repository', label: 'Document Repository', icon: FolderOpen },
        { id: 'expiring-documents', label: 'Expiring Documents', icon: ClockAlert, badge: 2, badgeColor: 'bg-red-700' }
      ]
    },
    {
      title: 'GOVERNANCE & AUDIT',
      items: [
        { id: 'contractor-dashboard', label: 'Contractors Hub', icon: HardHat },
        { id: 'contractor-compliance', label: 'Contractor Risk', icon: UserCheck },
        { id: 'environmental-monitoring', label: 'Environmental Telemetry', icon: Leaf },
        { id: 'labour-compliance', label: 'Labour Compliance', icon: Users },
        { id: 'production-monitoring', label: 'Production Monitoring', icon: Activity },
        { id: 'incident-management', label: 'Incident Reporting', icon: ShieldAlert },
        { id: 'alerts-escalations', label: 'Alerts & Escalations', icon: Bell, badge: 4, badgeColor: 'bg-red-700' },
        { id: 'management-reports', label: 'Management Reports', icon: BarChart3 },
        { id: 'audit-trail', label: 'Digital Audit Trail', icon: ScrollText },
        { id: 'settings', label: 'Settings', icon: Settings }
      ]
    }
  ];

  return (
    <aside className={`fixed top-0 left-0 bottom-0 z-40 bg-[#0B2545] text-slate-200 border-r border-[#07192F] transition-all duration-300 flex flex-col ${collapsed ? 'w-20' : 'w-72'}`}>
      <div className="h-16 flex items-center justify-between px-4 border-b border-[#0F3057] bg-[#06172D]">
        {!collapsed && (
          <div className="flex items-center space-x-3 cursor-pointer" onClick={() => setActiveTab('dashboard')}>
            <div className="w-8 h-8 rounded bg-[#134074] border border-slate-600 flex items-center justify-center text-white font-extrabold text-xs">
              CIL
            </div>
            <div>
              <h2 className="font-black text-sm tracking-wider text-white">MINEGUARD AI</h2>
              <p className="text-[10px] text-slate-300 font-medium">Smart Mining Governance</p>
            </div>
          </div>
        )}
        {collapsed && (
          <div className="mx-auto w-8 h-8 rounded bg-[#134074] border border-slate-600 flex items-center justify-center text-white font-extrabold text-xs cursor-pointer" onClick={() => setCollapsed(false)}>
            CIL
          </div>
        )}
      </div>

      <div className="flex-1 overflow-y-auto py-3 px-2 space-y-1">
        <button
          onClick={() => setActiveTab('landing')}
          className={`w-full flex items-center space-x-2.5 px-3 py-2 rounded text-xs font-bold transition-all ${
            activeTab === 'landing'
              ? 'bg-[#1D4E89] text-white'
              : 'text-slate-300 hover:text-white hover:bg-white/5'
          }`}
        >
          <Sparkles className="w-4 h-4 text-amber-400 shrink-0" />
          {!collapsed && <span>Portal & Institutional Overview</span>}
        </button>

        <button
          onClick={() => setActiveTab('dashboard')}
          className={`w-full flex items-center justify-between px-3 py-2 rounded text-xs font-bold transition-all ${
            activeTab === 'dashboard'
              ? 'bg-[#1D4E89] text-white border-l-4 border-amber-400 shadow-sm'
              : 'text-slate-300 hover:text-white hover:bg-white/5'
          }`}
        >
          <div className="flex items-center space-x-2.5">
            <LayoutDashboard className="w-4 h-4 shrink-0 text-amber-400" />
            {!collapsed && <span>Dashboard Overview</span>}
          </div>
        </button>

        <div className="py-1">
          <div className="h-[1px] bg-slate-700/60 mx-2" />
        </div>

        {navGroups.map(group => (
          <div key={group.title} className="pt-1">
            {!collapsed && (
              <button
                onClick={() => toggleSection(group.title)}
                className="w-full flex items-center justify-between px-3 py-1.5 text-[10px] font-extrabold uppercase tracking-widest text-slate-400 hover:text-slate-200"
              >
                <span>{group.title}</span>
                {openSections[group.title] ? <ChevronDown className="w-3 h-3" /> : <ChevronRight className="w-3 h-3" />}
              </button>
            )}

            {(collapsed || openSections[group.title]) && (
              <div className="space-y-0.5 mt-0.5">
                {group.items.map(item => {
                  const Icon = item.icon;
                  const isActive = activeTab === item.id;
                  return (
                    <button
                      key={item.id}
                      onClick={() => setActiveTab(item.id)}
                      title={collapsed ? item.label : undefined}
                      className={`w-full flex items-center justify-between px-3 py-1.5 rounded text-xs font-medium transition-all ${
                        isActive
                          ? 'bg-[#1D4E89] text-white font-bold border-l-3 border-amber-400'
                          : 'text-slate-300 hover:text-white hover:bg-white/5'
                      }`}
                    >
                      <div className="flex items-center space-x-2.5">
                        <Icon className={`w-3.5 h-3.5 shrink-0 ${isActive ? 'text-amber-400' : 'text-slate-400'}`} />
                        {!collapsed && <span className="truncate">{item.label}</span>}
                      </div>
                      {!collapsed && item.badge !== undefined && (
                        <span className={`text-[9px] font-bold px-1.5 py-0.2 rounded text-white ${item.badgeColor || 'bg-slate-700'}`}>
                          {item.badge}
                        </span>
                      )}
                    </button>
                  );
                })}
              </div>
            )}
          </div>
        ))}
      </div>

      <div className="p-3 border-t border-[#0F3057] bg-[#06172D] text-xs">
        {!collapsed ? (
          <div className="flex items-center space-x-2.5">
            <div className="w-7 h-7 rounded bg-[#134074] border border-slate-600 flex items-center justify-center font-bold text-[11px] text-white">
              {currentUser.name.charAt(0)}
            </div>
            <div className="overflow-hidden">
              <p className="font-bold text-white truncate text-xs">{currentUser.name}</p>
              <p className="text-[10px] text-slate-400 truncate">{currentUser.roleTitle}</p>
            </div>
          </div>
        ) : (
          <div className="w-7 h-7 mx-auto rounded bg-[#134074] border border-slate-600 flex items-center justify-center font-bold text-[11px] text-white">
            {currentUser.name.charAt(0)}
          </div>
        )}
      </div>
    </aside>
  );
};
"""

with open('src/components/layout/TopHeader.tsx', 'w', encoding='utf-8') as f:
    f.write(top_header)

with open('src/components/layout/Sidebar.tsx', 'w', encoding='utf-8') as f:
    f.write(sidebar)

print("Part 1b-nav: TopHeader and Sidebar written successfully!")
