# TLS & HTTPS Security Analysis

## Overview

This project explores the implementation and analysis of Transport Layer Security (TLS) and HTTPS using Python, OpenSSL, Wireshark, and Kali Linux. It demonstrates secure client-server communication through TLS handshakes, certificate validation, hostname verification, browser trust configuration, Subject Alternative Name (SAN) certificates, and HTTPS man-in-the-middle (MITM) proxy simulation. These exercises provide practical experience with the technologies that secure modern web communications.

---

## Skills Demonstrated

- TLS 1.3 Handshake Analysis
- HTTPS Communication
- Certificate Authority (CA) Validation
- Hostname Verification
- TLS Server Development
- X.509 Certificate Management
- Subject Alternative Name (SAN) Certificates
- Browser Certificate Trust
- HTTPS MITM Proxy Simulation
- OpenSSL Certificate Generation
- Network Traffic Analysis
- Docker-Based Lab Environment

---

## Technologies Used

- Python
- OpenSSL
- Wireshark
- Kali Linux
- Docker
- TLS 1.3
- HTTPS
- X.509 Certificates
- Linux Terminal

---

## Repository Structure

```text
tls-https-security-analysis/
│
├── README.md
├── LICENSE
├── TLS-HTTPS-Security-Analysis.pdf
├── docker-compose.yml
└── volumes/
    ├── handshake.py
    ├── server.py
    ├── httpsproxy.py
    ├── server_openssl.cnf
    ├── myopenssl.cnf
    ├── client-certs/
    ├── server-certs/
    ├── demoCA/
    ├── example.crt
    ├── example.csr
    ├── example.key
    ├── newserver.crt
    ├── newserver.csr
    ├── newserver.key
    ├── practice.crt
    ├── practice.csr
    └── practice.key
```

---

## Repository Layout

The project was developed inside a Docker-based cybersecurity lab environment. The `volumes/` directory mirrors the shared Docker volume used by the client and server containers and contains the Python source code, certificate files, OpenSSL configurations, and supporting resources required to reproduce the TLS experiments.

---

## Project Components

### TLS Handshake & Certificate Analysis

Established a secure TLS connection to a remote server and analyzed the complete TLS handshake using Wireshark. Examined TCP connection establishment, TLS negotiation, certificate exchange, and cipher suite selection to understand how encrypted communication is established.

---

### Certificate Authority Validation

Configured a custom certificate directory and manually imported trusted Certificate Authorities. Verified secure TLS communication after validating and hashing CA certificates using OpenSSL.

---

### Hostname Verification Analysis

Demonstrated how hostname verification protects clients from accepting certificates issued for different domains. Tested successful and failed TLS connections by enabling and disabling hostname verification.

---

### HTTPS Request & Response Testing

Extended the TLS client to send HTTPS GET requests and receive encrypted responses from remote web servers. Retrieved both web pages and binary image data over encrypted HTTPS connections.

---

### TLS Server Implementation

Developed a Python-based TLS server using self-generated certificates and configured secure client-server communication through encrypted HTTPS requests.

---

### Browser-Based TLS Validation

Configured Firefox to trust a custom Certificate Authority and successfully established HTTPS communication with the custom TLS server while monitoring encrypted traffic using Wireshark.

---

### SAN Certificate Deployment

Generated X.509 certificates containing multiple Subject Alternative Names (SANs) using OpenSSL and verified successful HTTPS communication across multiple hostnames.

---

### HTTPS MITM Proxy Simulation

Implemented an HTTPS man-in-the-middle proxy using forged certificates signed by a trusted Certificate Authority to demonstrate how trusted certificates can be abused to intercept encrypted HTTPS traffic.

---

## What I Learned

This project provided practical experience implementing and analyzing TLS and HTTPS security mechanisms using Python, OpenSSL, Docker, and Wireshark. I gained a deeper understanding of certificate authorities, hostname verification, browser trust stores, TLS handshakes, SAN certificates, HTTPS communication, and encrypted traffic interception. These exercises reinforced how TLS provides confidentiality, authentication, and data integrity in modern network security.

---

## Documentation

A detailed report containing implementation steps, screenshots, configurations, and analysis is included in this repository.

**TLS-HTTPS-Security-Analysis.pdf**

---

## Future Improvements

- Implement Mutual TLS (mTLS) authentication
- Support additional TLS versions and cipher suites
- Automate certificate generation using Bash scripts
- Implement certificate revocation checking
- Expand the HTTPS proxy with request inspection and filtering
- Add automated testing for TLS connections

---

## Author

**Diego Maciel Nava**
