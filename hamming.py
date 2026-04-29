# =========================================
# HAMMING CODE (7,4)
# =========================================


# Step 1: تحويل النص إلى Binary
def text_to_binary(text):
    binary = ""
    for char in text:
        binary += format(ord(char), '08b')
    return binary


# Step 2: تقسيم إلى 4 bits
def split_into_4bits(binary):
    chunks = []

    for i in range(0, len(binary), 4):
        chunk = binary[i:i+4]

        if len(chunk) < 4:
            chunk = chunk.ljust(4, '0')

        chunks.append(chunk)

    return chunks


# Step 3: Hamming Encoding (7,4)
def hamming_encode_4bits(data):
    d1, d2, d3, d4 = map(int, data)

    p1 = d1 ^ d2 ^ d4
    p2 = d1 ^ d3 ^ d4
    p4 = d2 ^ d3 ^ d4

    return f"{p1}{p2}{d1}{p4}{d2}{d3}{d4}"


# Step 4: Encode كامل
def hamming_encode(text):
    binary = text_to_binary(text)
    chunks = split_into_4bits(binary)

    encoded = ""

    for chunk in chunks:
        encoded += hamming_encode_4bits(chunk)

    return encoded, binary


# Step 5: Efficiency
def hamming_efficiency(original_binary, encoded):
    data_bits = len(original_binary)
    total_bits = len(encoded)

    if total_bits == 0:
        return 0

    return data_bits / total_bits


# Step 6: Main function
def hamming_process(text):
    text = text.strip()

    if not text:
        return {
            "encoded": "",
            "original_bits": 0,
            "encoded_bits": 0,
            "efficiency": 0
        }

    encoded, original_binary = hamming_encode(text)
    efficiency = hamming_efficiency(original_binary, encoded)

    return {
        "encoded": encoded,
        "original_bits": len(original_binary),
        "encoded_bits": len(encoded),
        "efficiency": round(efficiency * 100, 2)
    }