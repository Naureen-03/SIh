import React from 'react';
import {
  Pickaxe,
  ShieldCheck,
  Flame,
  Wrench,
  ClockAlert,
  ClipboardList,
  Sparkles,
  AlertTriangle,
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
} from 'recharts';
import { useApp } from '../context/AppContext';
import { useLanguage } from '../context/LanguageContext';
import { ClosedLoopVisualizer } from '../components/visualizer/ClosedLoopVisualizer';
import { RiskScoreCard } from '../components/visualizer/RiskScoreCard';

const COMPLIANCE_TREND_DATA = [
  { month: 'Apr 2026', actual: 79, target: 95 },
  { month: 'May 2026', actual: 81, target: 95 },
  { month: 'Jun 2026', actual: 83, target: 95 },
  { month: 'Jul 2026', actual: 84, target: 95 },
  { month: 'Aug 2026', actual: 87, target: 95 },
  { month: 'Sep 2026', actual: 88, target: 95 },
];

const CATEGORY_BREAKDOWN_DATA = [
  { category: 'Safety', count: 52, color: '#B91C1C' },
  { category: 'Environment', count: 31, color: '#D97706' },
  { category: 'Labour', count: 24, color: '#1D4E89' },
  { category: 'Operational', count: 18, color: '#475569' },
];

interface DashboardPageProps {
  setActiveTab: (tab: string) => void;
}

