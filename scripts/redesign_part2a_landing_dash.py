import os

landing = """import React from 'react';
import {
  ShieldCheck,
  CheckCircle2,
  FileText,
  MapPin,
  Flame,
  ArrowRight,
  Sparkles,
  Award,
  ExternalLink,
  Users,
  Building2,
  ScanEye,
  Bot
} from 'lucide-react';
import { ClosedLoopVisualizer } from '../components/visualizer/ClosedLoopVisualizer';
import { Footer } from '../components/layout/Footer';

interface LandingPageProps {
  onExploreDashboard: () => void;
  onStartInspection: () => void;
  onOpenCopilot: () => void;
}

export const LandingPage: React.FC<LandingPageProps> = ({
  onExploreDashboard,
  onStartInspection,
  onOpenCopilot
}) => {
  const pillars = [
    { title: 'Statutory Compliance Tracking', desc: 'Continuous monitoring of Coal Mines Regulations 2017, MoEFCC EC clearances, and DGMS circulars.', icon: ShieldCheck },
    { title: 'Digital Field Inspection', desc: 'Mobile-first field inspection register with GPS coordinates auto-lock, voice notes, and photo uploads.', icon: ScanEye },
    { title: 'Explainable AI Risk Scoring', desc: 'Multi-vector risk index (0-100) across safety, environmental, labour, production, and contractor factors.', icon: Flame },
    { title: 'Closed-Loop Governance', desc: 'End-to-end case remediation with SLA escalation timers, officer assignment, and evidence verification.', icon: CheckCircle2 },
    { title: 'GIS Spatial Infrastructure', desc: 'Geospatial mapping of high-risk coal basins, active mining faces, and geofenced hazard zones.', icon: MapPin },
    { title: 'OCR Document Intelligence', desc: 'Automated entity extraction from scanned DGMS permits, EC orders, and Form IV/VI registers.', icon: FileText },
    { title: 'Contractor Workforce Hub', desc: 'Mandatory Vocational Training (VTC) verification, Form B registry tracking, and risk auditing.', icon: Users },
    { title: 'Digital Governance Audit Trail', desc: 'Cryptographic SHA-256 block ledger recording every inspection, inference, and manager signoff.', icon: Building2 },
  ];

  return (
    <div className="min-h-screen bg-[#F4F6F9] text-slate-900 flex flex-col justify-between">
      <div>
        {/* Top Government Strip */}
        <div className="bg-[#0B2545] text-white border-b border-[#07192F]">
          <div className="gov-tricolor-strip" />
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5 flex flex-col sm:flex-row items-center justify-between gap-3">
            <div className="flex items-center space-x-3 text-center sm:text-left">
              <div className="w-10 h-10 rounded bg-white/10 border border-white/20 flex flex-col items-center justify-center font-bold text-white text-xs shadow-xs">
                <span>GOI</span>
                <span className="text-[7px] text-amber-400 uppercase">COAL</span>
              </div>
              <div>
                <div className="text-[11px] font-extrabold uppercase tracking-wider text-amber-400">
                  Government of India &bull; Ministry of Coal &bull; Coal India Limited
                </div>
                <div className="text-base font-black tracking-tight text-white">
                  MINEGUARD AI &mdash; Smart Mining Governance & Compliance System
                </div>
              </div>
            </div>

            <div className="flex items-center space-x-2">
              <span className="bg-[#134074] text-white border border-slate-600 px-3 py-1 rounded text-xs font-mono font-bold">
                SIH Problem Statement ID 26024
              </span>
              <button
                onClick={onExploreDashboard}
                className="gov-btn-primary bg-amber-500 hover:bg-amber-600 text-[#0B2545] font-black border-none"
              >
                <span>Enter Portal</span>
                <ArrowRight className="w-3.5 h-3.5" />
              </button>
            </div>
          </div>
        </div>

        {/* Hero Banner */}
        <section className="bg-white border-b border-slate-200 py-12 px-4 sm:px-6 lg:px-8">
          <div className="max-w-5xl mx-auto text-center space-y-4">
            <div className="inline-flex items-center space-x-2 bg-slate-100 text-slate-800 border border-slate-300 px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider">
              <Award className="w-3.5 h-3.5 text-amber-600" />
              <span>Smart India Hackathon 2026 Prototype</span>
            </div>

            <h1 className="text-3xl sm:text-4xl lg:text-5xl font-black text-[#0B2545] tracking-tight leading-tight">
              Smart Governance for India&apos;s Coal Mining Ecosystem
            </h1>

            <p className="text-sm sm:text-base text-slate-600 max-w-3xl mx-auto leading-relaxed">
              An AI-assisted digital governance and statutory compliance monitoring system designed for real-time transparency, regulatory accountability, and predictive risk mitigation across Coal India Limited and subsidiary mining operations.
            </p>

            <div className="flex flex-wrap items-center justify-center gap-3 pt-2">
              <button onClick={onExploreDashboard} className="gov-btn-primary text-xs py-3 px-6 text-sm">
                <span>Access Governance Dashboard</span>
                <ArrowRight className="w-4 h-4" />
              </button>
              <button onClick={onStartInspection} className="gov-btn-secondary text-xs py-3 px-6 text-sm">
                <span>Initiate Digital Field Inspection</span>
              </button>
              <button onClick={onOpenCopilot} className="gov-btn-secondary text-xs py-3 px-6 text-sm bg-slate-50">
                <Bot className="w-4 h-4 text-[#0B2545]" />
                <span>Consult MineGuard AI Assistant</span>
              </button>
            </div>
          </div>
        </section>

        {/* Main Content Area */}
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
          {/* Closed-Loop Pipeline */}
          <ClosedLoopVisualizer activeStep={1} />

          {/* 8 Core Capability Pillars */}
          <div className="space-y-4">
            <div className="text-center sm:text-left">
              <h2 className="text-base font-extrabold text-[#0B2545] uppercase tracking-wider">
                Key Governance Pillars
              </h2>
              <p className="text-xs text-slate-600 mt-0.5">
                Integrated modules fulfilling all statutory, environmental, safety, labour, and operational mandates
              </p>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
              {pillars.map((p, idx) => {
                const Icon = p.icon;
                return (
                  <div key={idx} className="gov-card p-4 space-y-2 hover:border-[#0B2545] transition-all">
                    <div className="w-8 h-8 rounded bg-[#0B2545] text-white flex items-center justify-center shadow-xs">
                      <Icon className="w-4 h-4 text-amber-400" />
                    </div>
                    <h3 className="text-xs font-extrabold text-slate-900 leading-snug">{p.title}</h3>
                    <p className="text-[11px] text-slate-600 leading-relaxed">{p.desc}</p>
                  </div>
                );
              })}
            </div>
          </div>

          {/* Multi-Stakeholder Matrix */}
          <div className="gov-card p-6 space-y-4">
            <h3 className="text-sm font-extrabold text-[#0B2545] uppercase tracking-wider text-center">
              Role-Based Governance Matrix
            </h3>
            <div className="grid grid-cols-1 sm:grid-cols-3 lg:grid-cols-6 gap-3 text-center text-xs">
              {[
                { role: 'Ministry of Coal', desc: 'National production, compliance & strategic policy' },
                { role: 'Coal India HQ', desc: 'Subsidiary performance benchmarking & resource allocation' },
                { role: 'DGMS / Regulatory', desc: 'Statutory safety orders, circulars & inquiry notices' },
                { role: 'Mine General Manager', desc: 'Mine-level SLA governance, case closure & approvals' },
                { role: 'Field Safety Officer', desc: 'On-site digital audits, GPS hazard capture & rectification' },
                { role: 'Contractor Cell', desc: 'Workforce VTC certification & Form B labour compliance' },
              ].map((s, idx) => (
                <div key={idx} className="p-3 bg-slate-50 rounded border border-slate-200">
                  <div className="w-7 h-7 rounded-full bg-[#0B2545] text-white flex items-center justify-center mx-auto mb-1.5 font-bold text-xs font-mono">
                    0{idx + 1}
                  </div>
                  <h4 className="font-extrabold text-slate-900 text-xs">{s.role}</h4>
                  <p className="text-[10px] text-slate-600 mt-1 leading-snug">{s.desc}</p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* Official Government Footer */}
      <Footer />
    </div>
  );
};
"""

