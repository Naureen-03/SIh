with open("src/pages/DashboardPage.tsx", "r", encoding="utf-8") as f:
    c = f.read()

c = c.replace("import { COMPLIANCE_TREND_DATA, CATEGORY_BREAKDOWN_DATA } from '../data/mockData';", """
const COMPLIANCE_TREND_DATA = [
  { month: 'Apr 2026', actual: 79, target: 95 },
  { month: 'May 2026', actual: 81, target: 95 },
  { month: 'Jun 2026', actual: 83, target: 95 },
  { month: 'Jul 2026', actual: 84, target: 95 },
  { month: 'Aug 2026', actual: 87, target: 95 },
  { month: 'Sep 2026', actual: 88, target: 95 },
];

const CATEGORY_BREAKDOWN_DATA = [
  { category: 'Safety', count: 52, color: '#B91C1C' },
  { category: 'Environment', count: 31, color: '#D97706' },
  { category: 'Labour', count: 24, color: '#1D4E89' },
  { category: 'Operational', count: 18, color: '#475569' },
];
""")

with open("src/pages/DashboardPage.tsx", "w", encoding="utf-8") as f:
    f.write(c)

print("DashboardPage.tsx trend data updated!")
