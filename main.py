from process_text import TextPreprocessor

def read_text_from_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        text = text.replace('\n', '')
    return text

if __name__ == "__main__":
    # text = "pembukaan 4 daftar wisuda dan pelaksanaannya lebih baik d umumkan di web UISI, tidak hanya di jurusan. sehingga memudahkan mahasiswa yang ada di luar kota. pelaksanaan wisuda sebaiknya terjadwal tidak tergantung pada kuota. sehingga lebih cepat mendapat ijazah."
    
    file_path = 'document/document4.txt'
    text = read_text_from_file(file_path)
    
    preprocessor = TextPreprocessor()
    # Tokenisasi
    tokens = preprocessor.tokenize(text)
    print("Tokens:", tokens)

    # Filtering
    filtered_tokens = preprocessor.filter_tokens(tokens)
    print("Filtered Tokens:", filtered_tokens)

    # Stemming
    stemmed_tokens = preprocessor.stem_tokens(filtered_tokens)
    print("Stemmed Tokens:", stemmed_tokens)