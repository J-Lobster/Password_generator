class alpha_tables:
    def __init__(self):
        self.get_max_letters = {
        8: 3,
        9: 4,
        10: 5,
        11: 6,
        12: 7,
        13: 8,
        14: 9,
        15: 10,
        16: 11,
        17: 12,
        18: 13,
        19: 14,
        20: 15
        }

class non_alpha_tables:
    def __init__(self):
        self.len20 = {
            15: [(1, 4), (4, 1), (3, 2), (2, 3)],
            14: [(1, 5), (5, 1), (2, 4), (4, 2), (3, 3)],
            13: [(1, 6), (6, 1), (2, 5), (5, 2), (3, 4), (4, 3)],
            12: [(1, 7), (7, 1), (2, 6), (6, 2), (3, 5), (5, 3), (4, 4)],
            11: [(1, 8), (8, 1), (2, 7), (7, 2), (3, 6), (6, 3), (4, 5), (5, 4)],
            10: [(1, 9), (9, 1), (2, 8), (8, 2), (3, 7), (7, 3), (4, 6), (6, 4), (5, 5)],
            9: [(1, 10), (10, 1), (2, 9), (9, 2), (3, 8), (8, 3), (4, 7), (7, 4), (5, 6), (6, 5)],
            8: [(1, 11), (11, 1), (2, 10), (10, 2), (3, 9), (9, 3), (4, 8), (8, 4), (5, 7), (7, 5), (6, 6)],
            7: [(1, 12), (12, 1), (2, 11), (11, 2),(3, 10), (10, 3), (4, 9), (9, 4), (5, 8), (8, 5), (6, 7), (7, 6)],
            6: [(1, 13), (13, 1), (2, 12), (12, 2), (3, 11), (11, 3), (4, 10), (10, 4), (5, 9), (9, 5), (6, 8), (8, 6), (7, 7)],
            5: [(1, 14), (14, 1), (2, 13), (13, 2), (3, 12), (12, 3), (4, 11), (11, 4), (5, 10), (10, 5), (6, 9), (9, 6), (7, 8), (8, 7)],
            4: [(1, 15), (15, 1), (2, 14), (14, 2), (3, 13), (13, 3), (4, 12), (12, 4), (5, 11), (11, 5), (6, 10), (10, 6), (7, 9), (9, 7), (8, 8)],
            3: [(1, 16), (16, 1), (2, 15), (15, 2), (3, 14), (14, 3), (4, 13), (13, 4), (5, 12), (12, 5), (6, 11), (11, 6), (7, 10), (10, 7), (8, 9), (9, 8)],
            2: [(1, 17),(17, 1), (2, 16), (16, 2), (3, 15), (15, 3), (4, 14), (14, 4), (5, 13), (13, 5), (6, 12), (12, 6), (7, 11), (11, 7), (8, 10), (10, 8), (9, 9)]
        }
        
        self.len19 = {
            14: [(1, 4), (4, 1), (3, 2), (2, 3)],
            13: [(1, 5), (5, 1), (2, 4), (4, 2), (3, 3)],
            12: [(1, 6), (6, 1), (2, 5), (5, 2), (3, 4), (4, 3)],
            11: [(1, 7), (7, 1), (2, 6), (6, 2), (3, 5), (5, 3), (4, 4)],
            10: [(1, 8), (8, 1), (2, 7), (7, 2), (3, 6), (6, 3), (4, 5), (5, 4)],
            9: [(1, 9), (9, 1), (2, 8), (8, 2), (3, 7), (7, 3), (4, 6), (6, 4), (5, 5)],
            8: [(1, 10), (10, 1), (2, 9), (9, 2), (3, 8), (8, 3), (4, 7), (7, 4), (5, 6), (6, 5)],
            7: [(1, 11), (11, 1), (2, 10), (10, 2), (3, 9), (9, 3), (4, 8), (8, 4), (5, 7), (7, 5), (6, 6)],
            6: [(1, 12), (12, 1), (2, 11), (11, 2), (3, 10), (10, 3), (4, 9), (9, 4), (5, 8), (8, 5), (6, 7), (7, 6)],
            5: [(1, 13), (13, 1), (2, 12), (12, 2), (3, 11), (11, 3), (4, 10), (10, 4), (5, 9), (9, 5), (6, 8), (8, 6), (7, 7)],
            4: [(1, 14), (14, 1), (2, 13), (13, 2), (3, 12), (12, 3), (4, 11), (11, 4), (5, 10), (10, 5), (6, 9), (9, 6), (7, 8), (8, 7)],
            3: [(1, 15), (15, 1), (2, 14), (14, 2), (3, 13), (13, 3), (4, 12), (12, 4), (5, 11), (11, 5), (6, 10), (10, 6), (7, 9), (9, 7), (8, 8)],
            2: [(1, 16), (16, 1), (2, 15), (15, 2), (3, 14), (14, 3), (4, 13), (13, 4), (5, 12), (12, 5), (6, 11), (11, 6), (7, 10), (10, 7), (8, 9), (9, 8)]
        }

        self.len18 = {
            13: [(1, 4), (4, 1), (3, 2), (2, 3)],
            12: [(1, 5), (5, 1), (2, 4), (4, 2), (3, 3)],
            11: [(1, 6), (6, 1), (2, 5), (5, 2), (3, 4), (4, 3)],
            10: [(1, 7), (7, 1), (2, 6), (6, 2), (3, 5), (5, 3), (4, 4)],
            9: [(1, 8), (8, 1), (2, 7), (7, 2), (3, 6), (6, 3), (4, 5), (5, 4)],
            8: [(1, 9), (9, 1), (2, 8), (8, 2), (3, 7), (7, 3), (4, 6), (6, 4), (5, 5)],
            7: [(1, 10), (10, 1), (2, 9), (9, 2), (3, 8), (8, 3), (4, 7), (7, 4), (5, 6), (6, 5)],
            6: [(1, 11), (11, 1), (2, 10), (10, 2), (3, 9), (9, 3), (4, 8), (8, 4), (5, 7), (7, 5), (6, 6)],
            5: [(1, 12), (12, 1), (2, 11), (11, 2), (3, 10), (10, 3), (4, 9), (9, 4), (5, 8), (8, 5), (6, 7), (7, 6)],
            4: [(1, 13), (13, 1), (2, 12), (12, 2), (3, 11), (11, 3), (4, 10), (10, 4), (5, 9), (9, 5), (6, 8), (8, 6), (7, 7)],
            3: [(1, 14), (14, 1), (2, 13), (13, 2), (3, 12), (12, 3), (4, 11), (11, 4), (5, 10), (10, 5), (6, 9), (9, 6), (7, 8), (8, 7)],
            2: [(1, 15), (15, 1), (2, 14), (14, 2), (3, 13), (13, 3), (4, 12), (12, 4), (5, 11), (11, 5), (6, 10), (10, 6), (7, 9), (9, 7), (8, 8)],
        }

        self.len17 = {
            12: [(1, 4), (4, 1), (3, 2), (2, 3)],
            11: [(1, 5), (5, 1), (2, 4), (4, 2), (3, 3)],
            10: [(1, 6), (6, 1), (2, 5), (5, 2), (3, 4), (4, 3)],
            9: [(1, 7), (7, 1), (2, 6), (6, 2), (3, 5), (5, 3), (4, 4)],
            8: [(1, 8), (8, 1), (2, 7), (7, 2), (3, 6), (6, 3), (4, 5), (5, 4)],
            7: [(1, 9), (9, 1), (2, 8), (8, 2), (3, 7), (7, 3), (4, 6), (6, 4), (5, 5)],
            6: [(1, 10), (10, 1), (2, 9), (9, 2), (3, 8), (8, 3), (4, 7), (7, 4), (5, 6), (6, 5)],
            5: [(1, 11), (11, 1), (2, 10), (10, 2), (3, 9), (9, 3), (4, 8), (8, 4), (5, 7), (7, 5), (6, 6)],
            4: [(1, 12), (12, 1), (2, 11), (11, 2), (3, 10), (10, 3), (4, 9), (9, 4), (5, 8), (8, 5), (6, 7), (7, 6)],
            3: [(1, 13), (13, 1), (2, 12), (12, 2), (3, 11), (11, 3), (4, 10), (10, 4), (5, 9), (9, 5), (6, 8), (8, 6), (7, 7)],
            2: [(1, 14), (14, 1), (2, 13), (13, 2), (3, 12), (12, 3), (4, 11), (11, 4), (5, 10), (10, 5), (6, 9), (9, 6), (7, 8), (8, 7)]
        }

        self.len16 = {
            11: [(1, 4), (4, 1), (3, 2), (2, 3)],
            10: [(1, 5), (5, 1), (2, 4), (4, 2), (3, 3)],
            9: [(1, 6), (6, 1), (2, 5), (5, 2), (3, 4), (4, 3)],
            8: [(1, 7), (7, 1), (2, 6), (6, 2), (3, 5), (5, 3), (4, 4)],
            7: [(1, 8), (8, 1), (2, 7), (7, 2), (3, 6), (6, 3), (4, 5), (5, 4)],
            6: [(1, 9), (9, 1), (2, 8), (8, 2), (3, 7), (7, 3), (4, 6), (6, 4), (5, 5)],
            5: [(1, 10), (10, 1), (2, 9), (9, 2), (3, 8), (8, 3), (4, 7), (7, 4), (5, 6), (6, 5)],
            4: [(1, 11), (11, 1), (2, 10), (10, 2), (3, 9), (9, 3), (4, 8), (8, 4), (5, 7), (7, 5), (6, 6)],
            3: [(1, 12), (12, 1), (2, 11), (11, 2), (3, 10), (10, 3), (4, 9), (9, 4), (5, 8), (8, 5), (6, 7), (7, 6)],
            2: [(1, 13), (13, 1), (2, 12), (12, 2), (3, 11), (11, 3), (4, 10), (10, 4), (5, 9), (9, 5), (6, 8), (8, 6), (7, 7)]
        }

        self.len15 = {
            10: [(1, 4), (4, 1), (3, 2), (2, 3)],
            9: [(1, 5), (5, 1), (2, 4), (4, 2), (3, 3)],
            8: [(1, 6), (6, 1), (2, 5), (5, 2), (3, 4), (4, 3)],
            7: [(1, 7), (7, 1), (2, 6), (6, 2), (3, 5), (5, 3), (4, 4)],
            6: [(1, 8), (8, 1), (2, 7), (7, 2), (3, 6), (6, 3), (4, 5), (5, 4)],
            5: [(1, 9), (9, 1), (2, 8), (8, 2), (3, 7), (7, 3), (4, 6), (6, 4), (5, 5)],
            4: [(1, 10), (10, 1), (2, 9), (9, 2), (3, 8), (8, 3), (4, 7), (7, 4), (5, 6), (6, 5)],
            3: [(1, 11), (11, 1), (2, 10), (10, 2), (3, 9), (9, 3), (4, 8), (8, 4), (5, 7), (7, 5), (6, 6)],
            2: [(1, 12), (12, 1), (2, 11), (11, 2), (3, 10), (10, 3), (4, 9), (9, 4), (5, 8), (8, 5), (6, 7), (7, 6)]
        }

        self.len14 = {
            9: [(1, 4), (4, 1), (3, 2), (2, 3)],
            8: [(1, 5), (5, 1), (2, 4), (4, 2), (3, 3)],
            7: [(1, 6), (6, 1), (2, 5), (5, 2), (3, 4), (4, 3)],
            6: [(1, 7), (7, 1), (2, 6), (6, 2), (3, 5), (5, 3), (4, 4)],
            5: [(1, 8), (8, 1), (2, 7), (7, 2), (3, 6), (6, 3), (4, 5), (5, 4)],
            4: [(1, 9), (9, 1), (2, 8), (8, 2), (3, 7), (7, 3), (4, 6), (6, 4), (5, 5)],
            3: [(1, 10), (10, 1), (2, 9), (9, 2), (3, 8), (8, 3), (4, 7), (7, 4), (5, 6), (6, 5)],
            2: [(1, 11), (11, 1), (2, 10), (10, 2), (3, 9), (9, 3), (4, 8), (8, 4), (5, 7), (7, 5), (6, 6)]
        }

        self.len13 = {
            8: [(1, 4), (4, 1), (3, 2), (2, 3)],
            7: [(1, 5), (5, 1), (2, 4), (4, 2), (3, 3)],
            6: [(1, 6), (6, 1), (2, 5), (5, 2), (3, 4), (4, 3)],
            5: [(1, 7), (7, 1), (2, 6), (6, 2), (3, 5), (5, 3), (4, 4)],
            4: [(1, 8), (8, 1), (2, 7), (7, 2), (3, 6), (6, 3), (4, 5), (5, 4)],
            3: [(1, 9), (9, 1), (2, 8), (8, 2), (3, 7), (7, 3), (4, 6), (6, 4), (5, 5)],
            2: [(1, 10), (10, 1), (2, 9), (9, 2), (3, 8), (8, 3), (4, 7), (7, 4), (5, 6), (6, 5)]
        }

        self.len12 = {
            7: [(1, 4), (4, 1), (3, 2), (2, 3)],
            6: [(1, 5), (5, 1), (2, 4), (4, 2), (3, 3)],
            5: [(1, 6), (6, 1), (2, 5), (5, 2), (3, 4), (4, 3)],
            4: [(1, 7), (7, 1), (2, 6), (6, 2), (3, 5), (5, 3), (4, 4)],
            3: [(1, 8), (8, 1), (2, 7), (7, 2), (3, 6), (6, 3), (4, 5), (5, 4)],
            2: [(1, 9), (9, 1), (2, 8), (8, 2), (3, 7), (7, 3), (4, 6), (6, 4), (5, 5)]
        }

        self.len11 = {
            6: [(1, 4), (4, 1), (3, 2), (2, 3)],
            5: [(1, 5), (5, 1), (2, 4), (4, 2), (3, 3)],
            4: [(1, 6), (6, 1), (2, 5), (5, 2), (3, 4), (4, 3)],
            3: [(1, 7), (7, 1), (2, 6), (6, 2), (3, 5), (5, 3), (4, 4)],
            2: [(1, 8), (8, 1), (2, 7), (7, 2), (3, 6), (6, 3), (4, 5), (5, 4)]
        }

        self.len10 = {
            5: [(1, 4), (4, 1), (3, 2), (2, 3)],
            4: [(1, 5), (5, 1), (2, 4), (4, 2), (3, 3)],
            3: [(1, 6), (6, 1), (2, 5), (5, 2), (3, 4), (4, 3)],
            2: [(1, 7), (7, 1), (2, 6), (6, 2), (3, 5), (5, 3), (4, 4)]
        }

        self.len9 = {
            5: [(1, 3), (3, 1), (2, 2)],
            4: [(1, 4), (4, 1), (2, 3), (3, 2)],
            3: [(1, 5), (5, 1), (2, 4), (4, 2), (3, 3)],
            2: [(1, 6), (6, 1), (2, 5), (5, 2), (3, 4), (4, 3)],     
        }

        self.len8 = {
            4: [(1, 3), (3, 1), (2, 2)],
            3: [(1, 4), (4, 1), (3, 2), (2, 3)],
            2: [(1, 5), (5, 1), (2, 4), (4, 2), (3, 3)],
        }

    def get_nonalpha_table(self, length):
        if length == 20:
            return self.len20
        elif length == 19:
            return self.len19
        elif length == 18:
            return self.len18
        elif length == 17:
            return self.len17
        elif length == 16:
            return self.len16
        elif length == 15:
            return self.len15
        elif length == 14:
            return self.len14
        elif length == 13:
            return self.len13
        elif length == 12:
            return self.len12
        elif length == 11:
            return self.len11
        elif length == 10:
            return self.len10
        elif length == 9:
            return self.len9
        elif length == 8:
            return self.len8
        else:
            raise ValueError("Invalid password length")



