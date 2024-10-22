import PyPDF2
from deep_translator import GoogleTranslator

# PDF faylini o'qish
def read_pdf(file_path, start_page=135, end_page=135):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in range(start_page - 1, min(end_page, len(reader.pages))):  # start_page-1 sababli
            text += reader.pages[page].extract_text() + "\n"
    return text

# Matnni bo'laklarga ajratish
def split_text(text, max_length=5000):
    # Matnni 5000 belgi bo'laklarga ajratish
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]

# Matnni tarjima qiling
def translate_text(text, dest_language='uz'):
    translator = GoogleTranslator(source='auto', target=dest_language)
    text_chunks = split_text(text)
    translated_chunks = []
    
    for chunk in text_chunks:
        # Agar bo'lak bo'sh bo'lsa, uni o'tkazib yuboramiz
        if chunk.strip():
            translated = translator.translate(chunk)
            translated_chunks.append(translated)
    
    return ''.join(translated_chunks)

# Natijani saqlash
def save_translated_text(translated_text, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translated_text)

# Asosiy funksiya
def main():
    pdf_file = 'Ibn_Haldun_Mukaddime_I.pdf'  # PDF fayl nomi
    output_file = 'muqaddima_ozb.txt'  # Tarjima qilingan fayl nomi
    
    # PDF dan matnni oling
    text = read_pdf(pdf_file)
    
    # Tarjima qiling
    translated_text = translate_text(text)
    
    # Natijani saqlang
    save_translated_text(translated_text, output_file)
    print("Tarjima qilish tugallandi!")

if __name__ == '__main__':
    main()
