import os

ai_risk = """import React from 'react';
import { BrainCircuit, ShieldAlert, TrendingUp } from 'lucide-react';
import { useApp } from '../../context/AppContext';
import { RiskScoreCard } from '../../components/visualizer/RiskScoreCard';

export const AIRiskAnalyticsPage: React.FC = () => {
  const { mines } = useApp();
  const gevra = mines[0];

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
          <BrainCircuit className="w-4 h-4 text-[#0B2545]" />
          <span>Multi-Vector Risk Analytics Engine</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">AI Risk Quantification & Analytics</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Dynamic mathematical risk scoring across 5 operational vectors: Safety, Environment, Labour, Production, and Contractor compliance.
        </p>
      </div>

      <RiskScoreCard mine={gevra} />
    </div>
  );
};
"""

ai_pred = """import React from 'react';
import { TrendingUp, AlertTriangle, Sparkles, ArrowRight } from 'lucide-react';

interface Props {
  setActiveTab: (tab: string) => void;
}

export const AIPredictionsPage: React.FC<Props> = ({ setActiveTab }) => {
  const predictions = [
    { id: 'PRED-101', mine: 'Gevra Mega Mine (SECL)', area: 'Slope Bench 3 East', prob: '84%', forecast: 'Overburden slope slippage probable within 14 days due to recent groundwater pooling.', recommendation: 'Deploy terrestrial laser scanner & regrade bench slope immediately.', risk: 'Critical' },
    { id: 'PRED-102', mine: 'Dudhichua Mine (NCL)', area: 'Haul Road Junction 2', prob: '78%', forecast: 'Dust concentration likely to breach CPCB 24-hr threshold (PM10 > 120 ug/m3).', recommendation: 'Increase mist cannon cycles from 2 to 6 hourly runs.', risk: 'High' },
    { id: 'PRED-103', mine: 'Moonidih Underground (BCCL)', area: 'Longwall Seam XVI', prob: '71%', forecast: 'Methane CH4 sensor drift detected (+0.04%/day trend).', recommendation: 'Calibrate optical methane sensors & inspect auxiliary fan ducting.', risk: 'High' }
  ];

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
          <TrendingUp className="w-4 h-4 text-[#0B2545]" />
          <span>Predictive Early-Warning Intelligence</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">14-Day AI Predictive Risk Forecasts</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Machine learning forecasts synthesizing IoT telemetry, geotechnical sensors, and historical violation rates.
        </p>
      </div>

      <div className="space-y-3">
        {predictions.map(p => (
          <div
            key={p.id}
            className={`gov-card p-4 space-y-3 ${
              p.risk === 'Critical' ? 'border-l-4 border-l-red-700' : 'border-l-4 border-l-amber-600'
            }`}
          >
            <div className="flex items-start justify-between">
              <div>
                <span className="text-[10px] font-bold bg-slate-100 text-slate-700 px-2 py-0.5 rounded font-mono">
                  {p.mine} &bull; {p.area}
                </span>
                <h3 className="text-sm font-extrabold text-slate-900 mt-1">{p.forecast}</h3>
              </div>
              <span className="font-mono font-bold text-red-700 text-xs bg-red-50 px-2 py-1 rounded border border-red-200">
                Probability: {p.prob}
              </span>
            </div>

            <div className="p-2.5 bg-slate-50 rounded border border-slate-200 text-xs">
              <span className="font-bold text-[#0B2545]">AI Preventive Directive:</span>
              <p className="text-slate-700 text-[11px] mt-0.5">{p.recommendation}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

ai_copilot = """import React, { useState } from 'react';
import { Bot, Send, Sparkles, User, FileText, ArrowRight } from 'lucide-react';
import { useLanguage } from '../../context/LanguageContext';
import { useApp } from '../../context/AppContext';
import { processCopilotQuery, CopilotResponse } from '../../services/copilotService';

interface Props {
  setActiveTab: (tab: string) => void;
}

