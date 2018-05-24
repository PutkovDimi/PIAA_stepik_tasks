from Wild_card.src.process_data import process_data

if __name__ == "__main__":
    text = input()
    L = process_data(text=text)
    for l in L:
        print(l[0])
