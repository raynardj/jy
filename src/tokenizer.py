def encode(text: str, pair_to_code):
    code_list = list(text.encode("utf8"))
    if len(code_list) < 2:
        return code_list
    while len(code_list) > 1:
        temp_vocab = dict()
        for c1, c2 in zip(code_list, code_list[1:]):
            token = pair_to_code.get((c1, c2))
            if token is None:
                continue
            else:
                temp_vocab[(c1, c2)] = token
        if len(temp_vocab) == 0:
            return code_list


        pair = min(temp_vocab, key=lambda x: temp_vocab[x])
        token = temp_vocab[pair]

        new_code_list = []

        i = 0
        while i < len(code_list):
            if i < len(code_list) - 1 and code_list[i] == pair[0] and code_list[i + 1] == pair[1]:
                new_code_list.append(token)
                i += 2
            else:
                new_code_list.append(code_list[i])
                i += 1
        
        code_list = new_code_list
            
    return code_list


def decode(tokens, vocab):
    result = list(tokens)

    while True:
        i = 0
        new_result = []
        temp_vocab = dict((i, vocab[i]) for i in result if i in vocab)
        if len(temp_vocab) == 0:
            break
        token = max(temp_vocab, key=lambda x: x)
        c1, c2 = temp_vocab[token]
        for t in result:
            if t == token:
                new_result.append(c1)
                new_result.append(c2)
            else:
                new_result.append(t)
        result = new_result

    return bytes(result).decode(errors="replace")


def by_token_decode(tokens, vocab):
    results = []
    for token in tokens:
        by_token_str = decode([token], vocab)
        results.append(by_token_str)
    return results

