import os

new_inspection = """import React, { useState } from 'react';
import {
  ClipboardList,
  MapPin,
  Camera,
  Mic,
  MicOff,
  Sparkles,
  CheckCircle2,
  AlertTriangle,
  Upload,
  ArrowRight,
  ShieldAlert,
  Flame,
  UserCheck
} from 'lucide-react';
import { useApp } from '../../context/AppContext';
import { useAuth } from '../../context/AuthContext';
import { simulateAIFindingsScan, AIClassificationResult } from '../../services/aiService';

interface Props {
  setActiveTab: (tab: string) => void;
}

export const NewInspectionPage: React.FC<Props> = ({ setActiveTab }) => {
  const { mines, addInspection, createIssueFromInspection } = useApp();
  const { currentUser } = useAuth();

  const [mineId, setMineId] = useState('mine-101');
  const [zone, setZone] = useState('Zone 4 - Primary Conveyor Line');
  const [reportText, setReportText] = useState('Missing protective barrier near conveyor belt trunk line 4B with high risk of personnel entanglement.');
  const [category, setCategory] = useState<'Safety' | 'Environment' | 'Labour' | 'Contractor Compliance' | 'Operational'>('Safety');
  const [isRecording, setIsRecording] = useState(false);
  const [gpsLocked, setGpsLocked] = useState(true);
  const [gpsCoords, setGpsCoords] = useState({ lat: 22.3392, lng: 82.6081, alt: 312 });
  const [selectedPhoto, setSelectedPhoto] = useState('https://images.unsplash.com/photo-1578328819058-b69f3a3b0f6b?auto=format&fit=crop&w=800&q=80');

  const [scanningPhase, setScanningPhase] = useState<number>(0);
  const [scanResult, setScanResult] = useState<AIClassificationResult | null>(null);

  const handleStartScan = async () => {
    setScanningPhase(1);
    for (let i = 1; i <= 6; i++) {
      setScanningPhase(i);
      await new Promise(r => setTimeout(r, 350));
    }
    const res = await simulateAIFindingsScan(reportText, category, zone);
    setScanResult(res);
    setScanningPhase(0);
  };

  const handleCreateCase = () => {
    if (!scanResult) return;
    const selectedMine = mines.find(m => m.id === mineId) || mines[0];

    createIssueFromInspection({
      title: 'Missing protective barrier near conveyor belt trunk line 4B',
      description: reportText,
      category: scanResult.category,
      severity: scanResult.severity,
      riskScore: scanResult.riskScore,
      mineId: selectedMine.id,
      mineName: selectedMine.name,
      subsidiary: selectedMine.subsidiary,
      zone: zone,
      latitude: gpsCoords.lat,
      longitude: gpsCoords.lng,
      reportedBy: currentUser.name,
      assignedTo: scanResult.recommendedAssignee.name,
      slaRemainingHours: scanResult.suggestedSLAHours,
      correctiveAction: {
        id: `ca-${Date.now()}`,
        issueId: '',
        title: 'Fabricate and install heavy-duty mesh guard & reconnect pull-wire switch',
        assignedTo: scanResult.recommendedAssignee.name,
        assignedDepartment: scanResult.suggestedDepartment,
        status: 'ASSIGNED',
        deadline: '24 Hours',
        slaHours: scanResult.suggestedSLAHours,
        beforeEvidenceUrl: selectedPhoto,
      }
    });

    setActiveTab('critical-issues');
  };

  const scanSteps = [
    'Collecting inspection telemetry & geo-stamps...',
    'Analyzing natural language field report & audio transcript...',
    'Running dual-phase neural computer vision raster scan...',
    'Checking historical violation clusters across subsidiary...',
    'Calculating multi-vector risk quantification score...',
    'Synthesizing smart assignee & SLA mitigation timeline...'
  ];

  return (
    <div className="max-w-4xl mx-auto space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
          <ClipboardList className="w-4 h-4 text-[#0B2545]" />
          <span>Mobile Digital Field Audit Register</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Digital Field Inspection Form</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Standardized field inspection entry complying with Directorate General of Mines Safety (DGMS) on-site hazard audit standards.
        </p>
      </div>

      {/* Form Card */}
      <div className="gov-card p-6 space-y-5">
        {/* Row 1: Mine and Zone */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
          <div>
            <label className="block text-slate-700 font-bold uppercase text-[11px] mb-1">Target Mine Location</label>
            <select
              value={mineId}
              onChange={e => setMineId(e.target.value)}
              className="w-full bg-slate-50 border border-slate-300 rounded p-2 text-slate-900 font-bold focus:outline-none focus:border-[#0B2545]"
            >
              {mines.map(m => (
                <option key={m.id} value={m.id}>{m.name} ({m.subsidiary})</option>
              ))}
            </select>
          </div>

          <div>
            <label className="block text-slate-700 font-bold uppercase text-[11px] mb-1">Operational Sector / Zone</label>
            <input
              type="text"
              value={zone}
              onChange={e => setZone(e.target.value)}
              className="w-full bg-slate-50 border border-slate-300 rounded p-2 text-slate-900 font-medium focus:outline-none focus:border-[#0B2545]"
            />
          </div>
        </div>

        {/* GPS Coordinates Auto-Lock Banner */}
        <div className="p-3 bg-slate-50 rounded border border-slate-200 flex flex-col sm:flex-row items-start sm:items-center justify-between text-xs gap-2">
          <div className="flex items-center space-x-2">
            <MapPin className="w-4 h-4 text-emerald-700" />
            <div>
              <span className="font-extrabold text-slate-900 uppercase text-[10px]">Geo-Location Stamp (WGS84)</span>
              <p className="font-mono text-slate-700 text-[11px]">
                {gpsCoords.lat.toFixed(4)}°N, {gpsCoords.lng.toFixed(4)}°E (Altitude: {gpsCoords.alt}m)
              </p>
            </div>
          </div>
          <span className="bg-emerald-50 text-emerald-800 border border-emerald-300 text-[10px] font-bold px-2 py-0.5 rounded uppercase">
            ✓ GPS Locked
          </span>
        </div>

        {/* Voice Note & Written Observation */}
        <div className="space-y-2 text-xs">
          <div className="flex items-center justify-between">
            <label className="block text-slate-700 font-bold uppercase text-[11px]">Inspector Field Observations</label>
            <button
              type="button"
              onClick={() => setIsRecording(!isRecording)}
              className={`px-3 py-1 rounded text-xs font-bold transition-all flex items-center space-x-1.5 ${
                isRecording ? 'bg-red-700 text-white animate-pulse' : 'bg-slate-100 hover:bg-slate-200 text-slate-800 border border-slate-300'
              }`}
            >
              {isRecording ? <MicOff className="w-3.5 h-3.5" /> : <Mic className="w-3.5 h-3.5 text-red-700" />}
              <span>{isRecording ? 'Listening...' : 'Voice Speech-to-Text'}</span>
            </button>
          </div>

          <textarea
            value={reportText}
            onChange={e => setReportText(e.target.value)}
            rows={3}
            className="w-full bg-slate-50 border border-slate-300 rounded p-2.5 text-xs text-slate-900 focus:outline-none focus:border-[#0B2545] leading-relaxed"
          />
        </div>

        {/* Evidence Photo */}
        <div className="space-y-2 text-xs">
          <label className="block text-slate-700 font-bold uppercase text-[11px]">Geo-Tagged Evidence Photo</label>
          <div className="flex items-center space-x-4">
            <img
              src={selectedPhoto}
              alt="Hazard Evidence"
              className="w-28 h-20 object-cover rounded border border-slate-300"
            />
            <div className="text-slate-600 text-[11px] space-y-1">
              <p className="font-bold text-slate-900">conveyor_rollers_pinch_point.jpg (1.8 MB)</p>
              <p>Resolution: 1920x1080 &bull; Timestamp: 10 Sep 2026, 08:32 AM</p>
              <span className="inline-block text-[10px] bg-emerald-50 text-emerald-800 border border-emerald-300 px-1.5 py-0.2 rounded font-mono">
                Exif Geo-Tag Verified
              </span>
            </div>
          </div>
        </div>

        {/* Scan Action Button */}
        <button
          type="button"
          onClick={handleStartScan}
          disabled={scanningPhase > 0}
          className="w-full gov-btn-primary py-3"
        >
          <Sparkles className="w-4 h-4 text-amber-400" />
          <span>{scanningPhase > 0 ? 'Executing Neural Classification Engine...' : 'Run AI Analysis & Risk Evaluation'}</span>
        </button>
      </div>

      {/* Scanning Phase Animation */}
      {scanningPhase > 0 && (
        <div className="gov-card p-5 space-y-3 bg-slate-50">
          <div className="flex items-center justify-between text-xs">
            <span className="font-bold uppercase text-slate-700 font-mono">Phase {scanningPhase} of 6</span>
            <span className="font-mono font-bold text-[#0B2545]">{Math.round((scanningPhase / 6) * 100)}%</span>
          </div>
          <div className="w-full h-2 bg-slate-200 rounded-full overflow-hidden">
            <div
              className="h-full bg-[#0B2545] transition-all duration-300"
              style={{ width: `${(scanningPhase / 6) * 100}%` }}
            />
          </div>
          <p className="text-xs text-slate-800 font-bold">{scanSteps[scanningPhase - 1]}</p>
        </div>
      )}

      {/* AI Output Card */}
      {scanResult && (
        <div className="gov-card p-6 space-y-5 border-l-4 border-l-red-700 bg-white">
          <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between pb-3 border-b border-slate-200 gap-2">
            <div>
              <span className="text-[10px] font-extrabold uppercase text-red-700 tracking-wider">
                AI-Assisted Analysis Result
              </span>
              <h3 className="text-base font-black text-slate-900">
                {scanResult.category.toUpperCase()} &bull; {scanResult.severity.toUpperCase()} SEVERITY
              </h3>
            </div>

            <div className="text-right">
              <div className="font-mono text-lg font-black text-red-700">
                Risk Score: {scanResult.riskScore} / 100
              </div>
              <span className="text-[10px] text-slate-500 font-mono">Confidence: {scanResult.confidence}%</span>
            </div>
          </div>

          {/* Explainable Factors */}
          <div className="space-y-2 text-xs">
            <span className="font-bold text-slate-900 uppercase text-[10px]">Explainable Risk Factors:</span>
            <ul className="space-y-1 text-slate-700">
              {scanResult.whySeverity.map((reason, i) => (
                <li key={i} className="flex items-start space-x-2">
                  <CheckCircle2 className="w-3.5 h-3.5 text-red-700 shrink-0 mt-0.5" />
                  <span>{reason}</span>
                </li>
              ))}
            </ul>
          </div>

          {/* Suggested Remediation & Assignee */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs pt-3 border-t border-slate-200">
            <div className="p-3 bg-slate-50 rounded border border-slate-200 space-y-1">
              <span className="text-[10px] text-slate-500 uppercase font-bold">Mandated Corrective Directive</span>
              <p className="font-bold text-slate-900">{scanResult.suggestedAction}</p>
              <p className="text-[10px] text-red-700 font-mono font-bold mt-1">
                Statutory SLA Window: {scanResult.suggestedSLAHours} Hours
              </p>
            </div>

            <div className="p-3 bg-slate-50 rounded border border-slate-200 space-y-1">
              <span className="text-[10px] text-slate-500 uppercase font-bold">Recommended Responsible Assignee</span>
              <p className="font-bold text-slate-900">{scanResult.recommendedAssignee.name}</p>
              <p className="text-[11px] text-slate-600">{scanResult.recommendedAssignee.role}</p>
            </div>
          </div>

          <button
            type="button"
            onClick={handleCreateCase}
            className="w-full gov-btn-primary py-3"
          >
            <CheckCircle2 className="w-4 h-4 text-amber-400" />
            <span>Generate Official Corrective Case & Initiate 24h SLA Countdown</span>
          </button>
        </div>
      )}
    </div>
  );
};
"""