export const DashboardPage: React.FC<DashboardPageProps> = ({
  setActiveTab,
}) => {
  const { stats, mines, issues } = useApp();
  const { t } = useLanguage();

  const gevraMine =
    mines.find(m => m.id === 'mine-101') || mines[0];

  const criticalList = issues
    .filter(
      i =>
        i.severity === 'Critical' &&
        i.status !== 'CLOSED'
    )
    .slice(0, 5);

  const kpis = [
    {
      title: 'TOTAL MINES',
      value: stats.totalMines,
      sub: '8 Subsidiaries',
      icon: Pickaxe,
      color: 'text-[#0B2545]',
      border: 'border-slate-300',
    },
    {
      title: 'COMPLIANCE RATE',
      value: `${stats.overallCompliance}%`,
      sub: '+8.0% vs Last Month',
      icon: ShieldCheck,
      color: 'text-emerald-800',
      border: 'border-emerald-300',
    },
    {
      title: 'OPEN ISSUES',
      value: stats.openIssues,
      sub: 'Active in Register',
      icon: AlertTriangle,
      color: 'text-amber-800',
      border: 'border-amber-300',
    },
    {
      title: 'CRITICAL ISSUES',
      value: stats.criticalIssues,
      sub: 'Immediate SLA Action',
      icon: Flame,
      color: 'text-red-700',
      border: 'border-red-300',
    },
    {
      title: 'OVERDUE ACTIONS',
      value: stats.overdueActions,
      sub: 'Level 2 Escalated',
      icon: ClockAlert,
      color: 'text-red-700',
      border: 'border-red-300',
    },
    {
      title: 'FIELD INSPECTIONS',
      value: stats.inspectionsThisMonth,
      sub: 'Completed This Month',
      icon: ClipboardList,
      color: 'text-blue-800',
      border: 'border-blue-300',
    },
    {
      title: 'PREDICTED RISKS',
      value: stats.predictedRisks,
      sub: '14-Day Forecast Window',
      icon: Sparkles,
      color: 'text-purple-800',
      border: 'border-purple-300',
    },
    {
      title: 'PENDING APPROVALS',
      value: 23,
      sub: 'Manager Review Queue',
      icon: Wrench,
      color: 'text-slate-800',
      border: 'border-slate-300',
    },
  ];

  return (
    <div className="space-y-6 pb-12">

      {/* Government Control Room Header */}
      <div className="gov-card p-5 flex flex-col md:flex-row items-start md:items-center justify-between gap-4">

        <div>

          <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">

            <span className="w-2.5 h-2.5 rounded-full bg-emerald-600 animate-pulse" />

            <span>
              National Coal Mine Governance Dashboard
            </span>

          </div>

          <h1 className="text-2xl font-black text-slate-900 mt-1">
            Centralized Command & Compliance Monitoring Control Room
          </h1>

          <p className="text-xs text-slate-600 mt-0.5">
            Real-time digital integration of statutory compliance, field audits,
            safety hazards, environmental telemetry, and closed-loop corrective
            actions across Coal India Limited.
          </p>

        </div>

        <div className="flex flex-col sm:flex-row items-start sm:items-center gap-3 self-stretch sm:self-auto text-xs">

          <div className="bg-slate-50 border border-slate-300 rounded p-2.5 font-mono text-[11px] text-slate-700">

            <p>
              Last Sync: <strong>10 Sep 2026, 08:45 AM</strong>
            </p>

            <p>
              Data Feed:{' '}
              <strong className="text-emerald-800">
                LIVE (Korba Cluster)
              </strong>
            </p>

          </div>

          <button
            onClick={() => setActiveTab('new-inspection')}
            className="gov-btn-primary"
          >
            <ClipboardList className="w-4 h-4 text-amber-400" />

            <span>
              New Field Inspection
            </span>

          </button>

        </div>

      </div>

      {/* Closed-Loop AI Flow Overview */}
      <ClosedLoopVisualizer activeStep={1} />

      {/* SECTION 1 */}
      <div>

        <div className="flex items-center space-x-2 pb-2">

          <span className="text-[10px] font-extrabold bg-[#0B2545] text-white px-2 py-0.5 rounded font-mono">
            SECTION 1
          </span>

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

                  <span className="text-[9px] font-extrabold uppercase tracking-wider">
                    {kpi.title}
                  </span>

                  <Icon className="w-3.5 h-3.5 text-slate-400" />

                </div>

                <div
                  className={`text-xl font-black font-mono ${kpi.color}`}
                >
                  {kpi.value}
                </div>

                <p className="text-[9px] text-slate-500 font-medium truncate">
                  {kpi.sub}
                </p>

              </div>
            );
          })}

        </div>

      </div>

      {/* SECTION 2 */}
      <div>

        <div className="flex items-center space-x-2 pb-2">

          <span className="text-[10px] font-extrabold bg-[#0B2545] text-white px-2 py-0.5 rounded font-mono">
            SECTION 2
          </span>

          <h2 className="text-xs font-extrabold uppercase tracking-wider text-slate-800">
            Statutory Compliance Trend & Category Distribution
          </h2>

        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">

          {/* Compliance Trend */}
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

                  <CartesianGrid
                    strokeDasharray="3 3"
                    stroke="#E2E8F0"
                  />

                  <XAxis
                    dataKey="month"
                    stroke="#64748B"
                    fontSize={11}
                  />

                  <YAxis
                    domain={[75, 100]}
                    stroke="#64748B"
                    fontSize={11}
                  />

                  <Tooltip
                    contentStyle={{
                      backgroundColor: '#FFFFFF',
                      borderColor: '#CBD5E1',
                      borderRadius: '4px',
                      fontSize: '11px',
                    }}
                  />

                  <Legend
                    wrapperStyle={{
                      fontSize: '11px',
                    }}
                  />

                  <Line
                    type="monotone"
                    dataKey="actual"
                    stroke="#0B2545"
                    strokeWidth={2.5}
                    name="Actual Compliance (%)"
                    dot={{ r: 4 }}
                  />

                  <Line
                    type="monotone"
                    dataKey="target"
                    stroke="#15803D"
                    strokeDasharray="4 4"
                    strokeWidth={2}
                    name="Mandatory Target (95%)"
                  />

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

              <span className="text-[10px] text-slate-500 font-mono">
                125 Total
              </span>

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
                    label={({ name, value }) =>
                      `${name} (${value})`
                    }
                    labelLine={false}
                  >

                    {CATEGORY_BREAKDOWN_DATA.map(
                      (entry, index) => (
                        <Cell
                          key={`cell-${index}`}
                          fill={entry.color}
                        />
                      )
                    )}

                  </Pie>

                  <Tooltip
                    contentStyle={{
                      backgroundColor: '#FFFFFF',
                      borderColor: '#CBD5E1',
                      borderRadius: '4px',
                      fontSize: '11px',
                    }}
                  />

                </PieChart>

              </ResponsiveContainer>

            </div>

          </div>

        </div>

      </div>

      {/* SECTION 3 */}
      <div>

        <div className="flex items-center space-x-2 pb-2">

          <span className="text-[10px] font-extrabold bg-[#0B2545] text-white px-2 py-0.5 rounded font-mono">
            SECTION 3
          </span>

          <h2 className="text-xs font-extrabold uppercase tracking-wider text-slate-800">
            Explainable AI Risk Engine & Root Cause Analysis
          </h2>

        </div>

        <RiskScoreCard mine={gevraMine} />

      </div>

      {/* SECTION 4 */}
      <div>

        <div className="flex items-center space-x-2 pb-2">

          <span className="text-[10px] font-extrabold bg-[#0B2545] text-white px-2 py-0.5 rounded font-mono">
            SECTION 4
          </span>

          <h2 className="text-xs font-extrabold uppercase tracking-wider text-slate-800">
            Top Priority Statutory Attention Items & SLA Timelines
          </h2>

        </div>

        <div className="gov-card overflow-hidden">

          <div className="overflow-x-auto">

            <table className="w-full text-left text-xs">

              <thead className="bg-slate-50 border-b border-slate-200 text-slate-700 font-bold uppercase tracking-wider text-[10px]">

                <tr>

                  <th className="p-3">
                    Issue Docket
                  </th>

                  <th className="p-3">
                    Mine Location
                  </th>

                  <th className="p-3">
                    Category
                  </th>

                  <th className="p-3">
                    Severity
                  </th>

                  <th className="p-3">
                    Responsible Assignee
                  </th>

                  <th className="p-3">
                    SLA Countdown
                  </th>

                  <th className="p-3 text-right">
                    Action
                  </th>

                </tr>

              </thead>

              <tbody className="divide-y divide-slate-200">

                {criticalList.map(item => (

                  <tr
                    key={item.id}
                    className="hover:bg-slate-50/80 transition-colors"
                  >

                    <td className="p-3 font-mono font-bold text-slate-900">

                      <div>
                        {item.issueCode}
                      </div>

                      <div className="text-[10px] text-slate-500 font-sans font-normal truncate max-w-xs">
                        {item.title}
                      </div>

                    </td>

                    <td className="p-3 text-slate-700 font-medium">

                      {item.mineName}{' '}

                      <span className="text-[10px] text-slate-500">
                        ({item.zone})
                      </span>

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
                        onClick={() =>
                          setActiveTab('evidence-verification')
                        }
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
