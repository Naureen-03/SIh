import os

app_main = """import React, { useState } from 'react';
import { AuthProvider } from './context/AuthContext';
import { LanguageProvider } from './context/LanguageContext';
import { AppProvider } from './context/AppContext';
import { Sidebar } from './components/layout/Sidebar';
import { TopHeader } from './components/layout/TopHeader';
import { BottomNav } from './components/layout/BottomNav';
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
    <div className="min-h-screen bg-coal-950 text-slate-100 flex flex-col selection:bg-safety-orange selection:text-white">
      {/* Sidebar for Desktop & Tablet */}
      {activeTab !== 'landing' && (
        <Sidebar
          activeTab={activeTab}
          setActiveTab={setActiveTab}
          collapsed={sidebarCollapsed}
          setCollapsed={setSidebarCollapsed}
        />
      )}

      {/* Top Header */}
      {activeTab !== 'landing' && (
        <TopHeader
          sidebarCollapsed={sidebarCollapsed}
          setSidebarCollapsed={setSidebarCollapsed}
          onOpenHeroDemo={() => setHeroDemoOpen(true)}
          setActiveTab={setActiveTab}
        />
      )}

      {/* Main Content Area */}
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
      </main>

      {/* Mobile Bottom Navigation */}
      {activeTab !== 'landing' && (
        <BottomNav activeTab={activeTab} setActiveTab={setActiveTab} />
      )}

      {/* Hero Demo Modal Tour */}
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

main_tsx = """import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
"""

index_html = """<!doctype html>
<html lang="en" class="dark">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23FF6B00'><path d='M14.5 2.5L12 5l-2.5-2.5L7 5l2.5 2.5L2 15l4.5 4.5 7.5-7.5 2.5 2.5 2.5-2.5-2.5-2.5 2.5-2.5z'/></svg>" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>MINEGUARD AI | Smart Governance & Compliance Monitoring System for Coal Mines</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  </head>
  <body class="bg-coal-950 text-slate-100 antialiased font-sans">
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
"""

with open('src/App.tsx', 'w', encoding='utf-8') as f:
    f.write(app_main)

with open('src/main.tsx', 'w', encoding='utf-8') as f:
    f.write(main_tsx)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print("App.tsx, main.tsx, and index.html generated successfully!")
