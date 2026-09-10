import os

new_inspection = """import React, { useState, useEffect } from 'react';
import {
  Pickaxe,
  Camera,
  Mic,
  MapPin,
  Clock,
  Sparkles,
  Upload,
  AlertTriangle,
  CheckCircle2,
  Cpu,
  Flame,
  UserCheck,
  RotateCcw,
  Radio,
  FileText
} from 'lucide-react';
import { useApp } from '../../context/AppContext';
import { useAuth } from '../../context/AuthContext';
import { simulateAIFindingsScan, AIClassificationResult } from '../../services/aiService';
import { Inspection, IssueCategory } from '../../types';

interface Props {
  setActiveTab: (tab: string) => void;
}

export const NewInspectionPage: React.FC<Props> = ({ setActiveTab }) => {
  const { addInspection, mines } = useApp();
  const { currentUser } = useAuth();

  const [mineId, setMineId] = useState('mine-gevra');
  const [siteZone, setSiteZone] = useState('Conveyor Trunk Line 4B');
  const [inspectionType, setInspectionType] = useState<'Safety Audit' | 'Environmental Check' | 'Labour Compliance' | 'Routine Patrol'>('Safety Audit');
  const [notes, setNotes] = useState('Missing mechanical protective barrier near high-speed conveyor drive rollers. Emergency pull chord switch is disconnected.');
  const [isRecording, setIsRecording] = useState(false);
  const [recordingSeconds, setRecordingSeconds] = useState(0);

  // GPS state
  const [gps, setGps] = useState({
    lat: 22.3392,
    lng: 82.6081,
    locationName: 'Korba Sector 4 (Gevra Mega Pit)'
  });

  // Processing state
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [scanStep, setScanStep] = useState(0);
  const [aiResult, setAiResult] = useState<AIClassificationResult | null>(null);

  const scanSteps = [
    'Collecting inspection telemetry & geo-stamps...',
    'Analyzing natural language field report & audio transcript...',
    'Running dual-phase neural computer vision raster scan...',
    'Checking historical violation clusters across subsidiary...',
    'Calculating multi-vector risk quantification score...',
    'Synthesizing smart assignee & SLA mitigation timeline...'
  ];

  useEffect(() => {
    let interval: any;
    if (isRecording) {
      interval = setInterval(() => setRecordingSeconds(s => s + 1), 1000);
    } else {
      setRecordingSeconds(0);
    }
    return () => clearInterval(interval);
  }, [isRecording]);

  const handleCaptureGPS = () => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        pos => {
          setGps({
            lat: Number(pos.coords.latitude.toFixed(4)),
            lng: Number(pos.coords.longitude.toFixed(4)),
            locationName: `GPS Auto-lock: Korba Zone 4`
          });
        },
        () => {
          setGps({ lat: 22.3392, lng: 82.6081, locationName: 'Simulated GPS: Gevra Zone 4' });
        }
      );
    }
  };

  const handleVoiceToggle = () => {
    if (!isRecording) {
      setIsRecording(true);
      setTimeout(() => {
        setNotes('Voice audio transcript: "Observed missing safety cage near conveyor belt drive 4B. Rollers exposed with active machinery operation."');
        setIsRecording(false);
      }, 3500);
    } else {
      setIsRecording(false);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsAnalyzing(true);
    setScanStep(0);

    for (let i = 0; i < scanSteps.length; i++) {
      setScanStep(i);
      await new Promise(r => setTimeout(r, 600));
    }

    const res = await simulateAIFindingsScan(notes, inspectionType, siteZone);
    setAiResult(res);
    setIsAnalyzing(false);

    // Add to state
    const newInsp: Inspection = {
      id: 'insp-' + Date.now(),
      inspectionNo: `INSP-2026-${Math.floor(1050 + Math.random() * 500)}`,
      mineId,
      mineName: mines.find(m => m.id === mineId)?.name || 'Gevra Mega Mine',
      siteZone,
      inspectionType,
      inspectorId: currentUser.id,
      inspectorName: currentUser.name,
      date: new Date().toISOString().split('T')[0],
      time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      gps,
      notes,
      voiceTranscript: notes,
      evidences: [
        {
          id: 'ev-' + Date.now(),
          type: 'photo',
          url: 'https://images.unsplash.com/photo-1578328819058-b69f3a3b0f6b?auto=format&fit=crop&w=800&q=80',
          caption: 'Hazard Evidence: Exposed conveyor rollers',
          timestamp: new Date().toLocaleTimeString()
        }
      ],
      findingsCount: 1,
      status: 'AI Analyzed',
      aiProcessed: true
    };

    addInspection(newInsp, {
      title: 'Missing protective barrier near conveyor belt trunk line 4B',
      description: notes,
      category: res.category,
      severity: res.severity,
      riskScore: res.riskScore,
      confidence: res.confidence,
      assignedDepartment: res.suggestedDepartment,
      assignedOfficer: res.recommendedAssignee.name,
      aiExplanation: {
        whySeverity: res.whySeverity,
        riskFactors: res.riskFactors,
        historicalContext: res.historicalContext
      }
    });
  };

  return (
    <div className="max-w-4xl mx-auto space-y-6 pb-12">
      {/* Title */}
      <div className="glass-panel p-5 rounded-2xl border border-slate-800 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2 text-xs text-safety-orange font-bold uppercase tracking-wider">
            <Radio className="w-4 h-4 text-safety-orange animate-pulse" />
            <span>Mobile-First Field Inspection Engine</span>
          </div>
          <h1 className="text-2xl font-black text-white mt-1">AI Field Inspection</h1>
          <p className="text-xs text-slate-400 mt-0.5">
            Auto-capture GPS, audio voice speech-to-text, photo raster evidence & instant neural risk scoring
          </p>
        </div>
      </div>

      {!aiResult && !isAnalyzing && (
        <form onSubmit={handleSubmit} className="glass-panel p-6 rounded-2xl border border-slate-800 space-y-5 shadow-2xl">
          {/* Metadata Grid */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div className="space-y-1.5">
              <label className="text-xs font-bold text-slate-300 uppercase">Mine Location</label>
              <select
                value={mineId}
                onChange={e => setMineId(e.target.value)}
                className="w-full bg-coal-800 text-white font-bold text-xs p-3 rounded-xl border border-slate-700 focus:outline-none focus:border-safety-orange"
              >
                {mines.map(m => (
                  <option key={m.id} value={m.id}>{m.name} ({m.subsidiary})</option>
                ))}
              </select>
            </div>

            <div className="space-y-1.5">
              <label className="text-xs font-bold text-slate-300 uppercase">Operational Zone / Site</label>
              <input
                type="text"
                value={siteZone}
                onChange={e => setSiteZone(e.target.value)}
                placeholder="e.g. Conveyor Trunk Line 4B"
                className="w-full bg-coal-800 text-white font-bold text-xs p-3 rounded-xl border border-slate-700 focus:outline-none focus:border-safety-orange"
              />
            </div>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div className="space-y-1.5">
              <label className="text-xs font-bold text-slate-300 uppercase">Inspection Type</label>
              <select
                value={inspectionType}
                onChange={e => setInspectionType(e.target.value as any)}
                className="w-full bg-coal-800 text-white font-bold text-xs p-3 rounded-xl border border-slate-700 focus:outline-none focus:border-safety-orange"
              >
                <option value="Safety Audit">Safety Audit (DGMS CMR 2017)</option>
                <option value="Environmental Check">Environmental Check (MoEFCC)</option>
                <option value="Labour Compliance">Labour Compliance (Form B / VTC)</option>
                <option value="Routine Patrol">Routine Shift Patrol</option>
              </select>
            </div>

            <div className="space-y-1.5">
              <label className="text-xs font-bold text-slate-300 uppercase">Inspector In-Charge</label>
              <input
                type="text"
                value={`${currentUser.name} (${currentUser.roleTitle.split(' ')[0]})`}
                disabled
                className="w-full bg-coal-900 text-slate-400 font-mono text-xs p-3 rounded-xl border border-slate-800 cursor-not-allowed"
              />
            </div>
          </div>

          {/* Auto-Captured Geo Sensors */}
          <div className="p-3.5 rounded-xl bg-coal-900/90 border border-slate-700/80 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 text-xs">
            <div className="flex items-center space-x-2">
              <MapPin className="w-4 h-4 text-emerald-400" />
              <div>
                <span className="font-mono text-white font-bold">{gps.lat}°N, {gps.lng}°E</span>
                <p className="text-[11px] text-slate-400">{gps.locationName}</p>
              </div>
            </div>
            <button
              type="button"
              onClick={handleCaptureGPS}
              className="px-3 py-1.5 rounded-lg bg-coal-800 text-safety-cyan border border-safety-cyan/30 text-xs font-bold hover:bg-coal-750"
            >
              Re-acquire GPS
            </button>
          </div>

          {/* Report Notes & Audio */}
          <div className="space-y-2">
            <div className="flex items-center justify-between">
              <label className="text-xs font-bold text-slate-300 uppercase">Observation & Defect Description</label>
              <button
                type="button"
                onClick={handleVoiceToggle}
                className={`flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-all ${
                  isRecording
                    ? 'bg-red-600 text-white animate-pulse'
                    : 'bg-coal-800 text-slate-300 border border-slate-700 hover:text-white'
                }`}
              >
                <Mic className="w-3.5 h-3.5 text-safety-orange" />
                <span>{isRecording ? `Recording... (${recordingSeconds}s)` : 'Record Voice Audio'}</span>
              </button>
            </div>
            <textarea
              value={notes}
              onChange={e => setNotes(e.target.value)}
              rows={4}
              placeholder="Describe the safety, environmental, or operational hazard in detail..."
              className="w-full bg-coal-950 border border-slate-700 rounded-xl p-3 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-safety-orange"
            />
          </div>

          {/* Photo Evidence Gallery */}
          <div className="space-y-2">
            <label className="text-xs font-bold text-slate-300 uppercase">Evidence Photographs (Captured on-site)</label>
            <div className="grid grid-cols-2 sm:grid-cols-3 gap-3">
              <div className="relative rounded-xl overflow-hidden border border-slate-700 group h-28 bg-coal-950">
                <img
                  src="https://images.unsplash.com/photo-1578328819058-b69f3a3b0f6b?auto=format&fit=crop&w=800&q=80"
                  alt="Conveyor Hazard"
                  className="w-full h-full object-cover"
                />
                <span className="absolute bottom-1 left-1 z-10 bg-coal-900/90 text-white text-[9px] px-1.5 py-0.5 rounded font-mono">
                  Hazard Raster 01
                </span>
              </div>
              <div className="border-2 border-dashed border-slate-700 rounded-xl flex flex-col items-center justify-center p-4 text-center text-slate-400 hover:border-safety-orange cursor-pointer transition-colors h-28">
                <Camera className="w-5 h-5 text-safety-orange mb-1" />
                <span className="text-[11px] font-bold text-slate-300">Add Live Photo</span>
                <span className="text-[9px] text-slate-500">Geo-stamped</span>
              </div>
            </div>
          </div>

          {/* Submit CTA */}
          <button
            type="submit"
            className="w-full py-3.5 rounded-xl bg-gradient-to-r from-safety-orange to-amber-500 hover:from-safety-orange/90 text-white font-extrabold text-xs uppercase tracking-wider shadow-xl shadow-safety-orange/20 transition-all flex items-center justify-center space-x-2"
          >
            <Sparkles className="w-4 h-4" />
            <span>Submit Inspection & Run AI Classification Scan</span>
          </button>
        </form>
      )}

      {/* 6-Stage Neural Scanning Progress */}
      {isAnalyzing && (
        <div className="glass-panel p-8 rounded-2xl border border-safety-orange/40 text-center space-y-6 animate-fade-in shadow-2xl">
          <div className="w-16 h-16 rounded-full border-4 border-safety-orange border-t-transparent animate-spin mx-auto flex items-center justify-center">
            <Cpu className="w-8 h-8 text-safety-orange" />
          </div>

          <div className="space-y-2">
            <h3 className="text-base font-extrabold text-white uppercase tracking-wider">
              MineGuard AI is analyzing your inspection...
            </h3>
            <p className="text-xs text-safety-orange font-mono font-bold animate-pulse">
              {scanSteps[scanStep]}
            </p>
          </div>

          <div className="w-full h-2 bg-coal-950 rounded-full overflow-hidden max-w-md mx-auto">
            <div
              className="h-full bg-gradient-to-r from-safety-orange to-amber-500 transition-all duration-300"
              style={{ width: `${((scanStep + 1) / scanSteps.length) * 100}%` }}
            />
          </div>
        </div>
      )}

      {/* AI Output Findings Card */}
      {aiResult && (
        <div className="glass-panel p-6 rounded-2xl border border-red-500/40 bg-coal-900/95 space-y-6 animate-slide-up shadow-2xl">
          <div className="flex items-center justify-between pb-4 border-b border-slate-800">
            <div className="flex items-center space-x-2.5">
              <div className="w-8 h-8 rounded-lg bg-red-600 text-white flex items-center justify-center font-bold">
                <Flame className="w-4 h-4" />
              </div>
              <div>
                <span className="text-[10px] font-extrabold uppercase tracking-widest text-red-400">
                  AI Inspection Scan Completed
                </span>
                <h3 className="text-base font-black text-white">AI FINDINGS & CLASSIFICATION</h3>
              </div>
            </div>
            <div className="text-right">
              <span className="text-xs text-slate-400">AI Risk Score</span>
              <div className="text-2xl font-black text-red-400 font-mono">{aiResult.riskScore} <span className="text-xs text-slate-400">/100</span></div>
            </div>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
            <div className="p-3 bg-coal-950 rounded-xl border border-slate-800">
              <span className="text-[10px] text-slate-400 uppercase font-bold">Category</span>
              <p className="text-xs font-black text-white mt-1">{aiResult.category}</p>
            </div>
            <div className="p-3 bg-coal-950 rounded-xl border border-slate-800">
              <span className="text-[10px] text-slate-400 uppercase font-bold">Severity</span>
              <p className="text-xs font-black text-red-400 mt-1">{aiResult.severity}</p>
            </div>
            <div className="p-3 bg-coal-950 rounded-xl border border-slate-800">
              <span className="text-[10px] text-slate-400 uppercase font-bold">Confidence</span>
              <p className="text-xs font-black text-emerald-400 font-mono mt-1">{aiResult.confidence}%</p>
            </div>
            <div className="p-3 bg-coal-950 rounded-xl border border-slate-800">
              <span className="text-[10px] text-slate-400 uppercase font-bold">Statutory SLA</span>
              <p className="text-xs font-black text-amber-400 font-mono mt-1">{aiResult.suggestedSLAHours} Hours</p>
            </div>
          </div>

          {/* AI RCA Reasoning */}
          <div className="p-4 rounded-xl bg-coal-950 border border-slate-800 space-y-2">
            <span className="text-xs font-extrabold text-white uppercase tracking-wider">AI Classification Explanation:</span>
            <ul className="space-y-1 text-xs text-slate-300">
              {aiResult.whySeverity.map((item, idx) => (
                <li key={idx} className="flex items-start space-x-2">
                  <span className="text-red-400 font-bold">•</span>
                  <span>{item}</span>
                </li>
              ))}
            </ul>
          </div>

          {/* Smart Assignee Suggestion */}
          <div className="p-4 rounded-xl bg-coal-950 border border-safety-orange/30 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 rounded-full bg-safety-orange/20 text-safety-orange flex items-center justify-center font-bold">
                <UserCheck className="w-5 h-5" />
              </div>
              <div>
                <span className="text-[10px] font-bold text-safety-orange uppercase tracking-wider">Recommended Assignee</span>
                <h4 className="text-xs font-extrabold text-white">{aiResult.recommendedAssignee.name}</h4>
                <p className="text-[11px] text-slate-400">{aiResult.recommendedAssignee.role} • Active Tasks: {aiResult.recommendedAssignee.activeWorkload}</p>
              </div>
            </div>

            <button
              onClick={() => setActiveTab('corrective-actions')}
              className="px-4 py-2 rounded-xl bg-safety-orange hover:bg-safety-orange/90 text-white font-extrabold text-xs shadow-lg shadow-safety-orange/20"
            >
              Dispatch Corrective Action
            </button>
          </div>
        </div>
      )}
    </div>
  );
};
"""

