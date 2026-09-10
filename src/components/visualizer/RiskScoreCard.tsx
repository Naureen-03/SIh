import React from 'react';
import { ShieldAlert, Info, Flame } from 'lucide-react';
import { Mine } from '../../types';

interface Props {
  mine: Mine;
}

export const RiskScoreCard: React.FC<Props> = ({ mine }) => {
  const breakdown = mine.riskBreakdown || {
    safety: 86,
    environment: 64,
    labour: 52,
    production: 61,
    contractor: 73
  };

  const waterfallFactors = [
    { factor: 'Recurring conveyor safety violations', points: '+20', positive: false },
    { factor: 'Overdue statutory corrective actions', points: '+15', positive: false },
    { factor: 'Contractor documentation & VTC gaps', points: '+10', positive: false },
    { factor: 'Upcoming statutory MoEFCC deadlines', points: '+8', positive: false },
    { factor: 'Recent successful DGMS quarterly audit', points: '-5', positive: true },
  ];

  return (
    <div className="gov-card p-5 space-y-5">
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between pb-3 border-b border-slate-200 gap-3">
        <div>
          <div className="flex items-center space-x-2">
            <ShieldAlert className="w-4 h-4 text-red-700" />
            <h3 className="text-xs font-extrabold uppercase tracking-wider text-slate-900">
              Explainable AI Risk Score & Factor Breakdown
            </h3>
          </div>
          <p className="text-xs text-slate-500 mt-0.5">
            Multi-vector risk quantification index calculated across 5 statutory domains
          </p>
        </div>

        <div className="flex items-center space-x-3 bg-slate-50 px-4 py-2 rounded border border-slate-300">
          <div>
            <div className="text-xl font-black text-slate-900 font-mono">
              {mine.riskScore} <span className="text-xs text-slate-500 font-normal">/ 100</span>
            </div>
            <div className="text-[10px] font-extrabold tracking-wider text-red-700 uppercase">
              {mine.riskScore > 70 ? 'CRITICAL RISK LEVEL' : 'HIGH RISK LEVEL'}
            </div>
          </div>
          <div className="w-8 h-8 rounded bg-red-100 text-red-800 border border-red-300 flex items-center justify-center font-bold">
            <Flame className="w-4 h-4" />
          </div>
        </div>
      </div>

      <div className="space-y-2.5">
        <h4 className="text-xs font-bold text-slate-700 uppercase tracking-wider">Statutory Risk Vectors</h4>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-3">
          {[
            { label: 'Safety Compliance', score: breakdown.safety, color: 'bg-red-700', text: 'text-red-700' },
            { label: 'Environmental', score: breakdown.environment, color: 'bg-amber-600', text: 'text-amber-700' },
            { label: 'Labour & VTC', score: breakdown.labour, color: 'bg-blue-700', text: 'text-blue-700' },
            { label: 'Production Deficit', score: breakdown.production, color: 'bg-slate-700', text: 'text-slate-700' },
            { label: 'Contractor Risk', score: breakdown.contractor, color: 'bg-purple-700', text: 'text-purple-700' },
          ].map(vec => (
            <div key={vec.label} className="bg-slate-50 p-3 rounded border border-slate-200">
              <div className="flex items-center justify-between text-xs mb-1">
                <span className="text-slate-600 font-medium text-[11px]">{vec.label}</span>
                <span className={`font-mono font-bold ${vec.text}`}>{vec.score}</span>
              </div>
              <div className="w-full h-2 bg-slate-200 rounded-full overflow-hidden">
                <div className={`h-full ${vec.color}`} style={{ width: `${vec.score}%` }} />
              </div>
            </div>
          ))}
        </div>
      </div>

      <div className="space-y-2">
        <h4 className="text-xs font-bold text-slate-700 uppercase tracking-wider">Contributing Factors (Waterfall Analysis)</h4>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-2">
          {waterfallFactors.map(f => (
            <div
              key={f.factor}
              className={`p-2 rounded border flex items-center justify-between text-xs ${
                f.positive
                  ? 'bg-emerald-50 border-emerald-300 text-emerald-900'
                  : 'bg-slate-50 border-slate-200 text-slate-800'
              }`}
            >
              <span className="text-[11px] truncate mr-2">{f.factor}</span>
              <span className={`font-mono font-black px-1.5 py-0.5 rounded text-[11px] ${
                f.positive ? 'bg-emerald-200 text-emerald-900' : 'bg-red-100 text-red-800'
              }`}>
                {f.points}
              </span>
            </div>
          ))}
        </div>
      </div>

      <div className="p-3.5 rounded bg-amber-50/70 border border-amber-200 flex items-start space-x-2.5 text-xs">
        <Info className="w-4 h-4 text-amber-800 shrink-0 mt-0.5" />
        <div>
          <span className="font-extrabold text-slate-900 uppercase text-[10px] tracking-wide block">
            Why is this mine high risk? (AI Reasoned Assessment)
          </span>
          <p className="text-slate-700 leading-relaxed mt-0.5">
            &ldquo;Mine risk increased by <strong>18% this month</strong> due to repeated conveyor safety violations in Zone 4, 7 overdue corrective actions, and two contractor certification gaps under Mines Vocational Training Rules.&rdquo;
          </p>
        </div>
      </div>
    </div>
  );
};
