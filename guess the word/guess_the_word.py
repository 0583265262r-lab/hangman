import random
WORDS = [
    "apple", "banana","water", "house", "table", "chair", "window",
    "school", "teacher", "student", "pencil", "paper",
    "computer", "keyboard", "mouse", "screen", "phone",
    "music", "guitar", "piano", "drum", "song",
    "river", "ocean", "beach", "mountain", "forest",
    "animal", "tiger", "lion", "zebra", "monkey",
    "rabbit", "horse", "sheep", "goat", "camel",
    "bird", "eagle", "snake", "fish", "shark",
    "pizza", "bread", "cheese", "salad", "soup",
    "coffee", "sugar", "honey", "butter", "cookie"]    
MAX_TRIES = 6
# הפונקציה מחזירה הודעת פתיחה למשחק
def enter_of_game():
    return "Welcome to the game Guess the Word"
# הפונקציה בוחרת מילה רנדומלית 
def choose_word(list_of_words):
    choosing_word=random.choice(list_of_words)
    return choosing_word

# קריאה לפנקצית בחירת מילה ותפיסת המילה ע"י משתנה
the_choose_word=choose_word(WORDS)


# פונקציה המחזירה את אורך המילה במערך כי אז יותר קל לרוץ על אינדקסים 
# ולבודד כל אות בפני עצמה
def showing_the_characters_of_the_hidden_word_to_the_player():
    hidden_word=the_choose_word
    list_of_the_characters=[]
    for char in range(len(hidden_word)):
        list_of_the_characters.append("_")
    return list_of_the_characters
# קריאה לפונקציית אורך המילה ותפיסה שלה ע"י משתנה
hidden_word=showing_the_characters_of_the_hidden_word_to_the_player()


# פונקציה המבקשת קלט מהמשתמש ומחיזרה אותו באות קטנה כדי לא שלא יהיו בעיות אם יכניס אות גדולה
def get_guess_from_the_user():
    guess_of_the_user=input("please enter your guess: ")
    return guess_of_the_user.lower()


def checking_the_correctness_of_the_guess(the_choose_word,hidden_word,the_choosen_char):
    if the_choosen_char not in the_choose_word:
        return False
    else:
        for i in range(len(the_choose_word)):
            if the_choose_word[i] == the_choosen_char:
                hidden_word[i]=the_choosen_char
        return True




def checking_the_correctness_of_the_character():
    counter=0
    attempts=6
    list_of_chars=[]
    while counter< MAX_TRIES:
        list_word=[l for l in the_choose_word]
        if list_word == hidden_word:
            return f"the word is {the_choose_word} \nHow wonderful you won"
        print(f"You have {attempts} attempts left")
        
        
        guess_of_the_player= get_guess_from_the_user()
        
        if guess_of_the_player not in list_of_chars:
           list_of_chars.append(guess_of_the_player)
           print(list_of_chars)
        else:
            counter-=1
            attempts+=1
        if len(guess_of_the_player)==1 and guess_of_the_player.isalpha():

            if not checking_the_correctness_of_the_guess(the_choose_word,hidden_word,guess_of_the_player):
                print(hidden_word)
                counter+=1
                attempts-=1
            else:
                 print(hidden_word)
                 continue
        else:
            print(hidden_word)
    if counter == MAX_TRIES:
        return f"the word was {the_choose_word} \nGAME OVER"
    
def printer():
    print(enter_of_game())
    print(hidden_word)
    print(checking_the_correctness_of_the_character())


def main():
    printer()



if __name__ == "__main__":
    main()







        




























































