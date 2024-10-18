### 1. String Operations
- **Splitting**: `text.split(" ")`
- **Replacing**: `text.replace("old", "new")`
- **Substring check**: `'sub' in text`
- **Whitespace removal**: `text.strip()`

### 2. List Operations
- **Creation/Iteration**: `for x in lst:`
- **List comprehension**: `[x**2 for x in range(5)]`
- **Sorting**: `sorted(lst)`, `sorted(lst, reverse=True)`

### 3. Dictionary Operations (Hashmaps)
- **Create**: `d = {"key": "value"}`
- **Update**: `d["key"] = "new_value"`
- **Iterate**: `for k, v in d.items():`
- **Check key**: `'key' in d`

### 4. Combining
Example: Count word frequencies.
```python
words = sentence.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
```

### Common Tasks

Anagram Detection: Checking if two strings are anagrams.
```python
from collections import Counter
def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

# Using sorted
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)
```

Counting Words: Counting the frequency of each word.
```python
from collections import Counter
words = text.split()
word_counts = Counter(words)
# Output
print(word_counts.most_common(3))
# Example Output
# [('the', 2), ('quick', 1), ('brown', 1)]
```


Tokenization: Splitting text into words.
```python
import re
words = re.findall(r'\w+', text.lower())
```

Stopword Removal: Removing common words.
```python
stopwords = set(["the", "a", "an"])
words = [w for w in words if w not in stopwords]
```

Stemming: Reducing words to their base form.
```python
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
words = [stemmer.stem(w) for w in words]
```
