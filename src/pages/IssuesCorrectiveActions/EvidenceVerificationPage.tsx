import React from 'react';
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
