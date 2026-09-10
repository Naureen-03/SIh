import os

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
  Radio,
  Layers,
  Leaf,
  Activity,
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
    'Mine Operations': true,
    'Compliance': true,
    'Inspections': true,
    'Issues & Corrective Actions': true,
    'AI Intelligence': true,
    'Documents': false,
    'Contractors': false,
    'Operational': false
  });

  const toggleSection = (title: string) => {
    setOpenSections(prev => ({ ...prev, [title]: !prev[title] }));
  };

  const navGroups: NavGroup[] = [
    {
      title: 'Mine Operations',
      items: [
        { id: 'mine-overview', label: 'Mine Overview', icon: Pickaxe },
        { id: 'gis-map', label: 'GIS Smart Map', icon: MapPin },
        { id: 'risk-zones', label: 'Risk Zones', icon: AlertTriangle }
      ]
    },
    {
      title: 'Compliance',
      items: [
        { id: 'compliance-tracker', label: 'Compliance Tracker', icon: ShieldCheck, badge: 2, badgeColor: 'bg-amber-500' },
        { id: 'statutory-reqs', label: 'Statutory Reqs', icon: FileCheck2 },
        { id: 'compliance-calendar', label: 'Compliance Calendar', icon: Calendar },
        { id: 'statutory-reports', label: 'Statutory Reports', icon: FileText }
      ]
    },
    {
      title: 'Inspections',
      items: [
        { id: 'new-inspection', label: 'New AI Inspection', icon: ClipboardList, badgeColor: 'bg-safety-orange' },
        { id: 'inspection-history', label: 'Inspection History', icon: History },
        { id: 'ai-findings', label: 'AI Findings', icon: ScanEye }
      ]
    },
    {
      title: 'Issues & Corrective Actions',
      items: [
        { id: 'all-issues', label: 'All Issues', icon: AlertTriangle, badge: stats.openIssues },
        { id: 'critical-issues', label: 'Critical Issues', icon: Flame, badge: stats.criticalIssues, badgeColor: 'bg-red-500 animate-pulse' },
        { id: 'corrective-actions', label: 'Corrective Actions', icon: Wrench },
        { id: 'evidence-verification', label: 'AI Verification', icon: CheckCircle2, badge: issues.filter(i => i.status === 'VERIFIED' || i.status === 'OPEN').length, badgeColor: 'bg-emerald-500' }
      ]
    },
    {
      title: 'AI Intelligence',
      items: [
        { id: 'ai-risk-analytics', label: 'AI Risk Analytics', icon: BrainCircuit },
        { id: 'ai-predictions', label: 'AI Predictions', icon: TrendingUp },
        { id: 'ai-copilot', label: 'MineGuard Copilot', icon: Bot, badgeColor: 'bg-blue-500' },
        { id: 'recurring-violations', label: 'Recurring Violations', icon: RefreshCw, badge: 4, badgeColor: 'bg-amber-500' },
        { id: 'cross-mine-learning', label: 'Cross-Mine Learning', icon: Share2 }
      ]
    },
    {
      title: 'Documents',
      items: [
        { id: 'doc-repository', label: 'Document Vault', icon: FolderOpen },
        { id: 'ocr-digitization', label: 'AI OCR Scanner', icon: ScanEye },
        { id: 'expiring-documents', label: 'Expiring Documents', icon: ClockAlert, badge: 2, badgeColor: 'bg-red-500' }
      ]
    },
    {
      title: 'Contractors',
      items: [
        { id: 'contractor-dashboard', label: 'Contractor Hub', icon: HardHat },
        { id: 'contractor-compliance', label: 'Contractor Risk', icon: UserCheck }
      ]
    },
    {
      title: 'Operational Governance',
      items: [
        { id: 'production-monitoring', label: 'Production Monitoring', icon: Activity },
        { id: 'environmental-monitoring', label: 'Environmental Telemetry', icon: Leaf },
        { id: 'labour-compliance', label: 'Labour Compliance', icon: Users },
        { id: 'incident-management', label: 'Incident Management', icon: ShieldAlert }
      ]
    }
  ];

  return (
    <aside className={`fixed top-0 left-0 bottom-0 z-40 bg-coal-900 border-r border-slate-800 transition-all duration-300 flex flex-col ${collapsed ? 'w-20' : 'w-72'}`}>
      {/* Brand Header */}
      <div className="h-16 flex items-center justify-between px-4 border-b border-slate-800 bg-coal-950/80">
        {!collapsed && (
          <div className="flex items-center space-x-3 cursor-pointer" onClick={() => setActiveTab('dashboard')}>
            <div className="w-10 h-10 rounded-lg bg-gradient-to-br from-safety-orange to-amber-600 flex items-center justify-center shadow-lg shadow-safety-orange/20">
              <Pickaxe className="w-6 h-6 text-white" />
            </div>
            <div>
              <div className="flex items-center space-x-1.5">
                <span className="font-extrabold text-base tracking-wider text-white">MINEGUARD</span>
                <span className="text-xs px-1.5 py-0.5 rounded bg-safety-orange/20 text-safety-orange font-mono font-bold">AI</span>
              </div>
              <p className="text-[10px] text-slate-400 font-medium">Ministry of Coal • CIL</p>
            </div>
          </div>
        )}
        {collapsed && (
          <div className="mx-auto w-10 h-10 rounded-lg bg-gradient-to-br from-safety-orange to-amber-600 flex items-center justify-center cursor-pointer" onClick={() => setCollapsed(false)}>
            <Pickaxe className="w-6 h-6 text-white" />
          </div>
        )}
      </div>

      {/* Navigation Links */}
      <div className="flex-1 overflow-y-auto py-3 px-2.5 space-y-1">
        {/* Landing Portal Button */}
        <button
          onClick={() => setActiveTab('landing')}
          className={`w-full flex items-center space-x-3 px-3 py-2.5 rounded-lg text-xs font-semibold transition-all ${
            activeTab === 'landing'
              ? 'bg-coal-800 text-safety-orange border border-safety-orange/30'
              : 'text-slate-400 hover:text-white hover:bg-coal-800/60'
          }`}
        >
          <Sparkles className="w-4 h-4 text-safety-orange shrink-0" />
          {!collapsed && <span>Public Portal & Vision</span>}
        </button>

        {/* Dashboard Link */}
        <button
          onClick={() => setActiveTab('dashboard')}
          className={`w-full flex items-center justify-between px-3 py-2.5 rounded-lg text-xs font-semibold transition-all ${
            activeTab === 'dashboard'
              ? 'bg-gradient-to-r from-safety-orange/20 to-transparent text-safety-orange border-l-4 border-safety-orange'
              : 'text-slate-300 hover:text-white hover:bg-coal-800/50'
          }`}
        >
          <div className="flex items-center space-x-3">
            <LayoutDashboard className="w-4 h-4 shrink-0" />
            {!collapsed && <span>Dashboard Overview</span>}
          </div>
        </button>

        <div className="pt-2 pb-1">
          <div className="h-[1px] bg-slate-800 mx-2" />
        </div>

        {/* Grouped Navigation */}
        {navGroups.map(group => (
          <div key={group.title} className="pt-1">
            {!collapsed && (
              <button
                onClick={() => toggleSection(group.title)}
                className="w-full flex items-center justify-between px-3 py-1.5 text-[11px] font-bold uppercase tracking-wider text-slate-400 hover:text-slate-200"
              >
                <span>{group.title}</span>
                {openSections[group.title] ? <ChevronDown className="w-3.5 h-3.5" /> : <ChevronRight className="w-3.5 h-3.5" />}
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
                      className={`w-full flex items-center justify-between px-3 py-2 rounded-lg text-xs font-medium transition-all ${
                        isActive
                          ? 'bg-coal-800 text-white font-semibold border-l-2 border-safety-orange shadow-sm'
                          : 'text-slate-400 hover:text-slate-200 hover:bg-coal-800/40'
                      }`}
                    >
                      <div className="flex items-center space-x-3">
                        <Icon className={`w-4 h-4 shrink-0 ${isActive ? 'text-safety-orange' : 'text-slate-400'}`} />
                        {!collapsed && <span className="truncate">{item.label}</span>}
                      </div>
                      {!collapsed && item.badge !== undefined && (
                        <span className={`text-[10px] font-bold px-1.5 py-0.2 rounded-full text-white ${item.badgeColor || 'bg-slate-700'}`}>
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

        <div className="pt-2 pb-1">
          <div className="h-[1px] bg-slate-800 mx-2" />
        </div>

        {/* Global Governance Modules */}
        <button
          onClick={() => setActiveTab('alerts-escalations')}
          className={`w-full flex items-center justify-between px-3 py-2 rounded-lg text-xs font-medium ${
            activeTab === 'alerts-escalations' ? 'bg-coal-800 text-white border-l-2 border-safety-orange' : 'text-slate-400 hover:text-slate-200 hover:bg-coal-800/40'
          }`}
        >
          <div className="flex items-center space-x-3">
            <Bell className="w-4 h-4 text-amber-500 shrink-0" />
            {!collapsed && <span>Alerts & Escalations</span>}
          </div>
          {!collapsed && <span className="text-[10px] font-bold px-1.5 rounded-full bg-red-500 text-white">4</span>}
        </button>

        <button
          onClick={() => setActiveTab('management-reports')}
          className={`w-full flex items-center space-x-3 px-3 py-2 rounded-lg text-xs font-medium ${
            activeTab === 'management-reports' ? 'bg-coal-800 text-white border-l-2 border-safety-orange' : 'text-slate-400 hover:text-slate-200 hover:bg-coal-800/40'
          }`}
        >
          <BarChart3 className="w-4 h-4 text-cyan-400 shrink-0" />
          {!collapsed && <span>Management Reports</span>}
        </button>

        <button
          onClick={() => setActiveTab('audit-trail')}
          className={`w-full flex items-center space-x-3 px-3 py-2 rounded-lg text-xs font-medium ${
            activeTab === 'audit-trail' ? 'bg-coal-800 text-white border-l-2 border-safety-orange' : 'text-slate-400 hover:text-slate-200 hover:bg-coal-800/40'
          }`}
        >
          <ScrollText className="w-4 h-4 text-emerald-400 shrink-0" />
          {!collapsed && <span>Digital Audit Trail</span>}
        </button>

        <button
          onClick={() => setActiveTab('settings')}
          className={`w-full flex items-center space-x-3 px-3 py-2 rounded-lg text-xs font-medium ${
            activeTab === 'settings' ? 'bg-coal-800 text-white border-l-2 border-safety-orange' : 'text-slate-400 hover:text-slate-200 hover:bg-coal-800/40'
          }`}
        >
          <Settings className="w-4 h-4 text-slate-400 shrink-0" />
          {!collapsed && <span>Settings & Rules</span>}
        </button>
      </div>

      {/* User Role Card */}
      <div className="p-3 border-t border-slate-800 bg-coal-950/90">
        {!collapsed ? (
          <div className="flex items-center space-x-3">
            <div className="w-8 h-8 rounded-full bg-safety-orange/20 border border-safety-orange/40 flex items-center justify-center font-bold text-xs text-safety-orange">
              {currentUser.name.charAt(0)}
            </div>
            <div className="overflow-hidden">
              <p className="text-xs font-bold text-white truncate">{currentUser.name}</p>
              <p className="text-[10px] text-slate-400 truncate">{currentUser.roleTitle}</p>
            </div>
          </div>
        ) : (
          <div className="w-8 h-8 mx-auto rounded-full bg-safety-orange/20 border border-safety-orange/40 flex items-center justify-center font-bold text-xs text-safety-orange">
            {currentUser.name.charAt(0)}
          </div>
        )}
      </div>
    </aside>
  );
};
"""

top_header = """import React, { useState } from 'react';
import {
  Bell,
  Search,
  Globe,
  HardHat,
  Radio,
  Sparkles,
  Menu,
  ChevronDown,
  CheckCircle2,
  RefreshCw,
  AlertOctagon,
  UserCheck
} from 'lucide-react';
import { useAuth } from '../../context/AuthContext';
import { useLanguage } from '../../context/LanguageContext';
import { useApp } from '../../context/AppContext';
import { UserRole } from '../../types';

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
    }, 1200);
  };

  return (
    <header className={`h-16 fixed top-0 right-0 z-30 bg-coal-900/95 backdrop-blur-md border-b border-slate-800 transition-all duration-300 flex items-center justify-between px-4 lg:px-6 ${sidebarCollapsed ? 'left-20' : 'left-72'}`}>
      {/* Left Section: Collapse button & Mine Badge */}
      <div className="flex items-center space-x-4">
        <button
          onClick={() => setSidebarCollapsed(!sidebarCollapsed)}
          className="p-1.5 rounded-lg bg-coal-800 text-slate-400 hover:text-white transition-colors"
        >
          <Menu className="w-5 h-5" />
        </button>

        <div className="hidden sm:flex items-center space-x-2 bg-coal-800/80 px-3 py-1.5 rounded-lg border border-slate-700/60">
          <div className="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse" />
          <span className="text-xs font-bold text-white tracking-wide">SECL • Gevra Mega Mine</span>
          <span className="text-[10px] bg-coal-950 px-2 py-0.5 rounded text-slate-400 font-mono">Korba Area</span>
        </div>

        <div className="hidden lg:flex items-center space-x-1.5 text-xs text-slate-400">
          <Radio className="w-3.5 h-3.5 text-emerald-400" />
          <span>Sync: 2m ago</span>
        </div>
      </div>

      {/* Right Section: Actions, Roles, Notifications */}
      <div className="flex items-center space-x-2.5 sm:space-x-3">
        {/* SIH Hero Demo Tour Button */}
        <button
          onClick={onOpenHeroDemo}
          className="flex items-center space-x-1.5 bg-gradient-to-r from-safety-orange to-amber-500 hover:from-safety-orange/90 hover:to-amber-500/90 text-white font-bold text-xs px-3.5 py-1.5 rounded-lg shadow-md shadow-safety-orange/20 transition-all transform hover:scale-105"
        >
          <Sparkles className="w-3.5 h-3.5 animate-spin" />
          <span className="hidden sm:inline">SIH Hero Demo (17 Steps)</span>
          <span className="sm:hidden">Demo</span>
        </button>

        {/* Offline Sync Indicator */}
        {offlineQueueCount > 0 && (
          <button
            onClick={handleSync}
            disabled={syncing}
            className="flex items-center space-x-1.5 bg-amber-500/15 border border-amber-500/30 text-amber-400 text-xs px-2.5 py-1.5 rounded-lg hover:bg-amber-500/25 transition-all"
            title="Offline queue pending synchronization"
          >
            <RefreshCw className={`w-3.5 h-3.5 ${syncing ? 'animate-spin' : ''}`} />
            <span className="hidden md:inline font-mono font-bold">{offlineQueueCount} Drafts</span>
          </button>
        )}

        {/* Multilingual Selector */}
        <button
          onClick={() => setLanguage(language === 'en' ? 'hi' : 'en')}
          className="flex items-center space-x-1.5 bg-coal-800 text-slate-300 hover:text-white px-2.5 py-1.5 rounded-lg text-xs border border-slate-700/60"
        >
          <Globe className="w-3.5 h-3.5 text-safety-cyan" />
          <span className="font-bold">{language === 'en' ? 'ENG' : 'हिंदी'}</span>
        </button>

        {/* Notification Bell */}
        <div className="relative">
          <button
            onClick={() => setShowNotifModal(!showNotifModal)}
            className="relative p-2 rounded-lg bg-coal-800 text-slate-300 hover:text-white border border-slate-700/60"
          >
            <Bell className="w-4 h-4" />
            {unreadNotifs.length > 0 && (
              <span className="absolute -top-1 -right-1 w-4 h-4 rounded-full bg-red-500 text-white text-[10px] font-bold flex items-center justify-center">
                {unreadNotifs.length}
              </span>
            )}
          </button>

          {/* Notifications Dropdown */}
          {showNotifModal && (
            <div className="absolute right-0 mt-2 w-80 sm:w-96 bg-coal-900 border border-slate-700 rounded-xl shadow-2xl z-50 p-3 animate-fade-in">
              <div className="flex items-center justify-between pb-2 border-b border-slate-800">
                <span className="text-xs font-bold text-white uppercase tracking-wider">Alert Center</span>
                <span className="text-[10px] bg-red-500/20 text-red-400 font-bold px-2 py-0.5 rounded">
                  {unreadNotifs.length} Critical / Urgent
                </span>
              </div>
              <div className="space-y-2 mt-2 max-h-72 overflow-y-auto">
                {notifications.map(n => (
                  <div
                    key={n.id}
                    onClick={() => { markNotificationRead(n.id); setShowNotifModal(false); setActiveTab('alerts-escalations'); }}
                    className={`p-2.5 rounded-lg border cursor-pointer transition-all ${
                      n.severity === 'Critical' ? 'bg-red-500/10 border-red-500/30' : 'bg-coal-800/80 border-slate-700'
                    }`}
                  >
                    <div className="flex items-center justify-between">
                      <span className={`text-[10px] font-bold px-1.5 py-0.2 rounded ${
                        n.severity === 'Critical' ? 'bg-red-500 text-white' : 'bg-amber-500 text-black'
                      }`}>
                        {n.severity}
                      </span>
                      <span className="text-[10px] text-slate-400">{n.timestamp}</span>
                    </div>
                    <p className="text-xs font-bold text-white mt-1">{n.title}</p>
                    <p className="text-[11px] text-slate-300 mt-0.5 line-clamp-2">{n.message}</p>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>

        {/* Role Switcher Pill */}
        <div className="relative">
          <button
            onClick={() => setShowRoleModal(!showRoleModal)}
            className="flex items-center space-x-2 bg-coal-800 hover:bg-coal-750 text-white px-3 py-1.5 rounded-lg border border-slate-700 text-xs font-semibold transition-all"
          >
            <UserCheck className="w-3.5 h-3.5 text-safety-orange" />
            <span className="max-w-[110px] sm:max-w-[150px] truncate">{currentUser.roleTitle.split(' ')[0]} ({currentUser.role.replace('_', ' ')})</span>
            <ChevronDown className="w-3.5 h-3.5 text-slate-400" />
          </button>

          {/* Role Dropdown */}
          {showRoleModal && (
            <div className="absolute right-0 mt-2 w-72 bg-coal-900 border border-slate-700 rounded-xl shadow-2xl z-50 p-2 animate-fade-in">
              <div className="px-2 py-1 text-[10px] font-bold uppercase tracking-wider text-slate-400 border-b border-slate-800 mb-1">
                Switch Perspective (6 Roles)
              </div>
              <div className="space-y-1">
                {availableRoles.map(item => (
                  <button
                    key={item.role}
                    onClick={() => { switchRole(item.role); setShowRoleModal(false); }}
                    className={`w-full text-left p-2 rounded-lg text-xs transition-all flex items-center justify-between ${
                      currentUser.role === item.role
                        ? 'bg-safety-orange/15 border border-safety-orange/40 text-white font-bold'
                        : 'text-slate-300 hover:bg-coal-800'
                    }`}
                  >
                    <div>
                      <p className="font-bold text-white">{item.title}</p>
                      <p className="text-[10px] text-slate-400">{item.desc}</p>
                    </div>
                    {currentUser.role === item.role && <CheckCircle2 className="w-4 h-4 text-safety-orange" />}
                  </button>
                ))}
              </div>
            </div>
          )}
        </div>
      </div>
    </header>
  );
};
"""

bottom_nav = """import React from 'react';
import {
  LayoutDashboard,
  ClipboardList,
  Flame,
  Bot,
  Bell
} from 'lucide-react';
import { useApp } from '../../context/AppContext';

interface BottomNavProps {
  activeTab: string;
  setActiveTab: (tab: string) => void;
}

export const BottomNav: React.FC<BottomNavProps> = ({ activeTab, setActiveTab }) => {
  const { stats } = useApp();

  const items = [
    { id: 'dashboard', label: 'Dashboard', icon: LayoutDashboard },
    { id: 'new-inspection', label: 'Inspect', icon: ClipboardList, highlight: true },
    { id: 'critical-issues', label: 'Critical', icon: Flame, badge: stats.criticalIssues },
    { id: 'ai-copilot', label: 'Copilot', icon: Bot },
    { id: 'alerts-escalations', label: 'Alerts', icon: Bell }
  ];

  return (
    <nav className="md:hidden fixed bottom-0 left-0 right-0 z-40 bg-coal-950/95 backdrop-blur-lg border-t border-slate-800 px-2 py-1.5 flex items-center justify-around">
      {items.map(item => {
        const Icon = item.icon;
        const isActive = activeTab === item.id;
        return (
          <button
            key={item.id}
            onClick={() => setActiveTab(item.id)}
            className={`flex flex-col items-center justify-center py-1 px-3 rounded-lg relative transition-all ${
              item.highlight
                ? 'text-safety-orange -mt-3 bg-coal-900 border border-safety-orange/40 rounded-full p-2.5 shadow-lg shadow-safety-orange/20'
                : isActive
                ? 'text-safety-orange font-bold'
                : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            <Icon className="w-5 h-5" />
            <span className="text-[10px] mt-0.5 font-medium">{item.label}</span>
            {item.badge !== undefined && item.badge > 0 && (
              <span className="absolute top-0 right-2 w-4 h-4 bg-red-500 text-white rounded-full text-[9px] font-bold flex items-center justify-center animate-pulse">
                {item.badge}
              </span>
            )}
          </button>
        );
      })}
    </nav>
  );
};
"""

closed_loop = """import React from 'react';
import {
  Scan,
  Cpu,
  Flame,
  UserCheck,
  Wrench,
  CheckCircle2,
  BrainCircuit,
  ArrowRight
} from 'lucide-react';

interface Props {
  activeStep?: number;
}

export const ClosedLoopVisualizer: React.FC<Props> = ({ activeStep = 1 }) => {
  const steps = [
    { num: 1, label: 'DETECT', desc: 'Field Mobile Scan', icon: Scan, color: 'border-blue-500 text-blue-400 bg-blue-500/10' },
    { num: 2, label: 'CLASSIFY', desc: 'AI Risk Engine', icon: Cpu, color: 'border-purple-500 text-purple-400 bg-purple-500/10' },
    { num: 3, label: 'PRIORITIZE', desc: 'Explainable Score', icon: Flame, color: 'border-red-500 text-red-400 bg-red-500/10' },
    { num: 4, label: 'ASSIGN', desc: 'Smart Assignee', icon: UserCheck, color: 'border-amber-500 text-amber-400 bg-amber-500/10' },
    { num: 5, label: 'RESOLVE', desc: 'Action Execution', icon: Wrench, color: 'border-cyan-500 text-cyan-400 bg-cyan-500/10' },
    { num: 6, label: 'VERIFY', desc: 'AI Before/After', icon: CheckCircle2, color: 'border-emerald-500 text-emerald-400 bg-emerald-500/10' },
    { num: 7, label: 'LEARN', desc: 'Cross-Mine Model', icon: BrainCircuit, color: 'border-safety-orange text-safety-orange bg-safety-orange/10' },
  ];

  return (
    <div className="glass-panel p-4 rounded-xl border border-slate-800/80 mb-6 shadow-xl">
      <div className="flex items-center justify-between mb-3">
        <div className="flex items-center space-x-2">
          <span className="w-2.5 h-2.5 rounded-full bg-safety-orange animate-ping" />
          <h3 className="text-xs font-extrabold uppercase tracking-wider text-white">
            Closed-Loop AI Governance Pipeline
          </h3>
        </div>
        <span className="text-[11px] text-slate-400 font-mono hidden sm:inline">
          USP: &ldquo;From Field Evidence to Governance Intelligence&rdquo;
        </span>
      </div>

      <div className="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-7 gap-2">
        {steps.map((step, idx) => {
          const Icon = step.icon;
          const isCurrent = activeStep === step.num;
          return (
            <div
              key={step.num}
              className={`p-3 rounded-lg border flex flex-col items-center text-center transition-all ${
                isCurrent
                  ? 'border-safety-orange bg-safety-orange/15 ring-2 ring-safety-orange/50 shadow-lg scale-105'
                  : 'border-slate-800 bg-coal-900/60 hover:bg-coal-800/60'
              }`}
            >
              <div className={`w-8 h-8 rounded-lg flex items-center justify-center mb-1.5 border ${step.color}`}>
                <Icon className="w-4 h-4" />
              </div>
              <span className="text-[11px] font-extrabold tracking-wide text-white">{step.label}</span>
              <span className="text-[9px] text-slate-400 mt-0.5 truncate max-w-full">{step.desc}</span>
            </div>
          );
        })}
      </div>
    </div>
  );
};
"""

with open('src/components/layout/Sidebar.tsx', 'w', encoding='utf-8') as f:
    f.write(sidebar)

with open('src/components/layout/TopHeader.tsx', 'w', encoding='utf-8') as f:
    f.write(top_header)

with open('src/components/layout/BottomNav.tsx', 'w', encoding='utf-8') as f:
    f.write(bottom_nav)

with open('src/components/visualizer/ClosedLoopVisualizer.tsx', 'w', encoding='utf-8') as f:
    f.write(closed_loop)

print("Layout and Visualizer components generated successfully!")
