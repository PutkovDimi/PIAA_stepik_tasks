from collections import deque


class Automaton(object):

    def __init__(self, keyword, wild_card):
        """ creates a trie of keywords, then sets fail transitions """
        self.AdjList = list()
        self.AdjList.append({'value': '', 'next_states': [], 'fail_state': 0, 'output': []})
        self.add_keyword(keyword, wild_card)
        self.set_fail_transitions(wild_card=wild_card)

    def find_next_state(self, current_state, value, wild_card):
        for node in self.AdjList[current_state]["next_states"]:
            if self.AdjList[node]["value"] == value or self.AdjList[node]["value"] == wild_card:
                return node
        return None

    def add_keyword(self, keyword, value=None, wild_card=None):
        """ add a keyword to the trie and mark output at the last node """
        current_state = 0
        j = 0
        child = self.find_next_state(current_state, keyword[j], wild_card)
        while child:
            current_state = child
            j = j + 1
            if j < len(keyword):
                child = self.find_next_state(current_state, keyword[j], wild_card)
            else:
                break
        for i in range(j, len(keyword)):
            node = {'value': keyword[i], 'next_states': [], 'fail_state': 0, 'output': []}
            self.AdjList.append(node)
            self.AdjList[current_state]["next_states"].append(len(self.AdjList) - 1)
            current_state = len(self.AdjList) - 1
        self.AdjList[current_state]["output"].append((keyword, value))

    def set_fail_transitions(self, wild_card):
        q = deque()
        for node in self.AdjList[0]["next_states"]:
            q.append(node)
            self.AdjList[node]["fail_state"] = 0
        while q:
            r = q.popleft()
            for child in self.AdjList[r]["next_states"]:
                q.append(child)
                state = self.AdjList[r]["fail_state"]
                while self.find_next_state(state, self.AdjList[child]["value"], wild_card) == None and state != 0:
                    state = self.AdjList[state]["fail_state"]
                self.AdjList[child]["fail_state"] = self.find_next_state(state, self.AdjList[child]["value"], wild_card)
                if self.AdjList[child]["fail_state"] is None:
                    self.AdjList[child]["fail_state"] = 0
                self.AdjList[child]["output"] = self.AdjList[child]["output"] + \
                                                self.AdjList[self.AdjList[child]["fail_state"]]["output"]

    def get_keywords_found(self, line, wild_card):
        """ returns true if line contains any keywords in trie, format: (start_idx,kw,value) """
        current_state = 0
        keywords_found = []

        for i in range(len(line)):
            while self.find_next_state(current_state, line[i], wild_card) is None and current_state != 0:
                current_state = self.AdjList[current_state]["fail_state"]
            current_state = self.find_next_state(current_state, line[i], wild_card)
            if current_state is None:
                current_state = 0
            else:
                for k, v in self.AdjList[current_state]["output"]:
                    keywords_found.append((i - len(k) + 2, k))

        return len(keywords_found)