inspection_hist = """import React from 'react';
import { History, Eye, Download, Search } from 'lucide-react';
import { useApp } from '../../context/AppContext';

export const InspectionHistoryPage: React.FC = () => {
  const { inspections } = useApp();

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
          <History className="w-4 h-4 text-[#0B2545]" />
          <span>Statutory Audit Logs Archive</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Digital Field Inspection History</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Archival log of all on-site inspections, GPS coordinates, voice transcriptions, and generated corrective cases.
        </p>
      </div>

      <div className="gov-card overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="bg-slate-50 border-b border-slate-200 text-slate-700 font-bold uppercase tracking-wider text-[10px]">
              <tr>
                <th className="p-3">Inspection ID</th>
                <th className="p-3">Mine & Sector</th>
                <th className="p-3">Inspector Officer</th>
                <th className="p-3">Date & Timestamp</th>
                <th className="p-3">Findings Recorded</th>
                <th className="p-3">Status</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-200">
              {inspections.map(insp => (
                <tr key={insp.id} className="hover:bg-slate-50/80 transition-colors">
                  <td className="p-3 font-mono font-bold text-slate-900">{insp.inspectionCode}</td>
                  <td className="p-3 font-bold text-slate-900">
                    <div>{insp.mineName}</div>
                    <div className="text-[10px] text-slate-500 font-normal">{insp.zone}</div>
                  </td>
                  <td className="p-3 text-slate-700">{insp.inspectorName}</td>
                  <td className="p-3 font-mono text-slate-600">{insp.date} {insp.time}</td>
                  <td className="p-3 text-slate-700 max-w-xs truncate">{insp.notes}</td>
                  <td className="p-3">
                    <span className="bg-emerald-50 text-emerald-800 border border-emerald-300 text-[10px] font-bold px-2 py-0.5 rounded uppercase">
                      {insp.status}
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

ai_findings = """import React from 'react';
import { ScanEye, AlertTriangle, ArrowRight } from 'lucide-react';
import { useApp } from '../../context/AppContext';

