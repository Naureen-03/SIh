import os

ai_service = """import { IssueCategory, SeverityLevel, Issue } from '../types';

export interface AIClassificationResult {
  category: IssueCategory;
  severity: SeverityLevel;
  riskScore: number;
  confidence: number;
  whySeverity: string[];
  riskFactors: { factor: string; points: number; positive?: boolean }[];
  historicalContext: string;
  suggestedAction: string;
  suggestedSLAHours: number;
  suggestedDepartment: string;
  recommendedAssignee: {
    name: string;
    role: string;
    department: string;
    activeWorkload: number;
    matchReason: string;
  };
}

export async function simulateAIFindingsScan(
  text: string,
  categoryHint?: string,
  zone?: string
): Promise<AIClassificationResult> {
  // Simulate 6-step cognitive processing
  const lower = text.toLowerCase();

  let category: IssueCategory = 'Safety';
  let severity: SeverityLevel = 'Critical';
  let riskScore = 92;
  let confidence = 94;
  let slaHours = 24;
  let department = 'Safety & Mechanical Maintenance';

  if (lower.includes('dust') || lower.includes('air') || lower.includes('water') || lower.includes('pollution') || lower.includes('etp')) {
    category = 'Environment';
    severity = 'High';
    riskScore = 78;
    confidence = 96;
    slaHours = 48;
    department = 'Environmental Management Division';
  } else if (lower.includes('contractor') || lower.includes('training') || lower.includes('vtc') || lower.includes('wage') || lower.includes('labour') || lower.includes('form b')) {
    category = 'Contractor Compliance';
    severity = 'High';
    riskScore = 74;
    confidence = 92;
    slaHours = 72;
    department = 'Human Resources & Contractor Governance';
  } else if (lower.includes('crack') || lower.includes('slope') || lower.includes('dump') || lower.includes('overburden')) {
    category = 'Safety';
    severity = 'Critical';
    riskScore = 95;
    confidence = 96;
    slaHours = 24;
    department = 'Geotechnical & Safety Division';
  } else if (lower.includes('methane') || lower.includes('gas') || lower.includes('ventilation') || lower.includes('airway')) {
    category = 'Safety';
    severity = 'Critical';
    riskScore = 96;
    confidence = 98;
    slaHours = 12;
    department = 'Underground Ventilation & Gas Safety';
  }

  const whySeverity = [
    `Issue involves active hazard vector in ${zone || 'Mining Operational Sector'} with personnel transit.`,
    'Historical correlation identifies 4 recurring events in this subsidiary cluster.',
    'Exceeds statutory compliance threshold under Coal Mines Regulations 2017.',
    'High severity rating assigned due to critical worker safety envelope protection.'
  ];

  const riskFactors = [
    { factor: 'Recurring safety violations (+20)', points: 20 },
    { factor: 'Overdue actions on sector (+15)', points: 15 },
    { factor: 'Machinery pinch point danger (+35)', points: 35 },
    { factor: 'High worker density zone (+22)', points: 22 }
  ];

  const assignees = [
    { name: 'Rajesh Kumar', role: 'Safety Officer (Zone 4 Lead)', department: 'Safety & Mechanical', activeWorkload: 3, matchReason: 'Handles machinery safety in this mining zone and currently has the lowest active task load.' },
    { name: 'Dr. Anita Banerjee', role: 'Senior Environmental Officer', department: 'Environmental Management', activeWorkload: 2, matchReason: 'Subject matter expert for CPCB compliance & ambient air monitoring.' },
    { name: 'M. K. Tripathi', role: 'Contractor Cell Manager', department: 'HR & VTC Administration', activeWorkload: 4, matchReason: 'Manages contractor safety training & statutory Form B registry audits.' },
    { name: 'R. K. Agrawal', role: 'Chief Geotechnical Lead', department: 'Mining Operations', activeWorkload: 2, matchReason: 'Certified slope stability expert for open-cast overburden benches.' }
  ];

  const selectedAssignee = assignees.find(a => a.department.includes(department.split(' ')[0])) || assignees[0];

  return {
    category,
    severity,
    riskScore,
    confidence,
    whySeverity,
    riskFactors,
    historicalContext: 'MineGuard Pattern Engine flagged this violation as part of an active cluster pattern. Similar incidents resolved in adjacent pits reduced recurrence by 42%.',
    suggestedAction: category === 'Safety' 
      ? 'Fabricate and install heavy-duty mesh guard & reconnect pull-wire switch immediately.'
      : 'Deploy mobile high-pressure mist cannons and submit compliance docket within statutory window.',
    suggestedSLAHours: slaHours,
    suggestedDepartment: department,
    recommendedAssignee: selectedAssignee
  };
}

export function calculateMineRiskScore(issues: Issue[]): {
  overallRisk: number;
  breakdown: { safety: number; environment: number; labour: number; production: number; contractor: number };
  factors: { factor: string; points: number; positive?: boolean }[];
  explanation: string;
} {
  const safetyIssues = issues.filter(i => i.category === 'Safety' && i.status !== 'CLOSED');
  const envIssues = issues.filter(i => i.category === 'Environment' && i.status !== 'CLOSED');
  const labourIssues = issues.filter((i => i.category === 'Labour' || i.category === 'Contractor Compliance') && i.status !== 'CLOSED');
  const openCritical = issues.filter(i => i.severity === 'Critical' && i.status !== 'CLOSED');

  const safetyRisk = Math.min(95, 40 + safetyIssues.length * 12 + openCritical.length * 15);
  const envRisk = Math.min(90, 35 + envIssues.length * 10);
  const labourRisk = Math.min(85, 30 + labourIssues.length * 9);
  const prodRisk = 61;
  const contractorRisk = Math.min(92, 45 + labourIssues.length * 8);

  const overallRisk = Math.round((safetyRisk * 0.35) + (envRisk * 0.2) + (labourRisk * 0.15) + (prodRisk * 0.15) + (contractorRisk * 0.15));

  const factors = [
    { factor: 'Recurring safety violations', points: 20 },
    { factor: 'Overdue corrective actions', points: 15 },
    { factor: 'Contractor documentation gaps', points: 10 },
    { factor: 'Upcoming statutory deadlines', points: 8 },
    { factor: 'Recent successful DGMS inspections', points: -5, positive: true }
  ];

  const explanation = `Mine overall risk stands at ${overallRisk}/100 (${overallRisk > 70 ? 'HIGH RISK' : 'MODERATE RISK'}). Risk increased recently due to repeated conveyor safety violations, ${openCritical.length} critical corrective actions, and contractor certification gaps.`;

  return {
    overallRisk,
    breakdown: {
      safety: safetyRisk,
      environment: envRisk,
      labour: labourRisk,
      production: prodRisk,
      contractor: contractorRisk
    },
    factors,
    explanation
  };
}
"""

