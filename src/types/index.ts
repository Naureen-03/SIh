
export type UserRole = 
  | 'MINE_OFFICIAL' 
  | 'FIELD_INSPECTOR' 
  | 'CORPORATE_OFFICIAL' 
  | 'REGULATORY_AUTHORITY' 
  | 'CONTRACTOR' 
  | 'ADMIN';

export type IssueCategory = 
  | 'Safety' 
  | 'Environment' 
  | 'Labour' 
  | 'Production' 
  | 'Equipment' 
  | 'Statutory Compliance' 
  | 'Contractor Compliance' 
  | 'Operational Issue';

export type SeverityLevel = 'Critical' | 'High' | 'Medium' | 'Low';

export type IssueStatus = 
  | 'OPEN' 
  | 'AI_CLASSIFIED' 
  | 'ASSIGNED' 
  | 'IN_PROGRESS' 
  | 'RESOLVED' 
  | 'VERIFIED' 
  | 'CLOSED';

export type ComplianceStatus = 
  | 'Compliant' 
  | 'Due Soon' 
  | 'Overdue' 
  | 'Under Review' 
  | 'Non-Compliant';

export type VerificationResult = 
  | 'LIKELY RESOLVED' 
  | 'REQUIRES MANUAL REVIEW' 
  | 'NOT RESOLVED';

export interface User {
  id: string;
  name: string;
  role: UserRole;
  roleTitle: string;
  email: string;
  mineId?: string;
  mineName?: string;
  subsidiary?: string;
  department?: string;
  avatar?: string;
}

export interface Subsidiary {
  id: string;
  code: string;
  name: string;
  headquarters: string;
  state: string;
  totalMines: number;
  complianceRate: number;
  openIssues: number;
  criticalIssues: number;
}

export interface MineZone {
  id: string;
  name: string;
  type: 'Pit' | 'Conveyor' | 'Overburden Dump' | 'Blasting Zone' | 'Workshop' | 'Ventilation Shaft' | 'Coal Handling Plant';
  riskLevel: SeverityLevel;
  activeSensors: number;
}

export interface Mine {
  id: string;
  name: string;
  code: string;
  subsidiary: string;
  state: string;
  district: string;
  lat: number;
  lng: number;
  complianceScore: number;
  riskScore: number;
  governanceHealthScore: number;
  openIssues: number;
  criticalIssues: number;
  overdueActions: number;
  inspectionsThisMonth: number;
  contractorCount: number;
  dailyProductionTargetTons: number;
  dailyProductionActualTons: number;
  status: 'Normal' | 'Alert' | 'Critical';
  zones: MineZone[];
  riskBreakdown: {
    safety: number;
    environment: number;
    labour: number;
    production: number;
    contractor: number;
  };
}

export interface InspectionEvidence {
  id: string;
  type: 'photo' | 'video' | 'voice' | 'document';
  url: string;
  caption?: string;
  timestamp: string;
  gps?: {
    lat: number;
    lng: number;
    altitude?: number;
    accuracy?: number;
  };
}

export interface Inspection {
  id: string;
  inspectionNo: string;
  mineId: string;
  mineName: string;
  siteZone: string;
  inspectionType: 'Safety Audit' | 'Environmental Check' | 'Labour Compliance' | 'Routine Patrol' | 'Surprise DGMS Audit';
  inspectorId: string;
  inspectorName: string;
  date: string;
  time: string;
  gps: {
    lat: number;
    lng: number;
    locationName: string;
  };
  notes: string;
  voiceTranscript?: string;
  evidences: InspectionEvidence[];
  findingsCount: number;
  status: 'Completed' | 'Sync Pending' | 'AI Analyzed';
  aiProcessed: boolean;
}

export interface IssueHistoryEntry {
  id: string;
  timestamp: string;
  action: string;
  performedBy: string;
  role: string;
  previousStatus?: IssueStatus;
  newStatus?: IssueStatus;
  notes?: string;
}

export interface CorrectiveAction {
  id: string;
  issueId: string;
  title: string;
  actionPlan: string;
  recommendedByAI: boolean;
  assignedOfficer: string;
  officerRole: string;
  department: string;
  assignedDate: string;
  deadline: string;
  slaHoursTotal: number;
  slaHoursRemaining: number;
  escalationLevel: 1 | 2 | 3 | 4;
  escalationStageName: string;
  status: IssueStatus;
  beforeEvidenceUrl: string;
  afterEvidenceUrl?: string;
  aiVerification?: {
    result: VerificationResult;
    confidence: number;
    detectedChanges: string[];
    analysisExplanation: string;
    verifiedAt?: string;
  };
  reworkNotes?: string;
}

