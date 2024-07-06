import random
import os
import jellyfish
import pandas as pd

def create_new_files(input_file):
    #znaki i słowa do eliminacji
    punctuations = ['.', ',', '-', ';', '«', ':', '!', '-', '(', ')', '?', '—', '…','»', '*']
    stopwords = ['a', 'aby', 'ach', 'acz', 'aczkolwiek', 'aj', 'albo', 'ale', 'ależ', 'ani', 'aż', 'bardziej', 'bardzo', 'bo', 'bowiem', 'by', 'byli', 'bynajmniej', 'być', 'był', 'była', 'było', 'były', 'będzie', 'będą', 'cali', 'cała', 'cały', 'ci', 'cię', 'ciebie', 'co', 'cokolwiek', 'coś', 'czasami', 'czasem', 'czemu', 'czy', 'czyli', 'daleko', 'dla', 'dlaczego', 'dlatego', 'do', 'dobrze', 'dokąd', 'dość', 'dużo', 'dwa', 'dwaj', 'dwie', 'dwoje', 'dziś', 'dzisiaj', 'gdy', 'gdyby', 'gdyż', 'gdzie', 'gdziekolwiek', 'gdzieś', 'i', 'ich', 'ile', 'im', 'inna', 'inne', 'inny', 'innych', 'iż', 'ja', 'ją', 'jak', 'jaka', 'jakaś', 'jakby', 'jaki', 'jakichś', 'jakie', 'jakiś', 'jakiż', 'jakkolwiek', 'jako', 'jakoś', 'je', 'jeden', 'jedna', 'jedno', 'jednak', 'jednakże', 'jego', 'jej', 'jemu', 'jest', 'jestem', 'jeszcze', 'jeśli', 'jeżeli', 'już', 'ją', 'każdy', 'kiedy', 'kilka', 'kimś', 'kto', 'ktokolwiek', 'ktoś', 'która', 'które', 'którego', 'której', 'który', 'których', 'którym', 'którzy', 'ku', 'lat', 'lecz', 'lub', 'ma', 'mają', 'mało', 'mam', 'mi', 'mimo', 'między', 'mną', 'mnie', 'mogą', 'moi', 'moim', 'moja', 'moje', 'może', 'możliwe', 'można', 'mój', 'mu', 'musi', 'my', 'na', 'nad', 'nam', 'nami', 'nas', 'nasi', 'nasz', 'nasza', 'nasze', 'naszego', 'naszych', 'natomiast', 'natychmiast', 'nawet', 'nią', 'nic', 'nich', 'nie', 'niech', 'niego', 'niej', 'niemu', 'nigdy', 'nim', 'nimi', 'niż', 'no', 'o', 'obok', 'od', 'około', 'on', 'ona', 'one', 'oni', 'ono', 'oraz', 'oto', 'owszem', 'pan', 'pana', 'pani', 'po', 'pod', 'podczas', 'pomimo', 'ponad', 'ponieważ', 'powinien', 'powinna', 'powinni', 'powinno', 'poza', 'prawie', 'przecież', 'przed', 'przede', 'przedtem', 'przez', 'przy', 'roku', 'również', 'sama', 'są', 'się', 'skąd', 'sobie', 'sobą', 'sposób', 'swoje', 'ta', 'tak', 'taka', 'taki', 'takie', 'także', 'tam', 'te', 'tego', 'tej', 'temu', 'ten', 'teraz', 'też', 'to', 'tobą', 'tobie', 'toteż', 'trzeba', 'tu', 'tutaj', 'twoi', 'twoim', 'twoja', 'twoje', 'twym', 'twój', 'ty', 'tych', 'tylko', 'tym', 'u', 'w', 'wam', 'wami', 'was', 'wasz', 'wasza', 'wasze', 'we', 'według', 'wiele', 'wielu', 'więc', 'więcej', 'wszyscy', 'wszystkich', 'wszystkie', 'wszystkim', 'wszystko', 'wtedy', 'wy', 'właśnie', 'z', 'za', 'zapewne', 'zawsze', 'ze', 'zł', 'znowu', 'znów', 'został', 'żaden', 'żadna', 'żadne', 'żadnych', 'że', 'żeby']

    #odczytanie oryginalnego pliku
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()

    cleaned_lines = []
    base, ext = os.path.splitext(input_file)

    #zapisanie w nowym pliku jednego słowna na linię
    with open(f"{base}_copy{ext}", 'w', encoding='utf-8') as file:
        for line in lines:
            if line.strip():
                for punct in punctuations:
                    line = line.replace(punct, "")
                words = line.split()
                filtered_words = [word for word in words if word.lower() not in stopwords]
                for word in filtered_words:
                    file.write(word.lower() + "\n")
                    cleaned_lines.append(word.lower())

    random50words=[]
    #losowanie 50 słów do nowego pliku
    with open('correct50words.txt', 'w', encoding='utf-8') as file:
        for _ in range(50):
            random_word = random.choice(cleaned_lines)
            file.write(random_word + "\n")
            random50words.append(random_word)

    #modyfikacja 50 słów do nowego pliku
    with open('50wordswithmistakes.txt', 'w', encoding='utf-8') as file:
        
        typo_types = ['swap', 'drop', 'replace']
        typo = random.choice(typo_types)
        
        for n in range(50):
            word = random50words[n]        
            typo = random.choice(typo_types)

            i, j = random.sample(range(len(word)), 2)
            word = list(word)

            if typo == "swap":
                word[i], word[j] = word[j], word[i]                
        
            elif typo == "drop":
                word[i] = ""

            elif typo == "replace":
                word[i], word[j] = word[i], word[i]      
            
            word = ''.join(word)
            file.write(word + "\n")


