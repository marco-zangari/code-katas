"""Order of Weight, Codewars Kata, level 7. Incomplete as of Jan. 19, 2017."""


def order_weight(li):
    """Return the lightest to heaviest grams, kg, to Tonnes.

    input = list of strings
    output = list of strings
    ex: "200G","300G","150G","100KG" => ["150G","200G","300G","100KG"]
    """
    output = []
    g = []
    kg = []
    t = []
    for el in li:
        if el[-1] == 'T':
            t.append(el[:-1])
        if el[-1] == 'G':
            if el[-2] == 'K':
                kg.append(el[:-2])
            else:
                g.append(el[:-2])
    stg = sorted(g)
    stkg = sorted(kg)
    stt = sorted(t)
    for g in stg:
        output.append(g + 'G')
    for kg in stkg:
        output.append(kg + 'KG')
    for t in stt:
        output.append(stt + 'T')

    return output


def order_weight2(li):
    """."""
    for el in li:
        if weight_converter(el) > weight_converter(el):

    g = []
    kg = []
    t = []
    for el in li:
        if el[-1] == 'T':
            t.append(int(el[:-1]))
        if el[-1] == 'G':
            if el[-2] == 'K':
                kg.append(int(el[:-2]))
            else:
                g.append(int(el[:-1]))


def weight_converter(li):
    """."""
    output = []
    for el in li:
        if el[-1] == 'T':
            output.append(int(el[:-1]) * 1000000)
        if el[-1] == 'G':
            if el[-2] == 'K':
                output.append(int(el[:-2]) * 1000)
            else:
                output.append(int(el[:-1]) * 1)
    return sorted(output)
