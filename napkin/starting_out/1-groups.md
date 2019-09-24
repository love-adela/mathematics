# Groups (군, 군론)

group(군)은 고등수학에서 가장 기본적인 구조 중 하나다.

* 학습목표
  * group이란?
  * 언제 두 group이 같다고 하는가?

## 1.1 Definition and examples of groups

### Prototypical example for this section

*The additive group of integers (Z, +) and the cyclic group Z/mz. Just don't let yourself forget that most groups are non-commutative.*

### Introduction

A group consists of two pieces of data: a set G, and an associative binary operation `⭐️` with some properties.

### Example 1.1.1 (Additive integers)

The pair (Z, +) is a group: Z = {..., -2, -1, 0, 1, 2, ...} is the set and the associative operation is addition.

Note that

* The element 0 ∈ Z is an identity: a + 0 = 0 + a for any a.
* Every element a ∈ Z has an additive inverse : a + (-a) = (-a) + a = 0
We call this group Z.

### Example 1.1.2

TODO

### Definition 1.1.3

A *group* is a pair G = (G, ⭐️) consisting of a set of elements G, and a binary operation ⭐️ on G, such that:

* G has an *identity element*, usually denoted 1G or just 1, with the property that 1G ⭐️g = g ⭐️1G = g for all g∈G.
* The operation is associative, meaning (a⭐b)⭐c = a⭐(b⭐c) for any a, b, c ∈ G. Consequently we generally don't write the parentheses.  
* Each element g G has an *inverse*, that is, an element h G such that `g⭐️h = h⭐️g = 1G`

---

### Additive Group (가군)

[출처](http://mathworld.wolfram.com/AdditiveGroup.html)

#### (1) Definition

An additive group is a group where the operation is called addition and denoted `+`.

#### (2) Condition

In an additive group, the **identity element** is called zero, and the **inverse of the element** a is denoted -a (minus a). The symbols and terminology are borrowed from the additive groups of numbers: the ring of integers Z, the field of rational numbers Q, the field of real numbers R, and the field of complex numbers C are all additive groups.

#### (3) Types of additive groups

Modules, abstract vector spaces, and algebras are all additive groups.

The sum of vectors of the vector space R^n is defined componentwise, and so is the sum of n * m matrices with entries in a ring R, which is part of the R-module structure of the set of matrices Mnm(R).

---

### Quotient Group

For a group G and a normal subgroup N of G, the quotient group of N in G, written G/N and read "G modulo N", is the set of cosets of N in G. Quotient groups are also called factor groups. The elements of G/N are written Na and form a group under the normal operation on the group N on the coefficient a. Thus `(Na)(Nb) = Nab.

Any *quotient group* G/H of an Abelian additive group G is again an additive group with respect to the induced addition of cosets, defined by `(a + H) + (b + H) = (a+b) + H` for all a, b∈ G

---

### Abelian Group

An abelian group is a group for which the elements commute (i.e., AB = BA for all elements A and B)
