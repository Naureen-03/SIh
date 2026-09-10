import React from 'react';
import { Leaf } from 'lucide-react';
import { ENVIRONMENTAL_TELEMETRY } from '../../data/mockData';

export const EnvironmentalMonitoringPage: React.FC = () => {
  const sensors = [
    { label: 'Ambient PM10 Dust', value: `${ENVIRONMENTAL_TELEMETRY.pm10} ug/m3`, limit: '100 ug/m3', status: 'Threshold Exceeded', alert: true },
    { label: 'Ambient PM2.5', value: `${ENVIRONMENTAL_TELEMETRY.pm25} ug/m3`, limit: '60 ug/m3', status: 'Moderate', alert: false },
    { label: 'Effluent Water pH', value: `${ENVIRONMENTAL_TELEMETRY.waterPh}`, limit: '6.5 - 8.5', status: 'Compliant', alert: false },
    { label: 'Ambient Noise Level', value: `${ENVIRONMENTAL_TELEMETRY.noiseDb} dB`, limit: '75 dB', status: 'Compliant', alert: false },
    { label: 'SO2 Concentration', value: `${ENVIRONMENTAL_TELEMETRY.so2} ug/m3`, limit: '80 ug/m3', status: 'Compliant', alert: false },
    { label: 'Air Quality Index (AQI)', value: `${ENVIRONMENTAL_TELEMETRY.airAqi}`, limit: '0 - 100', status: 'Poor (184)', alert: true },
  ];

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-emerald-800 font-extrabold uppercase tracking-wider">
          <Leaf className="w-4 h-4 text-emerald-800" />
          <span>Continuous Air & Water Telemetry</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Environmental Monitoring Dashboard</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Continuous Ambient Air Quality Monitoring Stations (CAAQMS) with direct CPCB statutory threshold alerts.
        </p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        {sensors.map(s => (
          <div
            key={s.label}
            className={`gov-card p-4 space-y-3 ${
              s.alert ? 'border-l-4 border-l-red-700 bg-red-50/20' : 'border-slate-200'
            }`}
          >
            <div className="flex items-center justify-between">
              <span className="text-xs font-bold text-slate-600 uppercase">{s.label}</span>
              <span className={`text-[10px] font-extrabold px-2 py-0.5 rounded ${
                s.alert ? 'bg-red-700 text-white' : 'bg-emerald-50 text-emerald-800 border border-emerald-300'
              }`}>
                {s.status}
              </span>
            </div>

            <div className="text-2xl font-black text-slate-900 font-mono">{s.value}</div>
            <p className="text-[11px] text-slate-500 font-mono">Statutory Permissible Limit: {s.limit}</p>
          </div>
        ))}
      </div>
    </div>
  );
};
