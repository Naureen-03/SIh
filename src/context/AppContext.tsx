import React, { createContext, useContext, useState, useEffect } from 'react';
import {
  Mine,
  Subsidiary,
  Issue,
  StatutoryComplianceRule,
  Contractor,
  DocumentRecord,
  AuditBlock,
  AppNotification,
  Inspection,
  IssueStatus
} from '../types';
import {
  INITIAL_MINES,
  INITIAL_SUBSIDIARIES,
  INITIAL_ISSUES,
  INITIAL_STATUTORY_RULES,
  INITIAL_CONTRACTORS,
  INITIAL_DOCUMENTS,
  INITIAL_AUDIT_LOGS,
  INITIAL_NOTIFICATIONS
} from '../data/mockData';
import { createAuditBlock } from '../services/auditService';

interface AppStats {
  totalMines: number;
  overallCompliance: number;
  openIssues: number;
  criticalIssues: number;
  overdueActions: number;
  inspectionsThisMonth: number;
  predictedRisks: number;
  pendingApprovals: number;
}

interface AppContextType {
  mines: Mine[];
  subsidiaries: Subsidiary[];
  issues: Issue[];
  rules: StatutoryComplianceRule[];
  contractors: Contractor[];
  documents: DocumentRecord[];
  auditLogs: AuditBlock[];
  notifications: AppNotification[];
  inspections: Inspection[];
  offlineQueueCount: number;
  isOnline: boolean;
  activeMineId: string;
  setActiveMineId: (id: string) => void;
  stats: AppStats;
  addInspection: (inspection: Inspection, newIssue?: Partial<Issue>) => void;
  addIssue: (issue: Issue) => void;
  assignIssue: (issueId: string, officerName: string, department: string) => void;
  updateIssueStatus: (issueId: string, newStatus: IssueStatus, notes?: string) => void;
  submitEvidenceVerification: (issueId: string, afterEvidenceUrl: string) => Promise<void>;
  closeVerifiedIssue: (issueId: string) => void;
  requestIssueRework: (issueId: string, notes: string) => void;
  syncOfflineQueue: () => void;
  markNotificationRead: (id: string) => void;
  resetDemoData: () => void;
}

const AppContext = createContext<AppContextType | undefined>(undefined);

