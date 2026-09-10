import {
  Subsidiary,
  Mine,
  Issue,
  StatutoryComplianceRule,
  Contractor,
  DocumentRecord,
  AuditBlock,
  EnvironmentalSensorData,
  ProductionMetric,
  AppNotification
} from '../types';

export const INITIAL_SUBSIDIARIES: Subsidiary[] = [
  { id: 'sub-1', code: 'SECL', name: 'South Eastern Coalfields Limited', headquarters: 'Bilaspur, Chhattisgarh', state: 'Chhattisgarh & MP', totalMines: 67, complianceRate: 88, openIssues: 34, criticalIssues: 3 },
  { id: 'sub-2', code: 'NCL', name: 'Northern Coalfields Limited', headquarters: 'Singrauli, MP', state: 'Madhya Pradesh & UP', totalMines: 10, complianceRate: 92, openIssues: 18, criticalIssues: 1 },
  { id: 'sub-3', code: 'MCL', name: 'Mahanadi Coalfields Limited', headquarters: 'Sambalpur, Odisha', state: 'Odisha', totalMines: 22, complianceRate: 85, openIssues: 26, criticalIssues: 2 },
  { id: 'sub-4', code: 'ECL', name: 'Eastern Coalfields Limited', headquarters: 'Sanctoria, West Bengal', state: 'West Bengal & Jharkhand', totalMines: 84, complianceRate: 81, openIssues: 42, criticalIssues: 4 },
  { id: 'sub-5', code: 'CCL', name: 'Central Coalfields Limited', headquarters: 'Ranchi, Jharkhand', state: 'Jharkhand', totalMines: 45, complianceRate: 84, openIssues: 29, criticalIssues: 2 },
  { id: 'sub-6', code: 'WCL', name: 'Western Coalfields Limited', headquarters: 'Nagpur, Maharashtra', state: 'Maharashtra & MP', totalMines: 58, complianceRate: 86, openIssues: 21, criticalIssues: 1 },
  { id: 'sub-7', code: 'BCCL', name: 'Bharat Coking Coal Limited', headquarters: 'Dhanbad, Jharkhand', state: 'Jharkhand', totalMines: 36, complianceRate: 79, openIssues: 38, criticalIssues: 5 },
  { id: 'sub-8', code: 'CMPDIL', name: 'Central Mine Planning & Design Institute', headquarters: 'Ranchi, Jharkhand', state: 'Pan-India', totalMines: 8, complianceRate: 96, openIssues: 4, criticalIssues: 0 },
];

