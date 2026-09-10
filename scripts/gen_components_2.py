import os

risk_card = """import React from 'react';
import {
  ShieldAlert,
  AlertTriangle,
  Info,
  TrendingUp,
  Flame,
  CheckCircle2
} from 'lucide-react';
import { Mine } from '../../types';

interface Props {
  mine: Mine;
}

export const RiskScoreCard: React.FC<Props> = ({ mine }) => {
  const breakdown = mine.riskBreakdown || {
    safety: 86,
    environment: 64,
    labour: 52,
    production: 61,
    contractor: 73
  };

  const waterfallFactors = [
    { factor: 'Recurring conveyor safety violations', points: '+20', positive: false },
    { factor: 'Overdue statutory corrective actions', points: '+15', positive: false },
    { factor: 'Contractor documentation & VTC gaps', points: '+10', positive: false },
    { factor: 'Upcoming statutory MoEFCC deadlines', points: '+8', positive: false },
    { factor: 'Recent successful DGMS quarterly audit', points: '-5', positive: true },
  ];

  return (
    <div className="glass-panel p-5 rounded-xl border border-slate-800 shadow-xl space-y-5">
      {/* Top Header & Gauge */}
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between pb-4 border-b border-slate-800 gap-4">
        <div>
          <div className="flex items-center space-x-2">
            <ShieldAlert className="w-5 h-5 text-red-500" />
            <h3 className="text-sm font-extrabold uppercase tracking-wider text-white">
              Explainable AI Risk Score
            </h3>
          </div>
          <p className="text-xs text-slate-400 mt-0.5">
            Real-time neural risk quantification across 5 statutory vectors
          </p>
        </div>

        <div className="flex items-center space-x-3 bg-coal-900/90 px-4 py-2 rounded-xl border border-red-500/30">
          <div>
            <div className="text-2xl font-black text-white font-mono">{mine.riskScore} <span className="text-xs text-slate-400 font-normal">/ 100</span></div>
            <div className="text-[10px] font-extrabold tracking-widest text-red-400 uppercase">
              {mine.riskScore > 70 ? 'CRITICAL RISK' : 'HIGH RISK'}
            </div>
          </div>
          <div className="w-12 h-12 rounded-full border-4 border-red-500 border-t-transparent animate-spin flex items-center justify-center">
            <Flame className="w-5 h-5 text-red-500" />
          </div>
        </div>
      </div>

      {/* 5 Vector Breakdown */}
      <div className="space-y-3">
        <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wider">Vector Breakdown</h4>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-3">
          {[
            { label: 'Safety Risk', score: breakdown.safety, color: 'bg-red-500', text: 'text-red-400' },
            { label: 'Environmental Risk', score: breakdown.environment, color: 'bg-amber-500', text: 'text-amber-400' },
            { label: 'Labour Compliance', score: breakdown.labour, color: 'bg-blue-500', text: 'text-blue-400' },
            { label: 'Production Deficit', score: breakdown.production, color: 'bg-cyan-500', text: 'text-cyan-400' },
            { label: 'Contractor Risk', score: breakdown.contractor, color: 'bg-purple-500', text: 'text-purple-400' },
          ].map(vec => (
            <div key={vec.label} className="bg-coal-900/80 p-3 rounded-lg border border-slate-800">
              <div className="flex items-center justify-between text-xs mb-1.5">
                <span className="text-slate-400 font-medium text-[11px]">{vec.label}</span>
                <span className={`font-mono font-bold ${vec.text}`}>{vec.score}</span>
              </div>
              <div className="w-full h-2 bg-coal-950 rounded-full overflow-hidden">
                <div className={`h-full ${vec.color}`} style={{ width: `${vec.score}%` }} />
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Factor Waterfall */}
      <div className="space-y-2.5">
        <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wider">
          Factors Contributing to Risk Score
        </h4>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-2">
          {waterfallFactors.map(f => (
            <div
              key={f.factor}
              className={`p-2.5 rounded-lg border flex items-center justify-between text-xs ${
                f.positive
                  ? 'bg-emerald-500/10 border-emerald-500/30 text-emerald-300'
                  : 'bg-coal-900/90 border-slate-800 text-slate-200'
              }`}
            >
              <span className="text-[11px] truncate mr-2">{f.factor}</span>
              <span className={`font-mono font-extrabold px-1.5 py-0.5 rounded text-[11px] ${
                f.positive ? 'bg-emerald-500/20 text-emerald-400' : 'bg-red-500/20 text-red-400'
              }`}>
                {f.points}
              </span>
            </div>
          ))}
        </div>
      </div>

      {/* AI Explanation Box */}
      <div className="p-3.5 rounded-xl bg-gradient-to-r from-red-950/40 via-coal-900 to-coal-900 border border-red-500/30 flex items-start space-x-3">
        <Info className="w-5 h-5 text-safety-orange shrink-0 mt-0.5" />
        <div className="text-xs space-y-1">
          <p className="font-extrabold text-white">Why is this mine high risk?</p>
          <p className="text-slate-300 leading-relaxed text-[11px]">
            &ldquo;Mine risk increased by <strong>18% this month</strong> due to repeated conveyor safety violations in Zone 4, 7 overdue corrective actions, and two contractor certification gaps under Mines Vocational Training Rules.&rdquo;
          </p>
        </div>
      </div>
    </div>
  );
};
"""

