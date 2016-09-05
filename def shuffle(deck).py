import random

def shuffle(deck):
	N = len(deck)
	for i in range(N-1):
		swap(deck,i,deckrandom.randrang(i,N))

def swap(deck,i,j):
	return deck[i],deck[j] = deck[j],deck[i]