"""Task 2 Module. Contains a function that prints the list sorted ascendingly.
"""


class MyList(list):
    """Subclass of the list class."""

    def print_sorted(self):
        """Prints the list sorted ascendingly.

        Args:
            self (MyList): The list to be sorted.

        """
        print(sorted(self))