export const INITIAL_MINES: Mine[] = [
  {
    id: 'mine-gevra',
    name: 'Gevra Mega Open Cast Mine',
    code: 'SECL-GEV-01',
    subsidiary: 'SECL',
    state: 'Chhattisgarh',
    district: 'Korba',
    lat: 22.3384,
    lng: 82.6075,
    complianceScore: 89,
    riskScore: 61,
    governanceHealthScore: 84,
    openIssues: 14,
    criticalIssues: 2,
    overdueActions: 3,
    inspectionsThisMonth: 38,
    contractorCount: 17,
    dailyProductionTargetTons: 145000,
    dailyProductionActualTons: 138500,
    status: 'Alert',
    zones: [
      { id: 'z-1', name: 'Conveyor Trunk Line 4B', type: 'Conveyor', riskLevel: 'Critical', activeSensors: 14 },
      { id: 'z-2', name: 'Main Excavation Pit 3', type: 'Pit', riskLevel: 'High', activeSensors: 28 },
      { id: 'z-3', name: 'South OB Dump Area', type: 'Overburden Dump', riskLevel: 'Medium', activeSensors: 12 },
      { id: 'z-4', name: 'Coal Handling Plant #2', type: 'Coal Handling Plant', riskLevel: 'Medium', activeSensors: 20 },
      { id: 'z-5', name: 'Drilling & Blasting Bench 8', type: 'Blasting Zone', riskLevel: 'High', activeSensors: 9 }
    ],
    riskBreakdown: { safety: 86, environment: 64, labour: 52, production: 61, contractor: 73 }
  },
  {
    id: 'mine-kusmunda',
    name: 'Kusmunda Open Cast Project',
    code: 'SECL-KUS-02',
    subsidiary: 'SECL',
    state: 'Chhattisgarh',
    district: 'Korba',
    lat: 22.3551,
    lng: 82.6958,
    complianceScore: 87,
    riskScore: 54,
    governanceHealthScore: 86,
    openIssues: 11,
    criticalIssues: 1,
    overdueActions: 2,
    inspectionsThisMonth: 34,
    contractorCount: 14,
    dailyProductionTargetTons: 130000,
    dailyProductionActualTons: 127800,
    status: 'Normal',
    zones: [
      { id: 'kz-1', name: 'Sector 2 Pit Face', type: 'Pit', riskLevel: 'Medium', activeSensors: 22 },
      { id: 'kz-2', name: 'Central In-Pit Crusher', type: 'Coal Handling Plant', riskLevel: 'High', activeSensors: 16 }
    ],
    riskBreakdown: { safety: 68, environment: 58, labour: 45, production: 52, contractor: 59 }
  },
  {
    id: 'mine-dipka',
    name: 'Dipka Open Cast Mine',
    code: 'SECL-DIP-03',
    subsidiary: 'SECL',
    state: 'Chhattisgarh',
    district: 'Korba',
    lat: 22.3180,
    lng: 82.5680,
    complianceScore: 91,
    riskScore: 42,
    governanceHealthScore: 90,
    openIssues: 8,
    criticalIssues: 0,
    overdueActions: 1,
    inspectionsThisMonth: 29,
    contractorCount: 12,
    dailyProductionTargetTons: 105000,
    dailyProductionActualTons: 104200,
    status: 'Normal',
    zones: [
      { id: 'dz-1', name: 'Deep Pit Extension 5', type: 'Pit', riskLevel: 'Medium', activeSensors: 18 }
    ],
    riskBreakdown: { safety: 48, environment: 44, labour: 38, production: 40, contractor: 46 }
  },
  {
    id: 'mine-jayant',
    name: 'Jayant Open Cast Project',
    code: 'NCL-JAY-01',
    subsidiary: 'NCL',
    state: 'Madhya Pradesh',
    district: 'Singrauli',
    lat: 24.1167,
    lng: 82.6500,
    complianceScore: 94,
    riskScore: 36,
    governanceHealthScore: 94,
    openIssues: 6,
    criticalIssues: 0,
    overdueActions: 0,
    inspectionsThisMonth: 42,
    contractorCount: 10,
    dailyProductionTargetTons: 85000,
    dailyProductionActualTons: 86400,
    status: 'Normal',
    zones: [
      { id: 'jz-1', name: 'Dragline Shovel Strip 4', type: 'Pit', riskLevel: 'Low', activeSensors: 30 }
    ],
    riskBreakdown: { safety: 32, environment: 40, labour: 28, production: 35, contractor: 38 }
  },
  {
    id: 'mine-dudhichua',
    name: 'Dudhichua Open Cast Mine',
    code: 'NCL-DUD-02',
    subsidiary: 'NCL',
    state: 'Madhya Pradesh & UP',
    district: 'Singrauli & Sonbhadra',
    lat: 24.1350,
    lng: 82.7230,
    complianceScore: 92,
    riskScore: 40,
    governanceHealthScore: 91,
    openIssues: 7,
    criticalIssues: 1,
    overdueActions: 1,
    inspectionsThisMonth: 36,
    contractorCount: 11,
    dailyProductionTargetTons: 65000,
    dailyProductionActualTons: 64100,
    status: 'Normal',
    zones: [
      { id: 'ddz-1', name: 'Inter-State Border Haul Road', type: 'Workshop', riskLevel: 'Medium', activeSensors: 15 }
    ],
    riskBreakdown: { safety: 42, environment: 46, labour: 36, production: 38, contractor: 41 }
  },
  {
    id: 'mine-rajmahal',
    name: 'Rajmahal Open Cast Project',
    code: 'ECL-RAJ-01',
    subsidiary: 'ECL',
    state: 'Jharkhand',
    district: 'Godda',
    lat: 25.0489,
    lng: 87.4124,
    complianceScore: 78,
    riskScore: 74,
    governanceHealthScore: 72,
    openIssues: 19,
    criticalIssues: 2,
    overdueActions: 4,
    inspectionsThisMonth: 27,
    contractorCount: 15,
    dailyProductionTargetTons: 55000,
    dailyProductionActualTons: 47200,
    status: 'Critical',
    zones: [
      { id: 'rz-1', name: 'North Highwall Slope Area', type: 'Pit', riskLevel: 'Critical', activeSensors: 14 }
    ],
    riskBreakdown: { safety: 82, environment: 71, labour: 68, production: 74, contractor: 77 }
  },
  {
    id: 'mine-jhanjra',
    name: 'Jhanjra Underground Mine',
    code: 'ECL-JHA-02',
    subsidiary: 'ECL',
    state: 'West Bengal',
    district: 'Paschim Bardhaman',
    lat: 23.6520,
    lng: 87.2790,
    complianceScore: 82,
    riskScore: 68,
    governanceHealthScore: 79,
    openIssues: 16,
    criticalIssues: 2,
    overdueActions: 3,
    inspectionsThisMonth: 30,
    contractorCount: 8,
    dailyProductionTargetTons: 12000,
    dailyProductionActualTons: 10800,
    status: 'Alert',
    zones: [
      { id: 'jhz-1', name: 'Continuous Miner Face 1W', type: 'Ventilation Shaft', riskLevel: 'Critical', activeSensors: 26 }
    ],
    riskBreakdown: { safety: 88, environment: 52, labour: 64, production: 66, contractor: 60 }
  },
  {
    id: 'mine-moonidih',
    name: 'Moonidih Underground Mine',
    code: 'BCCL-MOO-01',
    subsidiary: 'BCCL',
    state: 'Jharkhand',
    district: 'Dhanbad',
    lat: 23.7380,
    lng: 86.3450,
    complianceScore: 76,
    riskScore: 81,
    governanceHealthScore: 70,
    openIssues: 22,
    criticalIssues: 3,
    overdueActions: 5,
    inspectionsThisMonth: 29,
    contractorCount: 7,
    dailyProductionTargetTons: 8000,
    dailyProductionActualTons: 6800,
    status: 'Critical',
    zones: [
      { id: 'mz-1', name: 'Longwall Panel 18 Gas Drainage', type: 'Ventilation Shaft', riskLevel: 'Critical', activeSensors: 32 }
    ],
    riskBreakdown: { safety: 92, environment: 65, labour: 74, production: 78, contractor: 76 }
  }
];

