import React, { useState } from 'react';
import { Bot, Send, User } from 'lucide-react';
import { useLanguage } from '../../context/LanguageContext';
import { useApp } from '../../context/AppContext';
import { processCopilotQuery } from '../../services/copilotService';

interface Props {
  setActiveTab: (tab: string) => void;
}

interface KPI {
  label: string;
  value: string | number;
  change?: string;
  alert?: boolean;
}

interface ChatMessage {
  sender: 'user' | 'bot';
  text: string;
  data?: {
    kpis?: KPI[];
    tableData?: {
      headers: string[];
      rows: (string | number)[][];
    };
    recommendedActions?: {
      label: string;
      actionKey: string;
    }[];
  };
}

export const AICopilotPage: React.FC<Props> = ({ setActiveTab }) => {
  const { language } = useLanguage();

  const { mines, issues } = useApp();

  const [inputQuery, setInputQuery] = useState('');

  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      sender: 'bot',
      text:
        language === 'hi'
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

  const handleRecommendedAction = (actionKey: string) => {
    switch (actionKey) {
      case 'NAVIGATE_DASHBOARD':
        setActiveTab('dashboard');
        break;

      case 'START_INSPECTION':
        setActiveTab('new-inspection');
        break;

      case 'NAVIGATE_GIS':
        setActiveTab('gis');
        break;

      case 'NAVIGATE_COMPLIANCE':
        setActiveTab('statutory-compliance');
        break;

      case 'SCHEDULE_AUDIT':
        setActiveTab('inspections');
        break;

      default:
        break;
    }
  };

  const handleSend = async (queryText?: string) => {
    const q = queryText || inputQuery;

    if (!q.trim() || loading) return;

    const userMsg: ChatMessage = {
      sender: 'user',
      text: q
    };

    setMessages(prev => [...prev, userMsg]);
    setInputQuery('');
    setLoading(true);

    try {
      /*
       * The statutory rules are not currently exposed by AppContext.
       * Passing an empty rules array keeps the Copilot interface compatible
       * until the actual statutory-rule data source is connected.
       */
      const response = processCopilotQuery(
        q,
        mines,
        issues,
        [],
        language
      );

      setMessages(prev => [
        ...prev,
        {
          sender: 'bot',
          text: response.content,
          data: {
            kpis: response.kpis,
            tableData: response.tableData,
            recommendedActions: response.recommendedActions
          }
        }
      ]);
    } catch (error) {
      console.error('MineGuard Copilot error:', error);

      setMessages(prev => [
        ...prev,
        {
          sender: 'bot',
          text:
            language === 'hi'
              ? 'क्षमा करें, प्रश्न संसाधित करते समय एक त्रुटि हुई। कृपया पुनः प्रयास करें।'
              : 'Sorry, an error occurred while processing your query. Please try again.'
        }
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-4xl mx-auto space-y-4 pb-12">

      {/* Header */}
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
          <Bot className="w-4 h-4 text-[#0B2545]" />

          <span>
            Statutory Intelligence Service
          </span>
        </div>

        <h1 className="text-2xl font-black text-slate-900 mt-1">
          MINEGUARD AI ASSISTANT
        </h1>

        <p className="text-xs text-slate-600 mt-0.5">
          AI-assisted governance and compliance information service
          supporting English and हिन्दी.
        </p>
      </div>

      {/* Suggested Prompt Chips */}
      <div className="flex flex-wrap gap-2 text-xs">
        {promptChips.map(chip => (
          <button
            key={chip}
            onClick={() => handleSend(chip)}
            disabled={loading}
            className="px-3 py-1.5 rounded bg-white hover:bg-slate-50 text-slate-800 border border-slate-300 font-semibold transition-all shadow-xs disabled:opacity-50"
          >
            {chip}
          </button>
        ))}
      </div>

      {/* Chat Window */}
      <div className="gov-card p-4 space-y-4 min-h-[420px] max-h-[560px] overflow-y-auto">

        {messages.map((message, index) => (
          <div
            key={index}
            className={`flex items-start space-x-3 text-xs ${
              message.sender === 'user'
                ? 'flex-row-reverse space-x-reverse'
                : ''
            }`}
          >

            {/* Avatar */}
            <div
              className={`w-7 h-7 rounded flex items-center justify-center font-bold shrink-0 ${
                message.sender === 'user'
                  ? 'bg-[#0B2545] text-white'
                  : 'bg-amber-100 text-amber-900 border border-amber-300'
              }`}
            >
              {message.sender === 'user' ? (
                <User className="w-4 h-4" />
              ) : (
                <Bot className="w-4 h-4" />
              )}
            </div>

            {/* Message */}
            <div
              className={`p-3.5 rounded max-w-xl space-y-3 ${
                message.sender === 'user'
                  ? 'bg-[#0B2545] text-white'
                  : 'bg-slate-50 border border-slate-200 text-slate-900'
              }`}
            >

              <p className="leading-relaxed whitespace-pre-line">
                {message.text}
              </p>

              {/* Structured Data */}
              {message.data && (
                <div className="pt-2 border-t border-slate-200/80 space-y-2">

                  {/* KPI Cards */}
                  {message.data.kpis &&
                    message.data.kpis.length > 0 && (
                      <div className="grid grid-cols-1 sm:grid-cols-3 gap-2 text-center text-xs">

                        {message.data.kpis.map(
                          (kpi, kpiIndex) => (
                            <div
                              key={kpiIndex}
                              className={`bg-white p-2 rounded border ${
                                kpi.alert
                                  ? 'border-red-300'
                                  : 'border-slate-200'
                              }`}
                            >
                              <span className="text-[10px] text-slate-500 uppercase">
                                {kpi.label}
                              </span>

                              <div
                                className={`font-mono font-bold text-sm mt-0.5 ${
                                  kpi.alert
                                    ? 'text-red-700'
                                    : 'text-slate-900'
                                }`}
                              >
                                {kpi.value}
                              </div>

                              {kpi.change && (
                                <div className="text-[9px] text-slate-500 mt-0.5">
                                  {kpi.change}
                                </div>
                              )}
                            </div>
                          )
                        )}

                      </div>
                    )}

                  {/* Table */}
                  {message.data.tableData && (
                    <div className="overflow-x-auto mt-2">

                      <table className="w-full text-left text-[11px]">

                        <thead className="bg-slate-100 font-bold uppercase text-slate-600">
                          <tr>
                            {message.data.tableData.headers.map(
                              (header, headerIndex) => (
                                <th
                                  key={headerIndex}
                                  className="p-1.5"
                                >
                                  {header}
                                </th>
                              )
                            )}
                          </tr>
                        </thead>

                        <tbody className="divide-y divide-slate-200">

                          {message.data.tableData.rows.map(
                            (row, rowIndex) => (
                              <tr key={rowIndex}>
                                {row.map(
                                  (cell, cellIndex) => (
                                    <td
                                      key={cellIndex}
                                      className="p-1.5 font-mono"
                                    >
                                      {String(cell)}
                                    </td>
                                  )
                                )}
                              </tr>
                            )
                          )}

                        </tbody>

                      </table>

                    </div>
                  )}

                  {/* Recommended Actions */}
                  {message.data.recommendedActions &&
                    message.data.recommendedActions.length > 0 && (
                      <div className="pt-2 flex flex-wrap gap-2">

                        {message.data.recommendedActions.map(
                          (action, actionIndex) => (
                            <button
                              key={actionIndex}
                              onClick={() =>
                                handleRecommendedAction(
                                  action.actionKey
                                )
                              }
                              className="gov-btn-secondary text-[10px] py-1.5 px-2.5"
                            >
                              {action.label}
                            </button>
                          )
                        )}

                      </div>
                    )}

                </div>
              )}

            </div>

          </div>
        ))}

        {/* Loading Indicator */}
        {loading && (
          <div className="flex items-center space-x-2 text-xs text-slate-500 font-mono">

            <span className="w-2 h-2 rounded-full bg-[#0B2545] animate-bounce" />

            <span>
              Consulting MineGuard statutory knowledge base...
            </span>

          </div>
        )}

      </div>

      {/* Input Bar */}
      <div className="gov-card p-2 flex items-center space-x-2">

        <input
          type="text"
          placeholder="Ask MineGuard AI Assistant a statutory or governance question..."
          value={inputQuery}
          onChange={event =>
            setInputQuery(event.target.value)
          }
          onKeyDown={event => {
            if (event.key === 'Enter') {
              handleSend();
            }
          }}
          className="flex-1 bg-transparent px-3 py-2 text-xs text-slate-900 placeholder-slate-400 focus:outline-none"
        />

        <button
          onClick={() => handleSend()}
          disabled={!inputQuery.trim() || loading}
          className="gov-btn-primary py-2 px-4"
        >
          <Send className="w-3.5 h-3.5" />

          <span>
            Send
          </span>
        </button>

      </div>

    </div>
  );
};
