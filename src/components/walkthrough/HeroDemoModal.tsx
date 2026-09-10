import React, { useState } from 'react';
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