export const INITIAL_ISSUES: Issue[] = [
  {
    id: 'issue-2041',
    issueCode: 'ISSUE-2026-2041',
    title: 'Missing protective barrier near conveyor belt trunk line 4B',
    description: 'During safety inspection at Gevra Zone 4, observed missing mechanical safety barrier and emergency trip wire pull chord disconnected over a 12-meter stretch near high-speed conveyor drive.',
    category: 'Safety',
    severity: 'Critical',
    riskScore: 92,
    confidence: 94,
    mineId: 'mine-gevra',
    mineName: 'Gevra Mega Open Cast Mine',
    location: 'Conveyor Trunk Line 4B, Drive Head Section',
    gpsLat: 22.3392,
    gpsLng: 82.6081,
    reportedBy: 'Vikramaditya Rao (Field Inspector)',
    reportedDate: '2026-08-30 09:15',
    deadline: '2026-08-31 09:15',
    status: 'OPEN',
    isCritical: true,
    isRecurring: true,
    recurringCount: 4,
    assignedDepartment: 'Safety Department',
    assignedOfficer: 'Rajesh Kumar (Safety Officer)',
    aiExplanation: {
      whySeverity: [
        'Issue located near active 1200mm high-speed conveyor drive with continuous worker transit',
        'Similar guarding violation occurred 4 times in this mining zone during the last 60 days',
        'Previous corrective action was delayed by 36 hours beyond statutory SLA',
        'High probability of severe machinery entanglement and fatal injury under DGMS Standard #102'
      ],
      riskFactors: [
        { factor: 'Recurring safety violations (+20)', points: 20 },
        { factor: 'Overdue corrective actions on sector (+15)', points: 15 },
        { factor: 'Active machinery pinch point danger (+35)', points: 35 },
        { factor: 'High worker density zone (+22)', points: 22 }
      ],
      historicalContext: 'Repeated conveyor guarding lapses identified in Gevra Zone 4. Previous inspection reports (#INSP-882, #INSP-904) noted mechanical vibration damage to fastener brackets.'
    },
    evidences: [
      {
        id: 'ev-1',
        type: 'photo',
        url: 'https://images.unsplash.com/photo-1578328819058-b69f3a3b0f6b?auto=format&fit=crop&w=800&q=80',
        caption: 'BEFORE: Unsafe exposed conveyor rollers and missing safety cage',
        timestamp: '2026-08-30 09:16'
      }
    ],
    correctiveAction: {
      id: 'ca-2041',
      issueId: 'issue-2041',
      title: 'Fabricate and install heavy-duty mesh guard & reconnect pull-wire switch',
      actionPlan: 'Safety & Mechanical Maintenance team to fabricate ISO-compliant 2.2m mesh enclosure, secure with anti-vibration bolts, reconnect and test emergency pull-wire switch.',
      recommendedByAI: true,
      assignedOfficer: 'Rajesh Kumar',
      officerRole: 'Safety Officer (Zone 4 Lead)',
      department: 'Safety & Mechanical Maintenance',
      assignedDate: '2026-08-30 09:20',
      deadline: '2026-08-31 09:20',
      slaHoursTotal: 24,
      slaHoursRemaining: 18,
      escalationLevel: 1,
      escalationStageName: 'Assigned Officer (Level 1)',
      status: 'OPEN',
      beforeEvidenceUrl: 'https://images.unsplash.com/photo-1578328819058-b69f3a3b0f6b?auto=format&fit=crop&w=800&q=80',
      afterEvidenceUrl: 'https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=800&q=80',
      aiVerification: {
        result: 'LIKELY RESOLVED',
        confidence: 91,
        detectedChanges: [
          'Heavy-duty industrial steel mesh guard securely installed along 14m conveyor flank',
          'Emergency trip-wire pull chord reconnected with tension indicator verified green',
          'Restricted yellow hazard perimeter demarcation painted on concrete footing',
          'Mechanical pinch point hazard reduced to statutory compliant baseline'
        ],
        analysisExplanation: 'Dual-phase neural vision scan compared pre-inspection raster against post-rectification evidence. Safety cage bounding box IoU alignment 0.94 with 0 hazardous open apertures.'
      }
    },
    history: [
      { id: 'h-1', timestamp: '2026-08-30 09:15', action: 'Inspection Submitted', performedBy: 'Vikramaditya Rao', role: 'Field Inspector', notes: 'Inspection #INSP-2026-1049 captured via Mobile App with GPS & Voice recording.' },
      { id: 'h-2', timestamp: '2026-08-30 09:16', action: 'AI Automated Classification & Scoring', performedBy: 'MineGuard AI Engine', role: 'AI System', notes: 'Classified: Safety Critical (92/100). Auto-generated RCA and Smart Assignee recommendation.' },
      { id: 'h-3', timestamp: '2026-08-30 09:20', action: 'Smart Assignment Dispatched', performedBy: 'S. N. Mishra', role: 'Mine Manager', notes: 'Accepted AI recommendation: Assigned to Rajesh Kumar (Safety Dept).' }
    ]
  },
  {
    id: 'issue-2038',
    issueCode: 'ISSUE-2026-2038',
    title: 'Ambient PM10 dust level exceeding CPCB statutory threshold near residential buffer',
    description: 'Continuous ambient air quality station CAAQMS-02 recorded PM10 spike of 285 ug/m3 (statutory limit: 100 ug/m3) over 4 consecutive hours during active haulage.',
    category: 'Environment',
    severity: 'High',
    riskScore: 78,
    confidence: 96,
    mineId: 'mine-gevra',
    mineName: 'Gevra Mega Open Cast Mine',
    location: 'North Perimeter Haul Road & Buffer Greenbelt',
    reportedBy: 'Continuous Environmental Telemetry IoT',
    reportedDate: '2026-08-29 14:00',
    deadline: '2026-08-30 18:00',
    status: 'IN_PROGRESS',
    isCritical: false,
    isRecurring: true,
    recurringCount: 3,
    assignedDepartment: 'Environmental Management Division',
    assignedOfficer: 'Dr. Anita Banerjee',
    aiExplanation: {
      whySeverity: [
        'Sensor recorded 285% of permissible ambient dust threshold',
        'Downwind drift towards Korba township residential buffer zone',
        'Water sprinkler tanker fleet #04 was inactive due to pump breakdown'
      ],
      riskFactors: [
        { factor: 'Continuous sensor threshold breach (+28)', points: 28 },
        { factor: 'Regulatory CPCB penalty risk (+25)', points: 25 },
        { factor: 'Downwind residential vicinity (+25)', points: 25 }
      ],
      historicalContext: 'Dry season wind gusts frequently exacerbate haul road dust dispersion when suppression tankers miss scheduled 45-minute spray cycles.'
    },
    evidences: [
      { id: 'ev-2', type: 'photo', url: 'https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?auto=format&fit=crop&w=800&q=80', caption: 'Dense particulate haze across main haul corridor', timestamp: '2026-08-29 14:05' }
    ],
    correctiveAction: {
      id: 'ca-2038',
      issueId: 'issue-2038',
      title: 'Deploy 4 additional mist fogger cannons and service sprinkler bowsers',
      actionPlan: 'Deploy mobile high-pressure mist cannons along north perimeter. Expedite repair of stationary misting nozzles on Haul Road 3.',
      recommendedByAI: true,
      assignedOfficer: 'Dr. Anita Banerjee',
      officerRole: 'Senior Environmental Officer',
      department: 'Environmental Management',
      assignedDate: '2026-08-29 14:30',
      deadline: '2026-08-30 18:00',
      slaHoursTotal: 28,
      slaHoursRemaining: 3,
      escalationLevel: 2,
      escalationStageName: 'Department Head (Level 2)',
      status: 'IN_PROGRESS',
      beforeEvidenceUrl: 'https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?auto=format&fit=crop&w=800&q=80'
    },
    history: [
      { id: 'h-21', timestamp: '2026-08-29 14:00', action: 'Telemetry Alert Triggered', performedBy: 'IoT Stream', role: 'Sensors' },
      { id: 'h-22', timestamp: '2026-08-29 14:30', action: 'Action Assigned', performedBy: 'S. N. Mishra', role: 'Mine Manager' }
    ]
  },
  {
    id: 'issue-2035',
    issueCode: 'ISSUE-2026-2035',
    title: 'Contractor ABC Mining Services: 18 dump truck operators lacking mandatory VTC refresher',
    description: 'Labour compliance audit revealed 18 outsourced heavy earthmoving machinery operators operating in Bench 4 without valid Vocational Training Centre (VTC) annual safety refresher certification.',
    category: 'Contractor Compliance',
    severity: 'High',
    riskScore: 74,
    confidence: 98,
    mineId: 'mine-gevra',
    mineName: 'Gevra Mega Open Cast Mine',
    location: 'Bench 4 Excavation & Contractor Dispatch Gate',
    reportedBy: 'Sunil Verma (Labour Enforcement Inspector)',
    reportedDate: '2026-08-28 11:20',
    deadline: '2026-09-01 17:00',
    status: 'IN_PROGRESS',
    isCritical: false,
    isRecurring: false,
    assignedDepartment: 'Human Resources & Contractor Governance',
    assignedOfficer: 'M. K. Tripathi',
    aiExplanation: {
      whySeverity: [
        'Direct breach of Mines Vocational Training Rules 1966 Section 6',
        'Uncertified heavy equipment operators operating 100-ton rear dumpers in steep incline benches',
        'Contractor compliance score degraded to 68%'
      ],
      riskFactors: [
        { factor: 'Statutory VTC certification lapse (+30)', points: 30 },
        { factor: 'Critical heavy machinery operation (+28)', points: 28 },
        { factor: 'Contractor repeat compliance deficit (+16)', points: 16 }
      ],
      historicalContext: 'ABC Mining Services received 2 previous notices regarding delayed submission of Form B labour registers and VTC records.'
    },
    evidences: [
      { id: 'ev-3', type: 'document', url: '#', caption: 'Form B Audit Summary & Operator Registry Extract', timestamp: '2026-08-28 11:25' }
    ],
    correctiveAction: {
      id: 'ca-2035',
      issueId: 'issue-2035',
      title: 'Conduct accelerated 2-day VTC batch and ground uncertified operators',
      actionPlan: 'Immediately de-roster 18 uncertified operators. Schedule priority batch at SECL Korba Area VTC on Aug 30-31.',
      recommendedByAI: true,
      assignedOfficer: 'M. K. Tripathi',
      officerRole: 'Contractor Cell Manager',
      department: 'HR & VTC Administration',
      assignedDate: '2026-08-28 12:00',
      deadline: '2026-09-01 17:00',
      slaHoursTotal: 77,
      slaHoursRemaining: 48,
      escalationLevel: 1,
      escalationStageName: 'Assigned Officer (Level 1)',
      status: 'IN_PROGRESS',
      beforeEvidenceUrl: 'https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=800&q=80'
    },
    history: [
      { id: 'h-31', timestamp: '2026-08-28 11:20', action: 'Audit Logged', performedBy: 'Sunil Verma', role: 'Labour Inspector' }
    ]
  }
];

