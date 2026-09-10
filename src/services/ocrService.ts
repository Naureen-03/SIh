import { DocumentRecord } from '../types';

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
