Letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789(),.-!?\"' "


def read_data(fname):
    exemplars = []
    file = open(fname, 'r')
    for line in file:
        data = tuple([w.lower() for w in line.split()])
        exemplars += [(data[0::2])]
    file.close()
    return exemplars


p_l_l1 = {}

for c in Letters:
    p_l_l1[c] = {}
    for c1 in Letters:
        p_l_l1[c][c1] = 0.0

data = read_data('bc.train')

prior_prob = {}
trans_prob = {}

for line in data:
    temp = ' '.join(line)
    for character in temp:
        # print character
        if character not in Letters:
            continue

        if character in prior_prob.keys():
            prior_prob[character] = prior_prob[character] + 1
            # print character, prior_prob[character]
        else:
            prior_prob[character] = 1
            # print character, "else" , prior_prob[character]
            # break

total_characters = sum(prior_prob.values())

for keys in prior_prob.keys():
    prior_prob[keys] = (prior_prob[keys] / float(total_characters))

# #print prior_prob.items(), " \nlength is: ", len(prior_prob), "\n Total charaters are: ", total_characters
# Prior Probability calculation ends here. The probabilities are stored in the prior_prob dictionary.

# print prior_prob

# Starting the calculations for Transition probability.
for line in data:
    temp = ' '.join(line)
    # print temp[4]
    for index in range(0, len(temp) - 1):
        character = temp[index]
        if temp[index] not in trans_prob.keys():
            trans_prob[character] = {temp[index + 1]: 1}
        else:
            next_char = temp[index + 1]
            if next_char in trans_prob[character].keys():
                trans_prob[character][next_char] = trans_prob[character][next_char] + 1
            else:
                trans_prob[character][next_char] = 1

# #print trans_prob
# print " hello ",trans_prob['1']['t'], trans_prob['I']['t']
# # for e in trans_prob.items():
# #     print e
#
#

for key in trans_prob.keys():
    total = sum(trans_prob[key].values())
    # print total
    for i in trans_prob[key].keys():
        trans_prob[key][i] = (trans_prob[key][i] / float(total))
        print key, " ", trans_prob[key]
