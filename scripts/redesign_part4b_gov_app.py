import os

alerts_esc = """import React from 'react';
import { Bell } from 'lucide-react';
import { useApp } from '../../context/AppContext';

export const AlertsEscalationsPage: React.FC = () => {
  const { notifications, markNotificationRead } = useApp();

  const escalationTiers = [
    { level: 'Level 1 (0-24 Hours)', target: 'Assigned Field Officer', action: 'Direct on-site hazard containment' },
    { level: 'Level 2 (24-48 Hours)', target: 'Department Head', action: 'Resource reallocation & secondary audit' },
    { level: 'Level 3 (48-72 Hours)', target: 'Mine General Manager', action: 'Statutory stoppage notice warning' },
    { level: 'Level 4 (>72 Hours)', target: 'Corporate Director & Ministry', action: 'High-level inquiry & disciplinary notice' }
  ];

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-amber-800 font-extrabold uppercase tracking-wider">
          <Bell className="w-4 h-4 text-amber-700" />
          <span>SLA Countdown & 4-Tier Hierarchy</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Alerts & Escalation Center</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          Automated escalation timeline notifying responsible officers, department heads, mine managers, and corporate leadership.
        </p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
        {escalationTiers.map((t, idx) => (
          <div key={idx} className="gov-card p-3.5 space-y-1.5 border-t-4 border-t-[#0B2545]">
            <span className="text-[10px] font-extrabold text-[#0B2545] uppercase font-mono">{t.level}</span>
            <h4 className="text-xs font-bold text-slate-900">{t.target}</h4>
            <p className="text-[11px] text-slate-600">{t.action}</p>
          </div>
        ))}
      </div>

      <div className="space-y-3">
        {notifications.map(n => (
          <div
            key={n.id}
            className={`gov-card p-4 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 ${
              n.severity === 'Critical' ? 'border-l-4 border-l-red-700 bg-red-50/20' : 'border-slate-200'
            }`}
          >
            <div className="space-y-1">
              <div className="flex items-center space-x-2">
                <span className={`text-[10px] font-bold px-2 py-0.5 rounded ${
                  n.severity === 'Critical' ? 'bg-red-700 text-white' : 'bg-amber-600 text-white'
                }`}>
                  {n.severity}
                </span>
                <h3 className="text-xs font-bold text-slate-900">{n.title}</h3>
              </div>
              <p className="text-xs text-slate-700">{n.message}</p>
              <span className="text-[10px] text-slate-500 font-mono">{n.timestamp}</span>
            </div>

            <button
              onClick={() => markNotificationRead(n.id)}
              className="gov-btn-secondary text-xs py-1 px-3 self-end sm:self-center"
            >
              {n.read ? 'Acknowledged' : 'Acknowledge & Dismiss'}
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

reports = """import React from 'react';
import { BarChart3, Download, Sparkles } from 'lucide-react';
import { useApp } from '../../context/AppContext';

