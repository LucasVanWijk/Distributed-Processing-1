class Computer:
    def __init__(self, number):
        self.number = number
        self.failed = False
        self.decisions = []

    def handel_messsage(self, m):
        if self.failed is False:
            m.message_type.handel(self)

    def flip_failed(self):
        self.failed = not self.failed


class Accepter(Computer):
    def __init__(self, number):
        super().__init__(number)
        self.highest_prop_num = None
        self.consensus_val = None


class Proposer(Computer):
    def __init__(self, number):
        super().__init__(number)
        self.number_proposals = 1
        self.promise_list = []
        self.pro_number = 0
        self.value = 0
        self.accpeters = []



