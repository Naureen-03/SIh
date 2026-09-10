import os

doc_repo = """import React, { useState } from 'react';
import { FolderOpen, FileText, Download, Search } from 'lucide-react';
import { useApp } from '../../context/AppContext';

export const DocumentRepositoryPage: React.FC = () => {
  const { documents } = useApp();
  const [searchTerm, setSearchTerm] = useState('');

  const filtered = documents.filter(d => d.title.toLowerCase().includes(searchTerm.toLowerCase()) || d.documentNo.toLowerCase().includes(searchTerm.toLowerCase()));

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
            <FolderOpen className="w-4 h-4 text-[#0B2545]" />
            <span>Digital Document Vault</span>
          </div>
          <h1 className="text-2xl font-black text-slate-900 mt-1">Statutory Document Repository</h1>
          <p className="text-xs text-slate-600 mt-0.5">
            Cloud-indexed vault for Environmental Clearances, DGMS Mining Permits, and Consent to Operate licenses.
          </p>
        </div>

        <input
          type="text"
          placeholder="Search document no, authority..."
          value={searchTerm}
          onChange={e => setSearchTerm(e.target.value)}
          className="bg-slate-50 border border-slate-300 rounded px-3 py-1.5 text-xs text-slate-900 placeholder-slate-400 focus:outline-none focus:border-[#0B2545] w-64"
        />
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {filtered.map(doc => (
          <div key={doc.id} className="gov-card p-4 space-y-3">
            <div className="flex items-start justify-between">
              <div>
                <span className="text-[10px] font-bold bg-[#0B2545] text-white px-2 py-0.5 rounded font-mono">
                  {doc.type}
                </span>
                <h3 className="text-sm font-extrabold text-slate-900 mt-1">{doc.title}</h3>
                <p className="text-[11px] text-slate-500 font-mono">Doc No: {doc.documentNo}</p>
              </div>
              <span className={`text-[10px] font-bold px-2 py-0.5 rounded ${
                doc.status === 'Valid' ? 'bg-emerald-50 text-emerald-800 border border-emerald-300' : 'bg-red-50 text-red-800 border border-red-300'
              }`}>
                {doc.status}
              </span>
            </div>

            <div className="text-xs text-slate-700 space-y-1">
              <p>Authority: <strong>{doc.authority}</strong></p>
              <p>Validity: <strong>{doc.issueDate} to {doc.expiryDate}</strong> ({doc.daysToExpiry} days remaining)</p>
            </div>

            <div className="flex justify-end space-x-2 pt-2 border-t border-slate-200">
              <button className="gov-btn-secondary text-xs py-1 px-3">
                Preview Clauses
              </button>
              <button className="gov-btn-primary text-xs py-1 px-3">
                <Download className="w-3.5 h-3.5" />
                <span>Download</span>
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
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
          <ScanEye className="w-4 h-4 text-[#0B2545]" />
          <span>AI OCR & Document Intelligence</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">OCR Document Digitization</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Extract statutory clauses, validity dates, compliance conditions, and identify missing renewal attachments from scanned PDF and image records.
        </p>
      </div>

      <div className="gov-card p-8 border-2 border-dashed border-slate-300 hover:border-[#0B2545] text-center space-y-4 cursor-pointer transition-all">
        <div className="w-14 h-14 rounded-full bg-[#0B2545]/10 text-[#0B2545] flex items-center justify-center mx-auto">
          <Upload className="w-7 h-7" />
        </div>
        <div>
          <h3 className="text-sm font-extrabold text-slate-900">Upload Statutory Document (PDF, Scanned Image)</h3>
          <p className="text-xs text-slate-500 mt-0.5">Supported: EC Clearances, DGMS Circulars, CTOs, Form IV / Form VI</p>
        </div>
        <div className="inline-block bg-slate-100 px-4 py-2 rounded text-xs font-mono text-slate-800 border border-slate-300">
          Selected Docket: {selectedFile}
        </div>
        <div>
          <button
            onClick={handleScan}
            disabled={isScanning}
            className="gov-btn-primary py-2.5 px-6"
          >
            <Sparkles className="w-4 h-4 text-amber-400" />
            <span>{isScanning ? 'Processing OCR Engine...' : 'Run AI OCR Extraction'}</span>
          </button>
        </div>
      </div>

      {ocrResult && (
        <div className="gov-card p-6 border-l-4 border-l-emerald-700 space-y-4">
          <div className="flex items-center justify-between pb-3 border-b border-slate-200">
            <div>
              <span className="text-[10px] font-extrabold uppercase tracking-wider text-emerald-800">
                OCR Processing Completed
              </span>
              <h3 className="text-base font-black text-slate-900">{ocrResult.documentType}</h3>
            </div>
            <div className="text-right font-mono text-xs text-emerald-800 font-bold bg-emerald-50 px-2.5 py-1 rounded border border-emerald-300">
              Confidence: {ocrResult.confidence}%
            </div>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
            <div className="p-3 bg-slate-50 rounded border border-slate-200">
              <span className="text-[10px] text-slate-500 uppercase font-bold">Document Number</span>
              <p className="font-mono font-bold text-slate-900 mt-0.5">{ocrResult.documentNo}</p>
            </div>
            <div className="p-3 bg-slate-50 rounded border border-slate-200">
              <span className="text-[10px] text-slate-500 uppercase font-bold">Issuing Authority</span>
              <p className="font-bold text-slate-900 mt-0.5">{ocrResult.authority}</p>
            </div>
            <div className="p-3 bg-slate-50 rounded border border-slate-200">
              <span className="text-[10px] text-slate-500 uppercase font-bold">Validity Period</span>
              <p className="font-bold text-amber-900 mt-0.5 font-mono">{ocrResult.expiryDate} ({ocrResult.daysToExpiry} days left)</p>
            </div>
          </div>

          <div className="p-3.5 bg-slate-50 rounded border border-slate-200 space-y-1.5 text-xs">
            <span className="font-bold text-slate-900 uppercase text-[10px]">Extracted Statutory Clauses:</span>
            <ul className="space-y-1 text-slate-700">
              {ocrResult.extractedClauses.map((c, i) => (
                <li key={i} className="flex items-start space-x-2">
                  <CheckCircle2 className="w-3.5 h-3.5 text-emerald-700 shrink-0 mt-0.5" />
                  <span>{c}</span>
                </li>
              ))}
            </ul>
          </div>

          {ocrResult.missingFields.length > 0 && (
            <div className="p-3 bg-red-50 rounded border border-red-300 text-xs flex items-start space-x-2">
              <AlertTriangle className="w-4 h-4 text-red-700 shrink-0 mt-0.5" />
              <div>
                <span className="font-bold text-red-900 uppercase text-[10px]">Missing Mandatory Enclosure Detected:</span>
                <p className="text-slate-800 mt-0.5">{ocrResult.missingFields.join(', ')}</p>
              </div>
            </div>
          )}

          <div className="p-3 bg-amber-50 rounded border border-amber-300 text-xs">
            <span className="font-bold text-amber-900 uppercase text-[10px]">AI Action Recommendation:</span>
            <p className="text-slate-800 font-semibold mt-0.5">{ocrResult.aiActionRecommendation}</p>
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
      <div className="gov-card p-5 border-l-4 border-l-red-700">
        <div className="flex items-center space-x-2 text-xs text-red-700 font-extrabold uppercase tracking-wider">
          <ClockAlert className="w-4 h-4 text-red-700" />
          <span>Statutory Permit Expirations</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Expiring Documents & Licenses</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Proactive renewal alerts for Environmental Clearances, PESO explosive magazine licenses, and Consent to Operate (CTO).
        </p>
      </div>

      <div className="space-y-3">
        {expiring.map(doc => (
          <div
            key={doc.id}
            className="gov-card p-4 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 border-l-4 border-l-red-700"
          >
            <div className="space-y-1">
              <div className="flex items-center space-x-2">
                <span className="bg-red-700 text-white font-mono font-bold text-[10px] px-2 py-0.5 rounded">
                  EXPIRES IN {doc.daysToExpiry} DAYS
                </span>
                <span className="font-mono font-bold text-slate-900 text-xs">{doc.documentNo}</span>
              </div>
              <h3 className="text-sm font-extrabold text-slate-900">{doc.title}</h3>
              <p className="text-xs text-slate-600">Authority: <strong>{doc.authority}</strong> &bull; Mine: <strong>{doc.mineName}</strong></p>
            </div>

            <button className="gov-btn-primary text-xs py-2 px-4 self-end sm:self-center">
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
import { HardHat, UserCheck, ShieldCheck, AlertTriangle } from 'lucide-react';
import { useApp } from '../../context/AppContext';

export const ContractorDashboardPage: React.FC = () => {
  const { contractors } = useApp();

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
          <HardHat className="w-4 h-4 text-[#0B2545]" />
          <span>Outsourced Workforce Governance</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Contractor Management Hub</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Contractor safety index, mandatory VTC refresher tracking, Form B register verification, and statutory audit ranking.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {contractors.map(c => (
          <div
            key={c.id}
            className={`gov-card p-4 space-y-3 ${
              c.status === 'High Risk' ? 'border-l-4 border-l-red-700 bg-red-50/20' : 'border-slate-200'
            }`}
          >
            <div className="flex items-start justify-between">
              <div>
                <span className="text-[10px] font-bold bg-slate-100 text-slate-700 px-2 py-0.5 rounded font-mono">
                  {c.serviceType}
                </span>
                <h3 className="text-sm font-extrabold text-slate-900 mt-1">{c.name}</h3>
                <p className="text-[11px] text-slate-500">{c.mineName} ({c.subsidiary})</p>
              </div>

              <span className={`text-[10px] font-extrabold px-2 py-0.5 rounded uppercase ${
                c.status === 'High Risk' ? 'bg-red-700 text-white' : 'bg-emerald-50 text-emerald-800 border border-emerald-300'
              }`}>
                {c.status}
              </span>
            </div>

            <div className="grid grid-cols-3 gap-2 text-center text-xs">
              <div className="p-2 bg-slate-50 rounded border border-slate-200">
                <span className="text-[9px] text-slate-500 uppercase">Compliance</span>
                <div className="font-mono font-bold text-slate-900 text-base mt-0.5">{c.complianceScore}%</div>
              </div>
              <div className="p-2 bg-slate-50 rounded border border-slate-200">
                <span className="text-[9px] text-slate-500 uppercase">Risk Index</span>
                <div className={`font-mono font-bold text-base mt-0.5 ${c.riskScore > 60 ? 'text-red-700' : 'text-emerald-800'}`}>
                  {c.riskScore}/100
                </div>
              </div>
              <div className="p-2 bg-slate-50 rounded border border-slate-200">
                <span className="text-[9px] text-slate-500 uppercase">Deployed</span>
                <div className="font-mono font-bold text-[#0B2545] text-base mt-0.5">{c.activeWorkers}</div>
              </div>
            </div>

            <div className="p-2.5 bg-slate-50 rounded border border-slate-200 text-xs space-y-0.5">
              <span className="font-bold text-[#0B2545] text-[10px] uppercase">AI Audit Directive:</span>
              <p className="text-slate-700 text-[11px]">{c.auditRecommendation}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

contractor_comp = """import React from 'react';
import { UserCheck } from 'lucide-react';
import { useApp } from '../../context/AppContext';

