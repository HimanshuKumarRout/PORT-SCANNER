<div align="center">
  <h1>🔍 Port Scanner</h1>
  <p>
    <strong>A simple Python-based TCP port scanner for discovering open ports on a target host.</strong>
  </p>
  <p>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&amp;logo=python&amp;logoColor=white" />
    <img src="https://img.shields.io/badge/TCP-Port%20Scanner-success?style=for-the-badge" />
    <img src="https://img.shields.io/badge/IPv4%20%26%20IPv6-Supported-blue?style=for-the-badge" />
    <img src="https://img.shields.io/badge/Cybersecurity-Networking-red?style=for-the-badge" />
  </p>
</div>

<br />

## 🌟 Overview

**Port Scanner** is a lightweight Python application that scans a target host for open TCP ports within a specified range.

Built using Python's socket programming capabilities, the scanner supports both **IPv4 and IPv6 addresses**, offers **interactive and command-line execution modes**, and provides detailed scan results along with total scan duration.

This project is ideal for learning networking concepts, cybersecurity fundamentals, and port discovery techniques.

---

## 🚀 Key Features

* 🔍 **Host Scanning** – Scan hostnames, IPv4, and IPv6 addresses
* 📶 **Custom Port Range** – Specify start and end ports
* ⚡ **Fast TCP Port Detection** – Uses socket-based connections
* 🌍 **IPv4 & IPv6 Support**
* ⌨️ **Command-Line Mode**
* 🖱️ **Interactive Mode**
* 🛡️ **Input Validation & Error Handling**
* ⏱️ **Scan Duration Reporting**

---

## 🛠️ Tech Stack

* **Python 3.x**
* **Socket Programming**
* **TCP Networking**

---

## 📁 Project Structure

```text
PORT-SCANNER/
├── port_scanner.py                        # Main scanner application
└── README.md                              # Documentation
```

---

## ⚙️ Installation & Usage

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/HimanshuKumarRout/PORT-SCANNER.git
cd port-scanner
```

---

### 2️⃣ Run Using Command-Line Arguments

```bash
python port_scanner.py <target> <start_port> <end_port>
```

Example:

```bash
python port_scanner.py example.com 1 1024
```

---

### 3️⃣ Run in Interactive Mode

```bash
python port_scanner.py
```

Then enter:

* Target hostname or IP address
* Starting port
* Ending port

---

## 🖥️ Sample Output

```text
Scanning host: example.com

Port 80 is OPEN
Port 443 is OPEN

Scan completed in 2.146 seconds
```

---

## ⚠️ Important Notes

* Port numbers must be between **1 and 65535**
* Starting port must be less than or equal to the ending port
* Large port ranges may take additional time to scan
* Results depend on network accessibility and firewall configurations

---

## 🔮 Future Enhancements

* 🚀 Multi-threaded scanning
* 📊 Export results to CSV or JSON
* 🎨 GUI-based scanner interface
* 🔔 Service detection on open ports
* 🌐 UDP port scanning support
* 📡 Banner grabbing functionality

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a branch (`feature/new-feature`)
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 👨‍💻 Author

**Himanshu Kumar Rout**

* GitHub: https://github.com/HimanshuKumarRout
* Email: [himanshurout136@gmail.com](mailto:himanshurout136@gmail.com)

---

## ⭐ Support

If you like this project, please **star ⭐ the repository** and share it!

---

<p align="center">Built with 🔍 using Python & Socket Programming</p>
