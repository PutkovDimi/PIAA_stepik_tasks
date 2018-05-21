from Wild_card.src.Aho_Korasik import Automaton

def test_valid_string(wild_card, pattern, answer, text):
    pattern = pattern[0]
    print(pattern)
    A = Automaton(pattern, wild_card)
    print(answer)
    assert answer == str(A.get_keywords_found(text, wild_card))