vision_service = """import { VerificationResult } from '../types';

export interface VisionVerificationOutput {
  result: VerificationResult;
  confidence: number;
  detectedChanges: string[];
  analysisExplanation: string;
  hazardReductionPct: number;
  boundingBoxes: {
    x: number;
    y: number;
    width: number;
    height: number;
    label: string;
    status: 'hazard' | 'mitigated' | 'inspected';
  }[];
}

export async function verifyEvidenceWithAI(
  beforeUrl: string,
  afterUrl: string,
  category: string
): Promise<VisionVerificationOutput> {
  // Simulate neural image raster comparison & object detection
  await new Promise(resolve => setTimeout(resolve, 1200));

  return {
    result: 'LIKELY RESOLVED',
    confidence: 91,
    hazardReductionPct: 94,
    detectedChanges: [
      'Heavy-duty industrial steel mesh guard securely installed along 14m conveyor flank',
      'Emergency trip-wire pull chord reconnected with tension indicator verified in green band',
      'Restricted yellow hazard perimeter demarcation painted on concrete footing',
      'Mechanical pinch point hazard reduced to statutory compliant baseline'
    ],
    analysisExplanation: 'Dual-phase neural vision scan compared pre-inspection raster against post-rectification evidence. Safety cage bounding box IoU alignment 0.94 with 0 hazardous open apertures detected.',
    boundingBoxes: [
      { x: 18, y: 24, width: 62, height: 58, label: 'Installed ISO Guard Mesh', status: 'mitigated' },
      { x: 42, y: 76, width: 35, height: 18, label: 'Reconnected Pull-Cord Switch', status: 'mitigated' },
      { x: 12, y: 82, width: 75, height: 12, label: 'Safety Demarcation Line', status: 'inspected' }
    ]
  };
}
"""