evidence_comp = """import React, { useState } from 'react';
import {
  CheckCircle2,
  AlertTriangle,
  RotateCcw,
  Sparkles,
  ShieldCheck,
  Eye,
  Sliders
} from 'lucide-react';
import { useApp } from '../../context/AppContext';

interface Props {
  issueId?: string;
  onSuccess?: () => void;
}

export const EvidenceComparison: React.FC<Props> = ({ issueId = 'issue-2041', onSuccess }) => {
  const { issues, closeVerifiedIssue, requestIssueRework } = useApp();
  const [sliderPos, setSliderPos] = useState(50);
  const [showOverlays, setShowOverlays] = useState(true);
  const [reworkModalOpen, setReworkModalOpen] = useState(false);
  const [reworkNotes, setReworkNotes] = useState('');
  const [verifiedSuccess, setVerifiedSuccess] = useState(false);

  const issue = issues.find(i => i.id === issueId) || issues[0];
  const ca = issue?.correctiveAction;

  const beforeUrl = ca?.beforeEvidenceUrl || 'https://images.unsplash.com/photo-1578328819058-b69f3a3b0f6b?auto=format&fit=crop&w=800&q=80';
  const afterUrl = ca?.afterEvidenceUrl || 'https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=800&q=80';

  const handleApprove = () => {
    closeVerifiedIssue(issue.id);
    setVerifiedSuccess(true);
    if (onSuccess) onSuccess();
  };

  const handleRework = () => {
    if (reworkNotes.trim()) {
      requestIssueRework(issue.id, reworkNotes);
      setReworkModalOpen(false);
    }
  };

  return (
    <div className="glass-panel p-5 rounded-xl border border-slate-800 shadow-2xl space-y-5">
      {/* Title Bar */}
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between pb-4 border-b border-slate-800 gap-3">
        <div>
          <div className="flex items-center space-x-2">
            <span className="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse" />
            <h3 className="text-sm font-extrabold uppercase tracking-wider text-white">
              AI Before/After Evidence Verification
            </h3>
          </div>
          <p className="text-xs text-slate-400 mt-0.5">
            Issue #{issue.issueCode}: {issue.title}
          </p>
        </div>

        <div className="flex items-center space-x-2">
          <button
            onClick={() => setShowOverlays(!showOverlays)}
            className={`flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold border transition-all ${
              showOverlays
                ? 'bg-coal-800 text-safety-cyan border-safety-cyan/40'
                : 'bg-coal-900 text-slate-400 border-slate-700'
            }`}
          >
            <Eye className="w-3.5 h-3.5" />
            <span>AI Bounding Boxes</span>
          </button>
        </div>
      </div>

      {/* Side-by-Side Visual Comparison */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {/* BEFORE PANEL */}
        <div className="relative rounded-xl overflow-hidden border border-red-500/40 bg-coal-950 group">
          <div className="absolute top-3 left-3 z-20 bg-red-600/90 text-white font-extrabold text-[11px] px-2.5 py-1 rounded-md tracking-wider shadow-lg">
            BEFORE MITIGATION
          </div>
          <img
            src={beforeUrl}
            alt="Before Inspection"
            className="w-full h-64 object-cover object-center filter contrast-105"
          />
          {showOverlays && (
            <div className="absolute inset-0 pointer-events-none p-4">
              <div className="absolute top-16 left-12 w-48 h-32 border-2 border-dashed border-red-500 bg-red-500/15 rounded flex items-start p-1 animate-pulse">
                <span className="bg-red-600 text-white text-[9px] font-bold px-1 rounded">
                  Hazard: Missing Guard Mesh
                </span>
              </div>
            </div>
          )}
          <div className="p-3 bg-coal-900/95 border-t border-slate-800 text-xs">
            <span className="text-red-400 font-bold">Initial Risk: 92/100</span>
            <p className="text-slate-400 text-[11px] mt-0.5">Exposed high-speed conveyor drive rollers near transit passage.</p>
          </div>
        </div>

        {/* AFTER PANEL */}
        <div className="relative rounded-xl overflow-hidden border border-emerald-500/40 bg-coal-950 group">
          <div className="absolute top-3 left-3 z-20 bg-emerald-600/90 text-white font-extrabold text-[11px] px-2.5 py-1 rounded-md tracking-wider shadow-lg">
            AFTER RECTIFICATION
          </div>
          <img
            src={afterUrl}
            alt="After Verification"
            className="w-full h-64 object-cover object-center filter contrast-105"
          />
          {showOverlays && (
            <div className="absolute inset-0 pointer-events-none p-4">
              <div className="absolute top-12 left-10 w-56 h-40 border-2 border-emerald-400 bg-emerald-500/15 rounded flex items-start p-1">
                <span className="bg-emerald-600 text-white text-[9px] font-bold px-1 rounded flex items-center space-x-1">
                  <CheckCircle2 className="w-2.5 h-2.5" />
                  <span>Verified: ISO Mesh Enclosure (91%)</span>
                </span>
              </div>
            </div>
          )}
          <div className="p-3 bg-coal-900/95 border-t border-slate-800 text-xs">
            <span className="text-emerald-400 font-bold">Resolution Confidence: 91%</span>
            <p className="text-slate-400 text-[11px] mt-0.5">Dual-phase neural vision scan confirmed statutory compliant barrier.</p>
          </div>
        </div>
      </div>

      {/* AI Verification Score & Checklist */}
      <div className="p-4 rounded-xl bg-coal-900/90 border border-emerald-500/30 space-y-3">
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2">
          <div className="flex items-center space-x-2">
            <div className="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold">
              <Sparkles className="w-4 h-4" />
            </div>
            <div>
              <span className="text-xs font-bold text-slate-400 uppercase">AI Verification Result</span>
              <h4 className="text-sm font-black text-emerald-400 tracking-wider">LIKELY RESOLVED</h4>
            </div>
          </div>
          <div className="text-right">
            <span className="text-xs text-slate-400">Confidence Score</span>
            <div className="text-lg font-black text-white font-mono">91%</div>
          </div>
        </div>

        <div className="space-y-1.5 pt-2 border-t border-slate-800 text-xs text-slate-300">
          <span className="font-bold text-white text-[11px] uppercase tracking-wider">Detected Rectification Markers:</span>
          <ul className="space-y-1">
            {[
              'Heavy-duty industrial steel mesh guard securely installed along 14m conveyor flank',
              'Emergency trip-wire pull chord reconnected with tension indicator verified in green band',
              'Restricted yellow hazard perimeter demarcation painted on concrete footing',
              'Mechanical pinch point hazard reduced to statutory compliant baseline'
            ].map((item, idx) => (
              <li key={idx} className="flex items-start space-x-2 text-[11px]">
                <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400 shrink-0 mt-0.5" />
                <span>{item}</span>
              </li>
            ))}
          </ul>
        </div>
      </div>

      {/* Approval Actions */}
      <div className="flex items-center justify-end space-x-3 pt-2">
        <button
          onClick={() => setReworkModalOpen(true)}
          className="flex items-center space-x-1.5 px-4 py-2 rounded-lg bg-coal-800 text-slate-300 hover:text-white border border-slate-700 text-xs font-bold hover:bg-coal-700 transition-all"
        >
          <RotateCcw className="w-3.5 h-3.5 text-amber-400" />
          <span>Request Rework</span>
        </button>

        <button
          onClick={handleApprove}
          className="flex items-center space-x-1.5 px-5 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-extrabold shadow-lg shadow-emerald-600/30 transition-all transform hover:scale-105"
        >
          <ShieldCheck className="w-4 h-4" />
          <span>Approve & Close Issue</span>
        </button>
      </div>

      {/* Rework Modal */}
      {reworkModalOpen && (
        <div className="fixed inset-0 z-50 bg-black/75 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="bg-coal-900 border border-slate-700 p-5 rounded-xl max-w-md w-full space-y-4 animate-fade-in">
            <h4 className="text-sm font-bold text-white uppercase">Request Additional Mitigation</h4>
            <textarea
              value={reworkNotes}
              onChange={e => setReworkNotes(e.target.value)}
              placeholder="Specify defect or missing safety element..."
              rows={3}
              className="w-full bg-coal-950 border border-slate-700 rounded-lg p-2.5 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-amber-500"
            />
            <div className="flex justify-end space-x-2">
              <button
                onClick={() => setReworkModalOpen(false)}
                className="px-3 py-1.5 text-xs bg-coal-800 text-slate-300 rounded-lg"
              >
                Cancel
              </button>
              <button
                onClick={handleRework}
                className="px-4 py-1.5 text-xs bg-amber-600 text-white font-bold rounded-lg"
              >
                Submit Rework Request
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
"""