def jaro(s1, s2):
    if (s1 == s2):
        return 1.0
 
    len1 = len(s1)
    len2 = len(s2)
 
    if (len1 == 0 or len2 == 0):
        return 0.0
 
    max_dist = (max(len(s1), len(s2)) // 2 ) - 1
 
    match = 0
 
    hash_s1 = [0] * len(s1)
    hash_s2 = [0] * len(s2)
 
    for i in range(len1): 
 
        for j in range( max(0, i - max_dist), min(len2, i + max_dist + 1)): 
             
            if (s1[i] == s2[j] and hash_s2[j] == 0): 
                hash_s1[i] = 1
                hash_s2[j] = 1
                match += 1
                break
         
    if (match == 0):
        return 0.0
 
    t = 0 
    point = 0

    for i in range(len1): 
        if (hash_s1[i]):
            while (hash_s2[point] == 0):
                point += 1
 
            if (s1[i] != s2[point]):
                point += 1
                t += 1
            else:
                point += 1
                 
        t /= 2
 
    return ((match / len1 + match / len2 + (match - t) / match ) / 3.0)
 
def jaro_winkler(s1, s2, alpha): 
 
    jaro_dist = jaro(s1, s2)
 
    if (jaro_dist > 0.7):
        prefix = 0
 
        for i in range(min(len(s1), len(s2))) :
            if (s1[i] == s2[i]):
                prefix += 1
            else:
                break
 
        prefix = min(4, prefix)
 
        jaro_dist += (1-alpha) * prefix * (1 - jaro_dist)
 
    return jaro_dist


def main(input_file, alpha):
    create_new_files(input_file)
    with open('correct50words.txt', 'r', encoding='utf-8', errors='ignore') as file:
        goodwords = [line.strip() for line in file]
    with open('50wordswithmistakes.txt', 'r', encoding='utf-8', errors='ignore') as file:
        badwords = [line.strip() for line in file]

    results = []
    for n in range(50):
        distance = jaro_winkler(goodwords[n], badwords[n], alpha)
        results.append((badwords[n], goodwords[n], distance))

    df = pd.DataFrame(results, columns=['BadWord', 'GoodWord', 'Distance'])
    df.to_csv('jarowinkler_results.txt', index=False, sep='\t', encoding='utf-8')



input_file = 'pt.txt'
alpha = 0.9
main(input_file, alpha)