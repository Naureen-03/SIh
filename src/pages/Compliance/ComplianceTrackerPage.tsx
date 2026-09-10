import React, { useState } from 'react';
import {
  ShieldCheck,
  Search,
  Filter,
  Download,
  AlertTriangle,
  FileCheck2,
  Calendar,
  Building2
} from 'lucide-react';
import { useApp } from '../../context/AppContext';
import { INITIAL_STATUTORY_RULES } from '../../data/mockData';

export const ComplianceTrackerPage: React.FC = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCategory, setSelectedCategory] = useState<string>('All');
  const [selectedStatus, setSelectedStatus] = useState<string>('All');

  const filteredRules = INITIAL_STATUTORY_RULES.filter(rule => {
    if (selectedCategory !== 'All' && rule.category !== selectedCategory) return false;
    if (selectedStatus !== 'All' && rule.status !== selectedStatus) return false;
    if (searchTerm && !rule.title.toLowerCase().includes(searchTerm.toLowerCase()) && !rule.ruleCode.toLowerCase().includes(searchTerm.toLowerCase())) return false;
    return true;
  });

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
            <ShieldCheck className="w-4 h-4 text-[#0B2545]" />
            <span>National Statutory Compliance Matrix</span>
          </div>
          <h1 className="text-2xl font-black text-slate-900 mt-1">Statutory Compliance Register</h1>
          <p className="text-xs text-slate-600 mt-0.5">
            Searchable legal compliance register covering Coal Mines Regulations 2017, Mines Act 1952, and MoEFCC clearance conditions.
          </p>
        </div>

        <button className="gov-btn-primary">
          <Download className="w-3.5 h-3.5" />
          <span>Export Compliance Audit PDF</span>
        </button>
      </div>

      {/* Filter Bar */}
      <div className="gov-card p-3 flex flex-wrap items-center justify-between gap-3 text-xs">
        <div className="flex flex-wrap items-center gap-2">
          <input
            type="text"
            placeholder="Search regulation, act code, keywords..."
            value={searchTerm}
            onChange={e => setSearchTerm(e.target.value)}
            className="bg-slate-50 border border-slate-300 rounded px-3 py-1.5 text-xs text-slate-900 placeholder-slate-400 focus:outline-none focus:border-[#0B2545] w-64"
          />

          <select
            value={selectedCategory}
            onChange={e => setSelectedCategory(e.target.value)}
            className="bg-slate-50 border border-slate-300 rounded px-3 py-1.5 text-xs text-slate-900 font-bold focus:outline-none focus:border-[#0B2545]"
          >
            <option value="All">All Categories</option>
            <option value="Safety">Safety Regulations</option>
            <option value="Environment">Environmental Clearances</option>
            <option value="Labour">Labour & Welfare</option>
            <option value="Operational">Operational Clearances</option>
          </select>
        </div>

        <div className="text-xs font-mono text-slate-600">
          Showing <strong>{filteredRules.length}</strong> of {INITIAL_STATUTORY_RULES.length} statutory mandates
        </div>
      </div>

      {/* Compliance Register Table */}
      <div className="gov-card overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="bg-slate-50 border-b border-slate-200 text-slate-700 font-bold uppercase tracking-wider text-[10px]">
              <tr>
                <th className="p-3">Statutory Rule Code</th>
                <th className="p-3">Regulation Title</th>
                <th className="p-3">Governing Act</th>
                <th className="p-3">Enforcing Authority</th>
                <th className="p-3">Applicable Scope</th>
                <th className="p-3">Frequency</th>
                <th className="p-3">Compliance Status</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-200">
              {filteredRules.map(rule => (
                <tr key={rule.id} className="hover:bg-slate-50/80 transition-colors">
                  <td className="p-3 font-mono font-bold text-slate-900">{rule.ruleCode}</td>
                  <td className="p-3 font-bold text-slate-900">
                    <div>{rule.title}</div>
                    <div className="text-[10px] text-slate-500 font-normal">{rule.description}</div>
                  </td>
                  <td className="p-3 text-slate-700">{rule.act}</td>
                  <td className="p-3 font-bold text-[#0B2545]">{rule.authority}</td>
                  <td className="p-3 text-slate-600">{rule.applicableTo}</td>
                  <td className="p-3 font-mono text-slate-600">{rule.frequency}</td>
                  <td className="p-3">
                    <span className={`text-[10px] font-extrabold px-2 py-0.5 rounded uppercase ${
                      rule.status === 'Compliant'
                        ? 'bg-emerald-50 text-emerald-800 border border-emerald-300'
                        : rule.status === 'Overdue'
                        ? 'bg-red-50 text-red-800 border border-red-300'
                        : 'bg-amber-50 text-amber-800 border border-amber-300'
                    }`}>
                      {rule.status}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
