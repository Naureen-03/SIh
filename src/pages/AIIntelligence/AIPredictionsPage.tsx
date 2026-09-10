import React from 'react';
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
