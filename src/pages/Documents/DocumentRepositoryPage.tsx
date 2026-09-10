import React, { useState } from 'react';
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
