import React from 'react';
import { Activity, AlertTriangle } from 'lucide-react';
import { PRODUCTION_RECORDS } from '../../data/mockData';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Legend } from 'recharts';

export const ProductionMonitoringPage: React.FC = () => {
  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
          <Activity className="w-4 h-4 text-[#0B2545]" />
          <span>Operational Telemetry & Output Tracking</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Production Monitoring & Anomaly Detection</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Daily coal extraction vs target, overburden removal, equipment downtime telemetry, and AI root cause anomaly flags.
        </p>
      </div>

      <div className="gov-card p-4 border-l-4 border-l-red-700 bg-red-50/20 flex items-start space-x-3 text-xs">
        <AlertTriangle className="w-5 h-5 text-red-700 shrink-0 mt-0.5" />
        <div>
          <span className="font-extrabold text-red-900 uppercase text-[10px] tracking-wider">
            AI Anomaly Detected (28 Aug 2026):
          </span>
          <p className="text-slate-800 mt-0.5 leading-relaxed">
            &ldquo;Coal production decreased <strong>14.0% below expected target</strong> (124,700 T vs 145,000 T target) due to shovel #08 hydraulic motor failure and contractor driver absenteeism during shift B.&rdquo;
          </p>
        </div>
      </div>

      <div className="gov-card p-4 space-y-4">
        <h3 className="text-xs font-extrabold text-slate-900 uppercase tracking-wider">Daily Coal Extraction (Tons) vs Target</h3>
        <div className="h-64 w-full">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={PRODUCTION_RECORDS}>
              <CartesianGrid strokeDasharray="3 3" stroke="#E2E8F0" />
              <XAxis dataKey="date" stroke="#64748B" fontSize={11} />
              <YAxis stroke="#64748B" domain={[110000, 160000]} fontSize={11} />
              <Tooltip contentStyle={{ backgroundColor: '#FFFFFF', borderColor: '#CBD5E1', borderRadius: '4px', fontSize: '11px' }} />
              <Legend wrapperStyle={{ fontSize: '11px' }} />
              <Line type="monotone" dataKey="coalActualTons" stroke="#0B2545" strokeWidth={2.5} name="Actual Coal (Tons)" dot={{ r: 4 }} />
              <Line type="monotone" dataKey="coalTargetTons" stroke="#15803D" strokeDasharray="4 4" strokeWidth={2} name="Target (Tons)" />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
};
