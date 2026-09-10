import React, { createContext, useContext, useState, useEffect } from 'react';
import { User, UserRole } from '../types';

interface AuthContextType {
  currentUser: User;
  switchRole: (role: UserRole) => void;
  availableRoles: { role: UserRole; title: string; desc: string; user: User }[];
}

const USERS: Record<UserRole, User> = {
  MINE_OFFICIAL: {
    id: 'user-mo-1',
    name: 'S. N. Mishra',
    role: 'MINE_OFFICIAL',
    roleTitle: 'General Manager (Korba Mining Area)',
    email: 'sn.mishra@secl.coalindia.in',
    subsidiary: 'SECL',
    mineId: 'mine-gevra',
    mineName: 'Gevra Mega Open Cast Mine',
    department: 'Mine Operations & Management'
  },
  FIELD_INSPECTOR: {
    id: 'user-fi-1',
    name: 'Vikramaditya Rao',
    role: 'FIELD_INSPECTOR',
    roleTitle: 'Senior Field Safety & Compliance Inspector',
    email: 'v.rao@secl.coalindia.in',
    subsidiary: 'SECL',
    mineId: 'mine-gevra',
    mineName: 'Gevra Mega Open Cast Mine',
    department: 'Safety Inspection Cell'
  },
  CORPORATE_OFFICIAL: {
    id: 'user-co-1',
    name: 'Dr. Rameshwar Nath',
    role: 'CORPORATE_OFFICIAL',
    roleTitle: 'Director (Technical & Operations) — Coal India HQ',
    email: 'dir.tech@coalindia.in',
    subsidiary: 'Coal India Limited',
    department: 'Corporate Governance & Risk Monitoring'
  },
  REGULATORY_AUTHORITY: {
    id: 'user-ra-1',
    name: 'Pradeep Kumar Sahoo',
    role: 'REGULATORY_AUTHORITY',
    roleTitle: 'Director General of Mines Safety (DGMS)',
    email: 'pk.sahoo@dgms.gov.in',
    subsidiary: 'Ministry of Coal / DGMS',
    department: 'Directorate General of Mines Safety'
  },
  CONTRACTOR: {
    id: 'user-ct-1',
    name: 'Anil Agarwal',
    role: 'CONTRACTOR',
    roleTitle: 'Managing Director — ABC Mining Services Pvt Ltd',
    email: 'a.agarwal@abcmining.co.in',
    mineId: 'mine-gevra',
    mineName: 'Gevra Mega Open Cast Mine',
    department: 'Contractor Operations'
  },
  ADMIN: {
    id: 'user-ad-1',
    name: 'Harish Chandra',
    role: 'ADMIN',
    roleTitle: 'System Administrator (Ministry of Coal Cloud)',
    email: 'admin.mineguard@nic.in',
    department: 'IT & AI Infrastructure'
  }
};

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [currentUser, setCurrentUser] = useState<User>(() => {
    const saved = localStorage.getItem('mineguard_active_role');
    if (saved && USERS[saved as UserRole]) {
      return USERS[saved as UserRole];
    }
    return USERS.MINE_OFFICIAL;
  });

  const switchRole = (role: UserRole) => {
    if (USERS[role]) {
      setCurrentUser(USERS[role]);
      localStorage.setItem('mineguard_active_role', role);
    }
  };

  const availableRoles = [
    { role: 'MINE_OFFICIAL' as UserRole, title: 'Mine Official', desc: 'Monitor compliance, assign actions, review audits', user: USERS.MINE_OFFICIAL },
    { role: 'FIELD_INSPECTOR' as UserRole, title: 'Field Inspector', desc: 'Mobile-first inspection, GPS, voice, camera', user: USERS.FIELD_INSPECTOR },
    { role: 'CORPORATE_OFFICIAL' as UserRole, title: 'Corporate Official', desc: 'Multi-subsidiary analytics, CIL overview, risk trends', user: USERS.CORPORATE_OFFICIAL },
    { role: 'REGULATORY_AUTHORITY' as UserRole, title: 'Regulatory Authority', desc: 'DGMS/MoEFCC compliance verification, audits', user: USERS.REGULATORY_AUTHORITY },
    { role: 'CONTRACTOR' as UserRole, title: 'Contractor', desc: 'Contractor scorecard, workforce safety, VTC status', user: USERS.CONTRACTOR },
    { role: 'ADMIN' as UserRole, title: 'System Admin', desc: 'Manage users, escalation rules, AI models, settings', user: USERS.ADMIN },
  ];

  return (
    <AuthContext.Provider value={{ currentUser, switchRole, availableRoles }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error('useAuth must be used within AuthProvider');
  return ctx;
};
