#CITE SOURCE
#helper function for find_artist (calculates similarity of genre lists)
import math

def counter_cosine_similarity(c1, c2):
    terms = set(c1).union(c2)
    dotprod = sum(c1.get(k, 0) * c2.get(k, 0) for k in terms)
    magA = math.sqrt(sum(c1.get(k, 0)**2 for k in terms))
    magB = math.sqrt(sum(c2.get(k, 0)**2 for k in terms))
    if (magA == 0 or magB == 0):
        return 0
    else:
        return dotprod / (magA * magB)