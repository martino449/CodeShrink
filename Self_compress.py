import os
import zlib

# Dizionario per sostituire le parole chiave Python con abbreviazioni uniche racchiuse tra delimitatori
keywords = {
    'def': '[D]',
    'return': '[R]',
    'import': '[I]',
    'for': '[F]',
    'if': '[IF]',
    'else': '[E]',
    'elif': '[EI]',
    'while': '[W]',
    'class': '[C]',
    'try': '[T]',
    'except': '[EX]',
    'finally': '[FN]',
    'with': '[WT]',
    'as': '[AS]',
    'from': '[FR]',
    'print': '[P]'
}

# Dizionario inverso per la decodifica
inverse_keywords = {v: k for k, v in keywords.items()}

def compress_keywords(code):
    for key, value in keywords.items():
        code = code.replace(key, value)
    return code

def decompress_keywords(code):
    for key, value in inverse_keywords.items():
        code = code.replace(key, value)
    return code

def compress_zlib(code):
    # Comprimi il codice usando zlib
    compressed_code = zlib.compress(code.encode('utf-8'))
    return compressed_code

def decompress_zlib(compressed_code):
    # Decomprimi il codice usando zlib
    decompressed_code = zlib.decompress(compressed_code).decode('utf-8')
    return decompressed_code

def compress_script(code):
    # Passo 1: Compattazione tramite sostituzione di parole chiave
    code = compress_keywords(code)
    # Passo 2: Compress zlib
    compressed_code = compress_zlib(code)
    return compressed_code

def create_self_decompressor(compressed_code):
    # Template per lo script auto-decompressivo
    decompressor_code = f"""
import zlib

compressed_data = {compressed_code}

def decompress_and_execute():
    # Decompress the data
    decompressed_code = zlib.decompress(compressed_data).decode('utf-8')

    # Esegui il codice decompresso
    exec(decompressed_code)

# Avvia decompressione ed esecuzione
decompress_and_execute()
    """
    return decompressor_code

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)

def main():
    # Ottieni il percorso della directory corrente (dove si trova il programma)
    base_dir = os.path.dirname(os.path.abspath(__file__))

    while True:
        print("\nMenu:")
        print("1. Comprimi script Python da file e renderlo auto-decompressivo")
        print("2. Esci")
        choice = input("Seleziona un'opzione: ")

        if choice == '1':
            input_name = input("\nInserisci il nome del file Python da comprimere (con estensione .py):\n")
            output_name = input("Inserisci il nome del file di output auto-decompressivo (con estensione .py):\n")

            # Costruisci il percorso completo del file di input e output
            input_file = os.path.join(base_dir, input_name)
            output_file = os.path.join(base_dir, output_name)

            # Legge il codice dal file
            code = read_file(input_file)

            # Comprimi lo script
            compressed_script = compress_script(code)

            # Crea il file auto-decompressivo
            self_decompressing_script = create_self_decompressor(compressed_script)

            # Scrivi lo script auto-decompressivo su file
            write_file(output_file, self_decompressing_script)
            print(f"\nScript auto-decompressivo salvato in {output_file}")

        elif choice == '2':
            print("Uscita...")
            break

        else:
            print("Opzione non valida. Riprova.")

if __name__ == "__main__":
    main()



#Fine del codice
# ---------------------------------------------
# Copyright (c) 2024 Mario Pisano
#
# Questo programma è distribuito sotto la licenza EUPL, Versione 1.2 o – non appena 
# saranno approvate dalla Commissione Europea – versioni successive della EUPL 
# (la "Licenza");
# Puoi usare, modificare e/o ridistribuire il programma sotto i termini della 
# Licenza. 
# 
# Puoi trovare una copia della Licenza all'indirizzo:
# https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12