export const INITIAL_STATUTORY_RULES: StatutoryComplianceRule[] = [
  {
    id: 'rule-1',
    ruleCode: 'CMR-2017-R104',
    title: 'Protective Fencing & Guarding of Machinery & Conveyors',
    regulationBody: 'Coal Mines Regulations 2017',
    sectionRef: 'Regulation 104(1)(b) & (2)',
    mineId: 'mine-gevra',
    mineName: 'Gevra Mega Open Cast Mine',
    subsidiary: 'SECL',
    department: 'Safety & Mechanical',
    responsibleOfficer: 'Rajesh Kumar',
    dueDate: '2026-09-05',
    status: 'Non-Compliant',
    riskLevel: 'Critical',
    penaltyRisk: 'Statutory Work Stop Notice under Mines Act Section 22(3)',
    documentRef: 'DGMS/Tech/Circular/2021/04',
    lastAuditedDate: '2026-08-30'
  },
  {
    id: 'rule-2',
    ruleCode: 'MOEFCC-EC-2022-GEV',
    title: 'Half-Yearly Environmental Clearance (EC) Compliance Report & Ambient Monitoring',
    regulationBody: 'MoEFCC',
    sectionRef: 'EIA Notification 2006 / Condition VI(a)',
    mineId: 'mine-gevra',
    mineName: 'Gevra Mega Open Cast Mine',
    subsidiary: 'SECL',
    department: 'Environment',
    responsibleOfficer: 'Dr. Anita Banerjee',
    dueDate: '2026-09-15',
    status: 'Due Soon',
    riskLevel: 'High',
    penaltyRisk: 'Environmental Compensation Levy & EC revocation warning',
    documentRef: 'EC-J-11015/34/2021-IA.II(M)',
    lastAuditedDate: '2026-08-15'
  },
  {
    id: 'rule-3',
    ruleCode: 'MINES-ACT-1952-S23',
    title: 'Statutory Notice of Accidents and Dangerous Occurrences (Form IV-A)',
    regulationBody: 'Mines Act 1952',
    sectionRef: 'Section 23 & Regulation 8',
    mineId: 'mine-gevra',
    mineName: 'Gevra Mega Open Cast Mine',
    subsidiary: 'SECL',
    department: 'Safety Administration',
    responsibleOfficer: 'S. N. Mishra',
    dueDate: '2026-09-02',
    status: 'Compliant',
    riskLevel: 'Medium',
    penaltyRisk: 'Prosecution under Section 66 of Mines Act',
    documentRef: 'DGMS-FORM-IVA-2026',
    lastAuditedDate: '2026-08-25'
  },
  {
    id: 'rule-4',
    ruleCode: 'CLRA-1970-R75',
    title: 'Maintenance of Contractor Form B Register & Equal Remuneration Verification',
    regulationBody: 'Contract Labour Act',
    sectionRef: 'Section 12 & Rule 75',
    mineId: 'mine-gevra',
    mineName: 'Gevra Mega Open Cast Mine',
    subsidiary: 'SECL',
    department: 'Human Resources & Contractor Cell',
    responsibleOfficer: 'M. K. Tripathi',
    dueDate: '2026-09-10',
    status: 'Due Soon',
    riskLevel: 'Medium',
    penaltyRisk: 'Cancellation of Labour License / Section 23 penalties',
    documentRef: 'CLC-CENTRAL-REG-2025',
    lastAuditedDate: '2026-08-28'
  },
  {
    id: 'rule-5',
    ruleCode: 'CMR-2017-R153',
    title: 'Underground Methane Gas Drainage & Continuous Telemetric Monitoring',
    regulationBody: 'Coal Mines Regulations 2017',
    sectionRef: 'Regulation 153 & DGMS Gassy Mine Degree-III Standard',
    mineId: 'mine-moonidih',
    mineName: 'Moonidih Underground Mine',
    subsidiary: 'BCCL',
    department: 'Underground Safety',
    responsibleOfficer: 'T. K. Chatterjee',
    dueDate: '2026-08-30',
    status: 'Overdue',
    riskLevel: 'Critical',
    penaltyRisk: 'Immediate prohibition of underground shift work',
    documentRef: 'DGMS/EZ/DHN/2026/089',
    lastAuditedDate: '2026-08-29'
  }
];

