import hashlib

def sha256(data: str) -> str:
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def build_merkle_root(transactions: list) -> str:
    if not transactions:
        return ""


    current_level = [sha256(tx) for tx in transactions]

  
    while len(current_level) > 1:
      
        if len(current_level) % 2 != 0:
            current_level.append(current_level[-1])

        next_level = []
        
        for i in range(0, len(current_level), 2):
            combined_hash = current_level[i] + current_level[i + 1]
            next_level.append(sha256(combined_hash))

        current_level = next_level

    return current_level[0]


if __name__ == "__main__":
    print("=== BÀI 4: XÂY DỰNG MERKLE ROOT ===")

   
    n = int(input("Nhập số giao dịch N: "))
    tx_list = []
    for i in range(n):
        tx = input(f"Giao dịch {i + 1} (A,N,B): ").strip()
        tx_list.append(tx)

    merkle_root = build_merkle_root(tx_list)
    print(f"Giá trị Merkle Root cuối cùng: {merkle_root}")

   