export const ManagementReportsPage: React.FC = () => {
  const { stats } = useApp();

  return (
    <div className="space-y-6 pb-12 max-w-4xl mx-auto">
      <div className="gov-card p-5 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2 text-xs text-[#0B2545] font-extrabold uppercase tracking-wider">
            <BarChart3 className="w-4 h-4 text-[#0B2545]" />
            <span>Automated Governance Intelligence</span>
          </div>
          <h1 className="text-2xl font-black text-slate-900 mt-1">Official Management Reports</h1>
          <p className="text-xs text-slate-600 mt-0.5">
            Auto-compiled executive briefs, DGMS safety returns, and compliance audits with instant PDF export.
          </p>
        </div>

        <button className="gov-btn-primary">
          <Download className="w-4 h-4 text-amber-400" />
          <span>Export Monthly Governance PDF</span>
        </button>
      </div>

      <div className="gov-card p-6 space-y-4 border-l-4 border-l-[#0B2545]">
        <div className="flex items-center space-x-2">
          <Sparkles className="w-5 h-5 text-amber-600" />
          <h3 className="text-sm font-black text-slate-900 uppercase tracking-wider">
            AI Executive Governance Summary
          </h3>
        </div>
        <p className="text-xs text-slate-700 leading-relaxed">
          &ldquo;Overall coal mine governance compliance improved by <strong>+8.0% compared to last month</strong> across the Korba operational cluster. However, mechanical conveyor safety violations increased in Zone 4 due to recurring equipment protection lapses. 17 corrective actions are currently under active SLA countdown, with 1 critical hazard verified and ready for closure.&rdquo;
        </p>

        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-3 border-t border-slate-200">
          <div className="p-3 bg-slate-50 rounded border border-slate-200 text-center">
            <span className="text-[10px] text-slate-500 uppercase font-bold">Overall Compliance</span>
            <div className="text-xl font-black text-emerald-800 font-mono mt-0.5">{stats.overallCompliance}%</div>
          </div>
          <div className="p-3 bg-slate-50 rounded border border-slate-200 text-center">
            <span className="text-[10px] text-slate-500 uppercase font-bold">Open Issues</span>
            <div className="text-xl font-black text-amber-800 font-mono mt-0.5">{stats.openIssues}</div>
          </div>
          <div className="p-3 bg-slate-50 rounded border border-slate-200 text-center">
            <span className="text-[10px] text-slate-500 uppercase font-bold">Critical Risks</span>
            <div className="text-xl font-black text-red-700 font-mono mt-0.5">{stats.criticalIssues}</div>
          </div>
          <div className="p-3 bg-slate-50 rounded border border-slate-200 text-center">
            <span className="text-[10px] text-slate-500 uppercase font-bold">Field Audits</span>
            <div className="text-xl font-black text-[#0B2545] font-mono mt-0.5">{stats.inspectionsThisMonth}</div>
          </div>
        </div>
      </div>
    </div>
  );
};
"""

audit_trail = """import React, { useState } from 'react';
import { Lock, CheckCircle2, RefreshCw } from 'lucide-react';
import { useApp } from '../../context/AppContext';

