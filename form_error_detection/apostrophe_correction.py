import spacy
from spellchecker import SpellChecker

nlp = spacy.load("fr_core_news_md")


spell_checker = SpellChecker(language="fr")
FRENCH_WORDS = {word.lower() for word in spell_checker.word_frequency}

def is_in_dictionary(word: str) -> bool:
   
    return bool(word) and word.lower() in FRENCH_WORDS

def detect_apostrophe_issues(text: str):

    issues = []
    doc = nlp(text)
    tokens = [token.text for token in doc]

    index = 0
    while index < len(tokens):
        current_token = tokens[index]

        if "'" in current_token or "’" in current_token:
            if index + 1 < len(tokens) and tokens[index + 1].isalpha():
                merged_word = current_token + tokens[index + 1]
                issues.append({
                    "Error": f"{current_token} {tokens[index + 1]}",
                    "Suggestion": merged_word
                })
                index += 2
                continue

            cleaned_word = current_token.replace("'", "").replace("’", "")
            if is_in_dictionary(cleaned_word) and cleaned_word.lower() != current_token.lower():
                issues.append({
                    "Error": current_token,
                    "Suggestion": cleaned_word
                })
        index += 1

    return issues

def correct_apostrophes(text: str):
    
    corrections = detect_apostrophe_issues(text)
    corrected_text = text

    for correction in corrections:
        corrected_text = corrected_text.replace(
            correction["Error"], correction["Suggestion"]
        )

    return corrections, corrected_text

if __name__ == "__main__":
    sample_text = "Elle a dit d'ame et j' ai vu l' arbre. L' homme est gentil. Il parle de l'âme. D'âme"
    
    detected_issues, fixed_text = correct_apostrophes(sample_text)

    if detected_issues:
        print("Detected apostrophe issues:\n")
        for issue in detected_issues:
            print(f" - '{issue['Error']}' → '{issue['Suggestion']}'")

        print("\nCorrected paragraph:\n")
        print(fixed_text)
    else:
        print("No apostrophe issues detected.")