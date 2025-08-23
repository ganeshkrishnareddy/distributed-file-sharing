

````markdown
# 📡 Distributed File Sharing

A **decentralized file sharing system** that enables **secure, fast, and reliable transfer of data** across distributed nodes.  
This project is designed to provide **peer-to-peer (P2P) file sharing** without the need for a centralized server, ensuring **fault tolerance, scalability, and redundancy**.

---

## ✨ Features

- 🔗 **Peer-to-Peer File Transfer** – Direct client-to-client communication  
- 🔐 **End-to-End Encryption** – AES encryption for confidentiality  
- 🛡 **Fault Tolerance & Redundancy** – Data replicated across multiple nodes  
- 📈 **Scalable Architecture** – Add more peers/nodes seamlessly  
- ⚡ **Fast & Reliable** – Socket-based optimized communication  
- 🧩 **Modular Design** – Client, server, and utilities separated for maintainability  

---

## 📂 Project Structure

```bash
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

### 1. Clone the Repository

```bash
git clone https://github.com/ganeshkrishnareddy/distributed-file-sharing.git
cd distributed-file-sharing
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Start a Server Node

```bash
python server.py
```

This launches a file-sharing node that listens for incoming connections.

### Run a Client

```bash
python client.py
```

Available actions:

* Upload a file to the distributed system
* Download a file from peers
* Verify file integrity with hashing

---

## 📘 Example Workflows

### 🔼 Upload a File

```bash
Enter option: 1 (Upload)
Enter file path: ./sample.txt
✅ File encrypted and uploaded successfully!
```

### 🔽 Download a File

```bash
Enter option: 2 (Download)
Enter file name: sample.txt
✅ File downloaded and verified (SHA-256 matched)
```

### 🛠 Verify Integrity

```bash
Enter option: 3 (Verify)
Enter file name: sample.txt
✅ File hash matches. No tampering detected.
```

---

## 🔒 Security

* **Encryption**: Files are AES-encrypted before transfer
* **Decryption**: Only the intended peer can decrypt with the secret key
* **Integrity**: SHA-256 ensures files are not tampered during transfer

---

## 🤝 Contributing

Contributions are always welcome! 🎉

1. Fork this repository
2. Create a new branch (`feature-xyz`)
3. Commit your changes
4. Push to your branch and create a Pull Request

---

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Ganesh Krishna Reddy**
💡 Passionate about **Distributed Systems, Cybersecurity, and Peer-to-Peer Networking**

```

---


