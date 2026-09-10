import os

doc_repo = """import React, { useState } from 'react';
import { FolderOpen, FileText, Download, Eye, ClockAlert, Search, ShieldCheck } from 'lucide-react';
import { useApp } from '../../context/AppContext';

export const DocumentRepositoryPage: React.FC = () => {
  const { documents } = useApp();
  const [searchTerm, setSearchTerm] = useState('');

  const filtered = documents.filter(d => d.title.toLowerCase().includes(searchTerm.toLowerCase()) || d.documentNo.toLowerCase().includes(searchTerm.toLowerCase()));

  return (
    <div className="space-y-6 pb-12">
      <div className="glass-panel p-5 rounded-2xl border border-slate-800 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2 text-xs text-safety-cyan font-bold uppercase tracking-wider">
            <FolderOpen className="w-4 h-4 text-safety-cyan" />
            <span>Central Document Repository</span>
          </div>
          <h1 className="text-2xl font-black text-white mt-1">Statutory Document Vault</h1>
          <p className="text-xs text-slate-400 mt-0.5">
            Cloud-indexed repository of Environmental Clearances, DGMS Mining Permits, and Consent to Operate licenses
          </p>
        </div>

        <input
          type="text"
          placeholder="Search document no, authority..."
          value={searchTerm}
          onChange={e => setSearchTerm(e.target.value)}
          className="bg-coal-800 border border-slate-700 rounded-xl px-3 py-2 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-safety-orange w-full sm:w-64"
        />
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {filtered.map(doc => (
          <div key={doc.id} className="glass-panel p-5 rounded-xl border border-slate-800 space-y-3">
            <div className="flex items-start justify-between">
              <div>
                <span className="text-[10px] font-bold bg-coal-800 text-safety-orange px-2 py-0.5 rounded font-mono">
                  {doc.type}
                </span>
                <h3 className="text-sm font-extrabold text-white mt-1">{doc.title}</h3>
                <p className="text-[11px] text-slate-400 font-mono">Doc No: {doc.documentNo}</p>
              </div>
              <span className={`text-[10px] font-bold px-2 py-0.5 rounded ${
                doc.status === 'Valid' ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30' : 'bg-red-500/20 text-red-400 border border-red-500/30'
              }`}>
                {doc.status}
              </span>
            </div>

            <div className="text-xs text-slate-400 space-y-1">
              <p>Authority: <strong className="text-slate-200">{doc.authority}</strong></p>
              <p>Validity: <strong className="text-slate-200">{doc.issueDate} to {doc.expiryDate}</strong> ({doc.daysToExpiry} days remaining)</p>
            </div>

            <div className="flex justify-end space-x-2 pt-2 border-t border-slate-800">
              <button className="px-3 py-1.5 rounded-lg bg-coal-800 text-slate-300 hover:text-white text-xs font-bold border border-slate-700">
                Preview Clauses
              </button>
              <button className="px-3 py-1.5 rounded-lg bg-safety-orange text-white text-xs font-bold hover:bg-safety-orange/90">
                Download
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

ocr_digitization = """import React, { useState } from 'react';
import { ScanEye, Upload, Sparkles, CheckCircle2, AlertTriangle, FileText, ArrowRight } from 'lucide-react';
import { processDocumentOCR, OCRDigitizationOutput } from '../../services/ocrService';