dashboard = """import React from 'react';
import {
  Pickaxe,
  ShieldCheck,
  Flame,
  Wrench,
  ClockAlert,
  ClipboardList,
  Sparkles,
  ArrowRight,
  TrendingUp,
  AlertTriangle,
  FileText,
  MapPin,
  CheckCircle2,
  Calendar,
  Layers,
  Radio
} from 'lucide-react';
import {
  ResponsiveContainer,
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  PieChart,
  Pie,
  Cell,
  BarChart,
  Bar
} from 'recharts';
import { useApp } from '../context/AppContext';
import { useLanguage } from '../context/LanguageContext';
import { ClosedLoopVisualizer } from '../components/visualizer/ClosedLoopVisualizer';
import { RiskScoreCard } from '../components/visualizer/RiskScoreCard';
import { COMPLIANCE_TREND_DATA, CATEGORY_BREAKDOWN_DATA } from '../data/mockData';

interface DashboardPageProps {
  setActiveTab: (tab: string) => void;
}

export const DashboardPage: React.FC<DashboardPageProps> = ({ setActiveTab }) => {
  const { stats, mines, issues } = useApp();
  const { t } = useLanguage();

  const gevraMine = mines.find(m => m.id === 'mine-101') || mines[0];
  const criticalList = issues.filter(i => i.severity === 'Critical' && i.status !== 'CLOSED').slice(0, 5);

  const kpis = [
    { title: 'TOTAL MINES', value: stats.totalMines, sub: '8 Subsidiaries', icon: Pickaxe, color: 'text-[#0B2545]', border: 'border-slate-300' },
    { title: 'COMPLIANCE RATE', value: `${stats.overallCompliance}%`, sub: '+8.0% vs Last Month', icon: ShieldCheck, color: 'text-emerald-800', border: 'border-emerald-300' },
    { title: 'OPEN ISSUES', value: stats.openIssues, sub: 'Active in Register', icon: AlertTriangle, color: 'text-amber-800', border: 'border-amber-300' },
    { title: 'CRITICAL ISSUES', value: stats.criticalIssues, sub: 'Immediate SLA Action', icon: Flame, color: 'text-red-700', border: 'border-red-300' },
    { title: 'OVERDUE ACTIONS', value: stats.overdueActions, sub: 'Level 2 Escalated', icon: ClockAlert, color: 'text-red-700', border: 'border-red-300' },
    { title: 'FIELD INSPECTIONS', value: stats.inspectionsThisMonth, sub: 'Completed This Month', icon: ClipboardList, color: 'text-blue-800', border: 'border-blue-300' },
    { title: 'PREDICTED RISKS', value: stats.aiPredictedRisks, sub: '14-Day Forecast Window', icon: Sparkles, color: 'text-purple-800', border: 'border-purple-300' },
    { title: 'PENDING APPROVALS', value: 23, sub: 'Manager Review Queue', icon: Wrench, color: 'text-slate-800', border: 'border-slate-300' },
  ];

  return (
    <div className="space-y-6 pb-12">
      {/* Government Control Room Header */}
      <div className="gov-card p-5 flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
            <span className="w-2.5 h-2.5 rounded-full bg-emerald-600 animate-pulse" />
            <span>National Coal Mine Governance Dashboard</span>
          </div>
          <h1 className="text-2xl font-black text-slate-900 mt-1">
            Centralized Command & Compliance Monitoring Control Room
          </h1>
          <p className="text-xs text-slate-600 mt-0.5">
            Real-time digital integration of statutory compliance, field audits, safety hazards, environmental telemetry, and closed-loop corrective actions across Coal India Limited.
          </p>
        </div>

        <div className="flex flex-col sm:flex-row items-start sm:items-center gap-3 self-stretch sm:self-auto text-xs">
          <div className="bg-slate-50 border border-slate-300 rounded p-2.5 font-mono text-[11px] text-slate-700">
            <p>Last Sync: <strong>10 Sep 2026, 08:45 AM</strong></p>
            <p>Data Feed: <strong className="text-emerald-800">LIVE (Korba Cluster)</strong></p>
          </div>
          <button
            onClick={() => setActiveTab('new-inspection')}
            className="gov-btn-primary"
          >
            <ClipboardList className="w-4 h-4 text-amber-400" />
            <span>New Field Inspection</span>
          </button>
        </div>
      </div>

      {/* Closed-Loop AI Flow Overview */}
      <ClosedLoopVisualizer activeStep={1} />

      {/* SECTION 1: Top KPI Cards */}
      <div>
        <div className="flex items-center space-x-2 pb-2">
          <span className="text-[10px] font-extrabold bg-[#0B2545] text-white px-2 py-0.5 rounded font-mono">SECTION 1</span>
          <h2 className="text-xs font-extrabold uppercase tracking-wider text-slate-800">
            National Governance & Statutory Performance Register
          </h2>
        </div>

        <div className="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-8 gap-3">
          {kpis.map((kpi, idx) => {
            const Icon = kpi.icon;
            return (
              <div
                key={idx}
                className={`gov-card p-3 space-y-1 hover:border-[#0B2545] transition-all border ${kpi.border}`}
              >
                <div className="flex items-center justify-between text-slate-500">
                  <span className="text-[9px] font-extrabold uppercase tracking-wider">{kpi.title}</span>
                  <Icon className="w-3.5 h-3.5 text-slate-400" />
                </div>
                <div className={`text-xl font-black font-mono ${kpi.color}`}>
                  {kpi.value}
                </div>
                <p className="text-[9px] text-slate-500 font-medium truncate">{kpi.sub}</p>
              </div>
            );
          })}
        </div>
      </div>

      {/* SECTION 2: Compliance & Risk Intelligence */}
      <div>
        <div className="flex items-center space-x-2 pb-2">
          <span className="text-[10px] font-extrabold bg-[#0B2545] text-white px-2 py-0.5 rounded font-mono">SECTION 2</span>
          <h2 className="text-xs font-extrabold uppercase tracking-wider text-slate-800">
            Statutory Compliance Trend & Category Distribution
          </h2>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* 6-Month Trend */}
          <div className="gov-card p-4 lg:col-span-2 space-y-3">
            <div className="flex items-center justify-between border-b border-slate-200 pb-2">
              <h3 className="text-xs font-extrabold uppercase tracking-wider text-slate-900">
                6-Month Statutory Compliance Trend (%)
              </h3>
              <span className="text-[10px] font-bold text-emerald-800 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-300">
                Target: 95% Benchmark
              </span>
            </div>
            <div className="h-64 w-full">
              <ResponsiveContainer width="100%" height="100%">
                <LineChart data={COMPLIANCE_TREND_DATA}>
                  <CartesianGrid strokeDasharray="3 3" stroke="#E2E8F0" />
                  <XAxis dataKey="month" stroke="#64748B" fontSize={11} />
                  <YAxis domain={[75, 100]} stroke="#64748B" fontSize={11} />
                  <Tooltip contentStyle={{ backgroundColor: '#FFFFFF', borderColor: '#CBD5E1', borderRadius: '4px', fontSize: '11px' }} />
                  <Legend wrapperStyle={{ fontSize: '11px' }} />
                  <Line type="monotone" dataKey="actual" stroke="#0B2545" strokeWidth={2.5} name="Actual Compliance (%)" dot={{ r: 4 }} />
                  <Line type="monotone" dataKey="target" stroke="#15803D" strokeDasharray="4 4" strokeWidth={2} name="Mandatory Target (95%)" />
                </LineChart>
              </ResponsiveContainer>
            </div>
          </div>

          {/* Issue Category Pie */}
          <div className="gov-card p-4 space-y-3">
            <div className="flex items-center justify-between border-b border-slate-200 pb-2">
              <h3 className="text-xs font-extrabold uppercase tracking-wider text-slate-900">
                Issue Category Breakdown
              </h3>
              <span className="text-[10px] text-slate-500 font-mono">125 Total</span>
            </div>
            <div className="h-64 w-full">
              <ResponsiveContainer width="100%" height="100%">
                <PieChart>
                  <Pie
                    data={CATEGORY_BREAKDOWN_DATA}
                    dataKey="count"
                    nameKey="category"
                    cx="50%"
                    cy="50%"
                    outerRadius={75}
                    label={({ category, count }) => `${category} (${count})`}
                    labelLine={false}
                  >
                    {CATEGORY_BREAKDOWN_DATA.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={entry.color} />
                    ))}
                  </Pie>
                  <Tooltip contentStyle={{ backgroundColor: '#FFFFFF', borderColor: '#CBD5E1', borderRadius: '4px', fontSize: '11px' }} />
                </PieChart>
              </ResponsiveContainer>
            </div>
          </div>
        </div>
      </div>

      {/* SECTION 3: Explainable Risk Scoring */}
      <div>
        <div className="flex items-center space-x-2 pb-2">
          <span className="text-[10px] font-extrabold bg-[#0B2545] text-white px-2 py-0.5 rounded font-mono">SECTION 3</span>
          <h2 className="text-xs font-extrabold uppercase tracking-wider text-slate-800">
            Explainable AI Risk Engine & Root Cause Analysis
          </h2>
        </div>

        <RiskScoreCard mine={gevraMine} />
      </div>

      {/* SECTION 4: Top 5 Urgent Items with Live SLAs */}
      <div>
        <div className="flex items-center space-x-2 pb-2">
          <span className="text-[10px] font-extrabold bg-[#0B2545] text-white px-2 py-0.5 rounded font-mono">SECTION 4</span>
          <h2 className="text-xs font-extrabold uppercase tracking-wider text-slate-800">
            Top Priority Statutory Attention Items & SLA Timelines
          </h2>
        </div>

        <div className="gov-card overflow-hidden">
          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs">
              <thead className="bg-slate-50 border-b border-slate-200 text-slate-700 font-bold uppercase tracking-wider text-[10px]">
                <tr>
                  <th className="p-3">Issue Docket</th>
                  <th className="p-3">Mine Location</th>
                  <th className="p-3">Category</th>
                  <th className="p-3">Severity</th>
                  <th className="p-3">Responsible Assignee</th>
                  <th className="p-3">SLA Countdown</th>
                  <th className="p-3 text-right">Action</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-200">
                {criticalList.map(item => (
                  <tr key={item.id} className="hover:bg-slate-50/80 transition-colors">
                    <td className="p-3 font-mono font-bold text-slate-900">
                      <div>{item.issueCode}</div>
                      <div className="text-[10px] text-slate-500 font-sans font-normal truncate max-w-xs">{item.title}</div>
                    </td>
                    <td className="p-3 text-slate-700 font-medium">
                      {item.mineName} <span className="text-[10px] text-slate-500">({item.zone})</span>
                    </td>
                    <td className="p-3">
                      <span className="bg-slate-100 text-slate-800 border border-slate-300 text-[10px] font-bold px-2 py-0.5 rounded uppercase">
                        {item.category}
                      </span>
                    </td>
                    <td className="p-3">
                      <span className="bg-red-50 text-red-800 border border-red-300 text-[10px] font-bold px-2 py-0.5 rounded uppercase">
                        {item.severity}
                      </span>
                    </td>
                    <td className="p-3 text-slate-800 font-medium">
                      {item.assignedTo || 'Unassigned'}
                    </td>
                    <td className="p-3 font-mono text-red-700 font-bold">
                      {item.slaRemainingHours}h Left
                    </td>
                    <td className="p-3 text-right">
                      <button
                        onClick={() => setActiveTab('evidence-verification')}
                        className="gov-btn-secondary text-[11px] py-1 px-2.5"
                      >
                        Inspect Docket
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
};
"""

with open('src/pages/LandingPage.tsx', 'w', encoding='utf-8') as f:
    f.write(landing)

with open('src/pages/DashboardPage.tsx', 'w', encoding='utf-8') as f:
    f.write(dashboard)

print("Part 2a: LandingPage and DashboardPage written successfully!")