export const AppProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [mines, setMines] = useState<Mine[]>(() => {
    const saved = localStorage.getItem('mineguard_mines');
    return saved ? JSON.parse(saved) : INITIAL_MINES;
  });

  const [subsidiaries] = useState<Subsidiary[]>(INITIAL_SUBSIDIARIES);

  const [issues, setIssues] = useState<Issue[]>(() => {
    const saved = localStorage.getItem('mineguard_issues');
    return saved ? JSON.parse(saved) : INITIAL_ISSUES;
  });

  const [rules, setRules] = useState<StatutoryComplianceRule[]>(() => {
    const saved = localStorage.getItem('mineguard_rules');
    return saved ? JSON.parse(saved) : INITIAL_STATUTORY_RULES;
  });

  const [contractors] = useState<Contractor[]>(INITIAL_CONTRACTORS);
  const [documents] = useState<DocumentRecord[]>(INITIAL_DOCUMENTS);
  
  const [auditLogs, setAuditLogs] = useState<AuditBlock[]>(() => {
    const saved = localStorage.getItem('mineguard_audit_logs');
    return saved ? JSON.parse(saved) : INITIAL_AUDIT_LOGS;
  });

  const [notifications, setNotifications] = useState<AppNotification[]>(INITIAL_NOTIFICATIONS);
  const [inspections, setInspections] = useState<Inspection[]>([]);
  const [offlineQueueCount, setOfflineQueueCount] = useState(3);
  const [isOnline, setIsOnline] = useState(true);
  const [activeMineId, setActiveMineId] = useState<string>('mine-gevra');

  // Stats calculation
  const openIssuesCount = issues.filter(i => i.status !== 'CLOSED').length;
  const criticalIssuesCount = issues.filter(i => i.severity === 'Critical' && i.status !== 'CLOSED').length;
  const overdueCount = issues.filter(i => i.correctiveAction && i.correctiveAction.slaHoursRemaining <= 0 && i.status !== 'CLOSED').length + 2;

  const complianceRate = Math.round(87 + (INITIAL_ISSUES.length - issues.filter(i => i.status !== 'CLOSED').length) * 0.5);

  const stats: AppStats = {
    totalMines: 18,
    overallCompliance: Math.min(98, Math.max(70, complianceRate)),
    openIssues: 126 - (INITIAL_ISSUES.length - openIssuesCount),
    criticalIssues: 8 - (INITIAL_ISSUES.filter(i => i.severity === 'Critical' && i.status !== 'CLOSED').length - criticalIssuesCount),
    overdueActions: 17,
    inspectionsThisMonth: 342 + inspections.length,
    predictedRisks: 14,
    pendingApprovals: issues.filter(i => i.status === 'VERIFIED').length + 2
  };

  useEffect(() => {
    localStorage.setItem('mineguard_issues', JSON.stringify(issues));
  }, [issues]);

  useEffect(() => {
    localStorage.setItem('mineguard_audit_logs', JSON.stringify(auditLogs));
  }, [auditLogs]);

  const addInspection = (inspection: Inspection, newIssue?: Partial<Issue>) => {
    setInspections(prev => [inspection, ...prev]);

    const audit = createAuditBlock(
      inspection.inspectorName,
      'Field Inspector',
      'SUBMIT_AI_INSPECTION',
      'AI Field Inspection',
      inspection.mineName,
      `Captured inspection #${inspection.inspectionNo} at ${inspection.siteZone} with GPS (${inspection.gps.lat}, ${inspection.gps.lng}).`
    );
    setAuditLogs(prev => [audit, ...prev]);

    if (newIssue && newIssue.title) {
      const fullIssue: Issue = {
        id: 'issue-' + Date.now(),
        issueCode: `ISSUE-2026-${Math.floor(2050 + Math.random() * 800)}`,
        title: newIssue.title,
        description: newIssue.description || 'Observed hazard during mobile inspection.',
        category: newIssue.category || 'Safety',
        severity: newIssue.severity || 'Critical',
        riskScore: newIssue.riskScore || 92,
        confidence: newIssue.confidence || 94,
        mineId: inspection.mineId,
        mineName: inspection.mineName,
        location: inspection.siteZone,
        reportedBy: inspection.inspectorName,
        reportedDate: new Date().toISOString().replace('T', ' ').substring(0, 16),
        deadline: new Date(Date.now() + 24 * 3600 * 1000).toISOString().replace('T', ' ').substring(0, 16),
        status: 'OPEN',
        isCritical: (newIssue.severity || 'Critical') === 'Critical',
        isRecurring: true,
        recurringCount: 4,
        assignedDepartment: newIssue.assignedDepartment || 'Safety Department',
        assignedOfficer: newIssue.assignedOfficer || 'Rajesh Kumar',
        aiExplanation: newIssue.aiExplanation || {
          whySeverity: ['Located near active heavy machinery transit path', 'Similar violation occurred 4 times in this pit'],
          riskFactors: [{ factor: 'Active pinch point danger', points: 35 }],
          historicalContext: 'Historical violation cluster in sector.'
        },
        evidences: inspection.evidences,
        history: [
          { id: 'h-' + Date.now(), timestamp: new Date().toLocaleTimeString(), action: 'Inspection Logged', performedBy: inspection.inspectorName, role: 'Field Inspector' }
        ]
      };
      setIssues(prev => [fullIssue, ...prev]);
    }
  };

  const addIssue = (issue: Issue) => {
    setIssues(prev => [issue, ...prev]);
    const audit = createAuditBlock(
      issue.reportedBy,
      'Field Inspector',
      'CREATE_ISSUE',
      'Issues & Corrective Actions',
      issue.mineName,
      `Created issue #${issue.issueCode}: ${issue.title}`
    );
    setAuditLogs(prev => [audit, ...prev]);
  };

  const assignIssue = (issueId: string, officerName: string, department: string) => {
    setIssues(prev => prev.map(issue => {
      if (issue.id === issueId) {
        return {
          ...issue,
          assignedOfficer: officerName,
          assignedDepartment: department,
          status: 'ASSIGNED',
          history: [
            ...issue.history,
            {
              id: 'h-' + Date.now(),
              timestamp: new Date().toLocaleTimeString(),
              action: 'Smart Assignment Dispatched',
              performedBy: 'S. N. Mishra (Mine Manager)',
              role: 'Mine Official',
              previousStatus: issue.status,
              newStatus: 'ASSIGNED',
              notes: `Assigned to ${officerName} (${department})`
            }
          ]
        };
      }
      return issue;
    }));

    const audit = createAuditBlock(
      'S. N. Mishra',
      'Mine Manager',
      'DISPATCH_ASSIGNMENT',
      'Issues & Corrective Actions',
      'Gevra Mega Open Cast Mine',
      `Assigned issue ${issueId} to ${officerName} (${department}).`,
      'OPEN',
      'ASSIGNED'
    );
    setAuditLogs(prev => [audit, ...prev]);
  };

  const updateIssueStatus = (issueId: string, newStatus: IssueStatus, notes?: string) => {
    setIssues(prev => prev.map(issue => {
      if (issue.id === issueId) {
        return {
          ...issue,
          status: newStatus,
          history: [
            ...issue.history,
            {
              id: 'h-' + Date.now(),
              timestamp: new Date().toLocaleTimeString(),
              action: `Status changed to ${newStatus}`,
              performedBy: 'Rajesh Kumar',
              role: 'Safety Officer',
              previousStatus: issue.status,
              newStatus,
              notes
            }
          ]
        };
      }
      return issue;
    }));

    const audit = createAuditBlock(
      'Rajesh Kumar',
      'Safety Officer',
      'UPDATE_STATUS',
      'Issues & Corrective Actions',
      'Gevra Mega Open Cast Mine',
      `Changed issue status to ${newStatus}. Notes: ${notes || 'None'}`,
      'ASSIGNED',
      newStatus
    );
    setAuditLogs(prev => [audit, ...prev]);
  };

  const submitEvidenceVerification = async (issueId: string, afterEvidenceUrl: string) => {
    setIssues(prev => prev.map(issue => {
      if (issue.id === issueId) {
        return {
          ...issue,
          status: 'VERIFIED',
          correctiveAction: issue.correctiveAction ? {
            ...issue.correctiveAction,
            afterEvidenceUrl,
            status: 'VERIFIED',
            aiVerification: {
              result: 'LIKELY RESOLVED',
              confidence: 91,
              detectedChanges: [
                'Heavy-duty industrial steel mesh guard securely installed along 14m conveyor flank',
                'Emergency trip-wire pull chord reconnected with tension indicator verified green',
                'Restricted yellow hazard perimeter demarcation painted on concrete footing',
                'Mechanical pinch point hazard reduced to statutory compliant baseline'
              ],
              analysisExplanation: 'Dual-phase neural vision scan compared pre-inspection raster against post-rectification evidence. Safety cage bounding box IoU alignment 0.94 with 0 hazardous open apertures detected.',
              verifiedAt: new Date().toISOString()
            }
          } : undefined,
          history: [
            ...issue.history,
            {
              id: 'h-' + Date.now(),
              timestamp: new Date().toLocaleTimeString(),
              action: 'AI Evidence Verified (91% Likely Resolved)',
              performedBy: 'MineGuard AI Neural Engine',
              role: 'AI Verification System',
              previousStatus: issue.status,
              newStatus: 'VERIFIED'
            }
          ]
        };
      }
      return issue;
    }));

    const audit = createAuditBlock(
      'MineGuard AI Vision Engine',
      'AI Autonomous System',
      'AI_EVIDENCE_VERIFIED',
      'AI Evidence Verification',
      'Gevra Mega Open Cast Mine',
      `Dual-raster neural scan confirmed 91% resolution confidence for issue ${issueId}.`,
      'IN_PROGRESS',
      'VERIFIED'
    );
    setAuditLogs(prev => [audit, ...prev]);
  };

  const closeVerifiedIssue = (issueId: string) => {
    setIssues(prev => prev.map(issue => {
      if (issue.id === issueId) {
        return {
          ...issue,
          status: 'CLOSED',
          history: [
            ...issue.history,
            {
              id: 'h-' + Date.now(),
              timestamp: new Date().toLocaleTimeString(),
              action: 'Manager Signoff & Issue Closed',
              performedBy: 'S. N. Mishra',
              role: 'Mine Manager',
              previousStatus: 'VERIFIED',
              newStatus: 'CLOSED',
              notes: 'Corrective action verified via AI vision and on-site check. Issue closed successfully.'
            }
          ]
        };
      }
      return issue;
    }));

    const audit = createAuditBlock(
      'S. N. Mishra',
      'Mine Manager',
      'CLOSE_ISSUE',
      'Closed-Loop Governance',
      'Gevra Mega Open Cast Mine',
      `Manager verified and officially closed issue #${issueId}. Governance metrics updated.`,
      'VERIFIED',
      'CLOSED'
    );
    setAuditLogs(prev => [audit, ...prev]);
  };

  const requestIssueRework = (issueId: string, notes: string) => {
    setIssues(prev => prev.map(issue => {
      if (issue.id === issueId) {
        return {
          ...issue,
          status: 'IN_PROGRESS',
          history: [
            ...issue.history,
            {
              id: 'h-' + Date.now(),
              timestamp: new Date().toLocaleTimeString(),
              action: 'Rework Requested by Manager',
              performedBy: 'S. N. Mishra',
              role: 'Mine Manager',
              previousStatus: issue.status,
              newStatus: 'IN_PROGRESS',
              notes
            }
          ]
        };
      }
      return issue;
    }));
  };

  const syncOfflineQueue = () => {
    setOfflineQueueCount(0);
    const audit = createAuditBlock(
      'Vikramaditya Rao',
      'Field Inspector',
      'SYNC_OFFLINE_REPORTS',
      'Offline Mobile Mode',
      'Gevra Mega Open Cast Mine',
      'Synchronized 3 pending offline field inspection dockets with Cloud Repository.'
    );
    setAuditLogs(prev => [audit, ...prev]);
  };

  const markNotificationRead = (id: string) => {
    setNotifications(prev => prev.map(n => n.id === id ? { ...n, read: true } : n));
  };

  const resetDemoData = () => {
    localStorage.removeItem('mineguard_issues');
    localStorage.removeItem('mineguard_audit_logs');
    setIssues(INITIAL_ISSUES);
    setAuditLogs(INITIAL_AUDIT_LOGS);
  };

  return (
    <AppContext.Provider value={{
      mines,
      subsidiaries,
      issues,
      rules,
      contractors,
      documents,
      auditLogs,
      notifications,
      inspections,
      offlineQueueCount,
      isOnline,
      activeMineId,
      setActiveMineId,
      stats,
      addInspection,
      addIssue,
      assignIssue,
      updateIssueStatus,
      submitEvidenceVerification,
      closeVerifiedIssue,
      requestIssueRework,
      syncOfflineQueue,
      markNotificationRead,
      resetDemoData
    }}>
      {children}
    </AppContext.Provider>
  );
};

export const useApp = () => {
  const ctx = useContext(AppContext);
  if (!ctx) throw new Error('useApp must be used within AppProvider');
  return ctx;
};
