import os

critical_issues = """import React from 'react';
import { Flame, ClockAlert, ArrowUpRight, AlertTriangle } from 'lucide-react';
import { useApp } from '../../context/AppContext';

interface Props {
  setActiveTab: (tab: string) => void;
}

export const CriticalIssuesPage: React.FC<Props> = ({ setActiveTab }) => {
  const { issues } = useApp();
  const critical = issues.filter(i => i.severity === 'Critical');

  return (
    <div className="space-y-6 pb-12">
      <div className="glass-panel p-5 rounded-2xl border border-red-500/40 bg-red-950/20">
        <div className="flex items-center space-x-2 text-xs text-red-400 font-bold uppercase tracking-wider">
          <Flame className="w-4 h-4 text-red-500 animate-pulse" />
          <span>High Severity Emergency Matrix</span>
        </div>
        <h1 className="text-2xl font-black text-white mt-1">Critical Issues & Escalated SLAs</h1>
        <p className="text-xs text-slate-300 mt-0.5">
          Issues posing imminent danger to worker safety, DGMS statutory stoppage risk, or massive environmental breaches.
        </p>
      </div>

      <div className="space-y-3">
        {critical.map(issue => (
          <div
            key={issue.id}
            className="glass-panel p-5 rounded-xl border border-red-500/40 bg-coal-900/90 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 hover:border-red-500 transition-all"
          >
            <div className="space-y-1.5">
              <div className="flex items-center space-x-2">
                <span className="bg-red-600 text-white font-black text-[10px] px-2 py-0.5 rounded uppercase font-mono">
                  CRITICAL • RISK {issue.riskScore}/100
                </span>
                <span className="font-mono font-bold text-white text-xs">{issue.issueCode}</span>
                <span className="text-[10px] text-slate-400">• {issue.mineName}</span>
              </div>
              <h3 className="text-sm font-extrabold text-white">{issue.title}</h3>
              <p className="text-xs text-slate-300">{issue.description}</p>
              <div className="text-[11px] text-slate-400 font-mono">
                Assigned: <strong className="text-white">{issue.assignedOfficer}</strong> • Location: <strong>{issue.location}</strong>
              </div>
            </div>

            <div className="flex flex-col items-end space-y-2 shrink-0 self-end sm:self-center">
              <span className="text-xs font-mono font-black text-red-400 bg-red-950 px-3 py-1 rounded border border-red-800 animate-pulse">
                {issue.correctiveAction?.slaHoursRemaining ? `${issue.correctiveAction.slaHoursRemaining} Hours SLA Remaining` : 'SLA: 24 Hours'}
              </span>
              <button
                onClick={() => setActiveTab('evidence-verification')}
                className="px-3.5 py-1.5 rounded-lg bg-safety-orange hover:bg-safety-orange/90 text-white text-xs font-bold transition-all"
              >
                Open Verification
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

corrective_actions = """import React from 'react';
import { Wrench, UserCheck, Clock, CheckCircle2, ArrowRight } from 'lucide-react';
import { useApp } from '../../context/AppContext';

interface Props {
  setActiveTab: (tab: string) => void;
}

