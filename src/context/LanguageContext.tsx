import React, { createContext, useContext, useState } from 'react';

type Language = 'en' | 'hi';

interface LanguageContextType {
  language: Language;
  setLanguage: (lang: Language) => void;
  t: (key: string) => string;
}

const TRANSLATIONS: Record<string, Record<Language, string>> = {
  appName: { en: 'MINEGUARD AI', hi: 'माइनगार्ड एआई' },
  tagline: { en: 'AI-Based Smart Governance & Compliance Monitoring System', hi: 'कोयला खदानों हेतु एआई-आधारित स्मार्ट गवर्नेंस एवं अनुपालन निगरानी प्रणाली' },
  orgTitle: { en: 'Ministry of Coal • Coal India Limited', hi: 'कोयला मंत्रालय • कोल इंडिया लिमिटेड' },
  goodMorning: { en: 'Good Morning', hi: 'सुप्रभात' },
  mineLocation: { en: 'Korba Mining Area', hi: 'कोरबा खनन क्षेत्र' },
  lastSync: { en: 'Last synchronized: 2 mins ago', hi: 'अंतिम समन्वयन: 2 मिनट पहले' },
  totalMines: { en: 'Total Mines', hi: 'कुल खदानें' },
  overallCompliance: { en: 'Overall Compliance', hi: 'समग्र अनुपालन' },
  openIssues: { en: 'Open Issues', hi: 'खुले मुद्दे' },
  criticalIssues: { en: 'Critical Issues', hi: 'गंभीर मुद्दे' },
  overdueActions: { en: 'Overdue Actions', hi: 'बकाया कार्रवाइयां' },
  inspectionsThisMonth: { en: 'Inspections This Month', hi: 'इस माह के निरीक्षण' },
  predictedRisks: { en: 'AI Predicted Risks', hi: 'एआई अनुमानित जोखिम' },
  pendingApprovals: { en: 'Pending Approvals', hi: 'लंबित स्वीकृतियां' },
  startInspection: { en: 'Start Field Inspection', hi: 'फील्ड निरीक्षण शुरू करें' },
  exploreDashboard: { en: 'Explore Dashboard', hi: 'डैशबोर्ड देखें' },
  talkToAI: { en: 'Talk to MineGuard AI', hi: 'माइनगार्ड एआई से बात करें' },
  closedLoopTitle: { en: 'Closed-Loop AI Governance', hi: 'क्लोज्ड-लूप एआई गवर्नेंस' },
  detect: { en: 'DETECT', hi: 'पहचानें' },
  classify: { en: 'CLASSIFY', hi: 'वर्गीकृत करें' },
  prioritize: { en: 'PRIORITIZE', hi: 'प्राथमिकता दें' },
  assign: { en: 'ASSIGN', hi: 'सौंपें' },
  resolve: { en: 'RESOLVE', hi: 'समाधान करें' },
  verify: { en: 'VERIFY', hi: 'सत्यापित करें' },
  learn: { en: 'LEARN', hi: 'सीखें' }
};

const LanguageContext = createContext<LanguageContextType | undefined>(undefined);

export const LanguageProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [language, setLanguage] = useState<Language>('en');

  const t = (key: string): string => {
    if (TRANSLATIONS[key] && TRANSLATIONS[key][language]) {
      return TRANSLATIONS[key][language];
    }
    return key;
  };

  return (
    <LanguageContext.Provider value={{ language, setLanguage, t }}>
      {children}
    </LanguageContext.Provider>
  );
};

export const useLanguage = () => {
  const ctx = useContext(LanguageContext);
  if (!ctx) throw new Error('useLanguage must be used within LanguageProvider');
  return ctx;
};
