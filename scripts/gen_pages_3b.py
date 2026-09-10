import os

production_mon = """import React from 'react';
import { Activity, AlertTriangle } from 'lucide-react';
import { PRODUCTION_RECORDS } from '../../data/mockData';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Legend } from 'recharts';

export const ProductionMonitoringPage: React.FC = () => {
  return (
    <div className="space-y-6 pb-12">
      <div className="glass-panel p-5 rounded-2xl border border-slate-800">
        <div className="flex items-center space-x-2 text-xs text-safety-cyan font-bold uppercase tracking-wider">
          <Activity className="w-4 h-4 text-safety-cyan" />
          <span>Operational Telemetry & Output Tracking</span>
        </div>
        <h1 className="text-2xl font-black text-white mt-1">Production Monitoring & Anomaly Detection</h1>
        <p className="text-xs text-slate-400 mt-0.5">
          Daily coal extraction vs target, overburden removal, downtime telemetry, and AI root cause anomaly flags.
        </p>
      </div>

      <div className="p-4 rounded-xl bg-red-950/30 border border-red-500/40 flex items-start space-x-3 text-xs">
        <AlertTriangle className="w-5 h-5 text-red-400 shrink-0 mt-0.5" />
        <div>
          <span className="font-extrabold text-red-400 uppercase text-[10px] tracking-wider">
            AI Anomaly Detected (28 Aug 2026):
          </span>
          <p className="text-slate-200 mt-0.5">
            &ldquo;Coal production decreased <strong>14.0% below expected target</strong> (124,700 T vs 145,000 T target) due to shovel #08 hydraulic motor failure and contractor driver absenteeism during shift B.&rdquo;
          </p>
        </div>
      </div>

      <div className="glass-panel p-5 rounded-xl border border-slate-800 space-y-4">
        <h3 className="text-sm font-extrabold text-white uppercase tracking-wider">Daily Coal Extraction (Tons) vs Target</h3>
        <div className="h-64 w-full">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={PRODUCTION_RECORDS}>
              <CartesianGrid strokeDasharray="3 3" stroke="#1E2638" />
              <XAxis dataKey="date" stroke="#64748B" fontSize={11} />
              <YAxis stroke="#64748B" domain={[110000, 160000]} fontSize={11} />
              <Tooltip contentStyle={{ backgroundColor: '#0E131F', borderColor: '#334155', borderRadius: '8px' }} />
              <Legend />
              <Line type="monotone" dataKey="coalActualTons" stroke="#FF6B00" strokeWidth={3} name="Actual Coal (Tons)" dot={{ r: 4 }} />
              <Line type="monotone" dataKey="coalTargetTons" stroke="#10B981" strokeDasharray="4 4" strokeWidth={2} name="Target (Tons)" />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
};
"""

environmental_mon = """import React from 'react';
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
      <div className="glass-panel p-5 rounded-2xl border border-slate-800">
        <div className="flex items-center space-x-2 text-xs text-emerald-400 font-bold uppercase tracking-wider">
          <Leaf className="w-4 h-4 text-emerald-400" />
          <span>Real-Time Environmental Telemetry</span>
        </div>
        <h1 className="text-2xl font-black text-white mt-1">Environmental Monitoring Dashboard</h1>
        <p className="text-xs text-slate-400 mt-0.5">
          Continuous Ambient Air Quality Monitoring Stations (CAAQMS) with direct CPCB statutory threshold alerts.
        </p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        {sensors.map(s => (
          <div
            key={s.label}
            className={`glass-panel p-5 rounded-xl border space-y-3 ${
              s.alert ? 'border-red-500/40 bg-red-950/15' : 'border-slate-800'
            }`}
          >
            <div className="flex items-center justify-between">
              <span className="text-xs font-bold text-slate-400 uppercase">{s.label}</span>
              <span className={`text-[10px] font-extrabold px-2 py-0.5 rounded ${
                s.alert ? 'bg-red-500 text-white' : 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30'
              }`}>
                {s.status}
              </span>
            </div>

            <div className="text-2xl font-black text-white font-mono">{s.value}</div>
            <p className="text-[11px] text-slate-400 font-mono">Statutory Permissible Limit: {s.limit}</p>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

labour_compliance = """import React from 'react';
import { Users } from 'lucide-react';

