import os

landing_page = """import React from 'react';
import {
  Pickaxe,
  ShieldCheck,
  Zap,
  Sparkles,
  ArrowRight,
  BrainCircuit,
  MapPin,
  FileCheck,
  CheckCircle2,
  HardHat,
  Lock,
  Activity,
  Layers,
  Bot
} from 'lucide-react';
import { ClosedLoopVisualizer } from '../components/visualizer/ClosedLoopVisualizer';

interface Props {
  onExploreDashboard: () => void;
  onStartInspection: () => void;
  onOpenCopilot: () => void;
}

export const LandingPage: React.FC<Props> = ({
  onExploreDashboard,
  onStartInspection,
  onOpenCopilot
}) => {
  const corePillars = [
    {
      title: 'AI-Powered Compliance',
      desc: 'Automated statutory tracking across Mines Act 1952, Coal Mines Regulations 2017, and MoEFCC Environmental Clearances.',
      icon: ShieldCheck,
      color: 'from-blue-600 to-cyan-600'
    },
    {
      title: 'Smart Field Inspection',
      desc: 'Mobile-first inspection with GPS geo-tagging, voice audio transcription, multi-photo capture, and offline synchronization.',
      icon: Pickaxe,
      color: 'from-orange-500 to-amber-600'
    },
    {
      title: 'Predictive Risk Intelligence',
      desc: '14-day early warning failure probability forecasts, factor contribution waterfalls, and explainable AI root causes.',
      icon: BrainCircuit,
      color: 'from-purple-600 to-pink-600'
    },
    {
      title: 'Automated Governance Workflow',
      desc: 'Closed-loop issue lifecycle with AI smart assignment, countdown SLAs, and 4-tier management escalation.',
      icon: Zap,
      color: 'from-amber-500 to-red-600'
    },
    {
      title: 'GIS-Based Monitoring',
      desc: 'Interactive spatial telemetry across Coal India basins with real-time hazard zones, pit boundaries, and heatmaps.',
      icon: MapPin,
      color: 'from-emerald-500 to-teal-600'
    },
    {
      title: 'Digital Document Intelligence',
      desc: 'AI OCR extraction of statutory permits, EC clearance clauses, and proactive auto-renewal workflows.',
      icon: FileCheck,
      color: 'from-blue-500 to-indigo-600'
    },
    {
      title: 'Contractor Governance',
      desc: 'Workforce safety index, mandatory VTC refresher tracking, Form B register verification, and risk leaderboard.',
      icon: HardHat,
      color: 'from-yellow-500 to-orange-600'
    },
    {
      title: 'Secure Audit Trail',
      desc: 'Cryptographic SHA-256 block-hashed immutable ledger ensuring 100% transparent and tamper-proof governance.',
      icon: Lock,
      color: 'from-slate-600 to-slate-800'
    }
  ];

  return (
    <div className="min-h-screen bg-coal-950 text-slate-100 py-6 px-4 sm:px-8 max-w-7xl mx-auto space-y-12">
      {/* SIH Banner */}
      <div className="flex flex-wrap items-center justify-between gap-3 p-3.5 rounded-xl bg-coal-900/90 border border-slate-800 text-xs">
        <div className="flex items-center space-x-2">
          <span className="px-2.5 py-0.5 rounded bg-safety-orange font-bold text-white text-[11px] uppercase tracking-wider">
            SIH Problem ID 26024
          </span>
          <span className="text-slate-300 font-semibold">
            Ministry of Coal • Coal India Limited
          </span>
        </div>
        <div className="flex items-center space-x-2 text-slate-400 font-mono text-[11px]">
          <span>Theme: <strong>Smart Automation</strong></span>
          <span>•</span>
          <span>Category: <strong>Software</strong></span>
        </div>
      </div>

      {/* Hero Section */}
      <div className="text-center space-y-5 pt-4 max-w-4xl mx-auto">
        <div className="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full bg-safety-orange/10 border border-safety-orange/30 text-safety-orange text-xs font-bold tracking-wider uppercase">
          <Sparkles className="w-3.5 h-3.5 animate-spin" />
          <span>Next-Generation Coal Mine Governance</span>
        </div>

        <h1 className="text-3xl sm:text-5xl lg:text-6xl font-black text-white tracking-tight leading-tight">
          Smarter Governance. <br />
          <span className="bg-gradient-to-r from-safety-orange via-amber-400 to-yellow-500 bg-clip-text text-transparent">
            Safer Mines. Better Decisions.
          </span>
        </h1>

        <p className="text-sm sm:text-base text-slate-300 leading-relaxed max-w-3xl mx-auto">
          An AI-powered governance and compliance intelligence platform designed for real-time transparency, accountability, and predictive decision-making across India&apos;s coal mining ecosystem.
        </p>

        {/* Hero CTA Buttons */}
        <div className="flex flex-wrap items-center justify-center gap-3.5 pt-2">
          <button
            onClick={onExploreDashboard}
            className="flex items-center space-x-2 px-6 py-3 rounded-xl bg-gradient-to-r from-safety-orange to-amber-500 hover:from-safety-orange/90 hover:to-amber-500/90 text-white font-extrabold text-sm shadow-xl shadow-safety-orange/25 transition-all transform hover:scale-105"
          >
            <span>Explore Dashboard</span>
            <ArrowRight className="w-4 h-4" />
          </button>

          <button
            onClick={onStartInspection}
            className="flex items-center space-x-2 px-6 py-3 rounded-xl bg-coal-800 hover:bg-coal-750 text-white border border-slate-700 font-bold text-sm transition-all"
          >
            <Pickaxe className="w-4 h-4 text-safety-orange" />
            <span>Start Field Inspection</span>
          </button>

          <button
            onClick={onOpenCopilot}
            className="flex items-center space-x-2 px-5 py-3 rounded-xl bg-coal-900/90 hover:bg-coal-800 text-safety-cyan border border-safety-cyan/40 font-bold text-sm transition-all"
          >
            <Bot className="w-4 h-4 text-safety-cyan" />
            <span>Talk to MineGuard AI</span>
          </button>
        </div>
      </div>

      {/* Closed-Loop AI Visualizer */}
      <ClosedLoopVisualizer activeStep={1} />

      {/* USP Banner */}
      <div className="p-6 rounded-2xl bg-gradient-to-r from-coal-900 via-coal-850 to-coal-900 border border-safety-orange/30 shadow-2xl relative overflow-hidden">
        <div className="absolute -right-10 -bottom-10 w-48 h-48 bg-safety-orange/10 rounded-full blur-3xl pointer-events-none" />
        <div className="relative z-10 space-y-2 text-center sm:text-left">
          <span className="text-[11px] font-extrabold uppercase tracking-widest text-safety-orange">
            The Core Value Proposition
          </span>
          <h2 className="text-xl sm:text-2xl font-black text-white">
            &ldquo;From Field Evidence to Governance Intelligence&rdquo;
          </h2>
          <p className="text-xs sm:text-sm text-slate-300 max-w-3xl leading-relaxed">
            Replacing fragmented paperwork, spreadsheets, and delayed reporting with an automated, explainable, closed-loop AI ecosystem: <strong>Detect &rarr; Classify &rarr; Prioritize &rarr; Assign &rarr; Resolve &rarr; Verify &rarr; Learn.</strong>
          </p>
        </div>
      </div>

      {/* 8 Core Pillars */}
      <div className="space-y-4">
        <div className="text-center space-y-1">
          <h3 className="text-lg font-black text-white uppercase tracking-wider">
            Comprehensive Enterprise Capabilities
          </h3>
          <p className="text-xs text-slate-400">
            Digitally integrating mine-level governance, statutory reporting, and AI intelligence
          </p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          {corePillars.map(p => {
            const Icon = p.icon;
            return (
              <div
                key={p.title}
                className="glass-panel p-5 rounded-xl border border-slate-800 hover:border-safety-orange/40 transition-all duration-300 group flex flex-col justify-between"
              >
                <div className="space-y-3">
                  <div className={`w-10 h-10 rounded-lg bg-gradient-to-br ${p.color} flex items-center justify-center text-white shadow-lg`}>
                    <Icon className="w-5 h-5" />
                  </div>
                  <h4 className="text-sm font-extrabold text-white group-hover:text-safety-orange transition-colors">
                    {p.title}
                  </h4>
                  <p className="text-xs text-slate-400 leading-relaxed">
                    {p.desc}
                  </p>
                </div>
                <div className="mt-4 pt-3 border-t border-slate-800/80 flex items-center justify-between text-[11px] text-slate-500 font-mono">
                  <span>Standard 26024</span>
                  <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};
"""

