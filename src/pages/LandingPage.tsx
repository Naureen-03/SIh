import React from 'react';
import {
  ShieldCheck,
  CheckCircle2,
  FileText,
  MapPin,
  Flame,
  ArrowRight,
  Sparkles,
  Award,
  ExternalLink,
  Users,
  Building2,
  ScanEye,
  Bot
} from 'lucide-react';
import { ClosedLoopVisualizer } from '../components/visualizer/ClosedLoopVisualizer';
import { Footer } from '../components/layout/Footer';

interface LandingPageProps {
  onExploreDashboard: () => void;
  onStartInspection: () => void;
  onOpenCopilot: () => void;
}

export const LandingPage: React.FC<LandingPageProps> = ({
  onExploreDashboard,
  onStartInspection,
  onOpenCopilot
}) => {
  const pillars = [
    { title: 'Statutory Compliance Tracking', desc: 'Continuous monitoring of Coal Mines Regulations 2017, MoEFCC EC clearances, and DGMS circulars.', icon: ShieldCheck },
    { title: 'Digital Field Inspection', desc: 'Mobile-first field inspection register with GPS coordinates auto-lock, voice notes, and photo uploads.', icon: ScanEye },
    { title: 'Explainable AI Risk Scoring', desc: 'Multi-vector risk index (0-100) across safety, environmental, labour, production, and contractor factors.', icon: Flame },
    { title: 'Closed-Loop Governance', desc: 'End-to-end case remediation with SLA escalation timers, officer assignment, and evidence verification.', icon: CheckCircle2 },
    { title: 'GIS Spatial Infrastructure', desc: 'Geospatial mapping of high-risk coal basins, active mining faces, and geofenced hazard zones.', icon: MapPin },
    { title: 'OCR Document Intelligence', desc: 'Automated entity extraction from scanned DGMS permits, EC orders, and Form IV/VI registers.', icon: FileText },
    { title: 'Contractor Workforce Hub', desc: 'Mandatory Vocational Training (VTC) verification, Form B registry tracking, and risk auditing.', icon: Users },
    { title: 'Digital Governance Audit Trail', desc: 'Cryptographic SHA-256 block ledger recording every inspection, inference, and manager signoff.', icon: Building2 },
  ];

  return (
    <div className="min-h-screen bg-[#F4F6F9] text-slate-900 flex flex-col justify-between">
      <div>
        {/* Top Government Strip */}
        <div className="bg-[#0B2545] text-white border-b border-[#07192F]">
          <div className="gov-tricolor-strip" />
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5 flex flex-col sm:flex-row items-center justify-between gap-3">
            <div className="flex items-center space-x-3 text-center sm:text-left">
              <div className="w-10 h-10 rounded bg-white/10 border border-white/20 flex flex-col items-center justify-center font-bold text-white text-xs shadow-xs">
                <span>GOI</span>
                <span className="text-[7px] text-amber-400 uppercase">COAL</span>
              </div>
              <div>
                <div className="text-[11px] font-extrabold uppercase tracking-wider text-amber-400">
                  Government of India &bull; Ministry of Coal &bull; Coal India Limited
                </div>
                <div className="text-base font-black tracking-tight text-white">
                  MINEGUARD AI &mdash; Smart Mining Governance & Compliance System
                </div>
              </div>
            </div>

            <div className="flex items-center space-x-2">
              <span className="bg-[#134074] text-white border border-slate-600 px-3 py-1 rounded text-xs font-mono font-bold">
                SIH Problem Statement ID 26024
              </span>
              <button
                onClick={onExploreDashboard}
                className="gov-btn-primary bg-amber-500 hover:bg-amber-600 text-[#0B2545] font-black border-none"
              >
                <span>Enter Portal</span>
                <ArrowRight className="w-3.5 h-3.5" />
              </button>
            </div>
          </div>
        </div>

        {/* Hero Banner */}
        <section className="bg-white border-b border-slate-200 py-12 px-4 sm:px-6 lg:px-8">
          <div className="max-w-5xl mx-auto text-center space-y-4">
            <div className="inline-flex items-center space-x-2 bg-slate-100 text-slate-800 border border-slate-300 px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider">
              <Award className="w-3.5 h-3.5 text-amber-600" />
              <span>Smart India Hackathon 2026 Prototype</span>
            </div>

            <h1 className="text-3xl sm:text-4xl lg:text-5xl font-black text-[#0B2545] tracking-tight leading-tight">
              Smart Governance for India&apos;s Coal Mining Ecosystem
            </h1>

            <p className="text-sm sm:text-base text-slate-600 max-w-3xl mx-auto leading-relaxed">
              An AI-assisted digital governance and statutory compliance monitoring system designed for real-time transparency, regulatory accountability, and predictive risk mitigation across Coal India Limited and subsidiary mining operations.
            </p>

            <div className="flex flex-wrap items-center justify-center gap-3 pt-2">
              <button onClick={onExploreDashboard} className="gov-btn-primary text-xs py-3 px-6 text-sm">
                <span>Access Governance Dashboard</span>
                <ArrowRight className="w-4 h-4" />
              </button>
              <button onClick={onStartInspection} className="gov-btn-secondary text-xs py-3 px-6 text-sm">
                <span>Initiate Digital Field Inspection</span>
              </button>
              <button onClick={onOpenCopilot} className="gov-btn-secondary text-xs py-3 px-6 text-sm bg-slate-50">
                <Bot className="w-4 h-4 text-[#0B2545]" />
                <span>Consult MineGuard AI Assistant</span>
              </button>
            </div>
          </div>
        </section>

        {/* Main Content Area */}
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
          {/* Closed-Loop Pipeline */}
          <ClosedLoopVisualizer activeStep={1} />

          {/* 8 Core Capability Pillars */}
          <div className="space-y-4">
            <div className="text-center sm:text-left">
              <h2 className="text-base font-extrabold text-[#0B2545] uppercase tracking-wider">
                Key Governance Pillars
              </h2>
              <p className="text-xs text-slate-600 mt-0.5">
                Integrated modules fulfilling all statutory, environmental, safety, labour, and operational mandates
              </p>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
              {pillars.map((p, idx) => {
                const Icon = p.icon;
                return (
                  <div key={idx} className="gov-card p-4 space-y-2 hover:border-[#0B2545] transition-all">
                    <div className="w-8 h-8 rounded bg-[#0B2545] text-white flex items-center justify-center shadow-xs">
                      <Icon className="w-4 h-4 text-amber-400" />
                    </div>
                    <h3 className="text-xs font-extrabold text-slate-900 leading-snug">{p.title}</h3>
                    <p className="text-[11px] text-slate-600 leading-relaxed">{p.desc}</p>
                  </div>
                );
              })}
            </div>
          </div>

          {/* Multi-Stakeholder Matrix */}
          <div className="gov-card p-6 space-y-4">
            <h3 className="text-sm font-extrabold text-[#0B2545] uppercase tracking-wider text-center">
              Role-Based Governance Matrix
            </h3>
            <div className="grid grid-cols-1 sm:grid-cols-3 lg:grid-cols-6 gap-3 text-center text-xs">
              {[
                { role: 'Ministry of Coal', desc: 'National production, compliance & strategic policy' },
                { role: 'Coal India HQ', desc: 'Subsidiary performance benchmarking & resource allocation' },
                { role: 'DGMS / Regulatory', desc: 'Statutory safety orders, circulars & inquiry notices' },
                { role: 'Mine General Manager', desc: 'Mine-level SLA governance, case closure & approvals' },
                { role: 'Field Safety Officer', desc: 'On-site digital audits, GPS hazard capture & rectification' },
                { role: 'Contractor Cell', desc: 'Workforce VTC certification & Form B labour compliance' },
              ].map((s, idx) => (
                <div key={idx} className="p-3 bg-slate-50 rounded border border-slate-200">
                  <div className="w-7 h-7 rounded-full bg-[#0B2545] text-white flex items-center justify-center mx-auto mb-1.5 font-bold text-xs font-mono">
                    0{idx + 1}
                  </div>
                  <h4 className="font-extrabold text-slate-900 text-xs">{s.role}</h4>
                  <p className="text-[10px] text-slate-600 mt-1 leading-snug">{s.desc}</p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* Official Government Footer */}
      <Footer />
    </div>
  );
};
