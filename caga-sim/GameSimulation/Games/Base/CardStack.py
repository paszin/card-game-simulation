import copy
import random


class EmptyStackError(Exception):
    pass


class CardStack:

    def __init__(self, name=None, cards=None):
        self.name = name
        self.cards = cards or []
        self.acceptance_rule = lambda stack, card: True

    def __str__(self):
        return f"{self.name or 'Stack'}: {self.last_card} "

    def __repr__(self):
        return f"{self.name or 'Stack'}: {self.last_card} "

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, i):
        return self.cards[len(self) - 1 - i]

    def __iter__(self):
        return iter(self.cards)

    def set_acceptance_rule(self, func):
        """

        :param func: function that gets card as parameter
        :return:
        """
        self.acceptance_rule = func

    def accept(self, card):
        """

        :return:
        """
        return self.acceptance_rule(self, card)

    def push(self, card):
        """

        :param card:
        :return:
        """
        if not self.accept(card):
            raise RuntimeError(f"{card} is not accepted for {self}")
        self.cards.append(card)

    @property
    def last_card(self):
        """

        :return:
        """
        return self.cards[-1] if len(self.cards) > 0 else None

    def pop(self):
        try:
            return self.cards.pop(-1)
        except IndexError:
            raise EmptyStackError("no more cards")

    def shuffle(self):
        random.shuffle(self.cards)

    def copy_cards(self):
        return copy.deepcopy(self.cards)

    def add_cards(self, cards):
        self.cards = [] + cards + self.cards