gis_map = """import React, { useState } from 'react';
import { MapContainer, TileLayer, Marker, Popup, Circle } from 'react-leaflet';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import { useApp } from '../../context/AppContext';
import { Mine } from '../../types';
import { ShieldAlert, Flame, MapPin, CheckCircle2, AlertTriangle, Layers } from 'lucide-react';

interface Props {
  onSelectMine?: (mine: Mine) => void;
}

// Custom markers using HTML DivIcon
const createCustomIcon = (risk: number, status: string) => {
  let color = '#10B981'; // Green
  if (risk > 75) color = '#EF4444'; // Red
  else if (risk > 55) color = '#F59E0B'; // Orange / Amber
  else if (risk > 40) color = '#EAB308'; // Yellow

  return L.divIcon({
    className: 'custom-mine-pin',
    html: `
      <div style="
        background-color: ${color};
        width: 24px;
        height: 24px;
        border-radius: 50%;
        border: 3px solid #0E131F;
        box-shadow: 0 0 12px ${color};
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 10px;
        font-weight: 800;
      ">
        ●
      </div>
    `,
    iconSize: [24, 24],
    iconAnchor: [12, 12]
  });
};

export const GISMap: React.FC<Props> = ({ onSelectMine }) => {
  const { mines } = useApp();
  const [selectedMine, setSelectedMine] = useState<Mine | null>(mines[0] || null);
  const [layer, setLayer] = useState<'all' | 'critical' | 'heatmap'>('all');

  const filteredMines = mines.filter(m => {
    if (layer === 'critical') return m.riskScore > 65;
    return true;
  });

  return (
    <div className="relative w-full h-[520px] rounded-xl overflow-hidden border border-slate-800 shadow-2xl bg-coal-950">
      {/* Map Control Bar */}
      <div className="absolute top-3 right-3 z-[1000] flex items-center space-x-2 bg-coal-900/90 backdrop-blur-md p-1.5 rounded-lg border border-slate-700 shadow-lg">
        <button
          onClick={() => setLayer('all')}
          className={`px-2.5 py-1 text-[11px] font-bold rounded ${
            layer === 'all' ? 'bg-safety-orange text-white' : 'text-slate-400 hover:text-white'
          }`}
        >
          All 18 Mines
        </button>
        <button
          onClick={() => setLayer('critical')}
          className={`px-2.5 py-1 text-[11px] font-bold rounded ${
            layer === 'critical' ? 'bg-red-600 text-white' : 'text-slate-400 hover:text-white'
          }`}
        >
          Critical Zones
        </button>
        <button
          onClick={() => setLayer('heatmap')}
          className={`px-2.5 py-1 text-[11px] font-bold rounded ${
            layer === 'heatmap' ? 'bg-amber-600 text-white' : 'text-slate-400 hover:text-white'
          }`}
        >
          Risk Heatmap
        </button>
      </div>

      {/* Legend */}
      <div className="absolute bottom-3 left-3 z-[1000] bg-coal-900/90 backdrop-blur-md p-2.5 rounded-lg border border-slate-700 text-[10px] space-y-1 shadow-lg">
        <span className="font-extrabold uppercase text-slate-300 tracking-wider">Risk Legend</span>
        <div className="flex items-center space-x-2">
          <span className="w-2.5 h-2.5 rounded-full bg-red-500" />
          <span className="text-slate-300">Critical Risk (&gt;75)</span>
        </div>
        <div className="flex items-center space-x-2">
          <span className="w-2.5 h-2.5 rounded-full bg-amber-500" />
          <span className="text-slate-300">High Risk (55-75)</span>
        </div>
        <div className="flex items-center space-x-2">
          <span className="w-2.5 h-2.5 rounded-full bg-emerald-500" />
          <span className="text-slate-300">Compliant / Low Risk</span>
        </div>
      </div>

      {/* Leaflet Map */}
      <MapContainer
        center={[23.0, 83.0]}
        zoom={6}
        scrollWheelZoom={false}
        className="w-full h-full"
      >
        <TileLayer
          attribution='&copy; <a href="https://carto.com/">CARTO</a>'
          url="https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png"
        />

        {filteredMines.map(m => (
          <React.Fragment key={m.id}>
            <Marker
              position={[m.lat, m.lng]}
              icon={createCustomIcon(m.riskScore, m.status)}
              eventHandlers={{
                click: () => {
                  setSelectedMine(m);
                  if (onSelectMine) onSelectMine(m);
                }
              }}
            >
              <Popup className="custom-popup">
                <div className="p-1 text-coal-900">
                  <p className="font-bold text-xs">{m.name}</p>
                  <p className="text-[10px] text-slate-600">{m.subsidiary} • {m.district}, {m.state}</p>
                  <div className="flex items-center justify-between mt-2 pt-1 border-t border-slate-200 text-[11px]">
                    <span>Risk: <strong>{m.riskScore}/100</strong></span>
                    <span>Compliance: <strong>{m.complianceScore}%</strong></span>
                  </div>
                </div>
              </Popup>
            </Marker>

            {/* Heatmap radius simulator */}
            {layer === 'heatmap' && (
              <Circle
                center={[m.lat, m.lng]}
                radius={m.riskScore * 600}
                pathOptions={{
                  color: m.riskScore > 70 ? '#EF4444' : '#F59E0B',
                  fillColor: m.riskScore > 70 ? '#EF4444' : '#F59E0B',
                  fillOpacity: 0.25
                }}
              />
            )}
          </React.Fragment>
        ))}
      </MapContainer>
    </div>
  );
};
"""

