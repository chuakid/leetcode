from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        # make nodes with wildcard
        wildcarded_nodes = {}
        # wildcarded nodes maps wildcarded words to the words they can turn into
        # for instance, if "*ab" maps to ["aab","bab"], aab and bab are in wordList
        for word in wordList:
            for i in range(len(word)):
                wildcarded = word[0:i] + "*" + word[i + 1:]
                if wildcarded not in wildcarded_nodes:
                    wildcarded_nodes[wildcarded] = []
                wildcarded_nodes[wildcarded].append(word)
        # search
        q = deque()
        visited = set([beginWord])
        q.append(beginWord)
        ans = 1
        while q:
            for _ in range(len(q)):
                curr_word = q.popleft()
                if curr_word == endWord:
                    return ans
                for i in range(len(curr_word)):
                    neighbour = curr_word[0:i] + "*" + curr_word[i + 1:]
                    if neighbour not in wildcarded_nodes:
                        continue
                    for next_word in wildcarded_nodes[neighbour]:
                        if next_word in visited:
                            continue
                        visited.add(next_word)
                        q.append(next_word)

            ans += 1
        return 0


print(Solution().ladderLength("hot", "dog", ["hot", "dog", "dot"]))
