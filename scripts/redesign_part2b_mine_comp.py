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
  MapPin,
  Calendar,
  Layers,
  ArrowUpRight
} from 'lucide-react';
import { useApp } from '../../context/AppContext';
import { ClosedLoopVisualizer } from '../../components/visualizer/ClosedLoopVisualizer';
import { RiskScoreCard } from '../../components/visualizer/RiskScoreCard';
import { GISMap } from '../../components/map/GISMap';

interface Props {
  setActiveTab: (tab: string) => void;
}

export const MineOverviewPage: React.FC<Props> = ({ setActiveTab }) => {
  const { mines, issues, contractors } = useApp();
  const [selectedMineId, setSelectedMineId] = useState<string>('mine-101');

  const currentMine = mines.find(m => m.id === selectedMineId) || mines[0];
  const mineIssues = issues.filter(i => i.mineId === currentMine.id);
  const mineContractors = contractors.filter(c => c.mineId === currentMine.id);

  return (
    <div className="space-y-6 pb-12">
      {/* Header with Mine Selector */}
      <div className="gov-card p-5 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
            <Pickaxe className="w-4 h-4 text-[#0B2545]" />
            <span>Operational Mine Profile & Statutory Ledger</span>
          </div>
          <h1 className="text-2xl font-black text-slate-900 mt-1">{currentMine.name}</h1>
          <p className="text-xs text-slate-600 mt-0.5">
            Subsidiary: <strong>{currentMine.subsidiary}</strong> &bull; Mining Type: <strong>{currentMine.type}</strong> &bull; Annual Peak Target: <strong>{currentMine.annualProductionTargetMTPA} MTPA</strong>
          </p>
        </div>

        <div className="flex items-center space-x-2 w-full sm:w-auto">
          <label className="text-xs font-bold text-slate-700 uppercase whitespace-nowrap">Select Mine:</label>
          <select
            value={selectedMineId}
            onChange={e => setSelectedMineId(e.target.value)}
            className="bg-slate-50 border border-slate-300 rounded px-3 py-1.5 text-xs text-slate-900 font-bold focus:outline-none focus:border-[#0B2545] w-full sm:w-64"
          >
            {mines.map(m => (
              <option key={m.id} value={m.id}>
                {m.name} ({m.subsidiary})
              </option>
            ))}
          </select>
        </div>
      </div>

      {/* 4 Stat Cards */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs">
        <div className="gov-card p-3 space-y-1">
          <span className="text-[10px] text-slate-500 uppercase font-bold">Statutory Compliance</span>
          <div className="text-xl font-black text-emerald-800 font-mono">{currentMine.complianceScore}%</div>
          <p className="text-[10px] text-slate-500">DGMS Verified</p>
        </div>
        <div className="gov-card p-3 space-y-1">
          <span className="text-[10px] text-slate-500 uppercase font-bold">AI Risk Index</span>
          <div className="text-xl font-black text-red-700 font-mono">{currentMine.riskScore} / 100</div>
          <p className="text-[10px] text-slate-500">High Risk Threshold</p>
        </div>
        <div className="gov-card p-3 space-y-1">
          <span className="text-[10px] text-slate-500 uppercase font-bold">Active Workforce</span>
          <div className="text-xl font-black text-slate-900 font-mono">{currentMine.activeWorkers.toLocaleString()}</div>
          <p className="text-[10px] text-slate-500">Form B Verified</p>
        </div>
        <div className="gov-card p-3 space-y-1">
          <span className="text-[10px] text-slate-500 uppercase font-bold">Open Corrective Actions</span>
          <div className="text-xl font-black text-amber-800 font-mono">{currentMine.openIssuesCount}</div>
          <p className="text-[10px] text-slate-500">{currentMine.openCriticalCount} Critical SLA</p>
        </div>
      </div>

      {/* Explainable Risk Meter */}
      <RiskScoreCard mine={currentMine} />

      {/* GIS Location & Geo-Fenced Sectors */}
      <div className="space-y-3">
        <h3 className="text-xs font-extrabold uppercase tracking-wider text-slate-800">
          Geospatial Map & Active Extraction Faces
        </h3>
        <GISMap mines={[currentMine]} selectedMine={currentMine} />
      </div>
    </div>
  );
};
"""

gis_page = """import React from 'react';
import { MapPin, Layers, ShieldAlert, Sparkles, Filter } from 'lucide-react';
import { useApp } from '../../context/AppContext';
import { GISMap } from '../../components/map/GISMap';

export const GISMapPage: React.FC = () => {
  const { mines } = useApp();

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
          <MapPin className="w-4 h-4 text-[#0B2545]" />
          <span>National Geospatial Mining Cadastre</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Coal Mine GIS Monitoring</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Geospatial monitoring of mine locations, inspections, incidents and statutory compliance risks across all Indian coal basins.
        </p>
      </div>

      <GISMap mines={mines} />
    </div>
  );
};
"""

risk_zones = """import React from 'react';
import { AlertTriangle, MapPin, ShieldAlert, Zap } from 'lucide-react';
import { useApp } from '../../context/AppContext';