export const AICopilotPage: React.FC<Props> = ({ setActiveTab }) => {
  const { language } = useLanguage();
  const { mines, issues } = useApp();

  const [inputQuery, setInputQuery] = useState('');
  const [messages, setMessages] = useState<{ sender: 'user' | 'bot'; text: string; data?: any }[]>([
    {
      sender: 'bot',
      text: language === 'hi'
        ? 'नमस्ते। मैं माइनगार्ड एआई सहायक हूँ। आप मुझसे खदान अनुपालन, जोखिम स्कोर, या डीजीएमएस वैधानिक नियमों के बारे में पूछ सकते हैं।'
        : 'Welcome to MineGuard AI Assistant. I am your statutory governance and compliance intelligence service. Ask questions about mine risks, overdue DGMS filings, or contractor compliance.'
    }
  ]);
  const [loading, setLoading] = useState(false);

  const promptChips = [
    'Which mines require immediate statutory attention?',
    'What compliance requirements are currently overdue?',
    'Show contractor safety violations and VTC status',
    'Explain the risk score for Gevra Mega Mine'
  ];

  const handleSend = async (queryText?: string) => {
    const q = queryText || inputQuery;
    if (!q.trim()) return;

    const userMsg = { sender: 'user' as const, text: q };
    setMessages(prev => [...prev, userMsg]);
    setInputQuery('');
    setLoading(true);

    const res: CopilotResponse = await processCopilotQuery(q, language, { mines, issues });

    setLoading(false);
    setMessages(prev => [...prev, {
      sender: 'bot',
      text: res.text,
      data: res.structuredData
    }]);
  };

  return (
    <div className="max-w-4xl mx-auto space-y-4 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
          <Bot className="w-4 h-4 text-[#0B2545]" />
          <span>Statutory Intelligence Service</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">MINEGUARD AI ASSISTANT</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          AI-assisted governance and compliance information service supporting English and हिन्दी.
        </p>
      </div>

      {/* Suggested Prompt Chips */}
      <div className="flex flex-wrap gap-2 text-xs">
        {promptChips.map(chip => (
          <button
            key={chip}
            onClick={() => handleSend(chip)}
            className="px-3 py-1.5 rounded bg-white hover:bg-slate-50 text-slate-800 border border-slate-300 font-semibold transition-all shadow-xs"
          >
            {chip}
          </button>
        ))}
      </div>

      {/* Chat Window */}
      <div className="gov-card p-4 space-y-4 min-h-[420px] max-h-[560px] overflow-y-auto">
        {messages.map((m, idx) => (
          <div
            key={idx}
            className={`flex items-start space-x-3 text-xs ${
              m.sender === 'user' ? 'flex-row-reverse space-x-reverse' : ''
            }`}
          >
            <div className={`w-7 h-7 rounded flex items-center justify-center font-bold shrink-0 ${
              m.sender === 'user' ? 'bg-[#0B2545] text-white' : 'bg-amber-100 text-amber-900 border border-amber-300'
            }`}>
              {m.sender === 'user' ? <User className="w-4 h-4" /> : <Bot className="w-4 h-4" />}
            </div>

            <div className={`p-3.5 rounded max-w-xl space-y-2 ${
              m.sender === 'user'
                ? 'bg-[#0B2545] text-white'
                : 'bg-slate-50 border border-slate-200 text-slate-900'
            }`}>
              <p className="leading-relaxed whitespace-pre-line">{m.text}</p>

              {/* Structured Data Table if present */}
              {m.data && (
                <div className="pt-2 border-t border-slate-200/80">
                  {m.data.kpis && (
                    <div className="grid grid-cols-3 gap-2 text-center text-xs">
                      {m.data.kpis.map((k: any, ki: number) => (
                        <div key={ki} className="bg-white p-2 rounded border border-slate-200">
                          <span className="text-[10px] text-slate-500 uppercase">{k.label}</span>
                          <div className="font-mono font-bold text-slate-900 text-sm mt-0.5">{k.value}</div>
                        </div>
                      ))}
                    </div>
                  )}

                  {m.data.table && (
                    <div className="overflow-x-auto mt-2">
                      <table className="w-full text-left text-[11px]">
                        <thead className="bg-slate-100 font-bold uppercase text-slate-600">
                          <tr>
                            {m.data.table.headers.map((h: string) => (
                              <th key={h} className="p-1.5">{h}</th>
                            ))}
                          </tr>
                        </thead>
                        <tbody className="divide-y divide-slate-200">
                          {m.data.table.rows.map((row: string[], ri: number) => (
                            <tr key={ri}>
                              {row.map((cell, ci) => (
                                <td key={ci} className="p-1.5 font-mono">{cell}</td>
                              ))}
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  )}
                </div>
              )}
            </div>
          </div>
        ))}

        {loading && (
          <div className="flex items-center space-x-2 text-xs text-slate-500 font-mono">
            <span className="w-2 h-2 rounded-full bg-[#0B2545] animate-bounce" />
            <span>Consulting MineGuard statutory knowledge base...</span>
          </div>
        )}
      </div>

      {/* Input Bar */}
      <div className="gov-card p-2 flex items-center space-x-2">
        <input
          type="text"
          placeholder="Ask MineGuard AI Assistant a statutory or governance question..."
          value={inputQuery}
          onChange={e => setInputQuery(e.target.value)}
          onKeyDown={e => e.key === 'Enter' && handleSend()}
          className="flex-1 bg-transparent px-3 py-2 text-xs text-slate-900 placeholder-slate-400 focus:outline-none"
        />
        <button
          onClick={() => handleSend()}
          disabled={!inputQuery.trim() || loading}
          className="gov-btn-primary py-2 px-4"
        >
          <Send className="w-3.5 h-3.5" />
          <span>Send</span>
        </button>
      </div>
    </div>
  );
};
"""

recurring_viol = """import React from 'react';
import { RefreshCw, AlertTriangle } from 'lucide-react';
import { useApp } from '../../context/AppContext';

interface Props {
  setActiveTab: (tab: string) => void;
}

export const RecurringViolationsPage: React.FC<Props> = ({ setActiveTab }) => {
  const recurring = [
    { title: 'Conveyor Trunk Pinch-Point Guard Absence', occurrences: 4, cluster: 'Korba Area (SECL)', risk: 'Critical', dgmsClause: 'CMR 2017 Reg 184(2)', action: 'Mandatory structural audit of all conveyor flanks' },
    { title: 'Contractor Dump Truck Rear Optical Camera Failure', occurrences: 6, cluster: 'Singrauli Area (NCL)', risk: 'High', dgmsClause: 'DGMS Tech Circular 04/2019', action: 'Blacklist non-compliant transport vendor ABC Haulage' },
    { title: 'Excess Ambient PM10 Dust at Coal Loading Hopper', occurrences: 5, cluster: 'Kusmunda Area (SECL)', risk: 'High', dgmsClause: 'MoEFCC EC Condition IV(b)', action: 'Automate dry-fog dust suppression with CAAQMS link' }
  ];

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
          <RefreshCw className="w-4 h-4 text-[#0B2545]" />
          <span>Systemic Pattern Recognition</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Recurring Statutory Violations</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          AI pattern detection isolating chronic safety and environmental non-compliances repeating across mining clusters.
        </p>
      </div>

      <div className="space-y-3">
        {recurring.map((item, idx) => (
          <div key={idx} className="gov-card p-4 space-y-3 border-l-4 border-l-amber-600">
            <div className="flex items-start justify-between">
              <div>
                <span className="text-[10px] font-bold bg-slate-100 text-slate-700 px-2 py-0.5 rounded font-mono">
                  Cluster: {item.cluster} &bull; {item.dgmsClause}
                </span>
                <h3 className="text-sm font-extrabold text-slate-900 mt-1">{item.title}</h3>
              </div>
              <span className="bg-red-50 text-red-800 border border-red-300 text-xs font-mono font-bold px-2 py-0.5 rounded">
                {item.occurrences} Recurring Events
              </span>
            </div>

            <div className="p-2.5 bg-slate-50 rounded border border-slate-200 text-xs">
              <span className="font-bold text-[#0B2545]">Statutory Systemic Directive:</span>
              <p className="text-slate-700 text-[11px] mt-0.5">{item.action}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

cross_mine = """import React from 'react';
import { Share2, CheckCircle2, ArrowRight } from 'lucide-react';

export const CrossMineLearningPage: React.FC = () => {
  const learnings = [
    { title: 'Automatic Mist Cannon Interlocking with CAAQMS Sensors', origin: 'Jayant Mega Mine (NCL)', appliedTo: 'Gevra Mine (SECL)', impact: '-42% Dust Exceedances', description: 'Automating high-pressure mist cannons based on real-time PM10 telemetry eliminated human delay in dust suppression.' },
    { title: 'Optical Laser Geotechnical Slope Monitoring Protocol', origin: 'Dipka Open Cast (SECL)', appliedTo: 'Kusmunda Mine (SECL)', impact: 'Zero Bench Slips in 180 Days', description: 'Continuous millimetric slope radar prevented bench collapses across active 45m overburden cuts.' }
  ];

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
          <Share2 className="w-4 h-4 text-[#0B2545]" />
          <span>Cross-Mine Knowledge Transfer</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Cross-Subsidiary Best Practice Learning</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Transferring proven remediation workflows and safety engineering protocols across Coal India subsidiaries.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {learnings.map((l, idx) => (
          <div key={idx} className="gov-card p-4 space-y-3">
            <div className="flex items-start justify-between">
              <div>
                <span className="text-[10px] font-bold bg-slate-100 text-slate-700 px-2 py-0.5 rounded font-mono">
                  {l.origin} &rarr; {l.appliedTo}
                </span>
                <h3 className="text-sm font-extrabold text-slate-900 mt-1">{l.title}</h3>
              </div>
              <span className="bg-emerald-50 text-emerald-800 border border-emerald-300 text-xs font-mono font-bold px-2 py-0.5 rounded">
                {l.impact}
              </span>
            </div>

            <p className="text-xs text-slate-700 leading-relaxed">{l.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

with open('src/pages/AIIntelligence/AIRiskAnalyticsPage.tsx', 'w', encoding='utf-8') as f:
    f.write(ai_risk)

with open('src/pages/AIIntelligence/AIPredictionsPage.tsx', 'w', encoding='utf-8') as f:
    f.write(ai_pred)

with open('src/pages/AIIntelligence/AICopilotPage.tsx', 'w', encoding='utf-8') as f:
    f.write(ai_copilot)

with open('src/pages/AIIntelligence/RecurringViolationsPage.tsx', 'w', encoding='utf-8') as f:
    f.write(recurring_viol)

with open('src/pages/AIIntelligence/CrossMineLearningPage.tsx', 'w', encoding='utf-8') as f:
    f.write(cross_mine)

print("Part 3b: AI pages written successfully!")
