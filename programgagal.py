
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
# from nltk.stem import PorterStemmer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):

    tokens = word_tokenize(text.lower()) # mengubah text menjadi huruf kecil dan tokenisasi
    stop_words = set(stopwords.words('indonesian'))  # Menggunakan daftar stopwords bahasa Indonesia dari NLTK

    filtered_tokens = [token for token in tokens if token.isalnum() and token not in stop_words]  # Menghapus token yang bukan alfabet dan stopwords

    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]

    return filtered_tokens

teks = "pembukaan 4 daftar wisuda dan pelaksanaannya lebih baik d umumkan di web UISI, tidak hanya di jurusan. sehingga memudahkan mahasiswa yang ada di luar kota. pelaksanaan wisuda sebaiknya terjadwal tidak tergantung pada kuota. sehingga lebih cepat mendapat ijazah."

tokens = word_tokenize(teks)

print("Hasil Tokenisasi:")
print(tokens)