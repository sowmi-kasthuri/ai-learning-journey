"""Functions for creating, transforming, and adding prefixes to strings."""
# Little Sisters vocabulary

def add_prefix_un(word):
    return 'un'+word


def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    return " :: ".join([prefix] + [prefix + word for word in vocab_words[1:]])
    


def remove_suffix_ness(word):
    if word.endswith("iness"):
        # e.g. "heaviness" -> "heavy"
        return word[:-5] + "y"
    elif word.endswith("ness"):
        # e.g. "sadness" -> "sad"
        return word[:-4]
    else:
        return word


def adjective_to_verb(sentence, index):
    words = sentence.rstrip(".").split()
    return words[index] + "en"
 