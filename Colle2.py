def echange(T,a,b):
	c=T[a]
	T[a]=T[b]
	T[b]=c

def Tri(T,i,a,b):
	if(i==b):
		return;
	else:
		if (T[i]=='B'):
			echange(T,i,a)
			print(T)
			Tri(T,i,a+1,b)
		elif (T[i]=='R'):
			echange(T,i,b)
			print(T)
			Tri(T,i,a,b-1)
		else:
			print(T)
			Tri(T,i+1,a,b)

T=['C','B','B','R','B','R','C','B','R','C','B']
Tri(T,0,0,10)
print(T)

