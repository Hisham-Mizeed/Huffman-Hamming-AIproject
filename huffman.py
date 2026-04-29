# =========================================
# HUFFMAN CODING MODULE
# Used for Compression + Efficiency
# =========================================

import heapq
from graphviz import Digraph


# =========================================
# Step 1: Calculate Frequency
# =========================================
def calculate_frequency(text):
    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq


# =========================================
# Step 2: Node Class
# =========================================
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


# =========================================
# Step 3: Build Huffman Tree
# =========================================
def build_huffman_tree(freq):
    heap = []

    for char in freq:
        heapq.heappush(heap, Node(char, freq[char]))

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]


# =========================================
# Step 4: Generate Codes
# =========================================
def generate_codes(node, current_code="", codes=None):
    if codes is None:
        codes = {}

    if node is None:
        return codes

    if node.char is not None:
        codes[node.char] = current_code
        return codes

    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)

    return codes


# =========================================
# Step 5: Encode Text
# =========================================
def encode(text, codes):
    encoded_text = ""
    for char in text:
        encoded_text += codes[char]
    return encoded_text


# =========================================
# Step 6: Calculate Efficiency
# =========================================
def calculate_efficiency(text, encoded_text):
    original_bits = len(text) * 8
    compressed_bits = len(encoded_text)

    if original_bits == 0:
        return 0

    efficiency = (original_bits - compressed_bits) / original_bits
    return efficiency


# =========================================
# Step 7: Draw Huffman Tree (FIXED)
# =========================================
def draw_huffman_tree(root):
    dot = Digraph()

    def add_nodes(node, parent=None, label=""):
        if node is None:
            return

        node_id = str(id(node))

        # ✅ معالجة الـ whitespace
        if node.char is not None:
            if node.char == " ":
                display_char = "[SPACE]"
            elif node.char == "\n":
                display_char = "[ENTER]"
            elif node.char == "\t":
                display_char = "[TAB]"
            else:
                display_char = node.char

            node_label = f"{display_char}\n({node.freq})"
        else:
            node_label = f"{node.freq}"

        dot.node(node_id, node_label)

        if parent:
            dot.edge(parent, node_id, label=label)

        add_nodes(node.left, node_id, "0")
        add_nodes(node.right, node_id, "1")

    add_nodes(root)

    dot.render("static/huffman_tree", format="png", cleanup=True)

    return "huffman_tree.png"


# =========================================
# Step 8: Main Processing Function
# =========================================
def huffman_process(text):

    # ❗ نشيل بس newline مش space
    text = text.rstrip("\n")

    if not text:
        return {
            "codes": {},
            "encoded": "",
            "original_bits": 0,
            "compressed_bits": 0,
            "efficiency": 0,
            "tree": None
        }

    freq = calculate_frequency(text)
    root = build_huffman_tree(freq)
    codes = generate_codes(root)
    encoded = encode(text, codes)
    efficiency = calculate_efficiency(text, encoded)

    tree = draw_huffman_tree(root)

    return {
        "codes": codes,
        "encoded": encoded,
        "original_bits": len(text) * 8,
        "compressed_bits": len(encoded),
        "efficiency": round(efficiency * 100, 2),
        "tree": tree
    }