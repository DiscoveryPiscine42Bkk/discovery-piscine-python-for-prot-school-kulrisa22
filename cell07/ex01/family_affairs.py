def find_the_redheads(family_members):

    redheads = list(filter(lambda member: family_members[member] == "red", family_members))
    return redheads

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))