import os

closed_loop = """import React from 'react';
import {
  Scan,
  Cpu,
  Flame,
  UserCheck,
  Wrench,
  CheckCircle2,
  BrainCircuit,
  ArrowRight
} from 'lucide-react';

interface Props {
  activeStep?: number;
}

export const ClosedLoopVisualizer: React.FC<Props> = ({ activeStep = 1 }) => {
  const steps = [
    { num: 1, label: 'DETECT', desc: 'Digital Field Audit', icon: Scan, tag: 'Step 1' },
    { num: 2, label: 'CLASSIFY', desc: 'AI Risk Engine', icon: Cpu, tag: 'Step 2' },
    { num: 3, label: 'PRIORITIZE', desc: 'Explainable Score', icon: Flame, tag: 'Step 3' },
    { num: 4, label: 'ASSIGN', desc: 'Smart Allocation', icon: UserCheck, tag: 'Step 4' },
    { num: 5, label: 'RESOLVE', desc: 'SLA Remediation', icon: Wrench, tag: 'Step 5' },
    { num: 6, label: 'VERIFY', desc: 'AI Evidence Check', icon: CheckCircle2, tag: 'Step 6' },
    { num: 7, label: 'LEARN', desc: 'Cross-Mine Model', icon: BrainCircuit, tag: 'Step 7' },
  ];

  return (
    <div className="gov-card p-4 mb-6">
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between pb-3 mb-3 border-b border-slate-200 gap-2">
        <div className="flex items-center space-x-2">
          <span className="w-2.5 h-2.5 rounded-full bg-[#15803D]" />
          <h3 className="text-xs font-extrabold uppercase tracking-wider text-slate-900">
            Closed-Loop AI Governance Pipeline
          </h3>
          <span className="text-[10px] bg-slate-100 text-slate-700 px-2 py-0.5 rounded border border-slate-300 font-mono">
            USP Architecture
          </span>
        </div>
        <span className="text-xs text-slate-600 font-semibold">
          &ldquo;Detect &bull; Classify &bull; Prioritize &bull; Assign &bull; Resolve &bull; Verify &bull; Learn&rdquo;
        </span>
      </div>

      <div className="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-7 gap-2">
        {steps.map(step => {
          const Icon = step.icon;
          const isCurrent = activeStep === step.num;
          return (
            <div
              key={step.num}
              className={`p-2.5 rounded border text-center transition-all ${
                isCurrent
                  ? 'border-[#0B2545] bg-[#0B2545]/5 ring-2 ring-[#0B2545]/30 shadow-xs'
                  : 'border-slate-200 bg-white hover:bg-slate-50'
              }`}
            >
              <div className="text-[9px] font-extrabold uppercase text-slate-600 font-mono mb-1">{step.tag}</div>
              <div className="w-7 h-7 rounded bg-[#0B2545] text-white flex items-center justify-center mx-auto mb-1.5 shadow-xs">
                <Icon className="w-3.5 h-3.5" />
              </div>
              <span className="text-xs font-black tracking-wide text-slate-900 block">{step.label}</span>
              <span className="text-[10px] text-slate-600 mt-0.5 block truncate">{step.desc}</span>
            </div>
          );
        })}
      </div>
    </div>
  );
};
"""

