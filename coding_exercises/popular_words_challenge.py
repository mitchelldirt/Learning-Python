def popular_words(text: str, words: list) -> dict:
    """
    Count how many values of `words` there are in `text`.
    :param text: A string input.
    :param words: A list of words to compare against text.
    :return: Count of words in text.
    """
    text_lower = text.lower()
    text_split = text_lower.split()
    answer = {}
    for word in words:
        answer[word] = text_split.count(word)
    return answer


print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))