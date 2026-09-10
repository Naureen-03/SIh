import os

mine_overview = """import React, { useState } from 'react';
import {
  Pickaxe,
  ShieldCheck,
  Flame,
  HardHat,
  Leaf,
  Activity,
  Users,
  FileText,
  AlertTriangle,
  CheckCircle2,
  Calendar,
  Layers,
  ArrowUpRight
} from 'lucide-react';
import { useApp } from '../../context/AppContext';
import { Mine } from '../../types';

interface Props {
  setActiveTab: (tab: string) => void;
}

export const MineOverviewPage: React.FC<Props> = ({ setActiveTab }) => {
  const { mines, activeMineId, setActiveMineId } = useApp();
  const [selectedTab, setSelectedTab] = useState<'overview' | 'compliance' | 'safety' | 'environment' | 'production' | 'contractors'>('overview');

  const activeMine = mines.find(m => m.id === activeMineId) || mines[0];

  const tabs = [
    { id: 'overview', label: 'Overview' },
    { id: 'compliance', label: 'Statutory Compliance' },
    { id: 'safety', label: 'Safety & Zones' },
    { id: 'environment', label: 'Environmental' },
    { id: 'production', label: 'Production' },
    { id: 'contractors', label: 'Contractors' },
  ];

  return (
    <div className="space-y-6 pb-12">
      {/* Top Selector Bar */}
      <div className="glass-panel p-5 rounded-2xl border border-slate-800 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <span className="text-[11px] font-extrabold uppercase tracking-widest text-safety-orange">
            Comprehensive Mine Profile
          </span>
          <h1 className="text-2xl font-black text-white mt-0.5">{activeMine.name}</h1>
          <p className="text-xs text-slate-400">
            Subsidiary: <strong className="text-white">{activeMine.subsidiary}</strong> • District: <strong>{activeMine.district}, {activeMine.state}</strong>
          </p>
        </div>

        {/* Mine Switcher Dropdown */}
        <select
          value={activeMine.id}
          onChange={e => setActiveMineId(e.target.value)}
          className="bg-coal-800 text-white font-bold text-xs px-3.5 py-2.5 rounded-xl border border-slate-700 focus:outline-none focus:border-safety-orange"
        >
          {mines.map(m => (
            <option key={m.id} value={m.id}>
              {m.name} ({m.subsidiary})
            </option>
          ))}
        </select>
      </div>

      {/* Governance Health Score Banner */}
      <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3">
        <div className="glass-panel p-4 rounded-xl border border-safety-orange/40 bg-safety-orange/10">
          <span className="text-[10px] font-bold text-safety-orange uppercase tracking-wider">Gov Health Score</span>
          <div className="text-2xl font-black text-white font-mono mt-1">{activeMine.governanceHealthScore} <span className="text-xs text-slate-400">/100</span></div>
          <span className="text-[10px] text-slate-300">Composite Rating</span>
        </div>

        <div className="glass-panel p-4 rounded-xl border border-slate-800">
          <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider">Compliance</span>
          <div className="text-2xl font-black text-emerald-400 font-mono mt-1">{activeMine.complianceScore}%</div>
          <span className="text-[10px] text-slate-400">Statutory Index</span>
        </div>

        <div className="glass-panel p-4 rounded-xl border border-slate-800">
          <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider">AI Risk Index</span>
          <div className="text-2xl font-black text-red-400 font-mono mt-1">{activeMine.riskScore} /100</div>
          <span className="text-[10px] text-slate-400">5-Vector Blend</span>
        </div>

        <div className="glass-panel p-4 rounded-xl border border-slate-800">
          <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider">Open Issues</span>
          <div className="text-2xl font-black text-amber-400 font-mono mt-1">{activeMine.openIssues}</div>
          <span className="text-[10px] text-slate-400">{activeMine.criticalIssues} Critical</span>
        </div>

        <div className="glass-panel p-4 rounded-xl border border-slate-800">
          <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider">Inspections</span>
          <div className="text-2xl font-black text-cyan-400 font-mono mt-1">{activeMine.inspectionsThisMonth}</div>
          <span className="text-[10px] text-slate-400">This Month</span>
        </div>

        <div className="glass-panel p-4 rounded-xl border border-slate-800">
          <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider">Contractors</span>
          <div className="text-2xl font-black text-purple-400 font-mono mt-1">{activeMine.contractorCount}</div>
          <span className="text-[10px] text-slate-400">Active Agencies</span>
        </div>
      </div>

      {/* Tabs Bar */}
      <div className="flex border-b border-slate-800 space-x-1 overflow-x-auto">
        {tabs.map(tab => (
          <button
            key={tab.id}
            onClick={() => setSelectedTab(tab.id as any)}
            className={`px-4 py-2.5 text-xs font-bold transition-all border-b-2 whitespace-nowrap ${
              selectedTab === tab.id
                ? 'border-safety-orange text-safety-orange bg-coal-900/50'
                : 'border-transparent text-slate-400 hover:text-white'
            }`}
          >
            {tab.label}
          </button>
        ))}
      </div>

      {/* Tab Contents */}
      {selectedTab === 'overview' && (
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Active Operational Zones */}
          <div className="glass-panel p-5 rounded-xl border border-slate-800 space-y-4">
            <h3 className="text-sm font-extrabold text-white uppercase tracking-wider">Active Operational Sectors & Zones</h3>
            <div className="space-y-2.5">
              {activeMine.zones.map(z => (
                <div key={z.id} className="p-3 rounded-lg bg-coal-900/90 border border-slate-800 flex items-center justify-between">
                  <div>
                    <p className="text-xs font-bold text-white">{z.name}</p>
                    <span className="text-[10px] text-slate-400 font-mono">{z.type} • {z.activeSensors} Active IoT Telemetry Nodes</span>
                  </div>
                  <span className={`text-[10px] font-bold px-2 py-0.5 rounded ${
                    z.riskLevel === 'Critical' ? 'bg-red-500/20 text-red-400 border border-red-500/30' : 'bg-amber-500/20 text-amber-400'
                  }`}>
                    {z.riskLevel}
                  </span>
                </div>
              ))}
            </div>
          </div>

          {/* Production vs Target */}
          <div className="glass-panel p-5 rounded-xl border border-slate-800 space-y-4">
            <h3 className="text-sm font-extrabold text-white uppercase tracking-wider">Daily Production Run-Rate</h3>
            <div className="space-y-3">
              <div className="flex items-center justify-between text-xs">
                <span className="text-slate-400">Target Output:</span>
                <span className="font-mono font-bold text-white">{activeMine.dailyProductionTargetTons.toLocaleString()} Tons/day</span>
              </div>
              <div className="flex items-center justify-between text-xs">
                <span className="text-slate-400">Actual Extraction:</span>
                <span className="font-mono font-bold text-safety-orange">{activeMine.dailyProductionActualTons.toLocaleString()} Tons/day</span>
              </div>
              <div className="w-full h-3 bg-coal-950 rounded-full overflow-hidden">
                <div
                  className="h-full bg-gradient-to-r from-safety-orange to-amber-500"
                  style={{ width: `${(activeMine.dailyProductionActualTons / activeMine.dailyProductionTargetTons) * 100}%` }}
                />
              </div>
              <p className="text-[11px] text-slate-400">
                Achievement rate: <strong>{((activeMine.dailyProductionActualTons / activeMine.dailyProductionTargetTons) * 100).toFixed(1)}%</strong>
              </p>
            </div>
          </div>
        </div>
      )}

      {selectedTab !== 'overview' && (
        <div className="glass-panel p-6 rounded-xl border border-slate-800 text-center space-y-3">
          <CheckCircle2 className="w-8 h-8 text-emerald-400 mx-auto" />
          <h4 className="text-sm font-bold text-white uppercase">{selectedTab} Details for {activeMine.name}</h4>
          <p className="text-xs text-slate-400 max-w-md mx-auto">
            All real-time streams, telemetry sensors, and compliance dockets are mapped to the central governance pipeline.
          </p>
        </div>
      )}
    </div>
  );
};
"""