export const ContractorCompliancePage: React.FC = () => {
  const { contractors } = useApp();

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
          <UserCheck className="w-4 h-4 text-[#0B2545]" />
          <span>Statutory Labour & Training Verification</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Contractor Compliance & Risk</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Vocational Training Centre (VTC) compliance, Form B registers, and Periodic Medical Examination (PME) records.
        </p>
      </div>

      <div className="gov-card overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="bg-slate-50 border-b border-slate-200 text-slate-700 font-bold uppercase tracking-wider text-[10px]">
              <tr>
                <th className="p-3">Contractor Name</th>
                <th className="p-3">Service Area</th>
                <th className="p-3">Deployed Workers</th>
                <th className="p-3">VTC Trained</th>
                <th className="p-3">PME Medical Fit</th>
                <th className="p-3">Open Violations</th>
                <th className="p-3">Compliance Score</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-200">
              {contractors.map(c => (
                <tr key={c.id} className="hover:bg-slate-50/80 transition-colors">
                  <td className="p-3 font-bold text-slate-900">{c.name}</td>
                  <td className="p-3 text-slate-700 font-mono">{c.serviceType}</td>
                  <td className="p-3 font-mono text-slate-900">{c.stats.totalDeployed}</td>
                  <td className="p-3 font-mono text-emerald-800 font-bold">{c.stats.trainedVTC} / {c.stats.totalDeployed}</td>
                  <td className="p-3 font-mono text-slate-700">{c.stats.medicalFitPME}</td>
                  <td className="p-3 font-mono font-bold text-red-700">{c.openViolations}</td>
                  <td className="p-3 font-mono font-bold text-slate-900">{c.complianceScore}%</td>
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
    f.write(contractor_comp)

print("Part 4a: Documents and Contractors written successfully!")