export const OCRDigitizationPage: React.FC = () => {
  const [selectedFile, setSelectedFile] = useState('MoEFCC_EC_Expansion_70MTPA.pdf');
  const [isScanning, setIsScanning] = useState(false);
  const [ocrResult, setOcrResult] = useState<OCRDigitizationOutput | null>(null);

  const handleScan = async () => {
    setIsScanning(true);
    const res = await processDocumentOCR(selectedFile, 'pdf');
    setOcrResult(res);
    setIsScanning(false);
  };

  return (
    <div className="max-w-4xl mx-auto space-y-6 pb-12">
      <div className="glass-panel p-5 rounded-2xl border border-slate-800">
        <div className="flex items-center space-x-2 text-xs text-safety-cyan font-bold uppercase tracking-wider">
          <ScanEye className="w-4 h-4 text-safety-cyan" />
          <span>AI OCR & Document Intelligence</span>
        </div>
        <h1 className="text-2xl font-black text-white mt-1">OCR Document Digitization</h1>
        <p className="text-xs text-slate-400 mt-0.5">
          Extract statutory clauses, validity dates, compliance conditions, and identify missing renewal attachments.
        </p>
      </div>

      <div className="glass-panel p-8 rounded-2xl border-2 border-dashed border-slate-700 hover:border-safety-orange text-center space-y-4 cursor-pointer transition-all">
        <div className="w-16 h-16 rounded-full bg-safety-orange/15 text-safety-orange flex items-center justify-center mx-auto">
          <Upload className="w-8 h-8" />
        </div>
        <div>
          <h3 className="text-sm font-extrabold text-white">Upload Statutory Document (PDF, Scanned Image)</h3>
          <p className="text-xs text-slate-400 mt-0.5">Supported: EC Clearances, DGMS Circulars, CTOs, Form IV / Form VI</p>
        </div>
        <div className="inline-block bg-coal-800 px-4 py-2 rounded-xl text-xs font-mono text-white border border-slate-700">
          Selected: {selectedFile}
        </div>
        <div>
          <button
            onClick={handleScan}
            disabled={isScanning}
            className="px-6 py-3 rounded-xl bg-gradient-to-r from-safety-orange to-amber-500 hover:from-safety-orange/90 text-white font-extrabold text-xs uppercase tracking-wider shadow-lg shadow-safety-orange/25 transition-all"
          >
            {isScanning ? 'Processing Neural OCR Scanner...' : 'Run AI OCR Extraction'}
          </button>
        </div>
      </div>

      {ocrResult && (
        <div className="glass-panel p-6 rounded-2xl border border-emerald-500/40 bg-coal-900/95 space-y-5 animate-slide-up shadow-2xl">
          <div className="flex items-center justify-between pb-3 border-b border-slate-800">
            <div>
              <span className="text-[10px] font-bold uppercase tracking-widest text-emerald-400">OCR Extraction Completed</span>
              <h3 className="text-base font-black text-white">{ocrResult.documentType}</h3>
            </div>
            <div className="text-right font-mono text-xs text-emerald-400 font-bold">
              Confidence: {ocrResult.confidence}%
            </div>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
            <div className="p-3 bg-coal-950 rounded-xl border border-slate-800">
              <span className="text-[10px] text-slate-400 uppercase">Document Number</span>
              <p className="font-mono font-bold text-white mt-0.5">{ocrResult.documentNo}</p>
            </div>
            <div className="p-3 bg-coal-950 rounded-xl border border-slate-800">
              <span className="text-[10px] text-slate-400 uppercase">Issuing Authority</span>
              <p className="font-bold text-white mt-0.5 truncate">{ocrResult.authority}</p>
            </div>
            <div className="p-3 bg-coal-950 rounded-xl border border-slate-800">
              <span className="text-[10px] text-slate-400 uppercase">Validity Period</span>
              <p className="font-bold text-amber-400 mt-0.5 font-mono">{ocrResult.expiryDate} ({ocrResult.daysToExpiry} days left)</p>
            </div>
          </div>

          <div className="p-4 bg-coal-950 rounded-xl border border-slate-800 space-y-2 text-xs">
            <span className="font-bold text-white uppercase text-[10px]">Extracted Statutory Clauses:</span>
            <ul className="space-y-1 text-slate-300">
              {ocrResult.extractedClauses.map((c, i) => (
                <li key={i} className="flex items-start space-x-2">
                  <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400 shrink-0 mt-0.5" />
                  <span>{c}</span>
                </li>
              ))}
            </ul>
          </div>

          {ocrResult.missingFields.length > 0 && (
            <div className="p-3.5 bg-red-950/30 rounded-xl border border-red-500/40 text-xs flex items-start space-x-2">
              <AlertTriangle className="w-4 h-4 text-red-400 shrink-0 mt-0.5" />
              <div>
                <span className="font-bold text-red-400 uppercase text-[10px]">Missing Mandatory Enclosure Detected:</span>
                <p className="text-slate-300 mt-0.5">{ocrResult.missingFields.join(', ')}</p>
              </div>
            </div>
          )}

          <div className="p-3.5 bg-safety-orange/10 rounded-xl border border-safety-orange/30 text-xs">
            <span className="font-bold text-safety-orange uppercase text-[10px]">AI Action Recommendation:</span>
            <p className="text-white font-semibold mt-0.5">{ocrResult.aiActionRecommendation}</p>
          </div>
        </div>
      )}
    </div>
  );
};
"""

expiring_docs = """import React from 'react';
import { ClockAlert } from 'lucide-react';
import { useApp } from '../../context/AppContext';

