import React, { useState } from 'react';
import { MapContainer, TileLayer, Marker, Popup, Circle } from 'react-leaflet';
import L from 'leaflet';
import { Layers } from 'lucide-react';
import { Mine } from '../../types';

interface GISMapProps {
  mines: Mine[];
  selectedMine?: Mine | null;
  onSelectMine?: (mine: Mine) => void;
}

const createGovIcon = (risk: number, isCritical: boolean) => {
  const color =
    risk > 70 || isCritical
      ? '#B91C1C'
      : risk > 50
        ? '#D97706'
        : '#15803D';

  const label = risk > 70 || isCritical ? '!' : '✓';

  return L.divIcon({
    className: 'gov-custom-pin',
    html: `
      <div style="
        background-color: ${color};
        width: 28px;
        height: 28px;
        border-radius: 4px;
        border: 2px solid white;
        box-shadow: 0 2px 5px rgba(0,0,0,0.3);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: 900;
        font-size: 13px;
      ">
        ${label}
      </div>
    `,
    iconSize: [28, 28],
    iconAnchor: [14, 14],
    popupAnchor: [0, -14]
  });
};

export const GISMap: React.FC<GISMapProps> = ({
  mines,
  selectedMine,
  onSelectMine
}) => {
  const [activeLayer, setActiveLayer] = useState<'all' | 'critical' | 'heatmap'>('all');
  const [selectedBasin, setSelectedBasin] = useState<string>('All');

  const filteredMines = mines.filter(mine => {
    const criticalCount = mine.openCriticalCount ?? mine.criticalIssues ?? 0;

    if (
      activeLayer === 'critical' &&
      mine.riskScore <= 60 &&
      criticalCount === 0
    ) {
      return false;
    }

    if (
      selectedBasin !== 'All' &&
      !mine.name.includes(selectedBasin) &&
      !mine.subsidiary.includes(selectedBasin)
    ) {
      return false;
    }

    return true;
  });

  return (
    <div className="gov-card overflow-hidden">

      {/* Map Control Bar */}
      <div className="p-3 bg-slate-50 border-b border-slate-200 flex flex-wrap items-center justify-between gap-3 text-xs">

        <div className="flex items-center space-x-2">
          <Layers className="w-4 h-4 text-[#0B2545]" />

          <span className="font-extrabold uppercase text-slate-800 tracking-wider">
            Spatial Layer Control:
          </span>

          <div className="flex items-center space-x-1 bg-white p-0.5 rounded border border-slate-300">

            <button
              onClick={() => setActiveLayer('all')}
              className={`px-2.5 py-1 rounded font-bold transition-all ${
                activeLayer === 'all'
                  ? 'bg-[#0B2545] text-white'
                  : 'text-slate-700 hover:bg-slate-100'
              }`}
            >
              All Mines ({mines.length})
            </button>

            <button
              onClick={() => setActiveLayer('critical')}
              className={`px-2.5 py-1 rounded font-bold transition-all ${
                activeLayer === 'critical'
                  ? 'bg-red-700 text-white'
                  : 'text-slate-700 hover:bg-slate-100'
              }`}
            >
              Critical / High Risk
            </button>

          </div>
        </div>

        {/* Legend */}
        <div className="flex items-center space-x-3 text-[11px] font-bold">

          <div className="flex items-center space-x-1">
            <span className="w-3 h-3 rounded bg-red-700 inline-block" />
            <span className="text-slate-700">
              Critical Risk (&gt;70)
            </span>
          </div>

          <div className="flex items-center space-x-1">
            <span className="w-3 h-3 rounded bg-amber-600 inline-block" />
            <span className="text-slate-700">
              Moderate (50-70)
            </span>
          </div>

          <div className="flex items-center space-x-1">
            <span className="w-3 h-3 rounded bg-emerald-700 inline-block" />
            <span className="text-slate-700">
              Compliant (&lt;50)
            </span>
          </div>

        </div>
      </div>

      {/* Map Container */}
      <div className="h-[480px] w-full relative">

        <MapContainer
          center={[23.6, 83.8]}
          zoom={6}
          scrollWheelZoom={false}
          className="h-full w-full"
        >

          <TileLayer
            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />

          {filteredMines.map(mine => {
            // Use the existing canonical Mine fields.
            const latitude = mine.lat;
            const longitude = mine.lng;

            // Compatibility fallback for older mock-data structures.
            const criticalCount =
              mine.openCriticalCount ?? mine.criticalIssues ?? 0;

            const isCritical =
              mine.riskScore > 70 || criticalCount > 0;

            return (
              <React.Fragment key={mine.id}>

                {/* Mine Marker */}
                <Marker
                  position={[latitude, longitude]}
                  icon={createGovIcon(
                    mine.riskScore,
                    criticalCount > 0
                  )}
                  eventHandlers={{
                    click: () => {
                      if (onSelectMine) {
                        onSelectMine(mine);
                      }
                    }
                  }}
                >

                  <Popup>

                    <div className="p-1 space-y-2 text-xs min-w-[200px]">

                      {/* Mine Header */}
                      <div className="border-b border-slate-200 pb-1">

                        <span className="text-[10px] font-bold uppercase text-slate-500 font-mono">
                          {mine.subsidiary}
                          {' • '}
                          {mine.type ?? 'Coal Mine'}
                        </span>

                        <h4 className="font-extrabold text-slate-900 text-sm leading-tight mt-0.5">
                          {mine.name}
                        </h4>

                      </div>

                      {/* Risk / Compliance */}
                      <div className="grid grid-cols-2 gap-2 text-[11px]">

                        <div>
                          <span className="text-slate-500 block">
                            Risk Score
                          </span>

                          <span
                            className={`font-mono font-bold ${
                              mine.riskScore > 70
                                ? 'text-red-700'
                                : 'text-slate-900'
                            }`}
                          >
                            {mine.riskScore}/100
                          </span>
                        </div>

                        <div>
                          <span className="text-slate-500 block">
                            Compliance
                          </span>

                          <span className="font-mono font-bold text-emerald-800">
                            {mine.complianceScore}%
                          </span>
                        </div>

                      </div>

                      {/* Critical Issues */}
                      <div className="grid grid-cols-2 gap-2 text-[11px]">

                        <div>
                          <span className="text-slate-500 block">
                            Critical Issues
                          </span>

                          <span
                            className={`font-mono font-bold ${
                              criticalCount > 0
                                ? 'text-red-700'
                                : 'text-emerald-700'
                            }`}
                          >
                            {criticalCount}
                          </span>
                        </div>

                        <div>
                          <span className="text-slate-500 block">
                            Status
                          </span>

                          <span
                            className={`font-mono font-bold ${
                              isCritical
                                ? 'text-red-700'
                                : mine.status === 'Alert'
                                  ? 'text-amber-700'
                                  : 'text-emerald-700'
                            }`}
                          >
                            {mine.status}
                          </span>
                        </div>

                      </div>

                      {/* Coordinates */}
                      <div className="pt-1 text-[10px] text-slate-600">

                        <span>
                          Coordinates:{' '}
                          {latitude.toFixed(4)}°N,{' '}
                          {longitude.toFixed(4)}°E
                        </span>

                      </div>

                    </div>

                  </Popup>

                </Marker>

                {/* Risk Zone */}
                {mine.riskScore > 70 && (
                  <Circle
                    center={[latitude, longitude]}
                    radius={12000}
                    pathOptions={{
                      color: '#B91C1C',
                      fillColor: '#B91C1C',
                      fillOpacity: 0.15,
                      weight: 1.5,
                      dashArray: '4, 4'
                    }}
                  />
                )}

              </React.Fragment>
            );
          })}

        </MapContainer>

        {/* GIS Footer Info Stamp */}
        <div className="absolute bottom-2 left-2 z-[400] bg-white/95 backdrop-blur-xs px-2.5 py-1 rounded border border-slate-300 text-[10px] font-mono text-slate-700 shadow-sm">

          <span>
            Last GIS Telemetry Sync: 10 Sep 2026, 08:45 AM
            {' • '}
            Geo-Datum: WGS84
          </span>

        </div>

      </div>
    </div>
  );
};
