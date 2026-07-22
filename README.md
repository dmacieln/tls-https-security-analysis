# TLS & HTTPS Security Analysis

## Overview

This project explores the core concepts of Transport Layer Security (TLS) and HTTPS by implementing and analyzing secure communication protocols using Python, OpenSSL, Wireshark, and Kali Linux. It demonstrates TLS handshakes, certificate validation, hostname verification, HTTPS communication, TLS server implementation, Subject Alternative Name (SAN) certificates, browser certificate trust, and HTTPS man-in-the-middle (MITM) proxy simulation.

---

## Features

- TLS handshake analysis
- Certificate Authority (CA) validation
- Hostname verification
- HTTPS request and response testing
- TLS server implementation
- Browser certificate trust configuration
- Subject Alternative Name (SAN) certificate deployment
- HTTPS MITM proxy simulation
- Network traffic analysis using Wireshark

---

## Technologies Used

- Python
- OpenSSL
- Wireshark
- Kali Linux
- HTTPS
- TLS 1.3
- X.509 Certificates
- Linux Terminal

---

## Project Structure

```text
tls-https-security-analysis/
├── handshake.py
├── server.py
├── httpsproxy.py
├── server_openssl.cnf
├── TLS-HTTPS-Security-Analysis.pdf
├── README.md
└── LICENSE
```

---

## TLS Handshake & Certificate Analysis

Established a secure TLS connection to a remote server and analyzed the complete handshake process using Wireshark. Examined the negotiated TLS version, cipher suite, certificate chain, and TCP/TLS packet exchange to understand how secure communication is established.

---

## Certificate Authority Validation

Configured a custom certificate directory and manually trusted the required Certificate Authorities. Verified successful TLS connections after importing and hashing the appropriate CA certificates using OpenSSL.

---

## Hostname Verification Analysis

Demonstrated how hostname verification protects clients from accepting certificates issued to different domains. Tested successful and failed TLS connections by enabling and disabling hostname verification.

---

## HTTPS Request & Response Testing

Extended the TLS client to send HTTPS GET requests and receive encrypted responses from a remote web server. Retrieved both web content and binary image data to verify successful encrypted communication.

---

## TLS Server Implementation

Developed a custom Python TLS server using self-generated certificates. Configured secure client-server communication and validated encrypted HTTP requests between the client and server.

---

## Browser-Based TLS Validation

Imported a custom Certificate Authority into Firefox to establish browser trust. Verified successful HTTPS communication between the browser and the custom TLS server while capturing the encrypted traffic using Wireshark.

---

## SAN Certificate Deployment

Created and deployed X.509 certificates containing multiple Subject Alternative Names (SANs). Configured OpenSSL to support multiple DNS entries and verified secure HTTPS connections using the updated certificates.

---

## HTTPS MITM Proxy Simulation

Implemented an HTTPS man-in-the-middle proxy using forged certificates signed by a trusted Certificate Authority. Demonstrated how trusted certificates can intercept encrypted HTTPS traffic when a client accepts a malicious CA.

---

## What I Learned

This project provided practical experience implementing and analyzing TLS and HTTPS security mechanisms. I gained a deeper understanding of certificate validation, hostname verification, secure client-server communication, TLS server deployment, browser trust stores, SAN certificates, and HTTPS interception techniques. These exercises reinforced how TLS protects confidentiality, authentication, and data integrity in modern web communications.

---

## Documentation

A detailed project report containing implementation details, screenshots, methodology, and analysis is included in this repository.

**TLS-HTTPS-Security-Analysis.pdf**

---

## Future Improvements

- Support additional TLS versions and cipher suites
- Automate certificate generation using Bash scripts
- Implement mutual TLS (mTLS) authentication
- Add certificate revocation checking
- Expand the HTTPS proxy with request logging and filtering

---

## Author

**Diego Maciel Nava**
