# Network Challenge 3: Key Server

During this challenge, we needed to locate a flag stored on the ec521network server at port 5678. The challenge prompt identified this as a secure key server, suggesting encryption would be involved in accessing the flag. We were also informed this was specifically a TCP port.

## Initial Reconnaissance
To gather initial intelligence, I performed packet capture on the specified port using tcpdump:

```bash
tcpdump -i any 'port 5678 and host ec521network' -w capture.pcap
```

After collecting data for approximately 30 minutes, I analyzed the TCP payloads:

```bash
tcpdump -r capture.pcap -X tcp
```

## Pattern Discovery
The packet analysis revealed something interesting - clear text packets containing what appeared to be username and password combinations:

![Packet Payload Analysis](Media/challenge3_packetPayload.png)

Further investigation showed multiple instances of packets with different usernames but identical passwords. This pattern suggested a relationship between usernames and server responses.

## Testing the Hypothesis
Given that I was accessing the CTF environment through an SSH connection authenticated with my username, I attempted to connect to the server using my credentials. This resulted in receiving an encrypted key:

![Encrypted Key Response](Media/challenge3_encryptedKey.png)

## Decryption Analysis
The encrypted key's characteristics - particularly its non-alphabetic nature - pointed toward either a shifting cipher (like Caesar) or a stream cipher (like XOR). After testing these encryption algorithms, I discovered the key became readable when XORed with my username.

I implemented a Python script to perform the XOR decryption:

![XOR Decryption Script](Scripts/XOR.py)

The decryption successfully revealed the flag:

![Decrypted Flag](Media/challenge3_flagFound.png)

## Key Insights
- Packet analysis revealed patterns in server responses
- Username correlation with encrypted keys suggested a personalized encryption scheme
- XOR encryption using the username as the key proved to be the solution