risk_card = """import React from 'react';
import { ShieldAlert, Info, Flame } from 'lucide-react';
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
    <div className="gov-card p-5 space-y-5">
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between pb-3 border-b border-slate-200 gap-3">
        <div>
          <div className="flex items-center space-x-2">
            <ShieldAlert className="w-4 h-4 text-red-700" />
            <h3 className="text-xs font-extrabold uppercase tracking-wider text-slate-900">
              Explainable AI Risk Score & Factor Breakdown
            </h3>
          </div>
          <p className="text-xs text-slate-500 mt-0.5">
            Multi-vector risk quantification index calculated across 5 statutory domains
          </p>
        </div>

        <div className="flex items-center space-x-3 bg-slate-50 px-4 py-2 rounded border border-slate-300">
          <div>
            <div className="text-xl font-black text-slate-900 font-mono">
              {mine.riskScore} <span className="text-xs text-slate-500 font-normal">/ 100</span>
            </div>
            <div className="text-[10px] font-extrabold tracking-wider text-red-700 uppercase">
              {mine.riskScore > 70 ? 'CRITICAL RISK LEVEL' : 'HIGH RISK LEVEL'}
            </div>
          </div>
          <div className="w-8 h-8 rounded bg-red-100 text-red-800 border border-red-300 flex items-center justify-center font-bold">
            <Flame className="w-4 h-4" />
          </div>
        </div>
      </div>

      <div className="space-y-2.5">
        <h4 className="text-xs font-bold text-slate-700 uppercase tracking-wider">Statutory Risk Vectors</h4>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-3">
          {[
            { label: 'Safety Compliance', score: breakdown.safety, color: 'bg-red-700', text: 'text-red-700' },
            { label: 'Environmental', score: breakdown.environment, color: 'bg-amber-600', text: 'text-amber-700' },
            { label: 'Labour & VTC', score: breakdown.labour, color: 'bg-blue-700', text: 'text-blue-700' },
            { label: 'Production Deficit', score: breakdown.production, color: 'bg-slate-700', text: 'text-slate-700' },
            { label: 'Contractor Risk', score: breakdown.contractor, color: 'bg-purple-700', text: 'text-purple-700' },
          ].map(vec => (
            <div key={vec.label} className="bg-slate-50 p-3 rounded border border-slate-200">
              <div className="flex items-center justify-between text-xs mb-1">
                <span className="text-slate-600 font-medium text-[11px]">{vec.label}</span>
                <span className={`font-mono font-bold ${vec.text}`}>{vec.score}</span>
              </div>
              <div className="w-full h-2 bg-slate-200 rounded-full overflow-hidden">
                <div className={`h-full ${vec.color}`} style={{ width: `${vec.score}%` }} />
              </div>
            </div>
          ))}
        </div>
      </div>

      <div className="space-y-2">
        <h4 className="text-xs font-bold text-slate-700 uppercase tracking-wider">Contributing Factors (Waterfall Analysis)</h4>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-2">
          {waterfallFactors.map(f => (
            <div
              key={f.factor}
              className={`p-2 rounded border flex items-center justify-between text-xs ${
                f.positive
                  ? 'bg-emerald-50 border-emerald-300 text-emerald-900'
                  : 'bg-slate-50 border-slate-200 text-slate-800'
              }`}
            >
              <span className="text-[11px] truncate mr-2">{f.factor}</span>
              <span className={`font-mono font-black px-1.5 py-0.5 rounded text-[11px] ${
                f.positive ? 'bg-emerald-200 text-emerald-900' : 'bg-red-100 text-red-800'
              }`}>
                {f.points}
              </span>
            </div>
          ))}
        </div>
      </div>

      <div className="p-3.5 rounded bg-amber-50/70 border border-amber-200 flex items-start space-x-2.5 text-xs">
        <Info className="w-4 h-4 text-amber-800 shrink-0 mt-0.5" />
        <div>
          <span className="font-extrabold text-slate-900 uppercase text-[10px] tracking-wide block">
            Why is this mine high risk? (AI Reasoned Assessment)
          </span>
          <p className="text-slate-700 leading-relaxed mt-0.5">
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
  RotateCcw,
  Sparkles,
  ShieldCheck,
  Eye,
  FileCheck
} from 'lucide-react';
import { useApp } from '../../context/AppContext';

interface Props {
  issueId?: string;
  onSuccess?: () => void;
}

export const EvidenceComparison: React.FC<Props> = ({ issueId = 'issue-2041', onSuccess }) => {
  const { issues, closeVerifiedIssue, requestIssueRework } = useApp();
  const [showOverlays, setShowOverlays] = useState(true);
  const [reworkModalOpen, setReworkModalOpen] = useState(false);
  const [reworkNotes, setReworkNotes] = useState('');

  const issue = issues.find(i => i.id === issueId) || issues[0];
  const ca = issue?.correctiveAction;

  const beforeUrl = ca?.beforeEvidenceUrl || 'https://images.unsplash.com/photo-1578328819058-b69f3a3b0f6b?auto=format&fit=crop&w=800&q=80';
  const afterUrl = ca?.afterEvidenceUrl || 'https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=800&q=80';

  const handleApprove = () => {
    closeVerifiedIssue(issue.id);
    if (onSuccess) onSuccess();
  };

  const handleRework = () => {
    if (reworkNotes.trim()) {
      requestIssueRework(issue.id, reworkNotes);
      setReworkModalOpen(false);
    }
  };

  return (
    <div className="gov-card p-5 space-y-5">
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between pb-3 border-b border-slate-200 gap-2">
        <div>
          <div className="flex items-center space-x-2">
            <span className="w-2.5 h-2.5 rounded-full bg-[#15803D]" />
            <h3 className="text-xs font-extrabold uppercase tracking-wider text-slate-900">
              AI-Assisted Evidence Verification & Case Closure
            </h3>
          </div>
          <p className="text-xs text-slate-500 mt-0.5">
            Issue Docket #{issue.issueCode}: {issue.title}
          </p>
        </div>

        <button
          onClick={() => setShowOverlays(!showOverlays)}
          className="gov-btn-secondary text-xs"
        >
          <Eye className="w-3.5 h-3.5" />
          <span>Toggle AI Detection Boxes</span>
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div className="rounded border border-red-300 bg-slate-900 overflow-hidden relative">
          <div className="bg-red-800 text-white font-extrabold text-[10px] px-2.5 py-1 tracking-wider uppercase flex items-center justify-between">
            <span>BEFORE EVIDENCE (Inspection Record)</span>
            <span className="font-mono">RISK: 92/100</span>
          </div>
          <img
            src={beforeUrl}
            alt="Before Inspection"
            className="w-full h-60 object-cover"
          />
          {showOverlays && (
            <div className="absolute inset-0 pointer-events-none p-4 mt-6">
              <div className="absolute top-12 left-10 w-44 h-28 border-2 border-dashed border-red-500 bg-red-500/20 rounded flex items-start p-1">
                <span className="bg-red-700 text-white text-[9px] font-bold px-1 rounded">
                  Hazard: Missing Guard Mesh
                </span>
              </div>
            </div>
          )}
          <div className="p-2.5 bg-slate-100 border-t border-slate-200 text-xs">
            <span className="font-bold text-slate-900">Recorded Condition:</span>
            <p className="text-slate-600 text-[11px]">Exposed high-speed conveyor drive rollers lacking mandatory protective barrier.</p>
          </div>
        </div>

        <div className="rounded border border-emerald-400 bg-slate-900 overflow-hidden relative">
          <div className="bg-emerald-800 text-white font-extrabold text-[10px] px-2.5 py-1 tracking-wider uppercase flex items-center justify-between">
            <span>AFTER EVIDENCE (Rectification Docket)</span>
            <span className="font-mono">CONFIDENCE: 91%</span>
          </div>
          <img
            src={afterUrl}
            alt="After Verification"
            className="w-full h-60 object-cover"
          />
          {showOverlays && (
            <div className="absolute inset-0 pointer-events-none p-4 mt-6">
              <div className="absolute top-10 left-8 w-52 h-36 border-2 border-emerald-400 bg-emerald-500/20 rounded flex items-start p-1">
                <span className="bg-emerald-700 text-white text-[9px] font-bold px-1 rounded flex items-center space-x-1">
                  <CheckCircle2 className="w-2.5 h-2.5" />
                  <span>Verified: Heavy-Duty Guard Installed</span>
                </span>
              </div>
            </div>
          )}
          <div className="p-2.5 bg-slate-100 border-t border-slate-200 text-xs">
            <span className="font-bold text-slate-900">Verification Result:</span>
            <p className="text-slate-600 text-[11px]">Computer vision scan confirmed ISO standard mesh installed with emergency trip-wire active.</p>
          </div>
        </div>
      </div>

      <div className="p-4 rounded border border-emerald-300 bg-emerald-50/70 space-y-2.5 text-xs">
        <div className="flex items-center justify-between">
          <div>
            <span className="text-[10px] font-bold uppercase text-emerald-800 tracking-wider">AI Verification Assessment</span>
            <h4 className="text-sm font-black text-emerald-900">LIKELY RESOLVED (91% Confidence)</h4>
          </div>
          <span className="bg-emerald-200 text-emerald-900 text-xs font-mono font-black px-2.5 py-1 rounded">
            Hazard Reduction: 94%
          </span>
        </div>

        <div className="pt-2 border-t border-emerald-200/80 space-y-1 text-slate-800">
          <span className="font-bold text-[11px] uppercase tracking-wide">Detected Remediation Checklist:</span>
          <ul className="space-y-1 text-[11px]">
            {[
              'Heavy-duty industrial steel mesh guard securely installed along 14m conveyor flank',
              'Emergency trip-wire pull chord reconnected with tension indicator verified in green band',
              'Restricted yellow hazard perimeter demarcation painted on concrete footing',
              'Mechanical pinch point hazard reduced to statutory compliant baseline'
            ].map((item, idx) => (
              <li key={idx} className="flex items-start space-x-2">
                <CheckCircle2 className="w-3.5 h-3.5 text-emerald-700 shrink-0 mt-0.5" />
                <span>{item}</span>
              </li>
            ))}
          </ul>
        </div>
      </div>

      <div className="flex items-center justify-end space-x-3 pt-2">
        <button
          onClick={() => setReworkModalOpen(true)}
          className="gov-btn-secondary"
        >
          <RotateCcw className="w-3.5 h-3.5 text-amber-700" />
          <span>Request Additional Rework</span>
        </button>

        <button
          onClick={handleApprove}
          className="gov-btn-success"
        >
          <ShieldCheck className="w-4 h-4" />
          <span>Approve Evidence & Close Case</span>
        </button>
      </div>

      {reworkModalOpen && (
        <div className="fixed inset-0 z-50 bg-black/60 backdrop-blur-xs flex items-center justify-center p-4">
          <div className="bg-white border border-slate-300 p-5 rounded-lg max-w-md w-full space-y-4 shadow-gov-lg">
            <h4 className="text-sm font-bold text-slate-900 uppercase">Official Rework Directive</h4>
            <textarea
              value={reworkNotes}
              onChange={e => setReworkNotes(e.target.value)}
              placeholder="State precise statutory or structural deficiency..."
              rows={3}
              className="w-full bg-slate-50 border border-slate-300 rounded p-2.5 text-xs text-slate-900 focus:outline-none focus:border-[#0B2545]"
            />
            <div className="flex justify-end space-x-2">
              <button
                onClick={() => setReworkModalOpen(false)}
                className="gov-btn-secondary text-xs"
              >
                Cancel
              </button>
              <button
                onClick={handleRework}
                className="gov-btn-primary text-xs"
              >
                Issue Rework Notice
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
"""

