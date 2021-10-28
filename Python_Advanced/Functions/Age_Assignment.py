def age_assignment(*args, **kwargs):
    dict = {}
    for i in args:
        for e, v in kwargs.items():
            if i[0] == e:
                dict1 = {i: v}
                dict.update(dict1)
    return dict


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))