interface Props {
  setActiveTab: (tab: string) => void;
}

export const AIFindingsPage: React.FC<Props> = ({ setActiveTab }) => {
  const { issues } = useApp();
  const criticalFindings = issues.filter(i => i.severity === 'Critical');

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
          <ScanEye className="w-4 h-4 text-[#0B2545]" />
          <span>AI Computer Vision & NLP Findings</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Identified Hazards & Risk Findings</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Automatic risk classifications synthesized from field audits, raster comparison, and historical clusters.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {criticalFindings.map(item => (
          <div key={item.id} className="gov-card p-4 space-y-3 border-l-4 border-l-red-700">
            <div className="flex items-start justify-between">
              <div>
                <span className="text-[10px] font-bold bg-slate-100 text-slate-700 px-2 py-0.5 rounded font-mono">
                  {item.issueCode}
                </span>
                <h3 className="text-sm font-extrabold text-slate-900 mt-1">{item.title}</h3>
                <p className="text-[11px] text-slate-500">{item.mineName} &bull; {item.zone}</p>
              </div>
              <span className="text-[10px] font-black px-2 py-0.5 rounded bg-red-50 text-red-800 border border-red-300 font-mono">
                RISK {item.riskScore}/100
              </span>
            </div>

            <p className="text-xs text-slate-700 leading-relaxed">{item.description}</p>

            <div className="flex items-center justify-between pt-2 border-t border-slate-200 text-xs">
              <span className="text-slate-500 font-mono">SLA: {item.slaRemainingHours}h Left</span>
              <button
                onClick={() => setActiveTab('evidence-verification')}
                className="gov-btn-secondary text-[11px] py-1 px-3"
              >
                <span>Verify Remediation</span>
                <ArrowRight className="w-3 h-3" />
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

all_issues = """import React, { useState } from 'react';
import { AlertTriangle, Flame, CheckCircle2, Wrench, Search, Filter } from 'lucide-react';
import { useApp } from '../../context/AppContext';

interface Props {
  setActiveTab: (tab: string) => void;
}

export const AllIssuesPage: React.FC<Props> = ({ setActiveTab }) => {
  const { issues } = useApp();
  const [searchTerm, setSearchTerm] = useState('');

  const filtered = issues.filter(i => i.title.toLowerCase().includes(searchTerm.toLowerCase()) || i.issueCode.toLowerCase().includes(searchTerm.toLowerCase()));

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
            <AlertTriangle className="w-4 h-4 text-[#0B2545]" />
            <span>Official Non-Compliance & Safety Docket</span>
          </div>
          <h1 className="text-2xl font-black text-slate-900 mt-1">Open Issues Register</h1>
          <p className="text-xs text-slate-600 mt-0.5">
            Master register of all open statutory violations, safety observations, and environmental notices.
          </p>
        </div>

        <input
          type="text"
          placeholder="Search issue code, title..."
          value={searchTerm}
          onChange={e => setSearchTerm(e.target.value)}
          className="bg-slate-50 border border-slate-300 rounded px-3 py-1.5 text-xs text-slate-900 placeholder-slate-400 focus:outline-none focus:border-[#0B2545] w-64"
        />
      </div>

      <div className="gov-card overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="bg-slate-50 border-b border-slate-200 text-slate-700 font-bold uppercase tracking-wider text-[10px]">
              <tr>
                <th className="p-3">Docket No</th>
                <th className="p-3">Mine Location</th>
                <th className="p-3">Category</th>
                <th className="p-3">Severity</th>
                <th className="p-3">Risk Score</th>
                <th className="p-3">Assignee</th>
                <th className="p-3">Status</th>
                <th className="p-3 text-right">Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-200">
              {filtered.map(item => (
                <tr key={item.id} className="hover:bg-slate-50/80 transition-colors">
                  <td className="p-3 font-mono font-bold text-slate-900">
                    <div>{item.issueCode}</div>
                    <div className="text-[10px] text-slate-500 font-sans font-normal truncate max-w-xs">{item.title}</div>
                  </td>
                  <td className="p-3 font-bold text-slate-900">{item.mineName}</td>
                  <td className="p-3">
                    <span className="bg-slate-100 text-slate-800 border border-slate-300 text-[10px] font-bold px-2 py-0.5 rounded uppercase">
                      {item.category}
                    </span>
                  </td>
                  <td className="p-3">
                    <span className={`text-[10px] font-bold px-2 py-0.5 rounded uppercase ${
                      item.severity === 'Critical' ? 'bg-red-50 text-red-800 border border-red-300' : 'bg-amber-50 text-amber-800 border border-amber-300'
                    }`}>
                      {item.severity}
                    </span>
                  </td>
                  <td className="p-3 font-mono font-bold text-slate-900">{item.riskScore}</td>
                  <td className="p-3 text-slate-700">{item.assignedTo || 'Unassigned'}</td>
                  <td className="p-3">
                    <span className="bg-blue-50 text-blue-800 border border-blue-300 text-[10px] font-bold px-2 py-0.5 rounded uppercase">
                      {item.status}
                    </span>
                  </td>
                  <td className="p-3 text-right">
                    <button
                      onClick={() => setActiveTab('evidence-verification')}
                      className="gov-btn-secondary text-[11px] py-1 px-2.5"
                    >
                      Inspect
                    </button>
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

critical_issues = """import React from 'react';
import { Flame, ClockAlert, ArrowRight, AlertTriangle } from 'lucide-react';
import { useApp } from '../../context/AppContext';

interface Props {
  setActiveTab: (tab: string) => void;
}

export const CriticalIssuesPage: React.FC<Props> = ({ setActiveTab }) => {
  const { issues } = useApp();
  const critical = issues.filter(i => i.severity === 'Critical' && i.status !== 'CLOSED');

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5 border-l-4 border-l-red-700">
        <div className="flex items-center space-x-2 text-xs text-red-700 font-extrabold uppercase tracking-wider">
          <Flame className="w-4 h-4 text-red-700" />
          <span>Priority Emergency SLAs</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Critical Issues & Escalation Register</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          High-risk statutory non-conformances subject to automated 4-tier management escalation and DGMS notification rules.
        </p>
      </div>

      <div className="space-y-3">
        {critical.map(item => (
          <div
            key={item.id}
            className="gov-card p-4 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 border-l-4 border-l-red-700"
          >
            <div className="space-y-1">
              <div className="flex items-center space-x-2">
                <span className="bg-red-700 text-white font-mono font-bold text-[10px] px-2 py-0.5 rounded">
                  SLA: {item.slaRemainingHours}H REMAINING
                </span>
                <span className="font-mono font-bold text-slate-900 text-xs">{item.issueCode}</span>
              </div>
              <h3 className="text-sm font-extrabold text-slate-900">{item.title}</h3>
              <p className="text-xs text-slate-600">
                Location: <strong>{item.mineName} ({item.zone})</strong> &bull; Assignee: <strong>{item.assignedTo}</strong>
              </p>
            </div>

            <button
              onClick={() => setActiveTab('evidence-verification')}
              className="gov-btn-primary text-xs py-2 px-4 self-end sm:self-center"
            >
              <span>Inspect & Verify Evidence</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

corrective_actions = """import React from 'react';
import { Wrench, CheckCircle2, Clock } from 'lucide-react';
import { useApp } from '../../context/AppContext';

interface Props {
  setActiveTab: (tab: string) => void;
}

export const CorrectiveActionsPage: React.FC<Props> = ({ setActiveTab }) => {
  const { issues } = useApp();
  const list = issues.filter(i => i.correctiveAction);

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
          <Wrench className="w-4 h-4 text-[#0B2545]" />
          <span>Remediation Dispatch Hub</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Corrective Action Workflow Center</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Case management center tracking work orders from assignment, rectification, before/after verification, to final case closure.
        </p>
      </div>

      <div className="space-y-3">
        {list.map(item => {
          const ca = item.correctiveAction!;
          return (
            <div key={item.id} className="gov-card p-4 space-y-3">
              <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2 border-b border-slate-200 pb-2">
                <div>
                  <span className="text-[10px] font-bold bg-slate-100 text-slate-700 px-2 py-0.5 rounded font-mono">
                    Docket #{item.issueCode}
                  </span>
                  <h3 className="text-sm font-extrabold text-slate-900 mt-0.5">{ca.title}</h3>
                </div>

                <span className="bg-blue-50 text-blue-800 border border-blue-300 text-[10px] font-bold px-2 py-0.5 rounded uppercase">
                  {ca.status}
                </span>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
                <div>
                  <span className="text-slate-500 block text-[10px] uppercase">Assigned Officer</span>
                  <p className="font-bold text-slate-900">{ca.assignedTo}</p>
                </div>
                <div>
                  <span className="text-slate-500 block text-[10px] uppercase">Responsible Department</span>
                  <p className="font-bold text-slate-900">{ca.assignedDepartment}</p>
                </div>
                <div>
                  <span className="text-slate-500 block text-[10px] uppercase">SLA Deadline</span>
                  <p className="font-mono font-bold text-red-700">{ca.deadline}</p>
                </div>
              </div>

              <div className="flex justify-end pt-2 border-t border-slate-200">
                <button
                  onClick={() => setActiveTab('evidence-verification')}
                  className="gov-btn-primary text-xs py-1.5 px-3"
                >
                  Verify Rectification Evidence
                </button>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
"""

evidence_ver_page = """import React from 'react';
import { CheckCircle2, ShieldCheck } from 'lucide-react';
import { EvidenceComparison } from '../../components/visualizer/EvidenceComparison';

interface Props {
  setActiveTab: (tab: string) => void;
}

export const EvidenceVerificationPage: React.FC<Props> = ({ setActiveTab }) => {
  return (
    <div className="space-y-6 pb-12 max-w-5xl mx-auto">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-emerald-800 font-extrabold uppercase tracking-wider">
          <ShieldCheck className="w-4 h-4 text-emerald-800" />
          <span>Computer Vision Quality Assurance</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">AI-Assisted Evidence Verification</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Dual-phase computer vision comparison analyzing pre-inspection vs post-rectification imagery against DGMS safety standards.
        </p>
      </div>

      <EvidenceComparison
        issueId="issue-2041"
        onSuccess={() => setActiveTab('dashboard')}
      />
    </div>
  );
};
"""

with open('src/pages/Inspections/NewInspectionPage.tsx', 'w', encoding='utf-8') as f:
    f.write(new_inspection)

with open('src/pages/Inspections/InspectionHistoryPage.tsx', 'w', encoding='utf-8') as f:
    f.write(inspection_hist)

with open('src/pages/Inspections/AIFindingsPage.tsx', 'w', encoding='utf-8') as f:
    f.write(ai_findings)

with open('src/pages/IssuesCorrectiveActions/AllIssuesPage.tsx', 'w', encoding='utf-8') as f:
    f.write(all_issues)

with open('src/pages/IssuesCorrectiveActions/CriticalIssuesPage.tsx', 'w', encoding='utf-8') as f:
    f.write(critical_issues)

with open('src/pages/IssuesCorrectiveActions/CorrectiveActionsPage.tsx', 'w', encoding='utf-8') as f:
    f.write(corrective_actions)

with open('src/pages/IssuesCorrectiveActions/EvidenceVerificationPage.tsx', 'w', encoding='utf-8') as f:
    f.write(evidence_ver_page)

print("Part 3a: Inspections and Issues pages written successfully!")