export const INITIAL_CONTRACTORS: Contractor[] = [
  {
    id: 'cont-1',
    name: 'ABC Mining Services Pvt Ltd',
    serviceType: 'Overburden Excavation',
    mineId: 'mine-gevra',
    mineName: 'Gevra Mega Open Cast Mine',
    subsidiary: 'SECL',
    activeWorkers: 420,
    complianceScore: 68,
    riskScore: 74,
    openViolations: 3,
    expiredCertifications: 2,
    safetyTrainingScore: 71,
    auditRecommendation: 'Prioritize comprehensive contractor safety & labour audit within 7 days.',
    stats: { totalDeployed: 420, trainedVTC: 382, medicalFitPME: 410, safetyIndex: 68 },
    status: 'High Risk'
  },
  {
    id: 'cont-2',
    name: 'CoalTrans Logistics India Corp',
    serviceType: 'Coal Transportation',
    mineId: 'mine-gevra',
    mineName: 'Gevra Mega Open Cast Mine',
    subsidiary: 'SECL',
    activeWorkers: 280,
    complianceScore: 92,
    riskScore: 32,
    openViolations: 0,
    expiredCertifications: 0,
    safetyTrainingScore: 95,
    auditRecommendation: 'Benchmark contractor maintaining full fleet telematics & speed limiter compliance.',
    stats: { totalDeployed: 280, trainedVTC: 280, medicalFitPME: 278, safetyIndex: 94 },
    status: 'Approved'
  },
  {
    id: 'cont-3',
    name: 'Apex Drillers & Blasting Specialists',
    serviceType: 'Drilling & Blasting',
    mineId: 'mine-gevra',
    mineName: 'Gevra Mega Open Cast Mine',
    subsidiary: 'SECL',
    activeWorkers: 95,
    complianceScore: 84,
    riskScore: 56,
    openViolations: 1,
    expiredCertifications: 1,
    safetyTrainingScore: 88,
    auditRecommendation: 'Verify statutory explosive van driver PESO license renewal.',
    stats: { totalDeployed: 95, trainedVTC: 92, medicalFitPME: 94, safetyIndex: 85 },
    status: 'Review Required'
  },
  {
    id: 'cont-4',
    name: 'InfraCoal Heavy Earthmovers Ltd',
    serviceType: 'Equipment Maintenance',
    mineId: 'mine-kusmunda',
    mineName: 'Kusmunda Open Cast Project',
    subsidiary: 'SECL',
    activeWorkers: 310,
    complianceScore: 89,
    riskScore: 42,
    openViolations: 1,
    expiredCertifications: 0,
    safetyTrainingScore: 90,
    auditRecommendation: 'Routine quarterly audit schedule on track.',
    stats: { totalDeployed: 310, trainedVTC: 304, medicalFitPME: 308, safetyIndex: 89 },
    status: 'Approved'
  }
];

