# 🔐 Compression Tool (Huffman & Hamming)

A web-based tool for demonstrating:

* **Huffman Coding** (Data Compression)
* **Hamming Code (7,4)** (Error Detection & Correction)

Built using **Python + Flask** with visualization support.

---

# 📥 Clone the Repository

## Using HTTPS

```bash
git clone https://github.com/Hisham-Mizeed/Huffman-Hamming-AIproject.git
cd compression-tool
```

## Using SSH

```bash
git clone git@github.com:Hisham-Mizeed/Huffman-Hamming-AIproject.git
cd Huffman-Hamming-AIproject
```

---

# 🚀 Features

* Encode text using **Huffman Algorithm**
* Encode text using **Hamming Code (7,4)**
* Display compression efficiency
* Visualize Huffman Tree 🌳
* Handle whitespace characters:

  * SPACE
  * ENTER
  * TAB
* Clean and modern UI

---

# 🧠 Algorithms

## 1️⃣ Huffman Coding

* Used for **data compression**
* Assigns shorter codes to frequent characters
* Reduces total number of bits

---

## 2️⃣ Hamming Code (7,4)

* Used for **error detection and correction**
* Adds redundancy bits
* Increases reliability of transmission

---

# 📊 Comparison

| Feature    | Huffman     | Hamming          |
| ---------- | ----------- | ---------------- |
| Purpose    | Compression | Error Correction |
| Bits       | Decrease    | Increase         |
| Efficiency | Saves space | Adds redundancy  |

---

# 🖥️ Project Structure

```bash
.
├── app.py
├── huffman.py
├── hamming.py
├── templates/
│   └── index.html
├── static/
│   └── huffman_tree.png
└── Dockerfile
```

---

# ▶️ Run Locally

## Install dependencies

```bash
pip install flask graphviz
sudo apt install graphviz
```

## Run the app

```bash
python app.py
```

---

# 🐳 Run with Docker

## Build

```bash
docker build -t compression-app .
```

## Run

```bash
docker run -p 5000:5000 compression-app
```

---

# 🌐 Open in Browser

```
http://localhost:5000
```

---

# 💡 Notes

* Graphviz is required for tree visualization
* Whitespace characters are explicitly handled
* Efficiency is calculated differently for each algorithm

---

# 👨‍💻 Author
Hisham Mizeed

---

# ⭐ If you like it

Give it a star on GitHub ⭐
