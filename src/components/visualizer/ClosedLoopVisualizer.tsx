import React from 'react';
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
