import React, { useState } from 'react';
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
