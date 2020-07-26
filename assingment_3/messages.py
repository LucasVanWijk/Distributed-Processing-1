class Event:
    def __init__(self, src, dst, name, pro_number, value):
        self.src = src
        self.dst = dst
        self.name = name
        self.pro_number = pro_number
        self.value = value


# class Prepare(Event):
#     def __init__(self, src, dst, name, pro_number, value):
#         super().__init__(src, dst, name)




# class Propose(Event):
#     def __init__(self, src, dst, name, pro_number, value):
#         super().__init__(src, dst, name)
#         self.pro_number = pro_number
#         self.value = value


# class Promise(Event):
#     def __init__(self, src, dst, name, pro_number, prior):
#         super().__init__(src, dst, name)
#         self.pro_number = pro_number
#         self.prior = prior


# class Accept(Event):
#     def __init__(self, src, dst, name, pro_number, value):
#         super().__init__(src, dst, name)
#         self.pro_number = pro_number
#         self.value = value

# class Accepted(Event):
#     def __init__(self, src, dst, name, pro_number, value):
#         super().__init__(src, dst, name)
#         self.pro_number = pro_number
#         self.value = value

# class Rejected(Event):
#     def __init__(self, src, dst, name, pro_number, value):
#         super().__init__(src, dst, name)
#         self.pro_number = pro_number
#         self.value = value