import itertools, string

class AlphaTables:
    def get_alpha_table(self):
        self.get_alpha_table = {
        8: 4,
        9: 5,
        10: 6,
        11: 7,
        12: 8,
        13: 9,
        14: 10,
        15: 11,
        16: 12,
        17: 13,
        18: 14,
        19: 15,
        20: 16
        }


class NonAlphaTables:
    def __init__(self):
        self.tables = {}

        for letters in range(2,17):
            self.tables[letters] = self.generate_table(letters)

    def generate_table(self, letters):
        table = []
        num_pairs = letters - 1
        pairs = itertools.combinations_with_replacement(range(1, num_pairs + 1), 2)
        for pair in pairs:
            table.append(pair)
        if num_pairs % 2 == 0:
            table.append((num_pairs // 2 + 1, num_pairs // 2 + 1))
        return table

    def get_nonalpha_table(self, letters):
        if letters not in self.tables:
            raise ValueError("Invalid word length")
        return self.tables[letters]

# Example usage
non_alpha_tables = NonAlphaTables()
table = non_alpha_tables.get_nonalpha_table(len("words"))  # Replace with your desired word length
print(table)