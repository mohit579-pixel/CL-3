import numpy as np

A = {'x1': 0.6, 'x2': 0.8, 'x3': 1.0}
B = {'x1': 0.3, 'x2': 0.9, 'x3': 0.5}

def fuzzy_union(A, B):
    union = {}
    all_keys = set(A.keys()).union(B.keys())
    for key in all_keys:
        val_a = A.get(key, 0)
        val_b = B.get(key, 0)
        union[key] = max(val_a, val_b)
    return union

def fuzzy_intersection(A, B):
    intersection = {}
    common_keys = set(A.keys()).intersection(B.keys())
    for key in common_keys:
        val_a = A[key]
        val_b = B[key]
        intersection[key] = min(val_a, val_b)
    return intersection

def fuzzy_complement(A):
    complement = {}
    for key in A:
        complement[key] = 1 - A[key]
    return complement

def fuzzy_difference(A, B):
    difference = {}
    for key in A:
        val_a = A[key]
        val_b = B.get(key, 0)
        difference[key] = min(val_a, 1 - val_b)
    return difference

def cartesian_product(A, B):
    product = {}
    for a_key in A:
        for b_key in B:
            membership = min(A[a_key], B[b_key])
            product[(a_key, b_key)] = membership
    return product

def max_min_composition(R1, R2, X, Z):
    result = {}
    for x in X:
        for z in Z:
            min_list = []
            for y1 in ['y1', 'y2']:  
                key1 = (x, y1)
                key2 = (y1, z)
                if key1 in R1 and key2 in R2:
                    min_val = min(R1[key1], R2[key2])
                    min_list.append(min_val)
            if min_list:
                result[(x, z)] = max(min_list)
            else:
                result[(x, z)] = 0
    return result

print("Fuzzy Union:")
union_result = fuzzy_union(A, B)
for key in union_result:
    print(f"{key}: {union_result[key]}")

print("\nFuzzy Intersection:")
intersection_result = fuzzy_intersection(A, B)
for key in intersection_result:
    print(f"{key}: {intersection_result[key]}")

print("\nFuzzy Complement of A:")
complement_result = fuzzy_complement(A)
for key in complement_result:
    print(f"{key}: {complement_result[key]}")

print("\nFuzzy Difference (A - B):")
difference_result = fuzzy_difference(A, B)
for key in difference_result:
    print(f"{key}: {difference_result[key]}")

print("\nCartesian Product (Fuzzy Relation of A and B):")
relation_AB = cartesian_product(A, B)
for key in relation_AB:
    print(f"{key}: {relation_AB[key]}")

X = ['x1', 'x2']
Z = ['z1', 'z2']
R1 = {
    ('x1', 'y1'): 0.5,
    ('x1', 'y2'): 0.7,
    ('x2', 'y1'): 0.6,
    ('x2', 'y2'): 0.8
}
R2 = {
    ('y1', 'z1'): 0.6,
    ('y1', 'z2'): 0.3,
    ('y2', 'z1'): 0.9,
    ('y2', 'z2'): 0.5
}

print("\nMax-Min Composition (R1 ○ R2):")
composition_result = max_min_composition(R1, R2, X, Z)
for key in composition_result:
    print(f"{key}: {composition_result[key]}")