export const LabourCompliancePage: React.FC = () => {
  return (
    <div className="space-y-6 pb-12">
      <div className="glass-panel p-5 rounded-2xl border border-slate-800">
        <div className="flex items-center space-x-2 text-xs text-safety-orange font-bold uppercase tracking-wider">
          <Users className="w-4 h-4 text-safety-orange" />
          <span>Worker Health & Statutory Registers</span>
        </div>
        <h1 className="text-2xl font-black text-white mt-1">Labour & Worker Compliance</h1>
        <p className="text-xs text-slate-400 mt-0.5">
          Tracking Form B worker master registry, Vocational Training Centre (VTC) attendance, and Periodic Medical Examination (PME).
        </p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
        <div className="glass-panel p-5 rounded-xl border border-slate-800 space-y-2">
          <span className="text-xs font-bold text-slate-400 uppercase">Form B Register Status</span>
          <div className="text-xl font-black text-emerald-400">96.4% Verified</div>
          <p className="text-xs text-slate-400">Biometric fingerprint sync</p>
        </div>

        <div className="glass-panel p-5 rounded-xl border border-slate-800 space-y-2">
          <span className="text-xs font-bold text-slate-400 uppercase">Annual VTC Safety Refresher</span>
          <div className="text-xl font-black text-amber-400">89.2% Completed</div>
          <p className="text-xs text-slate-400">18 operators pending batch</p>
        </div>

        <div className="glass-panel p-5 rounded-xl border border-slate-800 space-y-2">
          <span className="text-xs font-bold text-slate-400 uppercase">PME Medical Fitness</span>
          <div className="text-xl font-black text-white font-mono">98.1% Current</div>
          <p className="text-xs text-slate-400">DGMS Standard Audiometry/Chest</p>
        </div>
      </div>
    </div>
  );
};
"""

incident_mgmt = """import React, { useState } from 'react';
import { ShieldAlert, Plus } from 'lucide-react';

export const IncidentManagementPage: React.FC = () => {
  const [showModal, setShowModal] = useState(false);

  const incidents = [
    { id: 'INC-2026-081', title: 'Hydraulic Hose Rupture on Dumper #14', location: 'Gevra Bench 4', date: '29 Aug 2026 11:30', reporter: 'P. K. Verma', status: 'Contained' },
    { id: 'INC-2026-080', title: 'Localized Water Logging near Pit Sump', location: 'Kusmunda Pit Face', date: '28 Aug 2026 15:40', reporter: 'R. S. Sahu', status: 'Resolved' }
  ];

  return (
    <div className="space-y-6 pb-12">
      <div className="glass-panel p-5 rounded-2xl border border-slate-800 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2 text-xs text-red-500 font-bold uppercase tracking-wider">
            <ShieldAlert className="w-4 h-4 text-red-500" />
            <span>Emergency Incident Reporting</span>
          </div>
          <h1 className="text-2xl font-black text-white mt-1">Incident Management</h1>
          <p className="text-xs text-slate-400 mt-0.5">
            Real-time hazard containment and automatic generation of closed-loop corrective actions.
          </p>
        </div>

        <button
          onClick={() => setShowModal(true)}
          className="flex items-center space-x-2 px-4 py-2.5 rounded-xl bg-red-600 hover:bg-red-500 text-white font-bold text-xs shadow-lg shadow-red-600/30"
        >
          <Plus className="w-4 h-4" />
          <span>Report Safety Incident</span>
        </button>
      </div>

      <div className="space-y-3">
        {incidents.map(inc => (
          <div key={inc.id} className="glass-panel p-4 rounded-xl border border-slate-800 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3">
            <div>
              <div className="flex items-center space-x-2">
                <span className="font-mono font-bold text-white text-xs">{inc.id}</span>
                <span className="text-[10px] bg-coal-800 text-slate-400 px-2 py-0.5 rounded">{inc.location}</span>
              </div>
              <h3 className="text-xs font-bold text-white mt-1">{inc.title}</h3>
              <p className="text-[11px] text-slate-400">Reported by {inc.reporter} • {inc.date}</p>
            </div>

            <span className="text-[10px] font-extrabold px-2.5 py-1 rounded bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">
              {inc.status} (Corrective Action Active)
            </span>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

with open('src/pages/Operational/ProductionMonitoringPage.tsx', 'w', encoding='utf-8') as f:
    f.write(production_mon)

with open('src/pages/Operational/EnvironmentalMonitoringPage.tsx', 'w', encoding='utf-8') as f:
    f.write(environmental_mon)

with open('src/pages/Operational/LabourCompliancePage.tsx', 'w', encoding='utf-8') as f:
    f.write(labour_compliance)

with open('src/pages/Operational/IncidentManagementPage.tsx', 'w', encoding='utf-8') as f:
    f.write(incident_mgmt)

print("Operational pages written successfully!")