hero_demo = """import React, { useState } from 'react';
import {
  Award,
  ChevronRight,
  ChevronLeft,
  X,
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
      title: 'Field Inspector Opens Digital Field Inspection',
      desc: 'Senior Inspector Vikramaditya Rao initiates mobile-first inspection at Gevra Mega Open Cast Mine.',
      actionLabel: 'Open Field Inspection',
      onTrigger: () => { switchRole('FIELD_INSPECTOR'); setActiveTab('new-inspection'); }
    },
    {
      step: 2,
      title: 'Auto-Capture Geo-Coordinates & Timestamp',
      desc: 'Mobile sensors lock GPS (22.3392°N, 82.6081°E), altitude 312m, and Korba Sector 4 stamp.',
      actionLabel: 'Verify GPS Lock',
      onTrigger: () => { setActiveTab('new-inspection'); }
    },
    {
      step: 3,
      title: 'Upload Hazard Photo & Transcribe Voice Report',
      desc: 'Inspector uploads evidence photo and records observation: "Missing protective barrier near conveyor belt trunk line 4B".',
      actionLabel: 'Inspect Evidence Form',
      onTrigger: () => { setActiveTab('new-inspection'); }
    },
    {
      step: 4,
      title: 'AI Classification & Multi-Vector Risk Score',
      desc: 'MineGuard AI analyzes report & historical clusters: Risk Score 92/100 (CRITICAL).',
      actionLabel: 'View AI Findings',
      onTrigger: () => { setActiveTab('ai-findings'); }
    },
    {
      step: 5,
      title: 'Explainable AI Root Cause Assessment',
      desc: 'System provides numbered explainable risk factors: 4 prior violations, high worker transit, CMR 2017 breach.',
      actionLabel: 'View Risk Analytics',
      onTrigger: () => { setActiveTab('ai-risk-analytics'); }
    },
    {
      step: 6,
      title: 'Smart Assignee Recommendation',
      desc: 'System auto-recommends Safety Officer Rajesh Kumar (Zone 4 Lead) based on competency and workload.',
      actionLabel: 'View Corrective Actions',
      onTrigger: () => { switchRole('MINE_OFFICIAL'); setActiveTab('corrective-actions'); }
    },
    {
      step: 7,
      title: 'Corrective Action Created with 24-Hour SLA Timer',
      desc: 'Case dispatched with active countdown SLA and 4-tier management escalation rules.',
      actionLabel: 'View Critical SLAs',
      onTrigger: () => { setActiveTab('critical-issues'); }
    },
    {
      step: 8,
      title: 'Officer Rectifies Hazard & Submits After Evidence',
      desc: 'Maintenance crew installs heavy-duty steel mesh enclosure and reconnects emergency trip-wire switch.',
      actionLabel: 'Open Evidence Verification',
      onTrigger: () => { setActiveTab('evidence-verification'); }
    },
    {
      step: 9,
      title: 'AI Evidence Verification (91% Resolution Confidence)',
      desc: 'Dual-phase neural comparison scans pre and post imagery, validating compliant safety cage.',
      actionLabel: 'Verify Evidence with AI',
      onTrigger: () => { submitEvidenceVerification('issue-2041', 'https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=800&q=80'); setActiveTab('evidence-verification'); }
    },
    {
      step: 10,
      title: 'Mine Manager Approval & Official Case Closure',
      desc: 'General Manager S. N. Mishra approves evidence and closes case in the official register.',
      actionLabel: 'Approve & Close Case',
      onTrigger: () => { closeVerifiedIssue('issue-2041'); setActiveTab('dashboard'); }
    },
    {
      step: 11,
      title: 'Management Dashboard Auto-Updates KPIs',
      desc: `Open Issues: 126 → ${stats.openIssues} | Critical: 8 → ${stats.criticalIssues} | Compliance: 87% → ${stats.overallCompliance}%.`,
      actionLabel: 'View Updated Dashboard',
      onTrigger: () => { setActiveTab('dashboard'); }
    },
    {
      step: 12,
      title: 'Cryptographic SHA-256 Digital Audit Trail',
      desc: 'Every action, inference, and signoff is immutably appended to the digital ledger.',
      actionLabel: 'Inspect Audit Ledger',
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
    <div className="fixed inset-0 z-50 bg-black/60 backdrop-blur-xs flex items-center justify-center p-4">
      <div className="bg-white border border-slate-300 rounded-lg max-w-2xl w-full p-6 shadow-gov-lg space-y-4 animate-slide-up relative">
        <div className="gov-tricolor-strip -mt-6 -mx-6 mb-2 rounded-t-lg" />
        
        <div className="flex items-center justify-between pb-3 border-b border-slate-200">
          <div className="flex items-center space-x-2.5">
            <div className="w-8 h-8 rounded bg-[#0B2545] text-white flex items-center justify-center font-bold">
              <Award className="w-4 h-4 text-amber-400" />
            </div>
            <div>
              <h3 className="text-sm font-extrabold text-[#0B2545] uppercase tracking-wider">
                SIH 2026 Problem ID 26024 — Hero Demo Tour
              </h3>
              <p className="text-[11px] text-slate-500 font-mono">
                Step {currentStep} of {demoSteps.length}: Closed-Loop Governance Flow
              </p>
            </div>
          </div>
          <button onClick={onClose} className="p-1 rounded text-slate-400 hover:text-slate-700 hover:bg-slate-100">
            <X className="w-5 h-5" />
          </button>
        </div>

        <div className="p-4 rounded border border-slate-200 bg-slate-50 space-y-2">
          <div className="flex items-center justify-between text-xs text-slate-600 font-mono">
            <span>PHASE {currentStep}: {current.title.toUpperCase()}</span>
            <span className="text-[#0B2545] font-bold">{Math.round((currentStep / demoSteps.length) * 100)}% Complete</span>
          </div>
          <div className="w-full h-2 bg-slate-200 rounded-full overflow-hidden">
            <div
              className="h-full bg-[#0B2545] transition-all duration-300"
              style={{ width: `${(currentStep / demoSteps.length) * 100}%` }}
            />
          </div>
          <h4 className="text-base font-extrabold text-slate-900 pt-1">{current.title}</h4>
          <p className="text-xs text-slate-700 leading-relaxed">{current.desc}</p>
        </div>

        <button
          onClick={current.onTrigger}
          className="w-full gov-btn-primary py-3"
        >
          <Zap className="w-4 h-4 text-amber-400" />
          <span>Execute & {current.actionLabel}</span>
        </button>

        <div className="flex items-center justify-between pt-2 border-t border-slate-200">
          <button
            onClick={handlePrev}
            disabled={currentStep === 1}
            className="gov-btn-secondary text-xs disabled:opacity-40"
          >
            <ChevronLeft className="w-4 h-4" />
            <span>Previous</span>
          </button>

          <span className="text-xs text-slate-600 font-mono">
            {currentStep} / {demoSteps.length}
          </span>

          <button
            onClick={handleNext}
            disabled={currentStep === demoSteps.length}
            className="gov-btn-primary text-xs disabled:opacity-40"
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

with open('src/components/visualizer/ClosedLoopVisualizer.tsx', 'w', encoding='utf-8') as f:
    f.write(closed_loop)

with open('src/components/visualizer/RiskScoreCard.tsx', 'w', encoding='utf-8') as f:
    f.write(risk_card)

with open('src/components/visualizer/EvidenceComparison.tsx', 'w', encoding='utf-8') as f:
    f.write(evidence_comp)

with open('src/components/walkthrough/HeroDemoModal.tsx', 'w', encoding='utf-8') as f:
    f.write(hero_demo)

print("Part 1b-viz: Visualizers and HeroDemoModal written successfully!")
