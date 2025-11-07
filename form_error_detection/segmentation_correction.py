import re
import spacy
from spellchecker import SpellChecker

nlp = spacy.load("fr_core_news_md")
spell = SpellChecker(language="fr")
FRENCH_WORDS = set(w.lower() for w in spell.word_frequency)


def in_dict(word: str) -> bool:
    return word and word.lower() in FRENCH_WORDS


def detect_simple_merges(paragraph, max_span=3):
    
    results = []
    doc = nlp(paragraph)
    tokens = [t.text for t in doc]
    n = len(tokens)

    for i in range(n):
        for span in range(2, max_span + 1):
            j = i + span - 1
            if j >= n:
                break

            span_tokens = tokens[i : j + 1]
            if any(re.fullmatch(r"[\.\,\;\:\!\?\(\)\[\]\']+", t) for t in span_tokens):
                continue
            merged = "".join(span_tokens)
            merged_clean = merged.replace(" ", "").replace("'", "").replace("’", "")

            if in_dict(merged_clean) or in_dict(merged):
                results.append({
                    "Error": " ".join(span_tokens),
                    "Suggestion": merged_clean if in_dict(merged_clean) else merged
                })
                break  

    return results


def correct_simple_merges(paragraph):
    doc = nlp(paragraph)
    tokens = [t.text for t in doc]
    merges = detect_simple_merges(paragraph)

    corrected_text = paragraph
    for m in merges:
        corrected_text = corrected_text.replace(m["Error"], m["Suggestion"])

    return merges, corrected_text


if __name__ == "__main__":
    text = (
        "L en demain sera meilleur. "
        "Le pre sident parle. "
        "Elle viendra ce so ir."
    )

    merges, corrected = correct_simple_merges(text)

    if merges:
        print("Detected simple merges:\n")
        for m in merges:
            print(f" - '{m['Error']}' → '{m['Suggestion']}'")

        print("\nCorrected paragraph:\n")
        print(corrected)
    else:
        print("No simple merges detected.")