export const CorrectiveActionsPage: React.FC<Props> = ({ setActiveTab }) => {
  const { issues, assignIssue } = useApp();

  return (
    <div className="space-y-6 pb-12">
      <div className="glass-panel p-5 rounded-2xl border border-slate-800">
        <div className="flex items-center space-x-2 text-xs text-safety-orange font-bold uppercase tracking-wider">
          <Wrench className="w-4 h-4 text-safety-orange" />
          <span>Automated Closed-Loop Mitigation</span>
        </div>
        <h1 className="text-2xl font-black text-white mt-1">Corrective Actions Hub</h1>
        <p className="text-xs text-slate-400 mt-0.5">
          AI Smart Assignment recommendations based on departmental competency, mine sector, and active task load.
        </p>
      </div>

      <div className="space-y-4">
        {issues.map(issue => {
          const ca = issue.correctiveAction;
          if (!ca) return null;
          return (
            <div key={issue.id} className="glass-panel p-5 rounded-xl border border-slate-800 space-y-3">
              <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between pb-3 border-b border-slate-800 gap-2">
                <div>
                  <span className="font-mono text-xs font-bold text-safety-orange">{ca.id.toUpperCase()}</span>
                  <h3 className="text-sm font-extrabold text-white mt-0.5">{ca.title}</h3>
                </div>
                <span className="text-xs font-mono font-bold text-amber-400 bg-coal-950 px-2.5 py-1 rounded border border-slate-700">
                  {ca.escalationStageName}
                </span>
              </div>

              <p className="text-xs text-slate-300">{ca.actionPlan}</p>

              {/* Smart Assignment Card */}
              <div className="p-3.5 rounded-xl bg-coal-950 border border-slate-800 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 text-xs">
                <div className="flex items-center space-x-3">
                  <div className="w-8 h-8 rounded-full bg-safety-orange/20 text-safety-orange flex items-center justify-center font-bold">
                    <UserCheck className="w-4 h-4" />
                  </div>
                  <div>
                    <p className="font-bold text-white">Assigned Officer: {ca.assignedOfficer}</p>
                    <p className="text-[11px] text-slate-400">{ca.department} • SLA: {ca.slaHoursTotal}h</p>
                  </div>
                </div>

                <div className="flex space-x-2 self-end sm:self-center">
                  <button
                    onClick={() => setActiveTab('evidence-verification')}
                    className="px-3.5 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs flex items-center space-x-1"
                  >
                    <span>Verify Evidence</span>
                    <ArrowRight className="w-3.5 h-3.5" />
                  </button>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
"""

evidence_page = """import React from 'react';
import { EvidenceComparison } from '../../components/visualizer/EvidenceComparison';
import { CheckCircle2, Sparkles } from 'lucide-react';

interface Props {
  setActiveTab: (tab: string) => void;
}

export const EvidenceVerificationPage: React.FC<Props> = ({ setActiveTab }) => {
  return (
    <div className="space-y-6 pb-12 max-w-5xl mx-auto">
      <div className="glass-panel p-5 rounded-2xl border border-slate-800">
        <div className="flex items-center space-x-2 text-xs text-emerald-400 font-bold uppercase tracking-wider">
          <Sparkles className="w-4 h-4 text-emerald-400" />
          <span>Core USP Feature</span>
        </div>
        <h1 className="text-2xl font-black text-white mt-1">AI Evidence Verification Workstation</h1>
        <p className="text-xs text-slate-400 mt-0.5">
          Dual-phase neural computer vision compares pre-inspection hazard raster against post-rectification evidence.
        </p>
      </div>

      <EvidenceComparison
        issueId="issue-2041"
        onSuccess={() => {
          setTimeout(() => setActiveTab('dashboard'), 1000);
        }}
      />
    </div>
  );
};
"""

ai_risk_analytics = """import React from 'react';
import { BrainCircuit, ShieldAlert, TrendingUp } from 'lucide-react';
import { useApp } from '../../context/AppContext';
import { RiskScoreCard } from '../../components/visualizer/RiskScoreCard';

export const AIRiskAnalyticsPage: React.FC = () => {
  const { mines, activeMineId } = useApp();
  const activeMine = mines.find(m => m.id === activeMineId) || mines[0];

  return (
    <div className="space-y-6 pb-12">
      <div className="glass-panel p-5 rounded-2xl border border-slate-800">
        <div className="flex items-center space-x-2 text-xs text-safety-orange font-bold uppercase tracking-wider">
          <BrainCircuit className="w-4 h-4 text-safety-orange" />
          <span>Explainable AI Risk Engine</span>
        </div>
        <h1 className="text-2xl font-black text-white mt-1">AI Risk Analytics</h1>
        <p className="text-xs text-slate-400 mt-0.5">
          Multi-vector neural scoring breaking down safety, environmental, labour, production, and contractor risks.
        </p>
      </div>

      <RiskScoreCard mine={activeMine} />
    </div>
  );
};
"""

ai_predictions = """import React from 'react';
import { TrendingUp, AlertTriangle, ShieldCheck, Sparkles, ArrowRight } from 'lucide-react';
import { useApp } from '../../context/AppContext';

interface Props {
  setActiveTab: (tab: string) => void;
}

export const AIPredictionsPage: React.FC<Props> = ({ setActiveTab }) => {
  const predictions = [
    {
      mine: 'Moonidih Underground Mine (BCCL)',
      probability: 78,
      vector: 'Safety & Methane Non-Compliance',
      timeframe: 'Next 14 Days',
      reason: '3 recurring ventilation velocity drops, 2 overdue auxiliary fan impellers, high gas make seam.',
      recommendation: 'Schedule DGMS special ventilation audit and deploy booster regulator unit.'
    },
    {
      mine: 'Rajmahal Open Cast Project (ECL)',
      probability: 64,
      vector: 'Geotechnical Slope Displacement',
      timeframe: 'Next 7 Days',
      reason: 'High monsoon pore water saturation (88%) on North Highwall slope.',
      recommendation: 'Deploy geodetic prism radar and regrade bench to 26 degrees.'
    },
    {
      mine: 'Gevra Mega Open Cast Mine (SECL)',
      probability: 52,
      vector: 'Ambient Dust Exceedance',
      timeframe: 'Next 10 Days',
      reason: 'Dry wind gusts forecast with 2 water bowsers on maintenance.',
      recommendation: 'Pre-position 4 mobile high-pressure mist foggers on haul road 3.'
    }
  ];

  return (
    <div className="space-y-6 pb-12">
      <div className="glass-panel p-5 rounded-2xl border border-slate-800">
        <div className="flex items-center space-x-2 text-xs text-purple-400 font-bold uppercase tracking-wider">
          <TrendingUp className="w-4 h-4 text-purple-400" />
          <span>Predictive Decision Support</span>
        </div>
        <h1 className="text-2xl font-black text-white mt-1">AI Risk Predictions</h1>
        <p className="text-xs text-slate-400 mt-0.5">
          14-day early warning failure probabilities trained on historical violations and telemetry anomalies.
        </p>
      </div>

      <div className="space-y-4">
        {predictions.map((p, idx) => (
          <div key={idx} className="glass-panel p-5 rounded-xl border border-slate-800 space-y-3">
            <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between pb-3 border-b border-slate-800 gap-2">
              <div>
                <h3 className="text-sm font-extrabold text-white">{p.mine}</h3>
                <span className="text-xs text-purple-400 font-semibold">{p.vector} • {p.timeframe}</span>
              </div>
              <div className="flex items-center space-x-2">
                <span className="text-xs text-slate-400">Failure Probability:</span>
                <span className="text-lg font-black text-red-400 font-mono">{p.probability}%</span>
              </div>
            </div>

            <div className="p-3 bg-coal-950 rounded-lg text-xs space-y-1">
              <p className="text-slate-300"><strong>Neural RCA:</strong> {p.reason}</p>
              <p className="text-safety-orange font-semibold"><strong>AI Recommendation:</strong> {p.recommendation}</p>
            </div>

            <div className="flex justify-end pt-1">
              <button
                onClick={() => setActiveTab('new-inspection')}
                className="text-xs font-bold text-safety-orange hover:underline flex items-center space-x-1"
              >
                <span>Schedule Targeted Inspection</span>
                <ArrowRight className="w-3.5 h-3.5" />
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

ai_copilot = """import React, { useState } from 'react';
import { Bot, Send, Sparkles, User, ShieldCheck, ArrowRight, Globe } from 'lucide-react';
import { useApp } from '../../context/AppContext';
import { useLanguage } from '../../context/LanguageContext';
import { processCopilotQuery } from '../../services/copilotService';
import { CopilotMessage } from '../../types';

interface Props {
  setActiveTab: (tab: string) => void;
}

export const AICopilotPage: React.FC<Props> = ({ setActiveTab }) => {
  const { mines, issues, rules } = useApp();
  const { language } = useLanguage();

  const [inputQuery, setInputQuery] = useState('');
  const [messages, setMessages] = useState<CopilotMessage[]>([
    {
      id: 'init-1',
      sender: 'assistant',
      timestamp: '09:00',
      language: 'en',
      content: 'Welcome to **MineGuard AI Copilot**. I am your real-time statutory governance and compliance assistant across Coal India Limited. How can I assist your operational decisions today?',
      kpis: [
        { label: 'Total Mines Monitored', value: '18' },
        { label: 'Overall Compliance', value: '87%' },
        { label: 'Active Critical Actions', value: '8', alert: true }
      ],
      recommendedActions: [
        { label: 'Show High-Risk Mines', actionKey: 'SHOW_HIGH_RISK' },
        { label: 'What statutory deadlines are overdue?', actionKey: 'SHOW_OVERDUE' },
        { label: 'Generate Compliance Executive Summary', actionKey: 'GEN_REPORT' }
      ]
    }
  ]);

  const promptChips = [
    'Which mines require immediate attention?',
    'What compliance requirements are overdue?',
    'Which contractor has the most violations?',
    'What corrective actions are pending for Gevra Mine?',
    'उच्च जोखिम वाली खदानें दिखाएं (Hindi)'
  ];

  const handleSend = (textToSend?: string) => {
    const q = textToSend || inputQuery;
    if (!q.trim()) return;

    const userMsg: CopilotMessage = {
      id: 'usr-' + Date.now(),
      sender: 'user',
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      content: q
    };

    setMessages(prev => [...prev, userMsg]);
    setInputQuery('');

    setTimeout(() => {
      const isHindi = q.includes('खदान') || q.includes('Hindi') || q.includes('नमस्ते') || language === 'hi';
      const botResponse = processCopilotQuery(q, mines, issues, rules, isHindi ? 'hi' : 'en');
      setMessages(prev => [...prev, botResponse]);
    }, 600);
  };

  return (
    <div className="max-w-4xl mx-auto space-y-6 pb-12">
      <div className="glass-panel p-5 rounded-2xl border border-slate-800 flex items-center justify-between">
        <div className="flex items-center space-x-3">
          <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-safety-orange to-amber-600 flex items-center justify-center text-white shadow-lg shadow-safety-orange/20">
            <Bot className="w-6 h-6" />
          </div>
          <div>
            <div className="flex items-center space-x-2">
              <h1 className="text-xl font-black text-white">MineGuard Copilot</h1>
              <span className="text-[10px] bg-safety-cyan/20 text-safety-cyan font-bold px-2 py-0.5 rounded font-mono">
                Multilingual AI
              </span>
            </div>
            <p className="text-xs text-slate-400">Natural language governance intelligence supporting English & Hindi</p>
          </div>
        </div>
      </div>

      {/* Suggested Prompt Chips */}
      <div className="flex flex-wrap gap-2">
        {promptChips.map((chip, idx) => (
          <button
            key={idx}
            onClick={() => handleSend(chip)}
            className="px-3 py-1.5 rounded-lg bg-coal-800 hover:bg-coal-750 text-slate-300 text-xs border border-slate-700 transition-all font-medium hover:border-safety-orange/40"
          >
            {chip}
          </button>
        ))}
      </div>

      {/* Chat Stream */}
      <div className="glass-panel p-5 rounded-2xl border border-slate-800 min-h-[420px] max-h-[560px] overflow-y-auto space-y-4 shadow-xl">
        {messages.map(msg => (
          <div
            key={msg.id}
            className={`flex items-start space-y-1 ${msg.sender === 'user' ? 'justify-end' : 'justify-start'}`}
          >
            <div
              className={`max-w-2xl p-4 rounded-2xl text-xs leading-relaxed ${
                msg.sender === 'user'
                  ? 'bg-safety-orange text-white rounded-tr-none font-medium'
                  : 'bg-coal-900/90 text-slate-200 border border-slate-800 rounded-tl-none space-y-3'
              }`}
            >
              <p className="whitespace-pre-line">{msg.content}</p>

              {/* KPI Cards inside AI response */}
              {msg.kpis && (
                <div className="grid grid-cols-2 sm:grid-cols-3 gap-2 pt-2">
                  {msg.kpis.map(k => (
                    <div key={k.label} className="p-2 bg-coal-950 rounded-lg border border-slate-800 text-center">
                      <span className="text-[9px] text-slate-400 font-bold uppercase">{k.label}</span>
                      <div className={`text-base font-black font-mono mt-0.5 ${k.alert ? 'text-red-400' : 'text-white'}`}>
                        {k.value}
                      </div>
                    </div>
                  ))}
                </div>
              )}

              {/* Table Data inside AI response */}
              {msg.tableData && (
                <div className="overflow-x-auto pt-2">
                  <table className="w-full text-left text-[11px]">
                    <thead className="bg-coal-950 text-slate-400 uppercase font-extrabold text-[9px]">
                      <tr>
                        {msg.tableData.headers.map((h, i) => (
                          <th key={i} className="p-2">{h}</th>
                        ))}
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-slate-800">
                      {msg.tableData.rows.map((row, i) => (
                        <tr key={i} className="hover:bg-coal-800/50">
                          {row.map((cell, j) => (
                            <td key={j} className="p-2 font-mono">{cell}</td>
                          ))}
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              )}

              {/* Action Buttons */}
              {msg.recommendedActions && (
                <div className="flex flex-wrap gap-2 pt-2 border-t border-slate-800">
                  {msg.recommendedActions.map((act, i) => (
                    <button
                      key={i}
                      onClick={() => {
                        if (act.actionKey === 'NAVIGATE_GIS') setActiveTab('gis-map');
                        else if (act.actionKey === 'START_INSPECTION') setActiveTab('new-inspection');
                        else if (act.actionKey === 'NAVIGATE_DASHBOARD') setActiveTab('dashboard');
                        else if (act.actionKey === 'NAVIGATE_COMPLIANCE') setActiveTab('compliance-tracker');
                        else handleSend(act.label);
                      }}
                      className="px-3 py-1 rounded-lg bg-coal-800 hover:bg-coal-750 text-safety-cyan text-[11px] font-bold border border-safety-cyan/30 flex items-center space-x-1 transition-all"
                    >
                      <span>{act.label}</span>
                      <ArrowRight className="w-3 h-3" />
                    </button>
                  ))}
                </div>
              )}
            </div>
          </div>
        ))}
      </div>

      {/* Query Input Bar */}
      <form
        onSubmit={e => { e.preventDefault(); handleSend(); }}
        className="flex items-center space-x-2"
      >
        <input
          type="text"
          value={inputQuery}
          onChange={e => setInputQuery(e.target.value)}
          placeholder="Ask MineGuard Copilot in English or Hindi (e.g. Show high-risk mines)..."
          className="flex-1 bg-coal-900 border border-slate-700 rounded-xl px-4 py-3 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-safety-orange shadow-lg"
        />
        <button
          type="submit"
          className="px-5 py-3 rounded-xl bg-gradient-to-r from-safety-orange to-amber-500 hover:from-safety-orange/90 text-white font-bold text-xs shadow-lg shadow-safety-orange/20 transition-all flex items-center space-x-1.5"
        >
          <span>Send</span>
          <Send className="w-3.5 h-3.5" />
        </button>
      </form>
    </div>
  );
};
"""

recurring_violations = """import React from 'react';
import { RefreshCw, Flame, AlertTriangle, ArrowRight } from 'lucide-react';

interface Props {
  setActiveTab: (tab: string) => void;
}

export const RecurringViolationsPage: React.FC<Props> = ({ setActiveTab }) => {
  const recurring = [
    {
      violation: 'Missing Conveyor Mechanical Guarding (CMR Reg 104)',
      occurrences: 7,
      location: 'Gevra Mine — Zone 4 Trunk Line',
      period: 'Last 60 Days',
      aiConclusion: 'Repeated conveyor guarding lapses indicate systemic vibration fastener degradation and contractor maintenance shortcutting.',
      action: 'Standardize anti-vibration lock fasteners across all 14 conveyor transfer points.'
    },
    {
      violation: 'Contractor Dump Truck Speed Limit Breaches (>30 km/h)',
      occurrences: 14,
      location: 'Kusmunda Mine — Sector 2 Haul Ramp',
      period: 'Last 30 Days',
      aiConclusion: 'Proximity telematics indicate drivers bypassing governor limiters on downhill haul segment.',
      action: 'Install automated radar speed gates and penalize carrier agency.'
    }
  ];

  return (
    <div className="space-y-6 pb-12">
      <div className="glass-panel p-5 rounded-2xl border border-slate-800">
        <div className="flex items-center space-x-2 text-xs text-amber-500 font-bold uppercase tracking-wider">
          <RefreshCw className="w-4 h-4 text-amber-500 animate-spin" />
          <span>Systemic Pattern Intelligence</span>
        </div>
        <h1 className="text-2xl font-black text-white mt-1">Recurring Violations Intelligence</h1>
        <p className="text-xs text-slate-400 mt-0.5">
          AI detects repeated procedural lapses to prevent catastrophic systemic safety failures
        </p>
      </div>

      <div className="space-y-4">
        {recurring.map((item, idx) => (
          <div key={idx} className="glass-panel p-5 rounded-xl border border-amber-500/40 bg-coal-900/90 space-y-3">
            <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between pb-3 border-b border-slate-800 gap-2">
              <div>
                <span className="text-[10px] font-extrabold px-2 py-0.5 rounded bg-amber-500 text-black uppercase font-mono">
                  {item.occurrences} RECURRENCES DETECTED
                </span>
                <h3 className="text-sm font-extrabold text-white mt-1">{item.violation}</h3>
              </div>
              <span className="text-xs text-slate-400 font-mono">{item.location}</span>
            </div>

            <p className="text-xs text-slate-300"><strong>AI Conclusion:</strong> {item.aiConclusion}</p>
            <p className="text-xs text-safety-orange font-semibold"><strong>Systemic Remediation:</strong> {item.action}</p>

            <div className="flex justify-end pt-1">
              <button
                onClick={() => setActiveTab('evidence-verification')}
                className="text-xs font-bold text-safety-orange hover:underline flex items-center space-x-1"
              >
                <span>Review Active Case</span>
                <ArrowRight className="w-3.5 h-3.5" />
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

cross_mine = """import React, { useState } from 'react';
import { Share2, Sparkles, CheckCircle2, ArrowRight } from 'lucide-react';

export const CrossMineLearningPage: React.FC = () => {
  const [recommendedMines, setRecommendedMines] = useState<string[]>([]);

  const handleApply = (id: string) => {
    setRecommendedMines(prev => [...prev, id]);
  };

  return (
    <div className="space-y-6 pb-12">
      <div className="glass-panel p-5 rounded-2xl border border-slate-800">
        <div className="flex items-center space-x-2 text-xs text-safety-cyan font-bold uppercase tracking-wider">
          <Share2 className="w-4 h-4 text-safety-cyan" />
          <span>Knowledge Transfer Engine</span>
        </div>
        <h1 className="text-2xl font-black text-white mt-1">Cross-Mine AI Best Practice Learning</h1>
        <p className="text-xs text-slate-400 mt-0.5">
          When one mine resolves a recurring violation, the neural recommendation engine automatically broadcasts the solution to peer mines.
        </p>
      </div>

      <div className="glass-panel p-6 rounded-xl border border-emerald-500/40 bg-coal-900/90 space-y-4">
        <div className="flex items-center justify-between pb-3 border-b border-slate-800">
          <div className="flex items-center space-x-2">
            <Sparkles className="w-5 h-5 text-emerald-400" />
            <h3 className="text-sm font-extrabold text-white">Proven Best Practice Detected: Jayant Mine (NCL)</h3>
          </div>
          <span className="text-xs font-mono font-bold text-emerald-400 bg-emerald-500/20 px-2 py-0.5 rounded">
            -42% Violation Reduction
          </span>
        </div>

        <p className="text-xs text-slate-300 leading-relaxed">
          &ldquo;Jayant Mine reduced conveyor machinery guarding violations by <strong>42%</strong> over 90 days by deploying modular quick-latch safety cages with digital RFID tamper sensors.&rdquo;
        </p>

        <div className="p-3.5 bg-coal-950 rounded-lg text-xs space-y-2 border border-slate-800">
          <span className="font-bold text-white uppercase text-[10px]">Recommended Transfer Target:</span>
          <p className="text-slate-400">Gevra Mega Open Cast Mine (SECL) — Zone 4 Trunk Line</p>
          
          <div className="flex justify-end pt-2">
            <button
              onClick={() => handleApply('gevra-1')}
              disabled={recommendedMines.includes('gevra-1')}
              className="px-4 py-2 rounded-lg bg-safety-orange text-white font-bold text-xs hover:bg-safety-orange/90 disabled:bg-emerald-600 flex items-center space-x-1.5"
            >
              {recommendedMines.includes('gevra-1') ? (
                <>
                  <CheckCircle2 className="w-3.5 h-3.5" />
                  <span>Best Practice Shared with Gevra Management</span>
                </>
              ) : (
                <>
                  <Share2 className="w-3.5 h-3.5" />
                  <span>Apply & Recommend Practice to Gevra Mine</span>
                </>
              )}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
"""

with open('src/pages/IssuesCorrectiveActions/CriticalIssuesPage.tsx', 'w', encoding='utf-8') as f:
    f.write(critical_issues)

with open('src/pages/IssuesCorrectiveActions/CorrectiveActionsPage.tsx', 'w', encoding='utf-8') as f:
    f.write(corrective_actions)

with open('src/pages/IssuesCorrectiveActions/EvidenceVerificationPage.tsx', 'w', encoding='utf-8') as f:
    f.write(evidence_page)

with open('src/pages/AIIntelligence/AIRiskAnalyticsPage.tsx', 'w', encoding='utf-8') as f:
    f.write(ai_risk_analytics)

with open('src/pages/AIIntelligence/AIPredictionsPage.tsx', 'w', encoding='utf-8') as f:
    f.write(ai_predictions)

with open('src/pages/AIIntelligence/AICopilotPage.tsx', 'w', encoding='utf-8') as f:
    f.write(ai_copilot)

with open('src/pages/AIIntelligence/RecurringViolationsPage.tsx', 'w', encoding='utf-8') as f:
    f.write(recurring_violations)

with open('src/pages/AIIntelligence/CrossMineLearningPage.tsx', 'w', encoding='utf-8') as f:
    f.write(cross_mine)

print("Critical, CorrectiveActions, Verification, and AI Intelligence pages written successfully!")
