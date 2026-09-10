import React, { useState } from 'react';
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
