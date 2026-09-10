import React, { useState } from 'react';
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
