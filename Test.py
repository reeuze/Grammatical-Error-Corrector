def replace_entities(text, entities):
    for entity, label in entities:
        if label in ["PERSON", "GPE", "DATE"]:  # Tambahkan "DATE" ke label yang diperbolehkan
            placeholder = f'[{label}]'
            text = text.replace(entity.lower(), placeholder)  # Gunakan lower() agar cocok dengan teks yang diinput
    return text

# Contoh penggunaan
entities = [('John Doe', 'PERSON'), ('New York', 'GPE'), ('July 5th, 2021', 'DATE')]
text = "john doe goes in new york on july 5th two thousand and twenty-one"

processed_text = replace_entities(text, entities)
print(processed_text)