export interface Issue {
  id: string;
  issueCode: string;
  title: string;
  description: string;
  category: IssueCategory;
  severity: SeverityLevel;
  riskScore: number;
  confidence: number;
  mineId: string;
  mineName: string;
  location: string;
  gpsLat?: number;
  gpsLng?: number;
  reportedBy: string;
  reportedDate: string;
  deadline: string;
  status: IssueStatus;
  isCritical: boolean;
  isRecurring: boolean;
  recurringCount?: number;
  assignedDepartment: string;
  assignedOfficer: string;
  aiExplanation: {
    whySeverity: string[];
    riskFactors: { factor: string; points: number; positive?: boolean }[];
    historicalContext: string;
  };
  evidences: InspectionEvidence[];
  correctiveAction?: CorrectiveAction;
  history: IssueHistoryEntry[];
}

export interface StatutoryComplianceRule {
  id: string;
  ruleCode: string;
  title: string;
  regulationBody: 'DGMS' | 'MoEFCC' | 'CPCB' | 'Mines Act 1952' | 'Coal Mines Regulations 2017' | 'Contract Labour Act';
  sectionRef: string;
  mineId: string;
  mineName: string;
  subsidiary: string;
  department: string;
  responsibleOfficer: string;
  dueDate: string;
  status: ComplianceStatus;
  riskLevel: SeverityLevel;
  penaltyRisk: string;
  documentRef?: string;
  lastAuditedDate?: string;
}

export interface ContractorWorkerStats {
  totalDeployed: number;
  trainedVTC: number;
  medicalFitPME: number;
  safetyIndex: number;
}

export interface Contractor {
  id: string;
  name: string;
  serviceType: 'Overburden Excavation' | 'Coal Transportation' | 'Drilling & Blasting' | 'Equipment Maintenance' | 'Security & Surveillance';
  mineId: string;
  mineName: string;
  subsidiary: string;
  activeWorkers: number;
  complianceScore: number;
  riskScore: number;
  openViolations: number;
  expiredCertifications: number;
  safetyTrainingScore: number;
  auditRecommendation: string;
  stats: ContractorWorkerStats;
  status: 'Approved' | 'Review Required' | 'High Risk';
}

export interface DocumentRecord {
  id: string;
  documentNo: string;
  title: string;
  type: 'Environmental Clearance' | 'DGMS Safety Certificate' | 'Consent to Operate (CTO)' | 'Form IV Annual Return' | 'Contractor Labour License' | 'Blasting Permit';
  mineId: string;
  mineName: string;
  authority: string;
  issueDate: string;
  expiryDate: string;
  daysToExpiry: number;
  status: 'Valid' | 'Expiring Soon' | 'Expired' | 'Under Renewal';
  fileSize: string;
  extractedClauses?: string[];
  missingFields?: string[];
  aiActionRecommendation?: string;
}

export interface AuditBlock {
  blockNumber: number;
  timestamp: string;
  user: string;
  role: string;
  action: string;
  module: string;
  mine: string;
  details: string;
  previousState?: string;
  newState?: string;
  blockHash: string;
  previousHash: string;
  ipAddress: string;
  verified: boolean;
}

export interface EnvironmentalSensorData {
  pm25: number;
  pm10: number;
  so2: number;
  nox: number;
  waterPh: number;
  noiseDb: number;
  dustStatus: 'Normal' | 'Moderate' | 'Above Permissible Threshold';
  waterStatus: 'Normal' | 'Slight Acidity' | 'Compliant';
  airAqi: number;
  timestamp: string;
  mineId: string;
}

export interface ProductionMetric {
  date: string;
  coalTargetTons: number;
  coalActualTons: number;
  obTargetBCM: number;
  obActualBCM: number;
  equipmentAvailabilityPct: number;
  downtimeHours: number;
  anomalyDetected: boolean;
  anomalyReason?: string;
}

export interface AppNotification {
  id: string;
  title: string;
  message: string;
  severity: SeverityLevel;
  type: 'safety' | 'compliance' | 'escalation' | 'document' | 'ai_prediction';
  timestamp: string;
  read: boolean;
  mineId?: string;
  issueId?: string;
  actionLink?: string;
}

export interface CopilotMessage {
  id: string;
  sender: 'user' | 'assistant';
  timestamp: string;
  content: string;
  language?: 'en' | 'hi';
  kpis?: { label: string; value: string | number; change?: string; alert?: boolean }[];
  tableData?: { headers: string[]; rows: (string | number)[][] };
  recommendedActions?: { label: string; actionKey: string; targetId?: string }[];
}
