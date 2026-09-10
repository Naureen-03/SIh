import React from 'react';
import { MapPin, Layers, ShieldAlert, Sparkles, Filter } from 'lucide-react';
import { useApp } from '../../context/AppContext';
import { GISMap } from '../../components/map/GISMap';

export const GISMapPage: React.FC = () => {
  const { mines } = useApp();

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
          <MapPin className="w-4 h-4 text-[#0B2545]" />
          <span>National Geospatial Mining Cadastre</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Coal Mine GIS Monitoring</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Geospatial monitoring of mine locations, inspections, incidents and statutory compliance risks across all Indian coal basins.
        </p>
      </div>

      <GISMap mines={mines} />
    </div>
  );
};
