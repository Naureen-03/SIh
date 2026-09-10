import React from 'react';
import { AlertTriangle, MapPin, ShieldAlert, Zap } from 'lucide-react';
import { useApp } from '../../context/AppContext';

interface Props {
  setActiveTab: (tab: string) => void;
}

export const RiskZonesPage: React.FC<Props> = ({ setActiveTab }) => {
  const { riskZones } = useApp();

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-red-700 font-extrabold uppercase tracking-wider">
          <ShieldAlert className="w-4 h-4 text-red-700" />
          <span>Geofenced High-Risk Sectors</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Identified Risk Zones & Hazard Clusters</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Continuous geospatial telemetry monitoring of conveyor galleries, overburden slope benches, and underground ventilation districts.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {riskZones.map(zone => (
          <div
            key={zone.id}
            className={`gov-card p-4 space-y-3 ${
              zone.severity === 'Critical' ? 'border-red-300 bg-red-50/30' : 'border-slate-200'
            }`}
          >
            <div className="flex items-start justify-between">
              <div>
                <span className="text-[10px] font-bold bg-slate-100 text-slate-700 px-2 py-0.5 rounded font-mono">
                  {zone.mineName}
                </span>
                <h3 className="text-sm font-extrabold text-slate-900 mt-1">{zone.name}</h3>
                <p className="text-[11px] text-slate-500 font-mono">Location: {zone.location}</p>
              </div>

              <span className={`text-[10px] font-extrabold px-2 py-0.5 rounded uppercase ${
                zone.severity === 'Critical' ? 'bg-red-700 text-white' : 'bg-amber-600 text-white'
              }`}>
                {zone.severity} Risk ({zone.riskScore}/100)
              </span>
            </div>

            <div className="p-2.5 bg-white rounded border border-slate-200 text-xs space-y-1">
              <span className="font-bold text-slate-900">Hazard Description:</span>
              <p className="text-slate-600 text-[11px]">{zone.description}</p>
            </div>

            <div className="p-2.5 bg-slate-50 rounded border border-slate-200 text-xs">
              <span className="font-bold text-[#0B2545]">Required Statutory Control:</span>
              <p className="text-slate-700 text-[11px] mt-0.5">{zone.remedialAction}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
