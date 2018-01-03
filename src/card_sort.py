"""
Kata Sort deck of cards - Use a sort function to put cards in order

#1 Best Practices: zebulan, Unnamed, acaccia, j_codez, Mr.Child, iamchingel (plus 8 more warriors)

def sort_cards(cards):
    return sorted(cards, key="A23456789TJQK".index)
."""


def sort_cards(cards):
    """Sort a deck of cards."""
    a_bucket = []
    t_bucket = []
    j_bucket = []
    q_bucket = []
    k_bucket = []
    num_bucket = []
    for item in cards:
        if item == 'A':
            a_bucket.append(item)
        elif item == 'T':
            t_bucket.append(item)
        elif item == 'J':
            j_bucket.append(item)
        elif item == 'Q':
            q_bucket.append(item)
        elif item == 'K':
            k_bucket.append(item)
        else:
            num_bucket.append(item)
    return a_bucket + sorted(num_bucket) + t_bucket + j_bucket + q_bucket + k_bucket