inspection_history = """import React from 'react';
import { History, Eye, MapPin, CheckCircle2, AlertTriangle, Calendar } from 'lucide-react';
import { useApp } from '../../context/AppContext';

export const InspectionHistoryPage: React.FC = () => {
  const { inspections } = useApp();

  const mockPastInspections = [
    { no: 'INSP-2026-1049', mine: 'Gevra Mega Mine', zone: 'Conveyor Trunk Line 4B', date: '30 Aug 2026 09:15', inspector: 'Vikramaditya Rao', status: 'AI Analyzed', findings: 'Critical Safety Hazard (92/100)' },
    { no: 'INSP-2026-1048', mine: 'Gevra Mega Mine', zone: 'South OB Dump Area', date: '29 Aug 2026 14:00', inspector: 'Alok Nandan', status: 'Completed', findings: 'Tension Crack Mitigated' },
    { no: 'INSP-2026-1047', mine: 'Moonidih Mine', zone: 'Panel 18 Return Airway', date: '29 Aug 2026 06:30', inspector: 'Subhashish Sen', status: 'In Progress', findings: 'Ventilation Velocity Deficit' },
    { no: 'INSP-2026-1046', mine: 'Kusmunda Mine', zone: 'Sector 2 Pit Face', date: '28 Aug 2026 11:20', inspector: 'Sunil Verma', status: 'Completed', findings: 'Contractor VTC Audit' }
  ];

  return (
    <div className="space-y-6 pb-12">
      <div className="glass-panel p-5 rounded-2xl border border-slate-800">
        <div className="flex items-center space-x-2 text-xs text-safety-orange font-bold uppercase tracking-wider">
          <History className="w-4 h-4 text-safety-orange" />
          <span>Audit & Inspection Logs</span>
        </div>
        <h1 className="text-2xl font-black text-white mt-1">Inspection History</h1>
        <p className="text-xs text-slate-400 mt-0.5">
          Archived field audits, geo-stamps, multi-raster hazard evidence, and inspector signatures
        </p>
      </div>

      <div className="space-y-3">
        {mockPastInspections.map(insp => (
          <div
            key={insp.no}
            className="glass-panel p-4 rounded-xl border border-slate-800 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 hover:border-slate-700 transition-all"
          >
            <div>
              <div className="flex items-center space-x-2">
                <span className="font-mono font-bold text-white text-xs">{insp.no}</span>
                <span className="text-[10px] bg-coal-800 text-slate-300 font-mono px-2 py-0.5 rounded">{insp.mine}</span>
              </div>
              <p className="text-xs font-bold text-slate-200 mt-1">{insp.zone}</p>
              <p className="text-[11px] text-slate-400 mt-0.5">Inspector: {insp.inspector} • {insp.date}</p>
            </div>

            <div className="flex items-center space-x-3 self-end sm:self-center">
              <span className="text-[11px] text-amber-400 font-mono font-bold">{insp.findings}</span>
              <span className="text-[10px] font-extrabold px-2.5 py-1 rounded bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 uppercase">
                {insp.status}
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

ai_findings = """import React from 'react';
import { ScanEye, Flame, CheckCircle2, UserCheck, ArrowRight } from 'lucide-react';
import { useApp } from '../../context/AppContext';