interface Props {
  setActiveTab: (tab: string) => void;
}

export const RiskZonesPage: React.FC<Props> = ({ setActiveTab }) => {
  const { riskZones } = useApp();

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-red-700 font-extrabold uppercase tracking-wider">
          <ShieldAlert className="w-4 h-4 text-red-700" />
          <span>Geofenced High-Risk Sectors</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Identified Risk Zones & Hazard Clusters</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Continuous geospatial telemetry monitoring of conveyor galleries, overburden slope benches, and underground ventilation districts.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {riskZones.map(zone => (
          <div
            key={zone.id}
            className={`gov-card p-4 space-y-3 ${
              zone.severity === 'Critical' ? 'border-red-300 bg-red-50/30' : 'border-slate-200'
            }`}
          >
            <div className="flex items-start justify-between">
              <div>
                <span className="text-[10px] font-bold bg-slate-100 text-slate-700 px-2 py-0.5 rounded font-mono">
                  {zone.mineName}
                </span>
                <h3 className="text-sm font-extrabold text-slate-900 mt-1">{zone.name}</h3>
                <p className="text-[11px] text-slate-500 font-mono">Location: {zone.location}</p>
              </div>

              <span className={`text-[10px] font-extrabold px-2 py-0.5 rounded uppercase ${
                zone.severity === 'Critical' ? 'bg-red-700 text-white' : 'bg-amber-600 text-white'
              }`}>
                {zone.severity} Risk ({zone.riskScore}/100)
              </span>
            </div>

            <div className="p-2.5 bg-white rounded border border-slate-200 text-xs space-y-1">
              <span className="font-bold text-slate-900">Hazard Description:</span>
              <p className="text-slate-600 text-[11px]">{zone.description}</p>
            </div>

            <div className="p-2.5 bg-slate-50 rounded border border-slate-200 text-xs">
              <span className="font-bold text-[#0B2545]">Required Statutory Control:</span>
              <p className="text-slate-700 text-[11px] mt-0.5">{zone.remedialAction}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

compliance_tracker = """import React, { useState } from 'react';
import {
  ShieldCheck,
  Search,
  Filter,
  Download,
  AlertTriangle,
  FileCheck2,
  Calendar,
  Building2
} from 'lucide-react';
import { useApp } from '../../context/AppContext';
import { STATUTORY_COMPLIANCE_RULES } from '../../data/mockData';

export const ComplianceTrackerPage: React.FC = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCategory, setSelectedCategory] = useState<string>('All');
  const [selectedStatus, setSelectedStatus] = useState<string>('All');

  const filteredRules = STATUTORY_COMPLIANCE_RULES.filter(rule => {
    if (selectedCategory !== 'All' && rule.category !== selectedCategory) return false;
    if (selectedStatus !== 'All' && rule.status !== selectedStatus) return false;
    if (searchTerm && !rule.title.toLowerCase().includes(searchTerm.toLowerCase()) && !rule.ruleCode.toLowerCase().includes(searchTerm.toLowerCase())) return false;
    return true;
  });

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
            <ShieldCheck className="w-4 h-4 text-[#0B2545]" />
            <span>National Statutory Compliance Matrix</span>
          </div>
          <h1 className="text-2xl font-black text-slate-900 mt-1">Statutory Compliance Register</h1>
          <p className="text-xs text-slate-600 mt-0.5">
            Searchable legal compliance register covering Coal Mines Regulations 2017, Mines Act 1952, and MoEFCC clearance conditions.
          </p>
        </div>

        <button className="gov-btn-primary">
          <Download className="w-3.5 h-3.5" />
          <span>Export Compliance Audit PDF</span>
        </button>
      </div>

      {/* Filter Bar */}
      <div className="gov-card p-3 flex flex-wrap items-center justify-between gap-3 text-xs">
        <div className="flex flex-wrap items-center gap-2">
          <input
            type="text"
            placeholder="Search regulation, act code, keywords..."
            value={searchTerm}
            onChange={e => setSearchTerm(e.target.value)}
            className="bg-slate-50 border border-slate-300 rounded px-3 py-1.5 text-xs text-slate-900 placeholder-slate-400 focus:outline-none focus:border-[#0B2545] w-64"
          />

          <select
            value={selectedCategory}
            onChange={e => setSelectedCategory(e.target.value)}
            className="bg-slate-50 border border-slate-300 rounded px-3 py-1.5 text-xs text-slate-900 font-bold focus:outline-none focus:border-[#0B2545]"
          >
            <option value="All">All Categories</option>
            <option value="Safety">Safety Regulations</option>
            <option value="Environment">Environmental Clearances</option>
            <option value="Labour">Labour & Welfare</option>
            <option value="Operational">Operational Clearances</option>
          </select>
        </div>

        <div className="text-xs font-mono text-slate-600">
          Showing <strong>{filteredRules.length}</strong> of {STATUTORY_COMPLIANCE_RULES.length} statutory mandates
        </div>
      </div>

      {/* Compliance Register Table */}
      <div className="gov-card overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="bg-slate-50 border-b border-slate-200 text-slate-700 font-bold uppercase tracking-wider text-[10px]">
              <tr>
                <th className="p-3">Statutory Rule Code</th>
                <th className="p-3">Regulation Title</th>
                <th className="p-3">Governing Act</th>
                <th className="p-3">Enforcing Authority</th>
                <th className="p-3">Applicable Scope</th>
                <th className="p-3">Frequency</th>
                <th className="p-3">Compliance Status</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-200">
              {filteredRules.map(rule => (
                <tr key={rule.id} className="hover:bg-slate-50/80 transition-colors">
                  <td className="p-3 font-mono font-bold text-slate-900">{rule.ruleCode}</td>
                  <td className="p-3 font-bold text-slate-900">
                    <div>{rule.title}</div>
                    <div className="text-[10px] text-slate-500 font-normal">{rule.description}</div>
                  </td>
                  <td className="p-3 text-slate-700">{rule.act}</td>
                  <td className="p-3 font-bold text-[#0B2545]">{rule.authority}</td>
                  <td className="p-3 text-slate-600">{rule.applicableTo}</td>
                  <td className="p-3 font-mono text-slate-600">{rule.frequency}</td>
                  <td className="p-3">
                    <span className={`text-[10px] font-extrabold px-2 py-0.5 rounded uppercase ${
                      rule.status === 'Compliant'
                        ? 'bg-emerald-50 text-emerald-800 border border-emerald-300'
                        : rule.status === 'Overdue'
                        ? 'bg-red-50 text-red-800 border border-red-300'
                        : 'bg-amber-50 text-amber-800 border border-amber-300'
                    }`}>
                      {rule.status}
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
import { FileCheck2, BookOpen, ExternalLink, ShieldCheck } from 'lucide-react';
import { STATUTORY_COMPLIANCE_RULES } from '../../data/mockData';

export const StatutoryReqsPage: React.FC = () => {
  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
          <BookOpen className="w-4 h-4 text-[#0B2545]" />
          <span>Regulatory Rulebook & Legal Citations</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Statutory Requirements & Mandates</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Official statutory citations across DGMS (Directorate General of Mines Safety), MoEFCC, and Central Pollution Control Board (CPCB).
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {STATUTORY_COMPLIANCE_RULES.map(rule => (
          <div key={rule.id} className="gov-card p-4 space-y-3">
            <div className="flex items-start justify-between">
              <div>
                <span className="text-[10px] font-bold bg-[#0B2545] text-white px-2 py-0.5 rounded font-mono">
                  {rule.ruleCode}
                </span>
                <h3 className="text-sm font-extrabold text-slate-900 mt-1">{rule.title}</h3>
                <p className="text-[11px] text-slate-500">{rule.act} &bull; {rule.authority}</p>
              </div>
              <span className="text-[10px] font-bold px-2 py-0.5 rounded bg-emerald-50 text-emerald-800 border border-emerald-300">
                {rule.penaltyClause ? 'Strict Liability' : 'Standard Mandate'}
              </span>
            </div>

            <p className="text-xs text-slate-700 leading-relaxed">{rule.description}</p>

            <div className="p-2.5 bg-slate-50 rounded border border-slate-200 text-xs">
              <span className="font-bold text-red-800">Statutory Non-Compliance Penalty:</span>
              <p className="text-slate-700 text-[11px] mt-0.5">{rule.penaltyClause}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

compliance_cal = """import React from 'react';
import { Calendar, Clock, AlertTriangle, CheckCircle2 } from 'lucide-react';
import { STATUTORY_COMPLIANCE_RULES } from '../../data/mockData';

export const ComplianceCalendarPage: React.FC = () => {
  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
          <Calendar className="w-4 h-4 text-[#0B2545]" />
          <span>Statutory Filing & Return Calendar</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Compliance Filing Calendar</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Upcoming deadlines for DGMS Form IV safety returns, MoEFCC six-monthly compliance reports, and Consent to Operate renewals.
        </p>
      </div>

      <div className="space-y-3">
        {STATUTORY_COMPLIANCE_RULES.map(rule => (
          <div
            key={rule.id}
            className="gov-card p-4 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3"
          >
            <div className="space-y-1">
              <div className="flex items-center space-x-2">
                <span className="font-mono font-bold text-slate-900 text-xs">{rule.ruleCode}</span>
                <span className="text-[10px] bg-slate-100 text-slate-700 px-2 py-0.5 rounded">{rule.authority}</span>
              </div>
              <h3 className="text-xs font-bold text-slate-900">{rule.title}</h3>
              <p className="text-[11px] text-slate-500">Statutory Frequency: {rule.frequency}</p>
            </div>

            <div className="flex items-center space-x-3 self-end sm:self-auto">
              <div className="text-right">
                <span className="text-[10px] text-slate-500 block">Due Date</span>
                <span className="font-mono font-bold text-slate-900 text-xs">15 Sep 2026</span>
              </div>
              <button className="gov-btn-primary text-xs py-1 px-3">
                File Docket
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

statutory_reports = """import React from 'react';
import { FileText, Download, CheckCircle2, Building2 } from 'lucide-react';

export const StatutoryReportsPage: React.FC = () => {
  const reports = [
    { code: 'FORM-IV', title: 'DGMS Annual Safety Return (Mines Act 1952)', period: 'Annual 2025-26', status: 'Submitted & Acknowledged' },
    { code: 'FORM-VI', title: 'Notice of Accident / Serious Bodily Injury Register', period: 'August 2026', status: 'Up to date' },
    { code: 'EC-RETURNS', title: 'MoEFCC Six-Monthly Environmental Compliance Return', period: 'Apr - Sep 2026', status: 'Draft Ready' },
    { code: 'FORM-B', title: 'Register of Employees (Contract Labour Act, 1970)', period: 'August 2026', status: 'Biometric Verified' },
  ];

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
          <FileText className="w-4 h-4 text-[#0B2545]" />
          <span>Statutory Returns & Form Submissions</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Official Statutory Reports Archive</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Standardized digital forms complying with Directorate General of Mines Safety and MoEFCC formats.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {reports.map(rep => (
          <div key={rep.code} className="gov-card p-4 space-y-3">
            <div className="flex items-start justify-between">
              <div>
                <span className="text-[10px] font-bold bg-[#0B2545] text-white px-2 py-0.5 rounded font-mono">
                  {rep.code}
                </span>
                <h3 className="text-sm font-extrabold text-slate-900 mt-1">{rep.title}</h3>
                <p className="text-[11px] text-slate-500 font-mono">Period: {rep.period}</p>
              </div>
              <span className="text-[10px] font-bold px-2 py-0.5 rounded bg-emerald-50 text-emerald-800 border border-emerald-300">
                {rep.status}
              </span>
            </div>

            <div className="flex justify-end space-x-2 pt-2 border-t border-slate-200">
              <button className="gov-btn-secondary text-xs py-1 px-3">
                Preview Form
              </button>
              <button className="gov-btn-primary text-xs py-1 px-3">
                <Download className="w-3.5 h-3.5" />
                <span>Download Signed PDF</span>
              </button>
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
    f.write(gis_page)

with open('src/pages/MineOperations/RiskZonesPage.tsx', 'w', encoding='utf-8') as f:
    f.write(risk_zones)

with open('src/pages/Compliance/ComplianceTrackerPage.tsx', 'w', encoding='utf-8') as f:
    f.write(compliance_tracker)

with open('src/pages/Compliance/StatutoryReqsPage.tsx', 'w', encoding='utf-8') as f:
    f.write(statutory_reqs)

with open('src/pages/Compliance/ComplianceCalendarPage.tsx', 'w', encoding='utf-8') as f:
    f.write(compliance_cal)

with open('src/pages/Compliance/StatutoryReportsPage.tsx', 'w', encoding='utf-8') as f:
    f.write(statutory_reports)

print("Part 2b: Mine Operations and Compliance pages written successfully!")
