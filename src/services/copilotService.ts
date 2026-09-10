import { CopilotMessage, Mine, Issue, StatutoryComplianceRule } from '../types';

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
        content: `**3 खदानों पर तत्काल ध्यान देने की आवश्यकता है:**\n\n1. **${highRiskMines[0]?.name || 'Moonidih Mine'}** — जोखिम स्कोर: **${highRiskMines[0]?.riskScore || 81}/100** (गंभीर)\n2. **${highRiskMines[1]?.name || 'Rajmahal Open Cast'}** — जोखिम स्कोर: **${highRiskMines[1]?.riskScore || 74}/100** (उच्च)\n3. **${highRiskMines[2]?.name || 'Gevra Mega Mine'}** — जोखिम स्कोर: **${highRiskMines[2]?.riskScore || 61}/100** (सतर्कता)\n\n**सिफारिश:** बार-बार सुरक्षा उल्लंघनों के कारण ${highRiskMines[0]?.name || 'Moonidih खदान'} को सर्वोच्च प्राथमिकता दें।`,
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
      content: `**3 mines require immediate governance attention:**\n\n1. **${highRiskMines[0]?.name || 'Moonidih Underground Mine'}** — Risk Score: **${highRiskMines[0]?.riskScore || 81}/100** (CRITICAL)\n2. **${highRiskMines[1]?.name || 'Rajmahal Open Cast'}** — Risk Score: **${highRiskMines[1]?.riskScore || 74}/100** (HIGH)\n3. **${highRiskMines[2]?.name || 'Gevra Mega Open Cast'}** — Risk Score: **${highRiskMines[2]?.riskScore || 61}/100** (ALERT)\n\n**Recommended priority:** Moonidih due to underground methane drainage deficits and overdue DGMS compliance actions.`,
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