hero_demo = """import React, { useState } from 'react';
import {
  Sparkles,
  CheckCircle2,
  ChevronRight,
  ChevronLeft,
  X,
  Play,
  RotateCcw,
  Pickaxe,
  Smartphone,
  Scan,
  ShieldCheck,
  Zap
} from 'lucide-react';
import { useApp } from '../../context/AppContext';
import { useAuth } from '../../context/AuthContext';

interface Props {
  isOpen: boolean;
  onClose: () => void;
  setActiveTab: (tab: string) => void;
}

export const HeroDemoModal: React.FC<Props> = ({ isOpen, onClose, setActiveTab }) => {
  const { switchRole } = useAuth();
  const { submitEvidenceVerification, closeVerifiedIssue, stats } = useApp();
  const [currentStep, setCurrentStep] = useState(1);

  if (!isOpen) return null;

  const demoSteps = [
    {
      step: 1,
      title: 'Field Inspector Opens Mobile AI Inspection',
      desc: 'Inspector Vikramaditya Rao opens MineGuard AI Mobile App on-site at Gevra Mega Open Cast Mine.',
      actionLabel: 'Go to New AI Inspection',
      onTrigger: () => { switchRole('FIELD_INSPECTOR'); setActiveTab('new-inspection'); }
    },
    {
      step: 2,
      title: 'Auto-Capture GPS Geo-Coordinates & Timestamp',
      desc: 'Mobile sensors automatically lock GPS (22.3392°N, 82.6081°E), altitude 312m, and Korba Zone 4.',
      actionLabel: 'Inspect GPS Auto-lock',
      onTrigger: () => { setActiveTab('new-inspection'); }
    },
    {
      step: 3,
      title: 'Record Field Voice Transcript & Upload Hazard Photo',
      desc: 'Inspector captures live photo of exposed conveyor rollers and records: "Missing protective barrier near conveyor belt trunk line 4B".',
      actionLabel: 'View Field Evidence',
      onTrigger: () => { setActiveTab('new-inspection'); }
    },
    {
      step: 4,
      title: '6-Stage Neural AI Analysis & Risk Calculation',
      desc: 'MineGuard AI analyzes text, image raster, and historical data: Risk Score 92/100 (CRITICAL).',
      actionLabel: 'View AI Findings Page',
      onTrigger: () => { setActiveTab('ai-findings'); }
    },
    {
      step: 5,
      title: 'Explainable AI Root Cause Explanation',
      desc: 'AI explains why it is Critical: 4 previous violations in 60d, active machinery transit, DGMS standard breach.',
      actionLabel: 'View AI Risk Analytics',
      onTrigger: () => { setActiveTab('ai-risk-analytics'); }
    },
    {
      step: 6,
      title: 'Smart Assignee Auto-Recommendation',
      desc: 'AI recommends Safety Officer Rajesh Kumar (Zone 4 Lead) based on expertise and active workload.',
      actionLabel: 'View Corrective Actions Hub',
      onTrigger: () => { switchRole('MINE_OFFICIAL'); setActiveTab('corrective-actions'); }
    },
    {
      step: 7,
      title: 'Corrective Action Created with 24-Hour SLA Timer',
      desc: 'Issue auto-assigned with live countdown timer: "18 hours remaining" and 4-tier escalation rules.',
      actionLabel: 'View Emergency Critical SLAs',
      onTrigger: () => { setActiveTab('critical-issues'); }
    },
    {
      step: 8,
      title: 'Officer Rectifies Hazard & Uploads After-Photo',
      desc: 'Maintenance team installs heavy-duty steel mesh enclosure and reconnects emergency trip-wire switch.',
      actionLabel: 'Open AI Evidence Verification',
      onTrigger: () => { setActiveTab('evidence-verification'); }
    },
    {
      step: 9,
      title: 'AI Before/After Evidence Verification Scan',
      desc: 'Dual-phase neural comparison verifies installed guard: "LIKELY RESOLVED" with 91% Confidence.',
      actionLabel: 'Verify Evidence with AI',
      onTrigger: () => { submitEvidenceVerification('issue-2041', 'https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=800&q=80'); setActiveTab('evidence-verification'); }
    },
    {
      step: 10,
      title: 'Mine Manager Verifies & Closes Issue',
      desc: 'General Manager S. N. Mishra approves verified evidence and closes the issue with full signoff.',
      actionLabel: 'Approve & Close Issue',
      onTrigger: () => { closeVerifiedIssue('issue-2041'); setActiveTab('dashboard'); }
    },
    {
      step: 11,
      title: 'Management Dashboard Auto-Updates Live KPIs',
      desc: `Open Issues: 126 → ${stats.openIssues} | Critical: 8 → ${stats.criticalIssues} | Compliance: 87% → ${stats.overallCompliance}%.`,
      actionLabel: 'View Updated Dashboard',
      onTrigger: () => { setActiveTab('dashboard'); }
    },
    {
      step: 12,
      title: 'Cryptographic SHA-256 Immutable Audit Trail',
      desc: 'Every single inspection, inference, assignment, and closure is immutably recorded in the digital ledger.',
      actionLabel: 'Inspect Blockchain Audit Ledger',
      onTrigger: () => { setActiveTab('audit-trail'); }
    }
  ];

  const current = demoSteps[currentStep - 1];

  const handleNext = () => {
    if (currentStep < demoSteps.length) {
      const next = currentStep + 1;
      setCurrentStep(next);
      demoSteps[next - 1].onTrigger();
    }
  };

  const handlePrev = () => {
    if (currentStep > 1) {
      const prev = currentStep - 1;
      setCurrentStep(prev);
      demoSteps[prev - 1].onTrigger();
    }
  };

  return (
    <div className="fixed inset-0 z-50 bg-black/80 backdrop-blur-md flex items-center justify-center p-4">
      <div className="bg-coal-900 border border-safety-orange/50 rounded-2xl max-w-2xl w-full p-6 shadow-2xl shadow-safety-orange/20 space-y-5 animate-slide-up relative">
        {/* Header */}
        <div className="flex items-center justify-between pb-3 border-b border-slate-800">
          <div className="flex items-center space-x-2.5">
            <div className="w-8 h-8 rounded-lg bg-safety-orange text-white flex items-center justify-center font-bold">
              <Sparkles className="w-4 h-4" />
            </div>
            <div>
              <h3 className="text-sm font-extrabold text-white uppercase tracking-wider">
                SIH Problem Statement 26024 — Hero Demo Tour
              </h3>
              <p className="text-[11px] text-safety-orange font-mono font-semibold">
                Step {currentStep} of {demoSteps.length}: Closed-Loop AI Governance Flow
              </p>
            </div>
          </div>
          <button onClick={onClose} className="p-1 rounded-lg text-slate-400 hover:text-white bg-coal-800">
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Step Visual Card */}
        <div className="p-4 rounded-xl bg-coal-950 border border-slate-800 space-y-2">
          <div className="flex items-center justify-between text-xs text-slate-400 font-mono">
            <span>PHASE {currentStep}: {current.title.toUpperCase()}</span>
            <span className="text-safety-orange font-bold">{Math.round((currentStep / demoSteps.length) * 100)}% Complete</span>
          </div>
          <div className="w-full h-2 bg-coal-900 rounded-full overflow-hidden">
            <div
              className="h-full bg-gradient-to-r from-safety-orange to-amber-500 transition-all duration-300"
              style={{ width: `${(currentStep / demoSteps.length) * 100}%` }}
            />
          </div>
          <h4 className="text-base font-extrabold text-white pt-2">{current.title}</h4>
          <p className="text-xs text-slate-300 leading-relaxed">{current.desc}</p>
        </div>

        {/* Execution Button */}
        <button
          onClick={current.onTrigger}
          className="w-full flex items-center justify-center space-x-2 py-3 rounded-xl bg-gradient-to-r from-safety-orange to-amber-500 hover:from-safety-orange/90 hover:to-amber-500/90 text-white font-extrabold text-xs shadow-lg shadow-safety-orange/25 transition-all"
        >
          <Zap className="w-4 h-4" />
          <span>Execute & {current.actionLabel}</span>
        </button>

        {/* Navigation Footer */}
        <div className="flex items-center justify-between pt-2 border-t border-slate-800">
          <button
            onClick={handlePrev}
            disabled={currentStep === 1}
            className="flex items-center space-x-1.5 px-3 py-1.5 rounded-lg bg-coal-800 text-slate-300 disabled:opacity-40 text-xs font-semibold"
          >
            <ChevronLeft className="w-4 h-4" />
            <span>Previous</span>
          </button>

          <span className="text-xs text-slate-400 font-mono">
            {currentStep} / {demoSteps.length}
          </span>

          <button
            onClick={handleNext}
            disabled={currentStep === demoSteps.length}
            className="flex items-center space-x-1.5 px-3 py-1.5 rounded-lg bg-safety-orange text-white disabled:opacity-40 text-xs font-semibold"
          >
            <span>Next Step</span>
            <ChevronRight className="w-4 h-4" />
          </button>
        </div>
      </div>
    </div>
  );
};
"""

with open('src/components/visualizer/RiskScoreCard.tsx', 'w', encoding='utf-8') as f:
    f.write(risk_card)

with open('src/components/visualizer/EvidenceComparison.tsx', 'w', encoding='utf-8') as f:
    f.write(evidence_comp)

with open('src/components/map/GISMap.tsx', 'w', encoding='utf-8') as f:
    f.write(gis_map)

with open('src/components/walkthrough/HeroDemoModal.tsx', 'w', encoding='utf-8') as f:
    f.write(hero_demo)

print("Visualizer, Map, and Hero Demo components generated successfully!")
