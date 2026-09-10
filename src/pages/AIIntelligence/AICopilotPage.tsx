import React, { useState } from 'react';
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
