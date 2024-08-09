def hitung_akurasi(tokenizer_tokens: list[list[str]], gold_std_tokens: list[list[str]]):
    """
    Fungsi ini menghitung akurasi dari hasil tokenisasi suatu tokenizer
    terhadap hasil tokenisasi gold standard (asumsikan bahwa fungsi ini
    menerima hasil tokenisasi dari semua teks di dataset testing sekaligus)
    """
    # TODO: Hitung akurasi
    return -1

if __name__ == "__main__":
    # Contoh pemanggilan akurasi seperti pada dokumen soal
    tokenizer_tokens = [
        ["Bukunya", "mahal", "."],
        ["Seharus", "nya", "kamu", "tidak", "terlambat", "."],
    ]

    gold_std_tokens = [
        ["Buku", "nya", "mahal", "."],
        ["Seharusnya", "kamu", "tidak", "terlambat", "."],
    ]

    epsilon = 1e-7
    assert abs(hitung_akurasi(tokenizer_tokens, gold_std_tokens) - 0.67) <= epsilon