interface Props {
  setActiveTab: (tab: string) => void;
}

export const AIFindingsPage: React.FC<Props> = ({ setActiveTab }) => {
  const { issues } = useApp();

  return (
    <div className="space-y-6 pb-12">
      <div className="glass-panel p-5 rounded-2xl border border-slate-800">
        <div className="flex items-center space-x-2 text-xs text-safety-orange font-bold uppercase tracking-wider">
          <ScanEye className="w-4 h-4 text-safety-orange" />
          <span>Neural Hazard Detection</span>
        </div>
        <h1 className="text-2xl font-black text-white mt-1">AI Findings & Anomaly Detection</h1>
        <p className="text-xs text-slate-400 mt-0.5">
          Real-time issues detected by AI field inspections, IoT air telemetry, and automated audit checks
        </p>
      </div>

      <div className="space-y-4">
        {issues.map(issue => (
          <div key={issue.id} className="glass-panel p-5 rounded-xl border border-slate-800 space-y-3">
            <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between pb-3 border-b border-slate-800 gap-2">
              <div className="flex items-center space-x-2">
                <span className={`text-[10px] font-extrabold px-2 py-0.5 rounded ${
                  issue.severity === 'Critical' ? 'bg-red-500 text-white' : 'bg-amber-500 text-black'
                }`}>
                  {issue.severity}
                </span>
                <span className="font-mono font-bold text-white text-xs">{issue.issueCode}</span>
                <span className="text-[10px] text-slate-400">• {issue.category}</span>
              </div>
              <div className="flex items-center space-x-3 text-xs font-mono">
                <span className="text-slate-400">Risk Score: <strong className="text-red-400">{issue.riskScore}/100</strong></span>
                <span className="text-slate-400">Confidence: <strong className="text-emerald-400">{issue.confidence}%</strong></span>
              </div>
            </div>

            <h3 className="text-sm font-extrabold text-white">{issue.title}</h3>
            <p className="text-xs text-slate-300">{issue.description}</p>

            <div className="p-3 bg-coal-950 rounded-lg text-xs space-y-1">
              <span className="font-bold text-slate-400 text-[10px] uppercase">AI Root Cause Reasoning:</span>
              <ul className="space-y-1 text-[11px] text-slate-300">
                {issue.aiExplanation.whySeverity.map((why, idx) => (
                  <li key={idx} className="flex items-start space-x-1.5">
                    <span className="text-safety-orange">•</span>
                    <span>{why}</span>
                  </li>
                ))}
              </ul>
            </div>

            <div className="flex items-center justify-between pt-2 text-xs">
              <span className="text-slate-400">Assigned: <strong className="text-white">{issue.assignedOfficer}</strong></span>
              <button
                onClick={() => setActiveTab('evidence-verification')}
                className="text-xs font-bold text-safety-orange hover:underline flex items-center space-x-1"
              >
                <span>Verify Evidence</span>
                <ArrowRight className="w-3.5 h-3.5" />
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
import { AlertTriangle, Filter, Search, Flame, ArrowUpRight, CheckCircle2 } from 'lucide-react';
import { useApp } from '../../context/AppContext';
import { IssueStatus } from '../../types';

interface Props {
  setActiveTab: (tab: string) => void;
}

export const AllIssuesPage: React.FC<Props> = ({ setActiveTab }) => {
  const { issues } = useApp();
  const [searchTerm, setSearchTerm] = useState('');
  const [filterCat, setFilterCat] = useState('ALL');

  const filtered = issues.filter(i => {
    const matchesSearch = i.title.toLowerCase().includes(searchTerm.toLowerCase()) || i.issueCode.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesCat = filterCat === 'ALL' || i.category === filterCat;
    return matchesSearch && matchesCat;
  });

  return (
    <div className="space-y-6 pb-12">
      <div className="glass-panel p-5 rounded-2xl border border-slate-800 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2 text-xs text-safety-orange font-bold uppercase tracking-wider">
            <AlertTriangle className="w-4 h-4 text-safety-orange" />
            <span>Closed-Loop Issue Repository</span>
          </div>
          <h1 className="text-2xl font-black text-white mt-1">All Mining Issues</h1>
          <p className="text-xs text-slate-400 mt-0.5">
            Full lifecycle tracking: OPEN &rarr; AI CLASSIFIED &rarr; ASSIGNED &rarr; IN PROGRESS &rarr; RESOLVED &rarr; VERIFIED &rarr; CLOSED
          </p>
        </div>

        <div className="flex items-center space-x-2 w-full sm:w-auto">
          <input
            type="text"
            placeholder="Search issues..."
            value={searchTerm}
            onChange={e => setSearchTerm(e.target.value)}
            className="bg-coal-800 border border-slate-700 rounded-xl px-3 py-2 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-safety-orange w-full sm:w-60"
          />
          <select
            value={filterCat}
            onChange={e => setFilterCat(e.target.value)}
            className="bg-coal-800 text-white font-bold text-xs px-3 py-2 rounded-xl border border-slate-700"
          >
            <option value="ALL">All Categories</option>
            <option value="Safety">Safety</option>
            <option value="Environment">Environment</option>
            <option value="Contractor Compliance">Contractor</option>
          </select>
        </div>
      </div>

      <div className="space-y-3">
        {filtered.map(issue => (
          <div
            key={issue.id}
            className="glass-panel p-4 rounded-xl border border-slate-800 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 hover:border-slate-700 transition-all"
          >
            <div className="space-y-1">
              <div className="flex items-center space-x-2">
                <span className={`text-[10px] font-extrabold px-2 py-0.5 rounded ${
                  issue.severity === 'Critical' ? 'bg-red-500 text-white' : 'bg-amber-500 text-black'
                }`}>
                  {issue.severity}
                </span>
                <span className="font-mono font-bold text-white text-xs">{issue.issueCode}</span>
                <span className="text-[10px] text-slate-400 font-mono">{issue.mineName}</span>
              </div>
              <h3 className="text-xs font-bold text-white">{issue.title}</h3>
              <p className="text-[11px] text-slate-400">Assigned: {issue.assignedOfficer} • Due: {issue.deadline}</p>
            </div>

            <div className="flex items-center space-x-3 self-end sm:self-center">
              <span className={`text-[10px] font-extrabold px-2.5 py-1 rounded uppercase font-mono ${
                issue.status === 'OPEN' ? 'bg-red-500/20 text-red-400 border border-red-500/30' :
                issue.status === 'ASSIGNED' ? 'bg-orange-500/20 text-orange-400' :
                issue.status === 'IN_PROGRESS' ? 'bg-amber-500/20 text-amber-400' :
                issue.status === 'VERIFIED' ? 'bg-cyan-500/20 text-cyan-400' :
                'bg-emerald-500/20 text-emerald-400'
              }`}>
                {issue.status}
              </span>
              <button
                onClick={() => setActiveTab('evidence-verification')}
                className="p-1.5 rounded-lg bg-coal-800 text-slate-300 hover:text-white"
              >
                <ArrowUpRight className="w-4 h-4" />
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

with open('src/pages/Inspections/NewInspectionPage.tsx', 'w', encoding='utf-8') as f:
    f.write(new_inspection)

with open('src/pages/Inspections/InspectionHistoryPage.tsx', 'w', encoding='utf-8') as f:
    f.write(inspection_history)

with open('src/pages/Inspections/AIFindingsPage.tsx', 'w', encoding='utf-8') as f:
    f.write(ai_findings)

with open('src/pages/IssuesCorrectiveActions/AllIssuesPage.tsx', 'w', encoding='utf-8') as f:
    f.write(all_issues)

print("NewInspection, History, Findings, and AllIssues pages written successfully!")
