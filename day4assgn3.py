import random

def movies(*names):
	result=random.sample(names,2)
	print("recomded movies are:",' , '.join(result))

movie_type=input("enter movie type:-")
if movie_type=="action":
	movies('Logan','Avengers: Endgame','Mission: Impossible','The 39 Steps','The Terminator','X-Men: Days of Future Past')
	print(movies)
elif movie_type=="animation":
	movies('Spirited Away','Zootopia','Inside Out','Coco',' Paddington 2','Up')
	print(movies)
elif movie_type=="thrillers":
	movies('Frequency','Chasing Sleep','Session 9','Chinatown','The Third Man','Touch of Evil')
	print(movies)
elif movie_type=="drama":
	movies('Les Diaboliques','Zodiac','Mulholland Drive','Taxi Driver','Seven','The Conversation ')
	print(movies)
elif movie_type=="romcom":
	movies('Her','Always Be My Maybe','Chasing Amy','As Good As It Gets','Shes All That','Funny Face')
	print(movies)
else:
	print("sorry.wrong movie type")
