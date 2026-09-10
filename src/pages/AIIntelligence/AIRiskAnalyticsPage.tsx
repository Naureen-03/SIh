import React from 'react';
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