export const AuditTrailPage: React.FC = () => {
  const { auditLogs } = useApp();
  const [verifying, setVerifying] = useState(false);

  const handleVerifyLedger = () => {
    setVerifying(true);
    setTimeout(() => {
      setVerifying(false);
    }, 1200);
  };

  return (
    <div className="space-y-6 pb-12">
      <div className="gov-card p-5 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2 text-xs text-emerald-800 font-extrabold uppercase tracking-wider">
            <Lock className="w-4 h-4 text-emerald-800" />
            <span>Cryptographic Digital Ledger</span>
          </div>
          <h1 className="text-2xl font-black text-slate-900 mt-1">Digital Governance Audit Trail</h1>
          <p className="text-xs text-slate-600 mt-0.5">
            Every inspection, classification, assignment, and manager signoff is secured in a SHA-256 hash-chained block.
          </p>
        </div>

        <button
          onClick={handleVerifyLedger}
          disabled={verifying}
          className="gov-btn-secondary"
        >
          <RefreshCw className={`w-3.5 h-3.5 ${verifying ? 'animate-spin text-[#0B2545]' : ''}`} />
          <span>{verifying ? 'Verifying Ledger...' : 'Verify Cryptographic Integrity'}</span>
        </button>
      </div>

      <div className="space-y-3">
        {auditLogs.map(log => (
          <div
            key={log.blockNumber}
            className="gov-card p-4 space-y-2 font-mono"
          >
            <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between text-xs pb-2 border-b border-slate-200 gap-2">
              <div className="flex items-center space-x-2">
                <span className="bg-[#0B2545] text-white font-black px-2 py-0.5 rounded text-[11px]">
                  BLOCK #{log.blockNumber}
                </span>
                <span className="font-bold text-slate-900 text-xs">{log.action}</span>
                <span className="text-[10px] text-slate-500">({log.module})</span>
              </div>
              <div className="flex items-center space-x-2 text-[10px] text-slate-500">
                <span>{log.timestamp}</span>
                <span className="text-emerald-800 font-bold flex items-center space-x-1">
                  <CheckCircle2 className="w-3 h-3" />
                  <span>SECURE AUDIT RECORD</span>
                </span>
              </div>
            </div>

            <p className="text-xs text-slate-800 font-sans">{log.details}</p>

            <div className="pt-2 text-[10px] text-slate-600 space-y-0.5 bg-slate-50 p-2.5 rounded border border-slate-200">
              <p className="truncate">Block Hash: <strong className="text-emerald-800">{log.blockHash}</strong></p>
              <p className="truncate">Prev Hash: <span className="text-slate-500">{log.previousHash}</span></p>
              <p>Signer: <strong className="text-slate-900 font-sans">{log.user} ({log.role})</strong> &bull; IP: {log.ipAddress}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

settings_page = """import React from 'react';
import { Settings } from 'lucide-react';
import { useAuth } from '../../context/AuthContext';
import { useLanguage } from '../../context/LanguageContext';

export const SettingsPage: React.FC = () => {
  const { currentUser } = useAuth();
  const { language, setLanguage } = useLanguage();

  return (
    <div className="max-w-4xl mx-auto space-y-6 pb-12">
      <div className="gov-card p-5">
        <div className="flex items-center space-x-2 text-xs text-slate-600 font-extrabold uppercase tracking-wider">
          <Settings className="w-4 h-4 text-slate-600" />
          <span>System Configuration</span>
        </div>
        <h1 className="text-2xl font-black text-slate-900 mt-1">Platform Settings</h1>
        <p className="text-xs text-slate-600 mt-0.5">
          User profile, escalation SLA timers, neural risk sensitivity thresholds, and language preferences.
        </p>
      </div>

      <div className="gov-card p-5 space-y-4">
        <h3 className="text-xs font-extrabold text-slate-900 uppercase tracking-wider">Active User Profile</h3>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
          <div>
            <span className="text-slate-500 block">Full Name:</span>
            <p className="font-bold text-slate-900 mt-0.5">{currentUser.name}</p>
          </div>
          <div>
            <span className="text-slate-500 block">Designation & Role:</span>
            <p className="font-bold text-[#0B2545] mt-0.5">{currentUser.roleTitle}</p>
          </div>
          <div>
            <span className="text-slate-500 block">Official Email:</span>
            <p className="font-mono text-slate-900 mt-0.5">{currentUser.email}</p>
          </div>
          <div>
            <span className="text-slate-500 block">Department:</span>
            <p className="font-bold text-slate-900 mt-0.5">{currentUser.department}</p>
          </div>
        </div>
      </div>

      <div className="gov-card p-5 space-y-4">
        <h3 className="text-xs font-extrabold text-slate-900 uppercase tracking-wider">Language & Regionalization</h3>
        <div className="flex items-center space-x-4">
          <button
            onClick={() => setLanguage('en')}
            className={`px-4 py-2 rounded text-xs font-bold border transition-all ${
              language === 'en' ? 'bg-[#0B2545] text-white border-[#0B2545]' : 'bg-slate-50 text-slate-800 border-slate-300'
            }`}
          >
            English (Standard)
          </button>
          <button
            onClick={() => setLanguage('hi')}
            className={`px-4 py-2 rounded text-xs font-bold border transition-all ${
              language === 'hi' ? 'bg-[#0B2545] text-white border-[#0B2545]' : 'bg-slate-50 text-slate-800 border-slate-300'
            }`}
          >
            हिंदी (Hindi)
          </button>
        </div>
      </div>
    </div>
  );
};
"""

app_main = """import React, { useState } from 'react';
import { AuthProvider } from './context/AuthContext';
import { LanguageProvider } from './context/LanguageContext';
import { AppProvider } from './context/AppContext';
import { Sidebar } from './components/layout/Sidebar';
import { TopHeader } from './components/layout/TopHeader';
import { BottomNav } from './components/layout/BottomNav';
import { Footer } from './components/layout/Footer';
import { HeroDemoModal } from './components/walkthrough/HeroDemoModal';

// Pages
import { LandingPage } from './pages/LandingPage';
import { DashboardPage } from './pages/DashboardPage';
import { MineOverviewPage } from './pages/MineOperations/MineOverviewPage';
import { GISMapPage } from './pages/MineOperations/GISMapPage';
import { RiskZonesPage } from './pages/MineOperations/RiskZonesPage';
import { ComplianceTrackerPage } from './pages/Compliance/ComplianceTrackerPage';
import { StatutoryReqsPage } from './pages/Compliance/StatutoryReqsPage';
import { ComplianceCalendarPage } from './pages/Compliance/ComplianceCalendarPage';
import { StatutoryReportsPage } from './pages/Compliance/StatutoryReportsPage';
import { NewInspectionPage } from './pages/Inspections/NewInspectionPage';
import { InspectionHistoryPage } from './pages/Inspections/InspectionHistoryPage';
import { AIFindingsPage } from './pages/Inspections/AIFindingsPage';
import { AllIssuesPage } from './pages/IssuesCorrectiveActions/AllIssuesPage';
import { CriticalIssuesPage } from './pages/IssuesCorrectiveActions/CriticalIssuesPage';
import { CorrectiveActionsPage } from './pages/IssuesCorrectiveActions/CorrectiveActionsPage';
import { EvidenceVerificationPage } from './pages/IssuesCorrectiveActions/EvidenceVerificationPage';
import { AIRiskAnalyticsPage } from './pages/AIIntelligence/AIRiskAnalyticsPage';
import { AIPredictionsPage } from './pages/AIIntelligence/AIPredictionsPage';
import { AICopilotPage } from './pages/AIIntelligence/AICopilotPage';
import { RecurringViolationsPage } from './pages/AIIntelligence/RecurringViolationsPage';
import { CrossMineLearningPage } from './pages/AIIntelligence/CrossMineLearningPage';
import { DocumentRepositoryPage } from './pages/Documents/DocumentRepositoryPage';
import { OCRDigitizationPage } from './pages/Documents/OCRDigitizationPage';
import { ExpiringDocumentsPage } from './pages/Documents/ExpiringDocumentsPage';
import { ContractorDashboardPage } from './pages/Contractors/ContractorDashboardPage';
import { ContractorCompliancePage } from './pages/Contractors/ContractorCompliancePage';
import { ProductionMonitoringPage } from './pages/Operational/ProductionMonitoringPage';
import { EnvironmentalMonitoringPage } from './pages/Operational/EnvironmentalMonitoringPage';
import { LabourCompliancePage } from './pages/Operational/LabourCompliancePage';
import { IncidentManagementPage } from './pages/Operational/IncidentManagementPage';
import { AlertsEscalationsPage } from './pages/Governance/AlertsEscalationsPage';
import { ManagementReportsPage } from './pages/Governance/ManagementReportsPage';
import { AuditTrailPage } from './pages/Governance/AuditTrailPage';
import { SettingsPage } from './pages/Settings/SettingsPage';

const MainLayout: React.FC = () => {
  const [activeTab, setActiveTab] = useState<string>('dashboard');
  const [sidebarCollapsed, setSidebarCollapsed] = useState<boolean>(false);
  const [heroDemoOpen, setHeroDemoOpen] = useState<boolean>(false);

  return (
    <div className="min-h-screen bg-[#F4F6F9] text-slate-900 flex flex-col selection:bg-[#0B2545] selection:text-white">
      {activeTab !== 'landing' && (
        <Sidebar
          activeTab={activeTab}
          setActiveTab={setActiveTab}
          collapsed={sidebarCollapsed}
          setCollapsed={setSidebarCollapsed}
        />
      )}

      {activeTab !== 'landing' && (
        <TopHeader
          sidebarCollapsed={sidebarCollapsed}
          setSidebarCollapsed={setSidebarCollapsed}
          onOpenHeroDemo={() => setHeroDemoOpen(true)}
          setActiveTab={setActiveTab}
        />
      )}

      <main
        className={`flex-1 transition-all duration-300 p-4 sm:p-6 md:p-8 ${
          activeTab === 'landing'
            ? 'w-full'
            : sidebarCollapsed
            ? 'md:ml-20 mt-16'
            : 'md:ml-72 mt-16'
        }`}
      >
        {activeTab === 'landing' && (
          <LandingPage
            onExploreDashboard={() => setActiveTab('dashboard')}
            onStartInspection={() => setActiveTab('new-inspection')}
            onOpenCopilot={() => setActiveTab('ai-copilot')}
          />
        )}
        {activeTab === 'dashboard' && <DashboardPage setActiveTab={setActiveTab} />}
        {activeTab === 'mine-overview' && <MineOverviewPage setActiveTab={setActiveTab} />}
        {activeTab === 'gis-map' && <GISMapPage />}
        {activeTab === 'risk-zones' && <RiskZonesPage setActiveTab={setActiveTab} />}
        {activeTab === 'compliance-tracker' && <ComplianceTrackerPage />}
        {activeTab === 'statutory-reqs' && <StatutoryReqsPage />}
        {activeTab === 'compliance-calendar' && <ComplianceCalendarPage />}
        {activeTab === 'statutory-reports' && <StatutoryReportsPage />}
        {activeTab === 'new-inspection' && <NewInspectionPage setActiveTab={setActiveTab} />}
        {activeTab === 'inspection-history' && <InspectionHistoryPage />}
        {activeTab === 'ai-findings' && <AIFindingsPage setActiveTab={setActiveTab} />}
        {activeTab === 'all-issues' && <AllIssuesPage setActiveTab={setActiveTab} />}
        {activeTab === 'critical-issues' && <CriticalIssuesPage setActiveTab={setActiveTab} />}
        {activeTab === 'corrective-actions' && <CorrectiveActionsPage setActiveTab={setActiveTab} />}
        {activeTab === 'evidence-verification' && <EvidenceVerificationPage setActiveTab={setActiveTab} />}
        {activeTab === 'ai-risk-analytics' && <AIRiskAnalyticsPage />}
        {activeTab === 'ai-predictions' && <AIPredictionsPage setActiveTab={setActiveTab} />}
        {activeTab === 'ai-copilot' && <AICopilotPage setActiveTab={setActiveTab} />}
        {activeTab === 'recurring-violations' && <RecurringViolationsPage setActiveTab={setActiveTab} />}
        {activeTab === 'cross-mine-learning' && <CrossMineLearningPage />}
        {activeTab === 'doc-repository' && <DocumentRepositoryPage />}
        {activeTab === 'ocr-digitization' && <OCRDigitizationPage />}
        {activeTab === 'expiring-documents' && <ExpiringDocumentsPage />}
        {activeTab === 'contractor-dashboard' && <ContractorDashboardPage />}
        {activeTab === 'contractor-compliance' && <ContractorCompliancePage />}
        {activeTab === 'production-monitoring' && <ProductionMonitoringPage />}
        {activeTab === 'environmental-monitoring' && <EnvironmentalMonitoringPage />}
        {activeTab === 'labour-compliance' && <LabourCompliancePage />}
        {activeTab === 'incident-management' && <IncidentManagementPage />}
        {activeTab === 'alerts-escalations' && <AlertsEscalationsPage />}
        {activeTab === 'management-reports' && <ManagementReportsPage />}
        {activeTab === 'audit-trail' && <AuditTrailPage />}
        {activeTab === 'settings' && <SettingsPage />}

        {activeTab !== 'landing' && <Footer />}
      </main>

      {activeTab !== 'landing' && (
        <BottomNav activeTab={activeTab} setActiveTab={setActiveTab} />
      )}

      <HeroDemoModal
        isOpen={heroDemoOpen}
        onClose={() => setHeroDemoOpen(false)}
        setActiveTab={setActiveTab}
      />
    </div>
  );
};

export default function App() {
  return (
    <AuthProvider>
      <LanguageProvider>
        <AppProvider>
          <MainLayout />
        </AppProvider>
      </LanguageProvider>
    </AuthProvider>
  );
}
"""

index_html = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%230B2545'><path d='M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5'/></svg>" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>MINEGUARD AI | Ministry of Coal &bull; Coal India Limited</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
  </head>
  <body class="bg-[#F4F6F9] text-slate-900 antialiased font-sans">
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
"""

with open('src/pages/Governance/AlertsEscalationsPage.tsx', 'w', encoding='utf-8') as f:
    f.write(alerts_esc)

with open('src/pages/Governance/ManagementReportsPage.tsx', 'w', encoding='utf-8') as f:
    f.write(reports)

with open('src/pages/Governance/AuditTrailPage.tsx', 'w', encoding='utf-8') as f:
    f.write(audit_trail)

with open('src/pages/Settings/SettingsPage.tsx', 'w', encoding='utf-8') as f:
    f.write(settings_page)

with open('src/App.tsx', 'w', encoding='utf-8') as f:
    f.write(app_main)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print("Part 4b-gov: Governance pages, App.tsx, and index.html written successfully!")
