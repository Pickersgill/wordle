import numpy as np

words = np.loadtxt("./words.txt", dtype=str, ndmin=2)
words = np.array(list(filter(lambda x : len(set(x[0])) == len(x[0]), words)))
word_mat = np.ones((len(words), 5), dtype=str)

for i, w in enumerate(words):
    r = np.array(list(w[0]))
    word_mat[i, :] = r

M = np.zeros((5, 26))

def as_int(char):
    return ord(char) - 97

for word in word_mat:
    for j in range(len(word)):
        M[j, as_int(word[j])] += 1

greenM = np.transpose(np.transpose(M) / np.sum(M, axis=1))
yellM = np.sum(M, axis=0) / (len(word_mat) * 5)

def joint(M, word):
    p = M[0, as_int(word[0])]
    for i in range(1, len(word)):
        p += M[i, as_int(word[i])]

    return p

ma = 0
ma_w = None

for w in word_mat:
    w = "".join(w)
    nm = joint(greenM, w)
    if ma_w is None or nm > ma:
        ma = nm
        ma_w = w

print("Optimal word if seeking highest likelihood of green hints.", ma_w)

ma = 0
ma_w = None

for w in word_mat:
    w = list(map(as_int, w))
    nm = np.sum(yellM[w])
    if ma_w is None or nm > ma:
        ma = nm
        ma_w = w

ma_w = "".join([chr(int(x) + 97) for x in ma_w])
print("Optimal word if seeking highest likelihood of yellow hints.", ma_w)


def H_joint(h, word):
    p = 0
    for i, letter in enumerate(w):
        g_p = greenM[i, as_int(letter)]
        y_p = yellM[as_int(letter)]
        p += (h * g_p + (1-h) * y_p)

    return p

for h in np.arange(0, 1, 0.2):
    ma = 0
    ma_w = None

    for w in word_mat:
        nm = H_joint(h, w)
        word = "".join(w)
        if ma_w is None or nm > ma:
            ma = nm
            ma_w = word

    print("H =", h, ": optimal word is: ", ma_w)


print("Independent optimal for green: ", "".join([chr(int(x) +97) for x in greenM.argmax(axis=1)]))
print("Independent optimal for yellow: ", "".join([chr(int(x)+97) for x in yellM.argsort()[:-11:-1]]))


