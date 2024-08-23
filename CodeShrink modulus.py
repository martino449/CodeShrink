import os
import zlib

# Dizionario per sostituire le parole chiave Python con abbreviazioni uniche racchiuse tra delimitatori
KEYWORDS = {
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
INVERSE_KEYWORDS = {v: k for k, v in KEYWORDS.items()}

class Compressor:
    @staticmethod
    def compress_keywords(code):
        """Sostituisce le parole chiave nel codice con abbreviazioni uniche."""
        for key, value in KEYWORDS.items():
            code = code.replace(key, value)
        return code

    @staticmethod
    def decompress_keywords(code):
        """Ripristina le parole chiave originali nel codice."""
        for key, value in INVERSE_KEYWORDS.items():
            code = code.replace(key, value)
        return code

    @staticmethod
    def compress_zlib(code):
        """Comprimi il codice usando zlib."""
        compressed_code = zlib.compress(code.encode('utf-8'))
        return compressed_code

    @staticmethod
    def decompress_zlib(compressed_code):
        """Decomprimi il codice usando zlib."""
        decompressed_code = zlib.decompress(compressed_code).decode('utf-8')
        return decompressed_code

    @staticmethod
    def compress_script(code):
        """Comprimi lo script in due fasi: sostituzione delle parole chiave e compressione zlib."""
        code = Compressor.compress_keywords(code)
        compressed_code = Compressor.compress_zlib(code)
        return compressed_code

    @staticmethod
    def decompress_script(compressed_code):
        """Decomprimi lo script in due fasi: decompressione zlib e ripristino delle parole chiave originali."""
        code = Compressor.decompress_zlib(compressed_code)
        code = Compressor.decompress_keywords(code)
        return code

    @staticmethod
    def read_file(file_path):
        """Leggi il contenuto di un file."""
        with open(file_path, 'r') as file:
            return file.read()

    @staticmethod
    def write_file(file_path, data):
        """Scrivi i dati in un file."""
        with open(file_path, 'wb') as file:
            file.write(data)






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