dashboard_page = """import React from 'react';
import {
  Pickaxe,
  ShieldCheck,
  AlertTriangle,
  Flame,
  ClockAlert,
  ClipboardList,
  BrainCircuit,
  CheckCircle2,
  TrendingUp,
  ArrowUpRight,
  ArrowDownRight,
  Sparkles,
  MapPin,
  ChevronRight
} from 'lucide-react';
import {
  LineChart,
  Line,
  BarChart,
  Bar,
  PieChart,
  Pie,
  Cell,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Legend
} from 'recharts';
import { useApp } from '../../context/AppContext';
import { useLanguage } from '../../context/LanguageContext';
import { ClosedLoopVisualizer } from '../../components/visualizer/ClosedLoopVisualizer';
import { RiskScoreCard } from '../../components/visualizer/RiskScoreCard';

interface Props {
  setActiveTab: (tab: string) => void;
}

export const DashboardPage: React.FC<Props> = ({ setActiveTab }) => {
  const { stats, mines, issues } = useApp();
  const { t } = useLanguage();

  const gevraMine = mines.find(m => m.id === 'mine-gevra') || mines[0];

  // 1. Compliance Trend (6 Months)
  const complianceTrendData = [
    { month: 'Mar 2026', compliance: 79, target: 85 },
    { month: 'Apr 2026', compliance: 82, target: 85 },
    { month: 'May 2026', compliance: 81, target: 88 },
    { month: 'Jun 2026', compliance: 84, target: 88 },
    { month: 'Jul 2026', compliance: 86, target: 90 },
    { month: 'Aug 2026', compliance: stats.overallCompliance, target: 90 }
  ];

  // 2. Issue Distribution
  const issueDistributionData = [
    { name: 'Safety', value: 42, color: '#EF4444' },
    { name: 'Environment', value: 24, color: '#F59E0B' },
    { name: 'Labour', value: 18, color: '#3B82F6' },
    { name: 'Production', value: 14, color: '#06B6D4' },
    { name: 'Equipment', value: 12, color: '#8B5CF6' },
    { name: 'Statutory', value: 10, color: '#10B981' },
    { name: 'Contractor', value: 6, color: '#EAB308' },
  ];

  // 3. Corrective Action Funnel
  const correctiveActionStatusData = [
    { stage: 'Open', count: 32, fill: '#EF4444' },
    { stage: 'Assigned', count: 28, fill: '#F97316' },
    { stage: 'In Progress', count: 36, fill: '#EAB308' },
    { stage: 'Resolved', count: 18, fill: '#06B6D4' },
    { stage: 'Verified', count: 8, fill: '#3B82F6' },
    { stage: 'Closed', count: 124, fill: '#10B981' }
  ];

  // 4. Multi-Mine Comparison
  const mineComparisonData = [
    { name: 'Gevra', compliance: gevraMine.complianceScore, risk: gevraMine.riskScore, safety: 86 },
    { name: 'Kusmunda', compliance: 87, risk: 54, safety: 68 },
    { name: 'Dipka', compliance: 91, risk: 42, safety: 48 },
    { name: 'Jayant', compliance: 94, risk: 36, safety: 32 },
    { name: 'Moonidih', compliance: 76, risk: 81, safety: 92 },
  ];

  // Top 5 critical items requiring attention
  const topAttentionItems = [
    { id: 'item-1', title: 'Conveyor protection & emergency trip-wire issue', mine: 'Gevra Mine', severity: 'CRITICAL', time: '18h SLA remaining', link: 'evidence-verification' },
    { id: 'item-2', title: 'Environmental Clearance renewal docket expiring', mine: 'Gevra Mine', severity: 'HIGH', time: '16 days remaining', link: 'expiring-documents' },
    { id: 'item-3', title: 'Contractor ABC Mining: 18 dumpers lacking VTC training', mine: 'Gevra Mine', severity: 'HIGH', time: '48h SLA remaining', link: 'contractor-dashboard' },
    { id: 'item-4', title: 'Longwall ventilation air velocity deficit', mine: 'Moonidih Mine', severity: 'CRITICAL', time: '2h SLA remaining', link: 'critical-issues' },
    { id: 'item-5', title: 'Form B labour biometric attendance register missing', mine: 'Rajmahal Mine', severity: 'MEDIUM', time: '5 days remaining', link: 'labour-compliance' }
  ];

  const kpiCards = [
    { title: t('totalMines'), value: stats.totalMines, sub: '8 Subsidiaries', icon: Pickaxe, color: 'text-blue-400' },
    { title: t('overallCompliance'), value: `${stats.overallCompliance}%`, sub: '+3.2% this quarter', icon: ShieldCheck, color: 'text-emerald-400', positive: true },
    { title: t('openIssues'), value: stats.openIssues, sub: 'Across all pits', icon: AlertTriangle, color: 'text-amber-400' },
    { title: t('criticalIssues'), value: stats.criticalIssues, sub: 'Immediate SLA priority', icon: Flame, color: 'text-red-400', alert: true },
    { title: t('overdueActions'), value: stats.overdueActions, sub: 'Level 2/3 Escalated', icon: ClockAlert, color: 'text-orange-400' },
    { title: t('inspectionsThisMonth'), value: stats.inspectionsThisMonth, sub: '+42 this week', icon: ClipboardList, color: 'text-cyan-400' },
    { title: t('predictedRisks'), value: stats.predictedRisks, sub: '14-day AI forecast', icon: BrainCircuit, color: 'text-purple-400' },
    { title: t('pendingApprovals'), value: stats.pendingApprovals, sub: 'Evidence Verification', icon: CheckCircle2, color: 'text-teal-400' }
  ];

  return (
    <div className="space-y-6 pb-12">
      {/* Top Header Card */}
      <div className="glass-panel p-5 rounded-2xl border border-slate-800 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2 text-xs text-safety-orange font-bold uppercase tracking-wider">
            <span className="w-2 h-2 rounded-full bg-safety-orange animate-ping" />
            <span>AI Autonomous Governance Active</span>
          </div>
          <h1 className="text-2xl font-black text-white mt-1">
            {t('goodMorning')}, Mine Officer
          </h1>
          <p className="text-xs text-slate-400 mt-0.5">
            Mine Jurisdiction: <strong className="text-white">{t('mineLocation')}</strong> • {t('lastSync')}
          </p>
        </div>

        <div className="flex items-center space-x-2">
          <button
            onClick={() => setActiveTab('new-inspection')}
            className="flex items-center space-x-2 px-4 py-2 rounded-xl bg-gradient-to-r from-safety-orange to-amber-500 hover:from-safety-orange/90 text-white font-extrabold text-xs shadow-lg shadow-safety-orange/20 transition-all"
          >
            <Pickaxe className="w-3.5 h-3.5" />
            <span>New AI Inspection</span>
          </button>
          <button
            onClick={() => setActiveTab('ai-copilot')}
            className="flex items-center space-x-2 px-4 py-2 rounded-xl bg-coal-800 text-safety-cyan border border-safety-cyan/30 text-xs font-bold hover:bg-coal-750 transition-all"
          >
            <BrainCircuit className="w-3.5 h-3.5" />
            <span>Copilot</span>
          </button>
        </div>
      </div>

      {/* 8 KPI Cards */}
      <div className="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-8 gap-3">
        {kpiCards.map(kpi => {
          const Icon = kpi.icon;
          return (
            <div
              key={kpi.title}
              className={`glass-panel p-3.5 rounded-xl border transition-all ${
                kpi.alert
                  ? 'border-red-500/40 bg-red-950/20 shadow-md shadow-red-500/10'
                  : 'border-slate-800/80 hover:border-slate-700'
              }`}
            >
              <div className="flex items-center justify-between text-slate-400 mb-1.5">
                <span className="text-[10px] font-bold uppercase tracking-wider truncate max-w-[85px]">
                  {kpi.title}
                </span>
                <Icon className={`w-3.5 h-3.5 ${kpi.color}`} />
              </div>
              <div className="text-xl font-black text-white font-mono">{kpi.value}</div>
              <div className="text-[9px] text-slate-400 mt-1 truncate">{kpi.sub}</div>
            </div>
          );
        })}
      </div>

      {/* Explainable AI Risk Score for Active Mine */}
      <RiskScoreCard mine={gevraMine} />

      {/* Charts Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* A. Compliance Trend */}
        <div className="glass-panel p-5 rounded-xl border border-slate-800 space-y-4">
          <div className="flex items-center justify-between">
            <div>
              <h3 className="text-sm font-extrabold text-white uppercase tracking-wider">Compliance Trend (6 Months)</h3>
              <p className="text-[11px] text-slate-400">Statutory index progression across all operational divisions</p>
            </div>
            <span className="text-xs font-mono font-bold text-emerald-400 bg-emerald-500/15 px-2 py-0.5 rounded">
              +8.0% YoY
            </span>
          </div>
          <div className="h-64 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={complianceTrendData}>
                <CartesianGrid strokeDasharray="3 3" stroke="#1E2638" />
                <XAxis dataKey="month" stroke="#64748B" fontSize={11} />
                <YAxis stroke="#64748B" domain={[60, 100]} fontSize={11} />
                <Tooltip contentStyle={{ backgroundColor: '#0E131F', borderColor: '#334155', borderRadius: '8px' }} />
                <Legend />
                <Line type="monotone" dataKey="compliance" stroke="#FF6B00" strokeWidth={3} name="Actual Compliance %" dot={{ r: 4 }} />
                <Line type="monotone" dataKey="target" stroke="#10B981" strokeDasharray="4 4" strokeWidth={2} name="Ministry Target" />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* B. Issue Distribution */}
        <div className="glass-panel p-5 rounded-xl border border-slate-800 space-y-4">
          <div className="flex items-center justify-between">
            <div>
              <h3 className="text-sm font-extrabold text-white uppercase tracking-wider">Issue Distribution by Category</h3>
              <p className="text-[11px] text-slate-400">Classified by MineGuard AI Neural Engine</p>
            </div>
            <span className="text-xs font-mono font-bold text-safety-orange bg-safety-orange/15 px-2 py-0.5 rounded">
              126 Total
            </span>
          </div>
          <div className="h-64 w-full flex items-center justify-center">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie
                  data={issueDistributionData}
                  cx="50%"
                  cy="50%"
                  innerRadius={55}
                  outerRadius={80}
                  paddingAngle={4}
                  dataKey="value"
                  label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
                >
                  {issueDistributionData.map(entry => (
                    <Cell key={entry.name} fill={entry.color} />
                  ))}
                </Pie>
                <Tooltip contentStyle={{ backgroundColor: '#0E131F', borderColor: '#334155', borderRadius: '8px' }} />
              </PieChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* C. Corrective Action Lifecycle Funnel */}
        <div className="glass-panel p-5 rounded-xl border border-slate-800 space-y-4">
          <div className="flex items-center justify-between">
            <div>
              <h3 className="text-sm font-extrabold text-white uppercase tracking-wider">Corrective Action Status Funnel</h3>
              <p className="text-[11px] text-slate-400">Closed-loop workflow execution tracking</p>
            </div>
            <button onClick={() => setActiveTab('corrective-actions')} className="text-xs text-safety-orange font-bold hover:underline flex items-center space-x-1">
              <span>View Hub</span>
              <ArrowUpRight className="w-3.5 h-3.5" />
            </button>
          </div>
          <div className="h-64 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={correctiveActionStatusData}>
                <CartesianGrid strokeDasharray="3 3" stroke="#1E2638" />
                <XAxis dataKey="stage" stroke="#64748B" fontSize={11} />
                <YAxis stroke="#64748B" fontSize={11} />
                <Tooltip contentStyle={{ backgroundColor: '#0E131F', borderColor: '#334155', borderRadius: '8px' }} />
                <Bar dataKey="count" name="Action Count" radius={[4, 4, 0, 0]}>
                  {correctiveActionStatusData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.fill} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* D. Multi-Mine Comparative Radar/Bar */}
        <div className="glass-panel p-5 rounded-xl border border-slate-800 space-y-4">
          <div className="flex items-center justify-between">
            <div>
              <h3 className="text-sm font-extrabold text-white uppercase tracking-wider">Multi-Mine Performance Comparison</h3>
              <p className="text-[11px] text-slate-400">Comparing Mega Open Cast & Underground Mines</p>
            </div>
            <button onClick={() => setActiveTab('mine-overview')} className="text-xs text-safety-cyan font-bold hover:underline flex items-center space-x-1">
              <span>Mine Profiles</span>
              <ArrowUpRight className="w-3.5 h-3.5" />
            </button>
          </div>
          <div className="h-64 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={mineComparisonData}>
                <CartesianGrid strokeDasharray="3 3" stroke="#1E2638" />
                <XAxis dataKey="name" stroke="#64748B" fontSize={11} />
                <YAxis stroke="#64748B" domain={[0, 100]} fontSize={11} />
                <Tooltip contentStyle={{ backgroundColor: '#0E131F', borderColor: '#334155', borderRadius: '8px' }} />
                <Legend />
                <Bar dataKey="compliance" name="Compliance Score" fill="#10B981" radius={[4, 4, 0, 0]} />
                <Bar dataKey="risk" name="Risk Index" fill="#EF4444" radius={[4, 4, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      {/* Top 5 Critical Actions Requiring Attention */}
      <div className="glass-panel p-5 rounded-xl border border-slate-800 space-y-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-2">
            <Flame className="w-5 h-5 text-red-500" />
            <h3 className="text-sm font-extrabold uppercase tracking-wider text-white">
              Top 5 Actions Requiring Immediate Attention
            </h3>
          </div>
          <span className="text-xs text-slate-400 font-mono">Real-time SLA Countdown</span>
        </div>

        <div className="space-y-2">
          {topAttentionItems.map((item, idx) => (
            <div
              key={item.id}
              onClick={() => setActiveTab(item.link)}
              className="p-3 rounded-lg bg-coal-900/90 border border-slate-800 hover:border-safety-orange/40 transition-all flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2 cursor-pointer group"
            >
              <div className="flex items-center space-x-3">
                <span className="w-6 h-6 rounded bg-coal-800 font-mono font-bold text-xs flex items-center justify-center text-slate-400 group-hover:text-safety-orange">
                  {idx + 1}
                </span>
                <div>
                  <div className="flex items-center space-x-2">
                    <p className="text-xs font-bold text-white group-hover:text-safety-orange transition-colors">{item.title}</p>
                    <span className={`text-[9px] font-extrabold px-1.5 py-0.2 rounded ${
                      item.severity === 'CRITICAL' ? 'bg-red-500/20 text-red-400 border border-red-500/30' : 'bg-amber-500/20 text-amber-400'
                    }`}>
                      {item.severity}
                    </span>
                  </div>
                  <p className="text-[11px] text-slate-400 mt-0.5">{item.mine}</p>
                </div>
              </div>

              <div className="flex items-center space-x-3 self-end sm:self-center">
                <span className="text-xs font-mono font-bold text-amber-400 bg-coal-950 px-2.5 py-1 rounded border border-slate-700">
                  {item.time}
                </span>
                <ChevronRight className="w-4 h-4 text-slate-500 group-hover:text-white" />
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
"""

with open('src/pages/LandingPage.tsx', 'w', encoding='utf-8') as f:
    f.write(landing_page)

with open('src/pages/DashboardPage.tsx', 'w', encoding='utf-8') as f:
    f.write(dashboard_page)

print("LandingPage and DashboardPage written successfully!")