export const INITIAL_DOCUMENTS: DocumentRecord[] = [
  {
    id: 'doc-1',
    documentNo: 'EC/MOEFCC/J-11015/34/2021',
    title: 'MoEFCC Environmental Clearance (70 MTPA Expansion)',
    type: 'Environmental Clearance',
    mineId: 'mine-gevra',
    mineName: 'Gevra Mega Open Cast Mine',
    authority: 'Ministry of Environment, Forest and Climate Change (MoEFCC)',
    issueDate: '2021-09-15',
    expiryDate: '2026-09-15',
    daysToExpiry: 16,
    status: 'Expiring Soon',
    fileSize: '4.8 MB',
    extractedClauses: [
      'Condition A(iii): Continuous ambient air quality monitoring stations (CAAQMS) with real-time CPCB server link.',
      'Condition B(viii): Minimum 33% total lease area under progressive afforestation canopy.',
      'Condition C(iv): 100% recycling of treated workshop effluent with zero liquid discharge into Lilagar River.'
    ],
    missingFields: ['Afforestation satellite survival audit certificate 2026'],
    aiActionRecommendation: 'Start EC renewal and compliance submission workflow immediately (16 days remaining).'
  },
  {
    id: 'doc-2',
    documentNo: 'DGMS/EZ/PERMIT/2024/77',
    title: 'DGMS Mechanised Surface Mining Operational Permit',
    type: 'DGMS Safety Certificate',
    mineId: 'mine-gevra',
    mineName: 'Gevra Mega Open Cast Mine',
    authority: 'Directorate General of Mines Safety (DGMS)',
    issueDate: '2024-03-10',
    expiryDate: '2027-03-09',
    daysToExpiry: 191,
    status: 'Valid',
    fileSize: '2.4 MB',
    extractedClauses: [
      'Maximum bench height 15m; overall slope angle not to exceed 28 degrees.',
      'Mandatory proximity warning devices on all 240-ton dumpers.'
    ]
  },
  {
    id: 'doc-3',
    documentNo: 'PESO/EXPLOSIVE/MAG/2025/308',
    title: 'Bulk Explosive Storage & Magazine License',
    type: 'Blasting Permit',
    mineId: 'mine-gevra',
    mineName: 'Gevra Mega Open Cast Mine',
    authority: 'Petroleum and Explosives Safety Organization (PESO)',
    issueDate: '2025-05-12',
    expiryDate: '2026-09-08',
    daysToExpiry: 9,
    status: 'Expiring Soon',
    fileSize: '1.9 MB',
    extractedClauses: [
      'Approved storage capacity: 150 MT Site Mixed Slurry (SMS) matrix and 25,000 electric detonators.',
      '24/7 CCTV surveillance perimeter with armed CISF post.'
    ],
    missingFields: ['Lightning conductor annual calibration test certificate'],
    aiActionRecommendation: 'Critical statutory permit expiring in 9 days. Submit renewal docket to PESO Nagpur.'
  }
];

