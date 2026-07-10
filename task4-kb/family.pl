% Male facts
male(john).
male(mike).
male(david).
male(robert).
male(kevin).

% Female facts
female(mary).
female(lisa).
female(susan).
female(emma).
female(anna).

% Parent facts
parent(john, mike).
parent(mary, mike).
parent(john, lisa).
parent(mary, lisa).
parent(mike, david).
parent(susan, david).
parent(lisa, emma).
parent(robert, emma).
parent(david, kevin).
parent(anna, kevin).

% Rules
grandparent(X, Z) :-
    parent(X, Y),
    parent(Y, Z).

sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.
