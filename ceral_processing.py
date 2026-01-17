scary_cereals = ['Cap \'n Creep','Quaking Oats', 'Tales of the Crisp','Boo Berry','Frightful Flakes']
monster_cereals = ['Apple Dracs','Ymmy Mummy','Count Chocula','Frute Brute','Franken Berry']
psycho_cereals = ['Chucky Harms','Fruity Krueger','Sugar Chops','Machete Mateys','Scream of Wheat']

def process_cereals(cereals):
    for cereal in cereals:
        cereal_name = cereal.split(' ')
        first = cereal_name[0]
        last=cereal_name[-1]
        #if the first or last word of the cereal has Berry - Add 'How Berry Scary'
        if first == 'Berry' or last=='Berry':
            print(f'{cereal} - How Berry Scary!')
        # if the first and last word of the cereal has C - Add 'CC is Double Creepy'
        elif first.startswith('C') and last.startswith('C'):
            print(f'{cereal} - CC is Double Creepy')
        # if the first or the last word of the cereal has C - Add'C is for Creepy'
        elif first.startswith('C') or last.startswith('C'):
            print(f'{cereal} - C is for Creepy')
        # If last three letters are same; rhyme Add - 'Very Scary Rhyme! at the end'
        elif first[-1:-4:-1]==last[-1:-4:-1]:
            print(f'{cereal} - Very Scary Rhyme!')
        # If the first and last words starts with same letter Add - 'Alarming Alliteration'
        elif first[0] == last[0]:
            print(f'{cereal} - Alarming Alliteration')
        # If cases satisfy both condition - precedence - Berry over alliteration; Double C over alliteration
        # If none of the rules apply then print the name of the cereal
        else:
            print(f'{cereal}')




process_cereals(psycho_cereals)

