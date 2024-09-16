def hitung_akurasi(tokenizer_tokens_list: list[list[str]], gold_std_tokens_list: list[list[str]]):
    """
    Fungsi ini menghitung akurasi dari hasil tokenisasi suatu tokenizer
    terhadap hasil tokenisasi gold standard (asumsikan bahwa fungsi ini
    menerima hasil tokenisasi dari semua teks di dataset testing sekaligus)
    """
    tokenizer_tokens_new = [item for sublist in tokenizer_tokens_list for item in sublist]
    gold_std_tokens_new = [item for sublist in gold_std_tokens_list for item in sublist]

    gold_index = tokenized_index = 0
    gold_char_ptr = tokenized_char_ptr = 0
    correct_tokens = 0
    total_tokens = len(gold_std_tokens_new)

    while gold_index < len(gold_std_tokens_new) and tokenized_index < len(tokenizer_tokens_new):
        # Get the current gold and tokenized tokens
        gold_token = gold_std_tokens_new[gold_index]
        tokenized_token = tokenizer_tokens_new[tokenized_index]
        
        # Handle [UNK] tokens
        if tokenized_token == "[UNK]":
            tokenized_index += 1
            tokenized_char_ptr = 0
            continue
            
        elif tokenized_token == gold_token:
            correct_tokens += 1
            tokenized_index += 1
            gold_index += 1
            tokenized_char_ptr = 0
            gold_char_ptr = 0
            continue
        
        # Compare characters in both tokens
        if gold_token[gold_char_ptr] == tokenized_token[tokenized_char_ptr]:
            gold_char_ptr += 1
            tokenized_char_ptr += 1
            
            if gold_char_ptr == len(gold_token):
                if tokenized_char_ptr == len(tokenized_token):
                    if len(tokenized_token) == len(gold_token):
                        correct_tokens += 1
                    tokenized_char_ptr = 0
                    tokenized_index += 1
                gold_index += 1
                gold_char_ptr = 0

            if tokenized_char_ptr == len(tokenized_token):
                tokenized_index += 1
                tokenized_char_ptr = 0
        else:
            if gold_char_ptr == len(gold_token) - 1:
                gold_index += 1
                gold_char_ptr = 0
            else:
                gold_char_ptr += 1

    accuracy = correct_tokens / total_tokens if total_tokens > 0 else 0
    return accuracy

if __name__ == "__main__":

    tokenizer_tokens_list = [
        ['[UNK]', ',', 'dalam', 'hir', 'ag', 'ana', ',', 'atau', '[UNK]', 'dalam', 'kat', 'akan', 'a', ',', 'adalah', 'sebuah', 'kan', 'a', 'dalam', 'bahasa', 'Jepang', ',', 'yang', 'masing', '-', 'masing', 'mel', 'am', 'bang', 'kan', 'suatu', 'm', 'ora', '.']
    ]

    gold_std_tokens_list = [
        ['ひ', ',', 'dalam', 'hiragana', ',', 'atau', 'ヒ', 'dalam', 'katakana', ',', 'adalah', 'sebuah', 'kana', 'dalam', 'bahasa', 'Jepang', ',', 'yang', 'masing-masing', 'melambangkan', 'suatu', 'mora', '.']
    ]
    print(hitung_akurasi(tokenizer_tokens_list, gold_std_tokens_list))