ocr_service = """import { DocumentRecord } from '../types';

export interface OCRDigitizationOutput {
  documentType: string;
  documentNo: string;
  authority: string;
  issueDate: string;
  expiryDate: string;
  daysToExpiry: number;
  status: 'Valid' | 'Expiring Soon' | 'Expired';
  extractedClauses: string[];
  missingFields: string[];
  aiActionRecommendation: string;
  confidence: number;
}

export async function processDocumentOCR(
  fileName: string,
  fileType: string
): Promise<OCRDigitizationOutput> {
  await new Promise(resolve => setTimeout(resolve, 1400));

  const lower = fileName.toLowerCase();

  if (lower.includes('ec') || lower.includes('environment') || lower.includes('clearance')) {
    return {
      documentType: 'Environmental Clearance (EC)',
      documentNo: 'EC/MOEFCC/J-11015/34/2021-IA.II(M)',
      authority: 'Ministry of Environment, Forest and Climate Change (MoEFCC)',
      issueDate: '2021-09-15',
      expiryDate: '2026-09-15',
      daysToExpiry: 16,
      status: 'Expiring Soon',
      extractedClauses: [
        'Condition A(iii): Continuous ambient air quality monitoring stations (CAAQMS) with real-time CPCB server link.',
        'Condition B(viii): Minimum 33% total lease area under progressive afforestation canopy.',
        'Condition C(iv): 100% recycling of treated workshop effluent with zero liquid discharge into Lilagar River.'
      ],
      missingFields: ['Afforestation satellite survival audit certificate 2026'],
      aiActionRecommendation: 'Start EC renewal and compliance submission workflow immediately (16 days remaining).',
      confidence: 97
    };
  }

  return {
    documentType: 'DGMS Safety Operational Permit',
    documentNo: 'DGMS/EZ/PERMIT/2026/89',
    authority: 'Directorate General of Mines Safety (DGMS)',
    issueDate: '2024-03-10',
    expiryDate: '2027-03-09',
    daysToExpiry: 191,
    status: 'Valid',
    extractedClauses: [
      'Maximum bench height 15m; overall slope angle not to exceed 28 degrees.',
      'Mandatory proximity warning devices on all heavy rear dumpers.'
    ],
    missingFields: [],
    aiActionRecommendation: 'Document valid and fully compliant. Next statutory review due in 180 days.',
    confidence: 95
  };
}
"""

audit_service = """import { AuditBlock } from '../types';

export function createAuditBlock(
  user: string,
  role: string,
  action: string,
  module: string,
  mine: string,
  details: string,
  previousState?: string,
  newState?: string,
  previousHash: string = '0x8f4d92a1c7e530b84f2910d5e3c8b1a9f0e2d4c6b8a07153e9c2b4a6f8e0d2c4'
): AuditBlock {
  const blockNumber = Math.floor(1040 + Math.random() * 900);
  const now = new Date();
  const timestamp = now.toISOString().replace('T', ' ').substring(0, 19);

  // Simulated SHA-256 hash generation
  const hashChars = '0123456789abcdef';
  let randomHex = '0x';
  for (let i = 0; i < 64; i++) {
    randomHex += hashChars[Math.floor(Math.random() * hashChars.length)];
  }

  return {
    blockNumber,
    timestamp,
    user,
    role,
    action,
    module,
    mine,
    details,
    previousState,
    newState,
    blockHash: randomHex,
    previousHash,
    ipAddress: '10.14.88.24 (SECL Secure Intranet)',
    verified: true
  };
}
"""