export const INITIAL_AUDIT_LOGS: AuditBlock[] = [
  {
    blockNumber: 1042,
    timestamp: '2026-08-30 09:20:15',
    user: 'S. N. Mishra',
    role: 'Mine Manager',
    action: 'DISPATCH_ASSIGNMENT',
    module: 'Issues & Corrective Actions',
    mine: 'Gevra Mega Open Cast Mine',
    details: 'Assigned Corrective Action #CA-2041 to Officer Rajesh Kumar (Safety Dept) following AI recommendation.',
    previousState: 'OPEN',
    newState: 'ASSIGNED',
    blockHash: '0x8f4d92a1c7e530b84f2910d5e3c8b1a9f0e2d4c6b8a07153e9c2b4a6f8e0d2c4',
    previousHash: '0x3a9b1c7d5e8f204681a90c2e4f6a8b0d1e3c5a7f9b0d2e4c6a8f0b2d4e6a8c0',
    ipAddress: '10.14.88.24 (SECL Intranet)',
    verified: true
  },
  {
    blockNumber: 1041,
    timestamp: '2026-08-30 09:16:42',
    user: 'MineGuard AI Engine',
    role: 'AI Autonomous System',
    action: 'AI_CLASSIFICATION_INFERENCE',
    module: 'Inspections & Risk Analytics',
    mine: 'Gevra Mega Open Cast Mine',
    details: 'Completed neural inspection scan for #INSP-2026-1049. Risk: 92/100 (Critical). Root cause: Missing conveyor guard.',
    previousState: 'RAW_SUBMISSION',
    newState: 'AI_CLASSIFIED',
    blockHash: '0x3a9b1c7d5e8f204681a90c2e4f6a8b0d1e3c5a7f9b0d2e4c6a8f0b2d4e6a8c0',
    previousHash: '0x1c8e4f20a7b9d6c4e0f8a2b5d7c9e1f3a5b7d9f1c3e5a7b9d1f3e5a7c9b1d3f5',
    ipAddress: '10.0.4.102 (AI Cluster Node 2)',
    verified: true
  },
  {
    blockNumber: 1040,
    timestamp: '2026-08-30 09:15:08',
    user: 'Vikramaditya Rao',
    role: 'Field Inspector',
    action: 'SUBMIT_INSPECTION',
    module: 'AI Field Inspection',
    mine: 'Gevra Mega Open Cast Mine',
    details: 'Logged mobile field inspection #INSP-2026-1049 at Conveyor Line 4B with geo-tag (22.3392, 82.6081) and audio transcript.',
    previousState: 'DRAFT_LOCAL',
    newState: 'OPEN',
    blockHash: '0x1c8e4f20a7b9d6c4e0f8a2b5d7c9e1f3a5b7d9f1c3e5a7b9d1f3e5a7c9b1d3f5',
    previousHash: '0x7e2d9a4b1c8f0e3d5a7b9c1e3f5a7d9b1c3e5f7a9b1d3e5f7a9c1e3b5d7f9a1',
    ipAddress: '192.168.43.51 (Mobile 5G)',
    verified: true
  }
];

