from src.kmp_alg import kmp_find_occurrences as kmp

pattern = str(input())
text = str(input())
print(kmp(pattern=pattern, text=text))
