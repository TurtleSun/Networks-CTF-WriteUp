# Network Security CTF Writeup
### EC521 Challenge Solutions by Michelle Sun

This repository documents my journey through various network security challenges, providing detailed solutions, analysis, and implementation scripts. Each challenge tested different aspects of network security, from packet analysis to timing attacks.

## Structure

- **WriteUps/**  
 Comprehensive markdown documentation for each challenge, including:
 - Detailed methodology
 - Technical analysis
 - Solution walkthrough
 - Lessons learned

- **Scripts/**  
 Implementation code used to solve the challenges:
 - Python scripts
 - Shell utilities
 - Helper functions

- **Media/**  
 Supporting visual documentation:
 - Wireshark captures
 - Network diagrams
 - Result screenshots

- **CTF/**
 Challenge files that don't require SSH connection:
 - challenge1.pcap - Packet capture for "Secret on the Wire"

## Challenges Overview

### 1. Secret on the Wire
**Skills: Packet Analysis, Wireshark**
- Analyzed network traffic to locate hidden flag
- Utilized Wireshark for deep packet inspection
- Extracted payload data from specific packets

### 2. Weather Forecast
**Skills: Network Monitoring, SSH**
- Intercepted weather service broadcasts
- Performed port-specific traffic analysis
- Extracted flag from encrypted SSH stream

### 3. Key Server
**Skills: Network Pattern Analysis, Cryptography**
- Implemented tcpdump-based monitoring
- Analyzed encryption patterns
- Developed automated flag extraction tool

### 4. Password Server
**Skills: Timing Analysis, Pattern Recognition**
- Exploited server response timing variations
- Developed adaptive password guessing algorithm
- Implemented efficient pattern recognition system

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/mlxs/Networks-CTF-WriteUp.git
cd Networks-CTF-WriteUp
```

2. Dependencies:
- Python 3.x
- Built-in Python libraries:
 - `telnetlib` - for Telnet connections
 - `time` - for timing operations
 - `socket` - for network connections
- Network access to target server (ec521network:1234)

3. Navigate to individual challenge documentation:
```bash
cd WriteUps/
```

### NOTICE:
This repository contains solutions for the EC521 Networks CTF challenges and is intended for educational purposes. The original challenges are not publicly available.