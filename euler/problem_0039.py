# Integer right triangles
# 
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three
# solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?

"""
Solution Approach :
===================

* The basic idea of a right angled triangle is that it satisfies the pythagoras theorem.
* so, if 'a', 'b' and 'c' are three sides of the triangle then
    * a^2 + b^2 = c^2
    * p = a + b + c
    * c = p-a-b; c^2 = (p-a-b)^2 = (p-a-b)(p-a-b) = p^2-pa-pb-pa+a^2+ab-pb+ab+b^2 = p^2+a^2+b^2-2pa-2pb+2ab
    * c = p^2+a^2+b^2+2(ab-p(a+b))
    * p-a-b = p^2+a^2+b^2+2ab-2pa-2pb
    * b = p-a-p^2-a^2-b^2-2ab+2pa+2pb
    * b+b^2+2ab-2pb = p-a-a^2+2pa-p^2
    * b(1+b+2a-2b) = p-a(1+a-2p+p)
    * b = p(1-a(1+a-2p+p)/(1+b+2a-2b)
    * b = p^2 - 2ap / 2p-2a = p(p-2a)/2(p-a)
* With an assumption that (a+b) > c we can reduce the iteration as p/(2+sqrt(2))
* Also the perimeter is an even number
"""


def get_max_possible_right_triangle(max_perimeter):
    sides_max = perimeter_max = 0
    for p in range(max_perimeter // 4 * 2, max_perimeter + 1, 2):
        sides = 0;
        for a in range(2, int(p / 3.4142) + 1):
            if p * (p - 2 * a) % (2 * (p - a)) == 0:
                sides += 1
                if sides > sides_max: sides_max, perimeter_max = sides, p
    return perimeter_max


print(get_max_possible_right_triangle(1000))
