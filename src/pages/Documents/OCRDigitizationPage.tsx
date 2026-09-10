import React, { useState } from 'react';
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