gis_map_page = """import React from 'react';
import { GISMap } from '../../components/map/GISMap';
import { Layers, MapPin, ShieldAlert, Sparkles } from 'lucide-react';
import { useApp } from '../../context/AppContext';

export const GISMapPage: React.FC = () => {
  const { mines } = useApp();

  return (
    <div className="space-y-6 pb-12">
      <div className="glass-panel p-5 rounded-2xl border border-slate-800 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2 text-xs text-safety-orange font-bold uppercase tracking-wider">
            <MapPin className="w-4 h-4 text-safety-orange" />
            <span>Interactive Spatial Telemetry</span>
          </div>
          <h1 className="text-2xl font-black text-white mt-1">GIS Smart Mine Map</h1>
          <p className="text-xs text-slate-400 mt-0.5">
            Geographic information monitoring 18 mega open cast & underground mines across 8 Coal India subsidiaries
          </p>
        </div>
      </div>

      <GISMap />

      {/* Basin Clusters Summary */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        {[
          { name: 'Korba Basin (SECL)', mines: 'Gevra, Kusmunda, Dipka', risk: 'High Risk (Conveyor Guarding)', color: 'border-red-500/40 text-red-400' },
          { name: 'Singrauli Basin (NCL)', mines: 'Jayant, Dudhichua, Nigahi', risk: 'Compliant / Stable', color: 'border-emerald-500/40 text-emerald-400' },
          { name: 'Jharia Coalfield (BCCL)', mines: 'Moonidih, Block II', risk: 'Critical Risk (Gas/Ventilation)', color: 'border-red-500/40 text-red-400' },
          { name: 'Talcher Coalfield (MCL)', mines: 'Lakhanpur, Bhubaneswari', risk: 'Moderate Risk (Dust/Water)', color: 'border-amber-500/40 text-amber-400' },
        ].map(basin => (
          <div key={basin.name} className="glass-panel p-4 rounded-xl border border-slate-800 space-y-2">
            <h4 className="text-xs font-bold text-white">{basin.name}</h4>
            <p className="text-[11px] text-slate-400">{basin.mines}</p>
            <div className={`text-[10px] font-extrabold px-2 py-0.5 rounded border inline-block ${basin.color}`}>
              {basin.risk}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

risk_zones_page = """import React from 'react';
import { AlertTriangle, Flame, ShieldAlert, Zap, ArrowUpRight } from 'lucide-react';
import { useApp } from '../../context/AppContext';