copilot_service = """import { CopilotMessage, Mine, Issue, StatutoryComplianceRule } from '../types';

export function processCopilotQuery(
  query: string,
  mines: Mine[],
  issues: Issue[],
  rules: StatutoryComplianceRule[],
  lang: 'en' | 'hi' = 'en'
): CopilotMessage {
  const lower = query.toLowerCase();
  const id = 'msg-' + Date.now();
  const timestamp = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

  // 1. High-risk mines query
  if (lower.includes('high-risk') || lower.includes('high risk') || lower.includes('risk mines') || lower.includes('जोखिम') || lower.includes('mines require immediate attention')) {
    const highRiskMines = mines.filter(m => m.riskScore > 65).sort((a, b) => b.riskScore - a.riskScore);

    if (lang === 'hi') {
      return {
        id,
        sender: 'assistant',
        timestamp,
        language: 'hi',
        content: `**3 खदानों पर तत्काल ध्यान देने की आवश्यकता है:**\\n\\n1. **${highRiskMines[0]?.name || 'Moonidih Mine'}** — जोखिम स्कोर: **${highRiskMines[0]?.riskScore || 81}/100** (गंभीर)\\n2. **${highRiskMines[1]?.name || 'Rajmahal Open Cast'}** — जोखिम स्कोर: **${highRiskMines[1]?.riskScore || 74}/100** (उच्च)\\n3. **${highRiskMines[2]?.name || 'Gevra Mega Mine'}** — जोखिम स्कोर: **${highRiskMines[2]?.riskScore || 61}/100** (सतर्कता)\\n\\n**सिफारिश:** बार-बार सुरक्षा उल्लंघनों के कारण ${highRiskMines[0]?.name || 'Moonidih खदान'} को सर्वोच्च प्राथमिकता दें।`,
        kpis: [
          { label: 'Critical Risk Mines', value: '3', alert: true },
          { label: 'Avg Compliance', value: '81%' },
          { label: 'Active Critical Actions', value: '7' }
        ],
        tableData: {
          headers: ['Mine Name', 'Subsidiary', 'Risk Score', 'Compliance', 'Critical Issues'],
          rows: highRiskMines.slice(0, 4).map(m => [m.name, m.subsidiary, `${m.riskScore}/100`, `${m.complianceScore}%`, m.criticalIssues])
        },
        recommendedActions: [
          { label: 'Schedule DGMS Audit for High Risk Mines', actionKey: 'SCHEDULE_AUDIT' },
          { label: 'View GIS Risk Heatmap', actionKey: 'NAVIGATE_GIS' }
        ]
      };
    }

    return {
      id,
      sender: 'assistant',
      timestamp,
      language: 'en',
      content: `**3 mines require immediate governance attention:**\\n\\n1. **${highRiskMines[0]?.name || 'Moonidih Underground Mine'}** — Risk Score: **${highRiskMines[0]?.riskScore || 81}/100** (CRITICAL)\\n2. **${highRiskMines[1]?.name || 'Rajmahal Open Cast'}** — Risk Score: **${highRiskMines[1]?.riskScore || 74}/100** (HIGH)\\n3. **${highRiskMines[2]?.name || 'Gevra Mega Open Cast'}** — Risk Score: **${highRiskMines[2]?.riskScore || 61}/100** (ALERT)\\n\\n**Recommended priority:** Moonidih due to underground methane drainage deficits and overdue DGMS compliance actions.`,
      kpis: [
        { label: 'Critical Risk Mines', value: '3', alert: true },
        { label: 'Avg Compliance', value: '81%' },
        { label: 'Active Critical Actions', value: '7' }
      ],
      tableData: {
        headers: ['Mine Name', 'Subsidiary', 'Risk Score', 'Compliance', 'Critical Issues'],
        rows: highRiskMines.slice(0, 4).map(m => [m.name, m.subsidiary, `${m.riskScore}/100`, `${m.complianceScore}%`, m.criticalIssues])
      },
      recommendedActions: [
        { label: 'Schedule DGMS Audit for High Risk Mines', actionKey: 'SCHEDULE_AUDIT' },
        { label: 'Open GIS Risk Heatmap', actionKey: 'NAVIGATE_GIS' }
      ]
    };
  }

  // 2. Overdue compliance query
  if (lower.includes('overdue') || lower.includes('pending') || lower.includes('बकाया') || lower.includes('deadlines')) {
    const overdueRules = rules.filter(r => r.status === 'Overdue' || r.status === 'Non-Compliant');

    return {
      id,
      sender: 'assistant',
      timestamp,
      language: lang,
      content: lang === 'hi'
        ? `वर्तमान में **${overdueRules.length} वैधानिक अनुपालन आवश्यकताएं** गैर-अनुपालन या समय सीमा पार कर चुकी हैं। मुख्य उल्लंघन: कन्वेयर गार्डिंग (CMR 2017) और भूमिगत मीथेन वेंटिलेशन।`
        : `Currently **${overdueRules.length} statutory requirements** are overdue or non-compliant across your operational jurisdiction. Primary risks involve conveyor machine guarding (CMR 2017 Reg 104) and methane drainage compliance.`,
      tableData: {
        headers: ['Rule Code', 'Title', 'Regulation Body', 'Mine', 'Due Date', 'Risk Level'],
        rows: overdueRules.map(r => [r.ruleCode, r.title.substring(0, 35) + '...', r.regulationBody, r.mineName, r.dueDate, r.riskLevel])
      },
      recommendedActions: [
        { label: 'Open Compliance Tracker', actionKey: 'NAVIGATE_COMPLIANCE' },
        { label: 'Notify Responsible Officers', actionKey: 'SEND_REMINDERS' }
      ]
    };
  }

  // 3. General response
  return {
    id,
    sender: 'assistant',
    timestamp,
    language: lang,
    content: lang === 'hi'
      ? `माइनगार्ड एआई कॉपायलट सक्रिय है। आपका प्रश्न: "${query}". प्रणाली 18 खदानों, 126 उल्लंघनों, और 30+ वैधानिक नियमों के डेटाबेस से वास्तविक समय की निगरानी कर रही है।`
      : `MineGuard Copilot is online. Analyzing query: "${query}". All real-time telemetry from 18 mines across 8 Coal India subsidiaries is indexed with active closed-loop AI validation.`,
    kpis: [
      { label: 'Total Mines Monitored', value: '18' },
      { label: 'Overall Compliance', value: '87%' },
      { label: 'Open Critical Issues', value: '8', alert: true },
      { label: 'AI Resolution Rate', value: '91%' }
    ],
    recommendedActions: [
      { label: 'Explore Management Dashboard', actionKey: 'NAVIGATE_DASHBOARD' },
      { label: 'Start AI Field Inspection', actionKey: 'START_INSPECTION' }
    ]
  };
}
"""

with open('src/services/aiService.ts', 'w', encoding='utf-8') as f:
    f.write(ai_service)

with open('src/services/visionService.ts', 'w', encoding='utf-8') as f:
    f.write(vision_service)

with open('src/services/ocrService.ts', 'w', encoding='utf-8') as f:
    f.write(ocr_service)

with open('src/services/auditService.ts', 'w', encoding='utf-8') as f:
    f.write(audit_service)

with open('src/services/copilotService.ts', 'w', encoding='utf-8') as f:
    f.write(copilot_service)

print("Services generated successfully!")
