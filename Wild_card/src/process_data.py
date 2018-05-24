from Wild_card.src.Aho_Korasik import Automaton


def process_data(text):
    keyword = input()
    wild_card = input()
    A = Automaton(keyword, wild_card)
    return A.get_keywords_found(text)
