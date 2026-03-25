from collections import Counter

STOPWORDS = {
    "the", "a", "an", "on", "in", "at", "of", "to", "and", "is", "are"
}

def score_token(token: str, freq: Counter) -> float:
    score = 0.0
    score += freq[token] * 1.0
    if len(token) >= 5:
        score += 1.0
    if token in STOPWORDS:
        score -= 1.5
    return score

def crs_filter(tokens, idx2word, keep_ratio=0.75):
    if not tokens:
        return tokens
    if keep_ratio >= 1.0:
        return tokens[:]

    words = [idx2word[t] for t in tokens]
    freq = Counter(words)

    scored = []
    for i, token_id in enumerate(tokens):
        word = idx2word[token_id]
        score = score_token(word, freq)
        scored.append((i, token_id, score))

    scored.sort(key=lambda x: x[2], reverse=True)
    keep_n = max(4, int(len(tokens) * keep_ratio))
    selected = scored[:keep_n]

    selected_indices = set()
    for i, token_id, _ in selected:
        selected_indices.add(i)
        if i - 1 >= 0:
            selected_indices.add(i - 1)
        if i + 1 < len(tokens):
            selected_indices.add(i + 1)

    selected_indices.add(0)
    selected_indices.add(len(tokens) - 1)

    final = [tokens[i] for i in sorted(selected_indices)]
    return final
