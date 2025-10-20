"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""

def get_rounds(number):
    return [number, number + 1, number + 2]

def concatenate_rounds(rounds_1, rounds_2):
    return(rounds_1 + rounds_2)

def list_contains_round(rounds, number):
    return number in rounds

def card_average(hand):
     return sum(hand) / len(hand) if hand else 0.0


def approx_average_is_average(hand):
    true_avg = sum(hand) / len(hand)
    first_last_avg = (hand[0] + hand[-1]) / 2
    middle = hand[len(hand) // 2]
    return true_avg == first_last_avg or true_avg == middle


def average_even_is_average_odd(hand):
    even_cards = hand[::2]  # Even-indexed cards (0, 2, ...)
    odd_cards = hand[1::2]  # Odd-indexed cards (1, 3, ...)
    if not even_cards or not odd_cards:
        return False
    even_avg = sum(even_cards) / len(even_cards)
    odd_avg = sum(odd_cards) / len(odd_cards)
    return even_avg == odd_avg


def maybe_double_last(hand):
    if hand and hand[-1] == 11:
        hand[-1] = hand[-1] * 2
    return hand

