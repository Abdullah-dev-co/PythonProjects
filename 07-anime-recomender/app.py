import random

print("ANIME RECOMENDOR ")
genres = {
    "shonen" :["Dragon Ball","One Piece","Naruto","Bleach"],
    "senin" : ["Berserk","Vinland Saga"],
    "isekai" : ["Rezero","Mushokotensi","chillin"]
}
choice = input("Enetr your anime genre (shonen/senin/isekai):\n ").lower().strip()
if choice not in genres:
    print("I don't have that genre!")
else:
    print(f"check out {random.choice(genres[choice])}")

