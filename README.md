# 🔐 Compression Tool (Huffman & Hamming)

A simple web-based tool for demonstrating:

- Huffman Coding (Data Compression)
- Hamming Code (Error Detection & Correction)

Built using Python + Flask with visualization support.

---

## 🚀 Features

- Encode text using Huffman Algorithm
- Encode text using Hamming (7,4)
- Display compression efficiency
- Visualize Huffman Tree 🌳
- Handle whitespace characters (SPACE, ENTER, TAB)
- Clean UI interface

---

## 🧠 Algorithms

### 1️⃣ Huffman Coding
- Used for data compression
- Assigns shorter codes to frequent characters
- Reduces total number of bits

### 2️⃣ Hamming Code (7,4)
- Used for error detection and correction
- Adds redundancy bits
- Increases reliability of transmission

---

## 📊 Comparison

| Feature | Huffman | Hamming |
|--------|--------|--------|
| Purpose | Compression | Error Correction |
| Bits | Decrease | Increase |
| Efficiency | Saves space | Adds redundancy |

---

## 🖥️ Project Structure


.
├── app.py
├── huffman.py
├── hamming.py
├── templates/
│ └── index.html
├── static/
│ └── huffman_tree.png
└── Dockerfile


---

## ▶️ Run Locally

### Install dependencies
```bash
pip install flask graphviz
sudo apt install graphviz
Run app
python app.py

Open:

http://localhost:5000
🐳 Run with Docker
Build
docker build -t huffman_hamming_image .
Run
docker run -p 5000:5000 huffman_hamming_cont
📸 Screenshots
Huffman Encoding
Hamming Encoding
Huffman Tree Visualization
💡 Notes
Graphviz is required for tree visualization
Whitespace characters are explicitly handled
Efficiency is calculated differently for each algorithm

👨‍💻 Author
Hisham Mizeed 

⭐ If you like it

Give it a star on GitHub ⭐