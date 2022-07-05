def make_dictionary(givenList,givenTuple):
    givenTuple = list(givenTuple)
    res = zip(givenList,givenTuple)
    return dict(res)
print(make_dictionary([50,10,62],("Borey","Thirak","Dane")))