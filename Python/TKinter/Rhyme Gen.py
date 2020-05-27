import random

print("Let me sing you a nursery rhyme!")

rhymes = [
        {
            "title" : "Old McDonald",
            "rhyme" : """Old McDonald had a farm. E-I-E-I-O
He lost his farm when he lost his wife. E-I-E-I-O
A lawsuit here! A lawsuit there!
Here a lawsuit! There a lawsuit! Everywhere a lawsuit!
Old McDonald had a farm. E-I-E-I..oh..."""
        },
        {
            "title" : "Little Ms. Muffit",
            "rhyme" : """Little Ms. Muffit, sat on her tuffit, eating her curds and weigh.
She had a cider, that went down inside her, and is poisioning her liver today."""
        },{
            "title" : "The Itsy-bitsy spider",
            "rhyme" : """The itsy bitsy spider went upto to Barney's house. Down came the pain that washed poor Barney out.
Up came the sunshine that dried up all the blood.
That itsy bitsy spider, that """
        }
    ]

num = random.randint(1, len(rhymes)) - 1
print("\n\n\n")
print(rhymes[num]['rhyme'])