export const INITIAL_NOTIFICATIONS: AppNotification[] = [
  {
    id: 'notif-1',
    title: 'CRITICAL SAFETY HAZARD DETECTED',
    message: 'Missing conveyor safety barrier at Gevra Zone 4 requires urgent mitigation (18h SLA remaining).',
    severity: 'Critical',
    type: 'safety',
    timestamp: '10 minutes ago',
    read: false,
    mineId: 'mine-gevra',
    issueId: 'issue-2041'
  },
  {
    id: 'notif-2',
    title: 'STATUTORY PERMIT EXPIRING',
    message: 'PESO Bulk Explosive Storage License for Gevra Mine expires in 9 days.',
    severity: 'High',
    type: 'document',
    timestamp: '1 hour ago',
    read: false,
    mineId: 'mine-gevra'
  },
  {
    id: 'notif-3',
    title: 'AI PREDICTIVE RISK ALERT',
    message: 'Mine Moonidih has 78% predicted probability of safety non-compliance in next 14 days.',
    severity: 'Critical',
    type: 'ai_prediction',
    timestamp: '3 hours ago',
    read: false,
    mineId: 'mine-moonidih'
  },
  {
    id: 'notif-4',
    title: 'SLA ESCALATION WARNING',
    message: 'Ambient PM10 dust mitigation action escalated to Level 2 (Department Head).',
    severity: 'Medium',
    type: 'escalation',
    timestamp: '5 hours ago',
    read: true,
    mineId: 'mine-gevra',
    issueId: 'issue-2038'
  }
];

export const ENVIRONMENTAL_TELEMETRY: EnvironmentalSensorData = {
  pm25: 68.4,
  pm10: 142.8,
  so2: 24.1,
  nox: 38.6,
  waterPh: 7.2,
  noiseDb: 74.5,
  dustStatus: 'Above Permissible Threshold',
  waterStatus: 'Compliant',
  airAqi: 184,
  timestamp: '2026-08-30 09:25:00',
  mineId: 'mine-gevra'
};

export const PRODUCTION_RECORDS: ProductionMetric[] = [
  { date: '2026-08-24', coalTargetTons: 145000, coalActualTons: 146200, obTargetBCM: 280000, obActualBCM: 282100, equipmentAvailabilityPct: 88, downtimeHours: 1.2, anomalyDetected: false },
  { date: '2026-08-25', coalTargetTons: 145000, coalActualTons: 144800, obTargetBCM: 280000, obActualBCM: 279500, equipmentAvailabilityPct: 87, downtimeHours: 1.5, anomalyDetected: false },
  { date: '2026-08-26', coalTargetTons: 145000, coalActualTons: 141200, obTargetBCM: 280000, obActualBCM: 274000, equipmentAvailabilityPct: 84, downtimeHours: 2.8, anomalyDetected: false },
  { date: '2026-08-27', coalTargetTons: 145000, coalActualTons: 139500, obTargetBCM: 280000, obActualBCM: 268000, equipmentAvailabilityPct: 81, downtimeHours: 4.1, anomalyDetected: false },
  { date: '2026-08-28', coalTargetTons: 145000, coalActualTons: 124700, obTargetBCM: 280000, obActualBCM: 238000, equipmentAvailabilityPct: 72, downtimeHours: 7.6, anomalyDetected: true, anomalyReason: 'Production decreased 14.0% below target due to shovel #08 hydraulic motor failure and contractor driver shortage.' },
  { date: '2026-08-29', coalTargetTons: 145000, coalActualTons: 138500, obTargetBCM: 280000, obActualBCM: 271000, equipmentAvailabilityPct: 85, downtimeHours: 2.1, anomalyDetected: false },
  { date: '2026-08-30', coalTargetTons: 145000, coalActualTons: 140200, obTargetBCM: 280000, obActualBCM: 275400, equipmentAvailabilityPct: 86, downtimeHours: 1.8, anomalyDetected: false }
];

export const STATUTORY_COMPLIANCE_RULES = INITIAL_STATUTORY_RULES;