interface Props {
  setActiveTab: (tab: string) => void;
}

export const RiskZonesPage: React.FC<Props> = ({ setActiveTab }) => {
  const { mines } = useApp();

  const allZones = mines.flatMap(m => m.zones.map(z => ({ ...z, mineName: m.name, subsidiary: m.subsidiary })));
  const criticalZones = allZones.filter(z => z.riskLevel === 'Critical');

  return (
    <div className="space-y-6 pb-12">
      <div className="glass-panel p-5 rounded-2xl border border-slate-800">
        <div className="flex items-center space-x-2 text-xs text-red-500 font-bold uppercase tracking-wider">
          <Flame className="w-4 h-4 text-red-500" />
          <span>Geofenced High-Risk Zones</span>
        </div>
        <h1 className="text-2xl font-black text-white mt-1">Operational Risk Zones</h1>
        <p className="text-xs text-slate-400 mt-0.5">
          Real-time perimeter monitoring of active conveyor drives, deep pit slopes, blasting perimeters, and gassy underground panels.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {allZones.map((zone, idx) => (
          <div
            key={idx}
            className={`glass-panel p-5 rounded-xl border transition-all ${
              zone.riskLevel === 'Critical'
                ? 'border-red-500/40 bg-red-950/15'
                : 'border-slate-800 hover:border-slate-700'
            }`}
          >
            <div className="flex items-center justify-between pb-3 border-b border-slate-800">
              <span className={`text-[10px] font-extrabold px-2 py-0.5 rounded uppercase ${
                zone.riskLevel === 'Critical' ? 'bg-red-500 text-white' : 'bg-amber-500 text-black'
              }`}>
                {zone.riskLevel} RISK
              </span>
              <span className="text-[10px] text-slate-400 font-mono">{zone.type}</span>
            </div>

            <div className="space-y-2 mt-3">
              <h4 className="text-sm font-extrabold text-white">{zone.name}</h4>
              <p className="text-xs text-slate-400">{zone.mineName} ({zone.subsidiary})</p>
              <div className="flex items-center justify-between text-xs pt-2 text-slate-300 font-mono">
                <span>Active IoT Sensors:</span>
                <strong className="text-safety-orange">{zone.activeSensors} Nodes</strong>
              </div>
            </div>

            <div className="mt-4 pt-3 border-t border-slate-800 flex justify-end">
              <button
                onClick={() => setActiveTab('new-inspection')}
                className="text-xs text-safety-orange font-bold hover:underline flex items-center space-x-1"
              >
                <span>Trigger Zone Audit</span>
                <ArrowUpRight className="w-3.5 h-3.5" />
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

compliance_tracker = """import React, { useState } from 'react';
import { ShieldCheck, Filter, AlertTriangle, FileText, CheckCircle2, ClockAlert, Search } from 'lucide-react';
import { useApp } from '../../context/AppContext';
import { ComplianceStatus, SeverityLevel } from '../../types';

export const ComplianceTrackerPage: React.FC = () => {
  const { rules } = useApp();
  const [searchTerm, setSearchTerm] = useState('');
  const [filterStatus, setFilterStatus] = useState<string>('ALL');

  const filteredRules = rules.filter(r => {
    const matchesSearch = r.title.toLowerCase().includes(searchTerm.toLowerCase()) || r.ruleCode.toLowerCase().includes(searchTerm.toLowerCase()) || r.mineName.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesStatus = filterStatus === 'ALL' || r.status === filterStatus;
    return matchesSearch && matchesStatus;
  });

  return (
    <div className="space-y-6 pb-12">
      <div className="glass-panel p-5 rounded-2xl border border-slate-800 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2 text-xs text-emerald-400 font-bold uppercase tracking-wider">
            <ShieldCheck className="w-4 h-4 text-emerald-400" />
            <span>Statutory Compliance Matrix</span>
          </div>
          <h1 className="text-2xl font-black text-white mt-1">Compliance Tracker</h1>
          <p className="text-xs text-slate-400 mt-0.5">
            DGMS, MoEFCC, Mines Act 1952, Coal Mines Regulations 2017 & Labour Acts
          </p>
        </div>

        {/* Filters */}
        <div className="flex items-center space-x-2 w-full sm:w-auto">
          <div className="relative flex-1 sm:w-64">
            <Search className="w-3.5 h-3.5 text-slate-400 absolute left-3 top-3" />
            <input
              type="text"
              placeholder="Search rule, mine, code..."
              value={searchTerm}
              onChange={e => setSearchTerm(e.target.value)}
              className="w-full bg-coal-800 border border-slate-700 rounded-xl pl-9 pr-3 py-2 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-safety-orange"
            />
          </div>

          <select
            value={filterStatus}
            onChange={e => setFilterStatus(e.target.value)}
            className="bg-coal-800 text-white font-bold text-xs px-3 py-2 rounded-xl border border-slate-700"
          >
            <option value="ALL">All Statuses</option>
            <option value="Compliant">Compliant</option>
            <option value="Due Soon">Due Soon</option>
            <option value="Overdue">Overdue</option>
            <option value="Non-Compliant">Non-Compliant</option>
          </select>
        </div>
      </div>

      {/* Rules Table */}
      <div className="glass-panel rounded-xl border border-slate-800 overflow-hidden shadow-xl">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="bg-coal-900 border-b border-slate-800 text-slate-400 font-extrabold uppercase tracking-wider text-[10px]">
              <tr>
                <th className="p-3.5">Code & Regulation</th>
                <th className="p-3.5">Requirement Title</th>
                <th className="p-3.5">Mine & Dept</th>
                <th className="p-3.5">Responsible Officer</th>
                <th className="p-3.5">Due Date</th>
                <th className="p-3.5">Status</th>
                <th className="p-3.5">Risk Level</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60">
              {filteredRules.map(rule => (
                <tr key={rule.id} className="hover:bg-coal-800/40 transition-colors">
                  <td className="p-3.5">
                    <span className="font-mono font-bold text-white text-xs">{rule.ruleCode}</span>
                    <p className="text-[10px] text-slate-400">{rule.regulationBody}</p>
                  </td>
                  <td className="p-3.5 max-w-xs">
                    <p className="font-bold text-white">{rule.title}</p>
                    <span className="text-[10px] text-slate-400">{rule.sectionRef}</span>
                  </td>
                  <td className="p-3.5">
                    <p className="text-slate-200 font-semibold">{rule.mineName}</p>
                    <span className="text-[10px] text-slate-400">{rule.department}</span>
                  </td>
                  <td className="p-3.5 text-slate-300 font-medium">
                    {rule.responsibleOfficer}
                  </td>
                  <td className="p-3.5 font-mono text-slate-300">
                    {rule.dueDate}
                  </td>
                  <td className="p-3.5">
                    <span className={`text-[10px] font-extrabold px-2 py-0.5 rounded ${
                      rule.status === 'Compliant' ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30' :
                      rule.status === 'Due Soon' ? 'bg-amber-500/20 text-amber-400 border border-amber-500/30' :
                      rule.status === 'Overdue' ? 'bg-red-500/20 text-red-400 border border-red-500/30' :
                      'bg-red-600 text-white'
                    }`}>
                      {rule.status}
                    </span>
                  </td>
                  <td className="p-3.5">
                    <span className={`text-[10px] font-bold ${
                      rule.riskLevel === 'Critical' ? 'text-red-400' : rule.riskLevel === 'High' ? 'text-amber-400' : 'text-slate-400'
                    }`}>
                      {rule.riskLevel}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
"""

statutory_reqs = """import React from 'react';
import { BookOpen, ShieldCheck, FileCheck2, ExternalLink } from 'lucide-react';

export const StatutoryReqsPage: React.FC = () => {
  const regulations = [
    {
      body: 'Coal Mines Regulations 2017 (CMR 2017)',
      authority: 'DGMS / Ministry of Labour & Employment',
      desc: 'Primary safety standard for mechanised open cast and underground coal extraction, haulage machinery guarding, and ventilation.',
      keySections: ['Regulation 104: Machinery Fencing', 'Regulation 153: Gassy Mine Ventilation', 'Regulation 112: Incline Haulage Track Safety']
    },
    {
      body: 'Mines Act 1952',
      authority: 'Parliament of India / DGMS',
      desc: 'Fundamental statutory framework governing employment conditions, maximum weekly working hours, inspections, and accident inquiries.',
      keySections: ['Section 22: Urgent Danger Notices', 'Section 23: Accident Notification (Form IV-A)', 'Section 28: Weekly Day of Rest']
    },
    {
      body: 'Environment (Protection) Act 1986 & EIA Notification 2006',
      authority: 'MoEFCC / Central Pollution Control Board',
      desc: 'Mandatory statutory environmental clearances, half-yearly compliance audits, ambient PM10/PM2.5 limits, and progressive afforestation.',
      keySections: ['Condition VI(a): Half-Yearly EC Compliance', 'CAAQMS Real-time Data Upload to CPCB']
    },
    {
      body: 'Contract Labour (Regulation and Abolition) Act 1970',
      authority: 'Chief Labour Commissioner (Central)',
      desc: 'Mandates Form B worker registry, equal pay for equal work, mandatory VTC safety training, and periodic medical examination (PME).',
      keySections: ['Rule 75: Form B Master Register', 'Rule 25: Minimum Statutory Amenities']
    }
  ];

  return (
    <div className="space-y-6 pb-12">
      <div className="glass-panel p-5 rounded-2xl border border-slate-800">
        <div className="flex items-center space-x-2 text-xs text-safety-orange font-bold uppercase tracking-wider">
          <BookOpen className="w-4 h-4 text-safety-orange" />
          <span>Statutory Rulebook & Legal Citations</span>
        </div>
        <h1 className="text-2xl font-black text-white mt-1">Regulatory Standards Repository</h1>
        <p className="text-xs text-slate-400 mt-0.5">
          Official statutory guidelines and legal compliance thresholds governing the Indian coal mining industry
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {regulations.map(reg => (
          <div key={reg.body} className="glass-panel p-5 rounded-xl border border-slate-800 space-y-3">
            <div className="flex items-center justify-between">
              <h3 className="text-sm font-extrabold text-white">{reg.body}</h3>
              <span className="text-[10px] bg-coal-800 text-slate-400 font-mono px-2 py-0.5 rounded">Statutory</span>
            </div>
            <p className="text-[11px] text-safety-orange font-semibold">{reg.authority}</p>
            <p className="text-xs text-slate-300 leading-relaxed">{reg.desc}</p>
            <div className="pt-2 border-t border-slate-800/80 space-y-1">
              <span className="text-[10px] font-bold text-slate-400 uppercase">Key Enforced Sections:</span>
              <div className="space-y-1">
                {reg.keySections.map((sec, idx) => (
                  <div key={idx} className="text-xs font-mono text-slate-300 flex items-center space-x-2">
                    <span className="text-safety-orange">•</span>
                    <span>{sec}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

compliance_calendar = """import React from 'react';
import { Calendar as CalendarIcon, Clock, AlertTriangle, ShieldCheck } from 'lucide-react';

export const ComplianceCalendarPage: React.FC = () => {
  const deadlines = [
    { date: '02 Sep 2026', title: 'DGMS Notice of Dangerous Occurrences (Form IV-A)', mine: 'Gevra Mine', type: 'Safety Filing', status: 'On Track' },
    { date: '05 Sep 2026', title: 'Conveyor Trunk Line 4B Mesh Guarding Rectification', mine: 'Gevra Mine', type: 'Corrective Action', status: 'Urgent SLA' },
    { date: '08 Sep 2026', title: 'PESO Bulk Explosives Storage License Renewal', mine: 'Gevra Mine', type: 'License Renewal', status: 'Critical Expiry' },
    { date: '10 Sep 2026', title: 'Contractor Form B Labour Registry Monthly Audit', mine: 'SECL Korba Area', type: 'Labour Audit', status: 'Upcoming' },
    { date: '15 Sep 2026', title: 'MoEFCC Half-Yearly Environmental Clearance Compliance', mine: 'Gevra Mine (70 MTPA)', type: 'Environmental Return', status: 'Statutory Filing' },
    { date: '18 Sep 2026', title: 'CECB Water Discharge Effluent Quality Submission', mine: 'Korba Area ETP', type: 'Pollution Board', status: 'Scheduled' }
  ];

  return (
    <div className="space-y-6 pb-12">
      <div className="glass-panel p-5 rounded-2xl border border-slate-800">
        <div className="flex items-center space-x-2 text-xs text-safety-cyan font-bold uppercase tracking-wider">
          <CalendarIcon className="w-4 h-4 text-safety-cyan" />
          <span>Statutory Schedule</span>
        </div>
        <h1 className="text-2xl font-black text-white mt-1">Compliance Calendar</h1>
        <p className="text-xs text-slate-400 mt-0.5">
          Upcoming statutory deadlines, license renewals, DGMS safety returns, and environmental filings
        </p>
      </div>

      <div className="space-y-3">
        {deadlines.map((item, idx) => (
          <div
            key={idx}
            className="glass-panel p-4 rounded-xl border border-slate-800 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 hover:border-slate-700 transition-all"
          >
            <div className="flex items-center space-x-4">
              <div className="w-14 h-14 rounded-xl bg-coal-800 border border-slate-700 flex flex-col items-center justify-center text-center font-mono">
                <span className="text-[10px] text-slate-400 uppercase">{item.date.split(' ')[1]}</span>
                <span className="text-lg font-black text-white">{item.date.split(' ')[0]}</span>
              </div>
              <div>
                <h4 className="text-xs font-bold text-white">{item.title}</h4>
                <p className="text-[11px] text-slate-400">{item.mine} • <span className="text-safety-orange font-semibold">{item.type}</span></p>
              </div>
            </div>

            <span className={`text-[10px] font-extrabold px-3 py-1 rounded-full uppercase ${
              item.status.includes('Critical') || item.status.includes('Urgent')
                ? 'bg-red-500/20 text-red-400 border border-red-500/30'
                : 'bg-coal-800 text-slate-300 border border-slate-700'
            }`}>
              {item.status}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

statutory_reports = """import React from 'react';
import { FileText, Download, Share2, Eye, CheckCircle2 } from 'lucide-react';

export const StatutoryReportsPage: React.FC = () => {
  const reports = [
    { title: 'Form IV — Annual Safety & Occupational Health Return', authority: 'DGMS', period: 'FY 2025-26', size: '2.4 MB', date: '15 Aug 2026' },
    { title: 'MoEFCC Half-Yearly Environmental Clearance Compliance Docket', authority: 'MoEFCC', period: 'Apr - Sep 2026', size: '8.1 MB', date: '25 Aug 2026' },
    { title: 'Form VI — Notice of Accidents and Fatal Occurrences Registry', authority: 'DGMS', period: 'Q2 2026', size: '1.2 MB', date: '28 Aug 2026' },
    { title: 'State Pollution Control Board Environmental Statement (Form V)', authority: 'CECB', period: 'Annual 2026', size: '3.6 MB', date: '10 Aug 2026' }
  ];

  return (
    <div className="space-y-6 pb-12">
      <div className="glass-panel p-5 rounded-2xl border border-slate-800 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2 text-xs text-safety-orange font-bold uppercase tracking-wider">
            <FileText className="w-4 h-4 text-safety-orange" />
            <span>Digital Document Archive</span>
          </div>
          <h1 className="text-2xl font-black text-white mt-1">Statutory Reports & Returns</h1>
          <p className="text-xs text-slate-400 mt-0.5">
            Auto-compiled Form IV, Form VI, DGMS Returns, and MoEFCC clearances with digital signatures
          </p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {reports.map((rep, idx) => (
          <div key={idx} className="glass-panel p-5 rounded-xl border border-slate-800 space-y-4">
            <div className="flex items-start justify-between">
              <div className="space-y-1">
                <span className="text-[10px] font-bold bg-safety-orange/15 text-safety-orange px-2 py-0.5 rounded font-mono">
                  {rep.authority}
                </span>
                <h3 className="text-sm font-extrabold text-white mt-1">{rep.title}</h3>
                <p className="text-xs text-slate-400 font-mono">Period: {rep.period} • {rep.size}</p>
              </div>
              <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
            </div>

            <div className="flex items-center justify-between pt-3 border-t border-slate-800 text-xs">
              <span className="text-slate-500 font-mono text-[11px]">Generated {rep.date}</span>
              <div className="flex space-x-2">
                <button className="flex items-center space-x-1 px-3 py-1.5 rounded-lg bg-coal-800 text-slate-300 hover:text-white border border-slate-700 font-bold text-[11px]">
                  <Eye className="w-3.5 h-3.5" />
                  <span>Preview</span>
                </button>
                <button className="flex items-center space-x-1 px-3 py-1.5 rounded-lg bg-safety-orange text-white font-bold text-[11px] hover:bg-safety-orange/90">
                  <Download className="w-3.5 h-3.5" />
                  <span>Export PDF</span>
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

with open('src/pages/MineOperations/MineOverviewPage.tsx', 'w', encoding='utf-8') as f:
    f.write(mine_overview)

with open('src/pages/MineOperations/GISMapPage.tsx', 'w', encoding='utf-8') as f:
    f.write(gis_map_page)

with open('src/pages/MineOperations/RiskZonesPage.tsx', 'w', encoding='utf-8') as f:
    f.write(risk_zones_page)

with open('src/pages/Compliance/ComplianceTrackerPage.tsx', 'w', encoding='utf-8') as f:
    f.write(compliance_tracker)

with open('src/pages/Compliance/StatutoryReqsPage.tsx', 'w', encoding='utf-8') as f:
    f.write(statutory_reqs)

with open('src/pages/Compliance/ComplianceCalendarPage.tsx', 'w', encoding='utf-8') as f:
    f.write(compliance_calendar)

with open('src/pages/Compliance/StatutoryReportsPage.tsx', 'w', encoding='utf-8') as f:
    f.write(statutory_reports)

print("MineOperations and Compliance pages written successfully!")
