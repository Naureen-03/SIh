import os

prod_mon = """import React from 'react';
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
"""

env_mon = """import React from 'react';
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
"""

labour_comp = """import React from 'react';
import { Users } from 'lucide-react';

export const LabourCompliancePage: React.FC = () => {
  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
          <Users className="w-4 h-4 text-[#0B2545]" />
          <span>Worker Health & Statutory Registers</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Labour & Worker Compliance</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Tracking Form B worker master registry, Vocational Training Centre (VTC) attendance, and Periodic Medical Examination (PME).
        </p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
        <div className="gov-card p-4 space-y-2">
          <span className="text-xs font-bold text-slate-600 uppercase">Form B Register Status</span>
          <div className="text-xl font-black text-emerald-800 font-mono">96.4% Verified</div>
          <p className="text-xs text-slate-500">Biometric fingerprint sync</p>
        </div>

        <div className="gov-card p-4 space-y-2">
          <span className="text-xs font-bold text-slate-600 uppercase">Annual VTC Safety Refresher</span>
          <div className="text-xl font-black text-amber-800 font-mono">89.2% Completed</div>
          <p className="text-xs text-slate-500">18 operators pending batch</p>
        </div>

        <div className="gov-card p-4 space-y-2">
          <span className="text-xs font-bold text-slate-600 uppercase">PME Medical Fitness</span>
          <div className="text-xl font-black text-slate-900 font-mono">98.1% Current</div>
          <p className="text-xs text-slate-500">DGMS Standard Audiometry/Chest</p>
        </div>
      </div>
    </div>
  );
};
"""

incident_mgmt = """import React, { useState } from 'react';
import { ShieldAlert, Plus } from 'lucide-react';

export const IncidentManagementPage: React.FC = () => {
  const incidents = [
    { id: 'INC-2026-081', title: 'Hydraulic Hose Rupture on Dumper #14', location: 'Gevra Bench 4', date: '29 Aug 2026 11:30', reporter: 'P. K. Verma', status: 'Contained' },
    { id: 'INC-2026-080', title: 'Localized Water Logging near Pit Sump', location: 'Kusmunda Pit Face', date: '28 Aug 2026 15:40', reporter: 'R. S. Sahu', status: 'Resolved' }
  ];

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2 text-xs text-red-700 font-extrabold uppercase tracking-wider">
            <ShieldAlert className="w-4 h-4 text-red-700" />
            <span>Emergency Incident Reporting</span>
          </div>
          <h1 className="text-2xl font-black text-slate-900 mt-1">Incident Management Register</h1>
          <p className="text-xs text-slate-600 mt-0.5">
            Real-time hazard containment and automatic generation of closed-loop corrective actions.
          </p>
        </div>

        <button className="gov-btn-danger">
          <Plus className="w-4 h-4" />
          <span>Report Safety Incident</span>
        </button>
      </div>

      <div className="space-y-3">
        {incidents.map(inc => (
          <div key={inc.id} className="gov-card p-4 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3">
            <div>
              <div className="flex items-center space-x-2">
                <span className="font-mono font-bold text-slate-900 text-xs">{inc.id}</span>
                <span className="text-[10px] bg-slate-100 text-slate-700 px-2 py-0.5 rounded">{inc.location}</span>
              </div>
              <h3 className="text-xs font-bold text-slate-900 mt-1">{inc.title}</h3>
              <p className="text-[11px] text-slate-500">Reported by {inc.reporter} &bull; {inc.date}</p>
            </div>

            <span className="text-[10px] font-extrabold px-2.5 py-1 rounded bg-emerald-50 text-emerald-800 border border-emerald-300">
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
    f.write(prod_mon)

with open('src/pages/Operational/EnvironmentalMonitoringPage.tsx', 'w', encoding='utf-8') as f:
    f.write(env_mon)

with open('src/pages/Operational/LabourCompliancePage.tsx', 'w', encoding='utf-8') as f:
    f.write(labour_comp)

with open('src/pages/Operational/IncidentManagementPage.tsx', 'w', encoding='utf-8') as f:
    f.write(incident_mgmt)

print("Part 4b-op: Operational pages written successfully!")
