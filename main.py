import random

def main(input_file, output_file):
    #znaki specjalne
    punctuations = ['.', ',', '-', ';', '«', ':', '!', '-', '(', ')', '?', '—', '…']
    #stoplista
    stopwords = ['a', 'aby', 'ach', 'acz', 'aczkolwiek', 'aj', 'albo', 'ale', 'ależ', 'ani', 'aż', 'bardziej', 'bardzo', 'bo', 'bowiem', 'by', 'byli', 'bynajmniej', 'być', 'był', 'była', 'było', 'były', 'będzie', 'będą', 'cali', 'cała', 'cały', 'ci', 'cię', 'ciebie', 'co', 'cokolwiek', 'coś', 'czasami', 'czasem', 'czemu', 'czy', 'czyli', 'daleko', 'dla', 'dlaczego', 'dlatego', 'do', 'dobrze', 'dokąd', 'dość', 'dużo', 'dwa', 'dwaj', 'dwie', 'dwoje', 'dziś', 'dzisiaj', 'gdy', 'gdyby', 'gdyż', 'gdzie', 'gdziekolwiek', 'gdzieś', 'i', 'ich', 'ile', 'im', 'inna', 'inne', 'inny', 'innych', 'iż', 'ja', 'ją', 'jak', 'jaka', 'jakaś', 'jakby', 'jaki', 'jakichś', 'jakie', 'jakiś', 'jakiż', 'jakkolwiek', 'jako', 'jakoś', 'je', 'jeden', 'jedna', 'jedno', 'jednak', 'jednakże', 'jego', 'jej', 'jemu', 'jest', 'jestem', 'jeszcze', 'jeśli', 'jeżeli', 'już', 'ją', 'każdy', 'kiedy', 'kilka', 'kimś', 'kto', 'ktokolwiek', 'ktoś', 'która', 'które', 'którego', 'której', 'który', 'których', 'którym', 'którzy', 'ku', 'lat', 'lecz', 'lub', 'ma', 'mają', 'mało', 'mam', 'mi', 'mimo', 'między', 'mną', 'mnie', 'mogą', 'moi', 'moim', 'moja', 'moje', 'może', 'możliwe', 'można', 'mój', 'mu', 'musi', 'my', 'na', 'nad', 'nam', 'nami', 'nas', 'nasi', 'nasz', 'nasza', 'nasze', 'naszego', 'naszych', 'natomiast', 'natychmiast', 'nawet', 'nią', 'nic', 'nich', 'nie', 'niech', 'niego', 'niej', 'niemu', 'nigdy', 'nim', 'nimi', 'niż', 'no', 'o', 'obok', 'od', 'około', 'on', 'ona', 'one', 'oni', 'ono', 'oraz', 'oto', 'owszem', 'pan', 'pana', 'pani', 'po', 'pod', 'podczas', 'pomimo', 'ponad', 'ponieważ', 'powinien', 'powinna', 'powinni', 'powinno', 'poza', 'prawie', 'przecież', 'przed', 'przede', 'przedtem', 'przez', 'przy', 'roku', 'również', 'sama', 'są', 'się', 'skąd', 'sobie', 'sobą', 'sposób', 'swoje', 'ta', 'tak', 'taka', 'taki', 'takie', 'także', 'tam', 'te', 'tego', 'tej', 'temu', 'ten', 'teraz', 'też', 'to', 'tobą', 'tobie', 'toteż', 'trzeba', 'tu', 'tutaj', 'twoi', 'twoim', 'twoja', 'twoje', 'twym', 'twój', 'ty', 'tych', 'tylko', 'tym', 'u', 'w', 'wam', 'wami', 'was', 'wasz', 'wasza', 'wasze', 'we', 'według', 'wiele', 'wielu', 'więc', 'więcej', 'wszyscy', 'wszystkich', 'wszystkie', 'wszystkim', 'wszystko', 'wtedy', 'wy', 'właśnie', 'z', 'za', 'zapewne', 'zawsze', 'ze', 'zł', 'znowu', 'znów', 'został', 'żaden', 'żadna', 'żadne', 'żadnych', 'że', 'żeby']

    #odczytanie oryginalnego pliku
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()

    cleaned_lines = []
    
    #zapisanie w nowym pliku jednego słowna na linię
    with open(output_file, 'w', encoding='utf-8') as file:
        for line in lines:
            if line.strip():
                for punct in punctuations:
                    line = line.replace(punct, "")
                words = line.split()
                filtered_words = [word for word in words if word.lower() not in stopwords]
                for word in filtered_words:
                    file.write(word.lower() + "\n")
                    cleaned_lines.append(word.lower())

    #losowanie 50 słów do nowego pliku
    with open('correct50words.txt', 'w', encoding='utf-8') as file:
        for _ in range(50):
            random_word = random.choice(cleaned_lines)
            file.write(random_word + "\n")
                
input_file = 'pt.txt'
output_file = 'pt_copy.txt'
main(input_file, output_file)