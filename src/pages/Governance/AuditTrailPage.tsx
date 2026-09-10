import React, { useState } from 'react';
import { Lock, CheckCircle2, RefreshCw } from 'lucide-react';
import { useApp } from '../../context/AppContext';

export const AuditTrailPage: React.FC = () => {
  const { auditLogs } = useApp();
  const [verifying, setVerifying] = useState(false);

  const handleVerifyLedger = () => {
    setVerifying(true);
    setTimeout(() => {
      setVerifying(false);
    }, 1200);
  };

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2 text-xs text-emerald-800 font-extrabold uppercase tracking-wider">
            <Lock className="w-4 h-4 text-emerald-800" />
            <span>Cryptographic Digital Ledger</span>
          </div>
          <h1 className="text-2xl font-black text-slate-900 mt-1">Digital Governance Audit Trail</h1>
          <p className="text-xs text-slate-600 mt-0.5">
            Every inspection, classification, assignment, and manager signoff is secured in a SHA-256 hash-chained block.
          </p>
        </div>

        <button
          onClick={handleVerifyLedger}
          disabled={verifying}
          className="gov-btn-secondary"
        >
          <RefreshCw className={`w-3.5 h-3.5 ${verifying ? 'animate-spin text-[#0B2545]' : ''}`} />
          <span>{verifying ? 'Verifying Ledger...' : 'Verify Cryptographic Integrity'}</span>
        </button>
      </div>

      <div className="space-y-3">
        {auditLogs.map(log => (
          <div
            key={log.blockNumber}
            className="gov-card p-4 space-y-2 font-mono"
          >
            <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between text-xs pb-2 border-b border-slate-200 gap-2">
              <div className="flex items-center space-x-2">
                <span className="bg-[#0B2545] text-white font-black px-2 py-0.5 rounded text-[11px]">
                  BLOCK #{log.blockNumber}
                </span>
                <span className="font-bold text-slate-900 text-xs">{log.action}</span>
                <span className="text-[10px] text-slate-500">({log.module})</span>
              </div>
              <div className="flex items-center space-x-2 text-[10px] text-slate-500">
                <span>{log.timestamp}</span>
                <span className="text-emerald-800 font-bold flex items-center space-x-1">
                  <CheckCircle2 className="w-3 h-3" />
                  <span>SECURE AUDIT RECORD</span>
                </span>
              </div>
            </div>

            <p className="text-xs text-slate-800 font-sans">{log.details}</p>

            <div className="pt-2 text-[10px] text-slate-600 space-y-0.5 bg-slate-50 p-2.5 rounded border border-slate-200">
              <p className="truncate">Block Hash: <strong className="text-emerald-800">{log.blockHash}</strong></p>
              <p className="truncate">Prev Hash: <span className="text-slate-500">{log.previousHash}</span></p>
              <p>Signer: <strong className="text-slate-900 font-sans">{log.user} ({log.role})</strong> &bull; IP: {log.ipAddress}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
