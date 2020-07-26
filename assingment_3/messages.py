class Event:
    def __init__(self, src, dst, name):
        self.src = src
        self.name = name

class Message(Event):
    def __init__(self, *event_var_dic, **kwargs):
        # This allows a dict to be passed.
        # all the keys will be turned into variables with it old value as it's value.
        # at the same time keyword arguments are still also possible.
        # the reason for all of this is to reduce line space at the initialization
        # and this way all the values from a old event can be put in a dict and
        # that dict can be passed in one go to this new event 
        for dic in event_var_dic:
            for key in dic:
                setattr(self, key, dic[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])

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