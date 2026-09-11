import React from 'react';
import {
  AlertTriangle,
  MapPin,
  ShieldAlert,
  Zap,
} from 'lucide-react';
import { useApp } from '../../context/AppContext';

interface Props {
  setActiveTab: (tab: string) => void;
}

export const RiskZonesPage: React.FC<Props> = ({
  setActiveTab,
}) => {
  const { mines } = useApp();

  /*
   * The existing MineZone type contains:
   * id
   * name
   * type
   * riskLevel
   * activeSensors
   *
   * Therefore this page derives the additional display
   * information locally instead of changing the global type.
   */

  const riskZones = mines.flatMap((mine) =>
    (mine.zones || []).map((zone) => {
      const riskScore =
        zone.riskLevel === 'Critical'
          ? 90
          : zone.riskLevel === 'High'
            ? 75
            : zone.riskLevel === 'Medium'
              ? 55
              : 30;

      const location =
        mine.district && mine.state
          ? `${mine.district}, ${mine.state}`
          : mine.state || 'Mine Site';

      const description =
        zone.riskLevel === 'Critical'
          ? `${zone.type} has been identified as a critical-risk operational zone requiring immediate attention.`
          : zone.riskLevel === 'High'
            ? `${zone.type} has elevated operational risk and requires prioritized monitoring.`
            : zone.riskLevel === 'Medium'
              ? `${zone.type} has moderate operational risk and should remain under enhanced monitoring.`
              : `${zone.type} is currently under routine operational monitoring.`;

      const remedialAction =
        zone.riskLevel === 'Critical'
          ? 'Immediate inspection and corrective action required.'
          : zone.riskLevel === 'High'
            ? 'Prioritize inspection and corrective action.'
            : zone.riskLevel === 'Medium'
              ? 'Continue enhanced monitoring and periodic inspection.'
              : 'Continue routine monitoring and periodic inspection.';

      return {
        ...zone,
        mineName: mine.name,
        location,
        riskScore,
        description,
        remedialAction,
      };
    })
  );

  const criticalZones = riskZones.filter(
    (zone) => zone.riskLevel === 'Critical'
  );

  const highRiskZones = riskZones.filter(
    (zone) => zone.riskLevel === 'High'
  );

  const totalSensors = riskZones.reduce(
    (total, zone) => total + zone.activeSensors,
    0
  );

  const getRiskBadge = (riskLevel: string) => {
    switch (riskLevel) {
      case 'Critical':
        return 'bg-red-100 text-red-700 border-red-300';

      case 'High':
        return 'bg-orange-100 text-orange-700 border-orange-300';

      case 'Medium':
        return 'bg-yellow-100 text-yellow-700 border-yellow-300';

      default:
        return 'bg-green-100 text-green-700 border-green-300';
    }
  };

  const getRiskText = (riskLevel: string) => {
    switch (riskLevel) {
      case 'Critical':
        return 'text-red-700';

      case 'High':
        return 'text-orange-700';

      case 'Medium':
        return 'text-yellow-700';

      default:
        return 'text-green-700';
    }
  };

  const getRiskBar = (riskLevel: string) => {
    switch (riskLevel) {
      case 'Critical':
        return 'bg-red-500';

      case 'High':
        return 'bg-orange-500';

      case 'Medium':
        return 'bg-yellow-500';

      default:
        return 'bg-green-500';
    }
  };

  return (
    <div className="space-y-6">

      {/* =====================================================
          PAGE HEADER
      ===================================================== */}

      <div>
        <div className="flex items-center gap-2">

          <ShieldAlert className="w-5 h-5 text-[#0B2545]" />

          <span className="text-xs font-extrabold uppercase tracking-wider text-[#0B2545]">
            AI Risk Intelligence
          </span>

        </div>

        <h1 className="text-2xl font-black text-slate-900 mt-1">
          Mine Risk Zones
        </h1>

        <p className="text-sm text-slate-500 mt-1">
          AI-powered identification and monitoring of
          high-risk operational zones across mines.
        </p>

      </div>

      {/* =====================================================
          SUMMARY CARDS
      ===================================================== */}

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">

        {/* Total Zones */}

        <div className="gov-card p-5">

          <div className="flex items-center justify-between">

            <div>

              <p className="text-xs font-bold uppercase tracking-wide text-slate-500">
                Total Risk Zones
              </p>

              <p className="text-2xl font-black text-slate-900 mt-1">
                {riskZones.length}
              </p>

            </div>

            <ShieldAlert className="w-8 h-8 text-[#0B2545]" />

          </div>

        </div>

        {/* Critical Zones */}

        <div className="gov-card p-5 border-l-4 border-l-red-600">

          <div className="flex items-center justify-between">

            <div>

              <p className="text-xs font-bold uppercase tracking-wide text-red-600">
                Critical Zones
              </p>

              <p className="text-2xl font-black text-red-700 mt-1">
                {criticalZones.length}
              </p>

            </div>

            <AlertTriangle className="w-8 h-8 text-red-600" />

          </div>

        </div>

        {/* High Risk */}

        <div className="gov-card p-5 border-l-4 border-l-orange-500">

          <div className="flex items-center justify-between">

            <div>

              <p className="text-xs font-bold uppercase tracking-wide text-orange-600">
                High Risk
              </p>

              <p className="text-2xl font-black text-orange-700 mt-1">
                {highRiskZones.length}
              </p>

            </div>

            <Zap className="w-8 h-8 text-orange-600" />

          </div>

        </div>

        {/* Active Sensors */}

        <div className="gov-card p-5">

          <div className="flex items-center justify-between">

            <div>

              <p className="text-xs font-bold uppercase tracking-wide text-slate-500">
                Active Sensors
              </p>

              <p className="text-2xl font-black text-slate-900 mt-1">
                {totalSensors}
              </p>

            </div>

            <MapPin className="w-8 h-8 text-emerald-700" />

          </div>

        </div>

      </div>

      {/* =====================================================
          RISK ZONE CARDS
      ===================================================== */}

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-5">

        {riskZones.map((zone) => (

          <div
            key={`${zone.id}-${zone.mineName}`}
            className="gov-card p-5"
          >

            {/* Zone Header */}

            <div className="flex items-start justify-between gap-4">

              <div className="min-w-0">

                <p className="text-[10px] font-extrabold uppercase tracking-wider text-slate-500">
                  {zone.mineName}
                </p>

                <h2 className="text-lg font-black text-slate-900 mt-1">
                  {zone.name}
                </h2>

                <p className="text-xs font-semibold text-slate-500 mt-1">
                  {zone.type}
                </p>

              </div>

              <span
                className={`shrink-0 px-2.5 py-1 rounded-full border text-[10px] font-extrabold uppercase ${getRiskBadge(
                  zone.riskLevel
                )}`}
              >
                {zone.riskLevel}
              </span>

            </div>

            {/* Location */}

            <div className="flex items-center gap-2 mt-4 text-xs text-slate-600">

              <MapPin className="w-4 h-4 text-slate-500 shrink-0" />

              <span>
                Location: {zone.location}
              </span>

            </div>

            {/* Risk Score */}

            <div className="mt-4 p-4 bg-slate-50 rounded border border-slate-200">

              <div className="flex items-center justify-between">

                <span className="text-[10px] font-extrabold uppercase tracking-wide text-slate-500">
                  AI Risk Score
                </span>

                <span
                  className={`text-lg font-black ${getRiskText(
                    zone.riskLevel
                  )}`}
                >
                  {zone.riskScore}/100
                </span>

              </div>

              <div className="w-full h-2 bg-slate-200 rounded-full overflow-hidden mt-2">

                <div
                  className={`h-full rounded-full transition-all ${getRiskBar(
                    zone.riskLevel
                  )}`}
                  style={{
                    width: `${zone.riskScore}%`,
                  }}
                />

              </div>

              <div className="flex justify-between mt-1">

                <span className="text-[9px] text-slate-400">
                  0
                </span>

                <span className="text-[9px] text-slate-400">
                  100
                </span>

              </div>

            </div>

            {/* Active Sensors */}

            <div className="flex items-center justify-between mt-4 py-3 border-y border-slate-200">

              <div className="flex items-center gap-2">

                <Zap className="w-4 h-4 text-[#0B2545]" />

                <span className="text-xs font-bold text-slate-600">
                  Active Monitoring Sensors
                </span>

              </div>

              <span className="text-sm font-black text-slate-900">
                {zone.activeSensors}
              </span>

            </div>

            {/* Description */}

            <div className="mt-4">

              <p className="text-[10px] font-extrabold uppercase tracking-wide text-slate-500">
                Risk Description
              </p>

              <p className="text-xs text-slate-700 leading-relaxed mt-1">
                {zone.description}
              </p>

            </div>

            {/* Recommended Action */}

            <div className="mt-4 p-3 bg-slate-50 rounded border border-slate-200">

              <div className="flex items-center gap-2">

                <AlertTriangle
                  className={`w-4 h-4 ${getRiskText(
                    zone.riskLevel
                  )}`}
                />

                <p className="text-[10px] font-extrabold uppercase tracking-wide text-slate-600">
                  Recommended Corrective Action
                </p>

              </div>

              <p className="text-xs font-bold text-slate-800 leading-relaxed mt-2">
                {zone.remedialAction}
              </p>

            </div>

          </div>

        ))}

      </div>

      {/* =====================================================
          EMPTY STATE
      ===================================================== */}

      {riskZones.length === 0 && (

        <div className="gov-card p-10 text-center">

          <ShieldAlert className="w-10 h-10 mx-auto text-slate-400" />

          <h3 className="text-base font-black text-slate-900 mt-3">
            No Risk Zones Available
          </h3>

          <p className="text-xs text-slate-500 mt-1">
            Risk-zone information will appear when mine
            zone data becomes available.
          </p>

        </div>

      )}

    </div>
  );
};
