import React from 'react';
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
