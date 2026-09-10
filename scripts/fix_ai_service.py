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
  const labourIssues = issues.filter(i => (i.category === 'Labour' || i.category === 'Contractor Compliance') && i.status !== 'CLOSED');
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

with open('src/services/aiService.ts', 'w', encoding='utf-8') as f:
    f.write(ai_service)

print("aiService.ts fixed successfully!")
