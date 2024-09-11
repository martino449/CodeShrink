# programma_info.rb
#
# Autore: Mario Pisano
# Licenza: EUPL (European Union Public License)
#


def mostra_info()
  nome_programma = 'CodeShrink'
  versione = '0.1.0'
  descrizione = 'CodeShrink 🐍✨ is a powerful and intuitive tool for compressing and decompressing Python scripts. With CodeShrink, you can easily reduce the size of your Python files while keeping the structure and functionality of your code intact.'

  puts "Nome del programma: #{nome_programma}"
  puts "Versione: #{versione}"
  puts "Descrizione: #{descrizione}"
end

# Esecuzione del programma
mostra_info()

# Aspetta l'input dell'utente prima di terminare
puts "Premi Invio per uscire..."
gets
