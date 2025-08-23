
```markdown
# Distributed File Sharing

A **decentralized file sharing system** that enables **secure, fast, and reliable transfer of data** across distributed nodes.  
This project is designed to provide **peer-to-peer (P2P) file sharing** without the need for a centralized server, ensuring **fault tolerance, scalability, and redundancy**.

---

## 🚀 Features

- 🔗 **Peer-to-Peer File Transfer** – Share files directly between clients and nodes.
- 🔐 **End-to-End Encryption** – Secure communication using AES encryption for data confidentiality.
- 🛡 **Fault Tolerance & Redundancy** – Data is distributed across nodes, ensuring availability even if one node fails.
- 📈 **Scalability** – Easily scale by adding new peers/nodes to the system.
- ⚡ **Fast & Reliable** – Optimized socket-based communication for efficient file transfers.
- 🧩 **Modular Design** – Separate client, server, and utility modules for better maintainability.

---

## 📂 Project Structure

```

distributed-file-sharing/
│── client.py        # Client-side application for uploading & downloading files
│── server.py        # Server-side node handling file storage and requests
│── utils.py         # Utility functions (encryption, decryption, hashing, etc.)
│── requirements.txt # Python dependencies
│── README.md        # Project documentation
│── LICENSE          # Open-source MIT License

````

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ganeshkrishnareddy/distributed-file-sharing.git
   cd distributed-file-sharing
````

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

### Start a Server Node

```bash
python server.py
```

This starts a file-sharing node that listens for incoming connections.

### Run a Client

```bash
python client.py
```

Options include:

* Upload a file to the distributed system.
* Download a file from peers.
* Verify file integrity using hashing.

---

## 🔒 Security

* **Encryption**: Files are encrypted with AES before transfer.
* **Decryption**: Only the intended recipient can decrypt using the shared secret key.
* **Integrity**: Hash checks ensure files are not tampered with during transfer.

---

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Ganesh Krishna Reddy**
Passionate about **Distributed Systems, Cybersecurity, and Peer-to-Peer Networking**.

````

---

## 📌 New `requirements.txt`

```txt
# Networking and sockets
socket

# Cryptography for encryption/decryption
cryptography>=41.0.0

# For handling secure random key generation
secrets

# For hashing and file integrity checks
hashlib

# For file handling utilities
os
````

⚠️ Note: `socket`, `os`, `hashlib`, and `secrets` are part of Python’s **standard library**, so they don’t need to be installed separately. To make `requirements.txt` practical, we only include **external dependencies**.
So the **final clean version** should be:

```txt
cryptography>=41.0.0
```

---

