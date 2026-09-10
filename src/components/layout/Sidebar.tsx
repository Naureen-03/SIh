import React, { useState } from 'react';
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