export const ExpiringDocumentsPage: React.FC = () => {
  const { documents } = useApp();
  const expiring = documents.filter(d => d.daysToExpiry < 30);

  return (
    <div className="space-y-6 pb-12">
      <div className="glass-panel p-5 rounded-2xl border border-red-500/40 bg-red-950/20">
        <div className="flex items-center space-x-2 text-xs text-red-400 font-bold uppercase tracking-wider">
          <ClockAlert className="w-4 h-4 text-red-500 animate-pulse" />
          <span>Statutory Permit Expirations</span>
        </div>
        <h1 className="text-2xl font-black text-white mt-1">Expiring Documents & Licenses</h1>
        <p className="text-xs text-slate-300 mt-0.5">
          Proactive renewal alerts for Environmental Clearances, PESO explosive magazine licenses, and CTOs.
        </p>
      </div>

      <div className="space-y-3">
        {expiring.map(doc => (
          <div
            key={doc.id}
            className="glass-panel p-5 rounded-xl border border-red-500/40 bg-coal-900/90 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4"
          >
            <div className="space-y-1">
              <div className="flex items-center space-x-2">
                <span className="bg-red-600 text-white font-mono font-bold text-[10px] px-2 py-0.5 rounded">
                  EXPIRES IN {doc.daysToExpiry} DAYS
                </span>
                <span className="font-mono font-bold text-white text-xs">{doc.documentNo}</span>
              </div>
              <h3 className="text-sm font-extrabold text-white">{doc.title}</h3>
              <p className="text-xs text-slate-400">Authority: {doc.authority} • Mine: {doc.mineName}</p>
            </div>

            <button className="px-4 py-2 rounded-xl bg-safety-orange hover:bg-safety-orange/90 text-white font-bold text-xs shadow-lg self-end sm:self-center">
              Initiate Renewal Docket
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

contractor_dashboard = """import React from 'react';
import { HardHat } from 'lucide-react';
import { useApp } from '../../context/AppContext';

export const ContractorDashboardPage: React.FC = () => {
  const { contractors } = useApp();

  return (
    <div className="space-y-6 pb-12">
      <div className="glass-panel p-5 rounded-2xl border border-slate-800">
        <div className="flex items-center space-x-2 text-xs text-safety-orange font-bold uppercase tracking-wider">
          <HardHat className="w-4 h-4 text-safety-orange" />
          <span>Outsourced Workforce Governance</span>
        </div>
        <h1 className="text-2xl font-black text-white mt-1">Contractor Management Hub</h1>
        <p className="text-xs text-slate-400 mt-0.5">
          Contractor safety index, mandatory VTC refresher tracking, Form B register verification, and audit ranking.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {contractors.map(c => (
          <div
            key={c.id}
            className={`glass-panel p-5 rounded-xl border space-y-4 ${
              c.status === 'High Risk' ? 'border-red-500/40 bg-red-950/15' : 'border-slate-800'
            }`}
          >
            <div className="flex items-start justify-between">
              <div>
                <span className="text-[10px] font-bold bg-coal-800 text-slate-400 px-2 py-0.5 rounded font-mono">
                  {c.serviceType}
                </span>
                <h3 className="text-sm font-extrabold text-white mt-1">{c.name}</h3>
                <p className="text-[11px] text-slate-400">{c.mineName} ({c.subsidiary})</p>
              </div>

              <span className={`text-[10px] font-extrabold px-2 py-0.5 rounded uppercase ${
                c.status === 'High Risk' ? 'bg-red-500 text-white' : 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30'
              }`}>
                {c.status}
              </span>
            </div>

            <div className="grid grid-cols-3 gap-2 text-center text-xs">
              <div className="p-2 bg-coal-950 rounded-lg border border-slate-800">
                <span className="text-[9px] text-slate-400 uppercase">Compliance</span>
                <div className="font-mono font-bold text-white text-base mt-0.5">{c.complianceScore}%</div>
              </div>
              <div className="p-2 bg-coal-950 rounded-lg border border-slate-800">
                <span className="text-[9px] text-slate-400 uppercase">Risk Index</span>
                <div className={`font-mono font-bold text-base mt-0.5 ${c.riskScore > 60 ? 'text-red-400' : 'text-emerald-400'}`}>
                  {c.riskScore}/100
                </div>
              </div>
              <div className="p-2 bg-coal-950 rounded-lg border border-slate-800">
                <span className="text-[9px] text-slate-400 uppercase">Deployed</span>
                <div className="font-mono font-bold text-safety-cyan text-base mt-0.5">{c.activeWorkers}</div>
              </div>
            </div>

            <div className="p-3 bg-coal-950 rounded-lg text-xs space-y-1">
              <span className="font-bold text-safety-orange text-[10px] uppercase">AI Audit Directive:</span>
              <p className="text-slate-300 text-[11px]">{c.auditRecommendation}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

contractor_compliance = """import React from 'react';
import { UserCheck } from 'lucide-react';
import { useApp } from '../../context/AppContext';

export const ContractorCompliancePage: React.FC = () => {
  const { contractors } = useApp();

  return (
    <div className="space-y-6 pb-12">
      <div className="glass-panel p-5 rounded-2xl border border-slate-800">
        <div className="flex items-center space-x-2 text-xs text-safety-orange font-bold uppercase tracking-wider">
          <UserCheck className="w-4 h-4 text-safety-orange" />
          <span>Statutory Labour & Training Verification</span>
        </div>
        <h1 className="text-2xl font-black text-white mt-1">Contractor Compliance & Risk</h1>
        <p className="text-xs text-slate-400 mt-0.5">
          Vocational Training Centre (VTC) compliance, Form B registers, and Periodic Medical Examination (PME) records.
        </p>
      </div>

      <div className="glass-panel rounded-xl border border-slate-800 overflow-hidden shadow-xl">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="bg-coal-900 border-b border-slate-800 text-slate-400 font-extrabold uppercase tracking-wider text-[10px]">
              <tr>
                <th className="p-3.5">Contractor Name</th>
                <th className="p-3.5">Service Area</th>
                <th className="p-3.5">Deployed Workers</th>
                <th className="p-3.5">VTC Trained</th>
                <th className="p-3.5">PME Medical Fit</th>
                <th className="p-3.5">Open Violations</th>
                <th className="p-3.5">Compliance Score</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60">
              {contractors.map(c => (
                <tr key={c.id} className="hover:bg-coal-800/40">
                  <td className="p-3.5 font-bold text-white">{c.name}</td>
                  <td className="p-3.5 text-slate-300 font-mono">{c.serviceType}</td>
                  <td className="p-3.5 font-mono text-white">{c.stats.totalDeployed}</td>
                  <td className="p-3.5 font-mono text-emerald-400 font-bold">{c.stats.trainedVTC} / {c.stats.totalDeployed}</td>
                  <td className="p-3.5 font-mono text-slate-300">{c.stats.medicalFitPME}</td>
                  <td className="p-3.5 font-mono font-bold text-red-400">{c.openViolations}</td>
                  <td className="p-3.5 font-mono font-bold text-safety-orange">{c.complianceScore}%</td>
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

with open('src/pages/Documents/DocumentRepositoryPage.tsx', 'w', encoding='utf-8') as f:
    f.write(doc_repo)

with open('src/pages/Documents/OCRDigitizationPage.tsx', 'w', encoding='utf-8') as f:
    f.write(ocr_digitization)

with open('src/pages/Documents/ExpiringDocumentsPage.tsx', 'w', encoding='utf-8') as f:
    f.write(expiring_docs)

with open('src/pages/Contractors/ContractorDashboardPage.tsx', 'w', encoding='utf-8') as f:
    f.write(contractor_dashboard)

with open('src/pages/Contractors/ContractorCompliancePage.tsx', 'w', encoding='utf-8') as f:
    f.write(contractor_compliance)

print("Documents and Contractors pages written successfully!")
