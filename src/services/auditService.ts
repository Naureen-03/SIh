import { AuditBlock } from '../types';

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
