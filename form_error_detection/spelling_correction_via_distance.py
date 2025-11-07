from spellchecker import SpellChecker

spell = SpellChecker(language='fr')
french_words = list(spell.word_frequency)

def damerau_levenshtein(word1, word2):
    len1, len2 = len(word1), len(word2)
    #create a matrix of size (len1+1)*(len2+1) that contain as initial values 0
    d = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    #fill the first column by the cost of deletion of all the word1 (the wrong one) to get an "" (empty string)
    for i in range(len1 + 1):
        d[i][0] = i

    #fill the first row by the cost of insertion that we need to transform the "" to word2 (the correct word)
    for j in range(len2 + 1):
        d[0][j] = j

    #fill the matrix by the letters of the words if the letters match the cost will be 0 and otherwise 1
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            cost = 0 if word1[i - 1] == word2[j - 1] else 1
            # we choose the cheapest way to match the 2 words
            d[i][j] = min(
                d[i - 1][j] + 1,#dlete a letter
                d[i][j - 1] + 1,#insert a letter
                d[i - 1][j - 1] + cost # change a letter
            )

            # check if we can swap two adj letters to match words (cost 0.5)
            if (
                i > 1 and j > 1
                and word1[i - 1] == word2[j - 2]
                and word1[i - 2] == word2[j - 1]
            ):
                
                d[i][j] = min(d[i][j], d[i - 2][j - 2] + 0.5)
     #the distance between words (cost)           
    return d[len1][len2]


def detect_error_type(original, corrected):
    if original == corrected:
        return "Correct word"
    #the difference between words length
    diff = len(corrected) - len(original)
    #if the difference is big them we may have multiple errors
    if abs(diff) > 1:
        return "Multiple errors"
    #if the differnce between the corrected word and the worong word is 1 then it will be a missing letter
    if diff == 1:
        return "Missing letter"
    #if the difference is -1 then the wrong word is containing extra letter
    elif diff == -1:
        return "Extra letter"
    #if the length is the same the the error may be swapped letters or an incorrect letter
    if diff == 0:
        # try to check the swap process if it will correct the word
        for i in range(len(original) - 1):
            if (
                original[i] != corrected[i]
                and original[i + 1] != corrected[i + 1]
                and original[i] == corrected[i + 1]
                and original[i + 1] == corrected[i]
            ):
                return "Swapped letters"
        #if the swap doesn't work then it will be a wrong letter 
        return "Wrong letter"

    return "Unknown error"


def correct_word_filtered(word, dictionary, max_len_diff=3):
    best_match = word
    min_distance = float("inf")

    # we choose thhe words that start withe same 2 letters and with len diff at max 3
    candidates = [
        w for w in dictionary
        if w[:2] == word[:2]  # same first two letters
        and abs(len(w) - len(word)) <= max_len_diff
    ]

    # if there is no word that start withe the same 2 letters then we do the same process but for the first letter only
    if not candidates:
        candidates = [
            w for w in dictionary
            if w[0] == word[0] and abs(len(w) - len(word)) <= max_len_diff
        ]

    for candidate in candidates:
        dist = damerau_levenshtein(word, candidate)
        # prefer words slightly longer if distance is equal (to fix voitre→voiture)
        if dist < min_distance or (dist == min_distance and len(candidate) > len(best_match)):
            min_distance = dist
            best_match = candidate

    error_type = detect_error_type(word, best_match)
    return best_match, error_type


test_words = ["commanteire", "alumete", "pome", "bonjor", "voitre", "frmasge","pommme","lendmain"]

for w in test_words:
    corrected, error_type = correct_word_filtered(w, french_words)
    print(f"{w} → {corrected} ({error_type})")