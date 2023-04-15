import io
import string
import random
import nltk
import pickle
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# arrays for essage
error_messages = ["Sorry, I didn't quite catch that. Can you try again?", "Oops, I didn't understand what you said. Run it by me again?", "My bad, your message went right over my head. Would you mind trying again?"]
champ_names = []

### HANDLING CODE & KNOWLEDGE BASE FOR TFT
# unpickled dictionary that contains all TFT champions

champ_file = open("champs.p", "rb")
champ_dict = pickle.load(champ_file)
champ_file.close()

for champ_name in champ_dict.keys():
    champ_names.append(champ_name)
    
# Handling edge cases for champion names
# Edge case for Twisted Fate
champ_names.append("TF")

# Edge case for Nunu & Willump
champ_names.append("Nunu")

# Edge cases for Aurelion Sol
champ_names.append("A Sol")
champ_names.append("Asol")

# Edge case for Ultimate Ezreal
champ_names.append("Ultimate Ez")

# Edge case for Mordekaiser
champ_names.append("Morde")

# Edge case for Lee Sin
champ_names.append("Lee")

    
# Print each champion name  
# print(champ_dict)

"""
Returns the user data from the users.json file based on the given user_id.
If the user is not found in the file, returns None.
"""

class User:
    def __init__(self, name, rank, favchamp):
        self.name = name
        self.rank = rank
        self.favchamp = favchamp

def set_user_data():
    tempname = input("What's your name?")
    u = User(tempname, None, None)
    return u


# function to save user data
def respond_to_message(message, user):

    if message.lower() == user.name or "my name is" in message.lower() or "what is my name" in message.lower():
        out = ""
        if user.name is not None:
            out += "Your name is " + user.name + " "
        if user.rank is not None:
            out += "with a stored rank of " + user.rank + " "
        if user.favchamp is not None:
            out += "and you have a stored favorite champion of " + user.favchamp
        return out
    
    # Hello tag
    if message.lower() in ['hello', 'hi', 'hey', 'hi there', 'greetings', "hey there"]:
        return random.choice(['Hello!', 'Hi there!', 'Hey!', 'Hi!', "Hello! Hope you're doing well.", "Hi! Hope you have a good day!"])

    # Greeting tag
    elif message.lower() in ['how are you', "how's your day going", "what's up"]:
        return "I'm doing good! I'm here to answer your TFT questions!"
    
     # Good morning tag
    elif message.lower() in ['good morning', 'morning']:
        return random.choice(["Good morning!", "Good morning! The birds are chirping, the sun is out, and… guess I’ll play some TFT.", "Morning! It’s the perfect time to play TFT."])
 
    # Good evening tag
    elif message.lower() in ['bye', 'goodbye', 'see you later', 'see ya', 'peace', 'thank you', 'exit', 'cya', 'bye bye', 'take care', 'farewell']:
        return "Goodbye!"
    
    # Creator tag
    elif message.lower() in ['who made you', 'where are you from', 'who created you', 'who developed you', 'who are the developers', 'developers']:
        return "I was made by Meinhard Capucao and Hrithik Ochani."
    
     # Champion list tag
    elif message.lower() in ['what are the champions', 'list of champions', 'what is the list of champions', 'can you print the list of champions', 'show me the champions', 'whats the champions in this game', 'list me the champs in this game', 'what are the list of champions in this game', 'give me all the champs', 'give me the champions in this game', 'give me a list of all champions in this game']:
        return champ_names

     # Favorite champion tag
    elif message.lower() in ['your favorite champion', 'what is your favorite champion', 'which champion do you like the best', 'champion you like the best'] :
        return "My favorite champion is Blitzcrank! He’s a robot, just like me…"
    
    #General questions / knowledge tag
    
    elif 'what is' in message.lower() or "what's" in message.lower() or "explain" in message.lower() or 'let me know about' in message.lower() or 'give me an explanation' in message.lower() or 'give me a rundown' in message.lower() or 'tell me' in message.lower() or 'explain to me' or 'what is a' in message.lower() or 'what are' in message.lower():         
        tft_explanation = message.lower()
        if any(word in tft_explanation.split()[-1] for word in ['tft', 'teamfight tactics', 'tft game', "tft game about", "tft about", "teamfight tactics about", "teamfight tactics game about"]):
            return "Teamfight Tactics (TFT) is an auto battler game mode in League of Legends. It's a game where you build a team of champions, each with their own unique abilities, equip items, and fight against other teams. The goal is to be the last player standing by defeating all other players."
        elif 'champion' in message.lower() or 'champions' in message.lower():
            return "Champions can be bought from your shop, and serve as the units you play. Champions can have different costs, traits, and more information."
        elif 'ability' in message.lower() or 'abilities' in message.lower():
            return "Abilities are different unique passives that champions have in the game. They activate it once their mana bar is full."
        elif 'mana' in message.lower() or 'mana cost' in message.lower():
            return "Mana in Teamfight Tactics is a resource used by most champions. Mana usually starts at 0 and is gained by attacking or being attacked. Once a champion's mana bar is full, they cast their ability and empty their mana bar."
        elif "item" in message.lower(): 
            return "Items in Teamfight Tactics can be equipped by various champions. Champions can hold a maximum of 3 items."
        elif "best champion" in message.lower(): 
            return "There is no best champion in TFT, as the meta evolves. However, you can ask what are the winrates of certain champions, what are the tiers, or the list of all champions"
        elif "champion costs" in message.lower() or "champions cost" in message.lower(): 
            return "Champion costs are divided into: 1, 2, 3, 4, or 5. 1 costs are common, 2 are uncommon, 3 are rare, 4 are epic, and 5 are legendary. The power of the units will scale based on cost."
            
    #How to tag
    elif 'how do you' in message.lower() or 'how' in message.lower() or 'tft tutorial' in message.lower():
        if 'play tft' in message.lower() or 'does tft work' in message.lower() or 'how do i start':
                return "In TFT, you start by selecting a champion and buying other champions from the store to build a team of 5. Each champion has their own unique abilities that can be combined to create powerful synergies. Your goal is to defeat the other players' teams by managing your economy, positioning your champions strategically, and building the right team composition. You gain gold each round that you can use to buy more champions, level up your team, or buy items to make your champions stronger."
        elif 'buy units' in message.lower() or 'purchase units' in message.lower() or 'buy champions' in message.lower() or 'purchase champions' in message.lower():
                return "In TFT, you can buy units buy clicking their icon on the shop. It costs gold to buy units."
        elif "learn" in message.lower(): 
                return "The best way to learn in TFT is to watch better streamers on YouTube/Twitch. I recommend going to the community tab on twitch and finding high elo streamers"
        elif "win" in message.lower(): 
                return "You win in TFT by having more HP than the rest of your opponents. You can place 1st - 8th, and 1st - 4th is considered a win."
        
    elif 'my favorite champ' in message.lower() or 'my favorite champion' in message.lower():
     # Iterate through the champion names in the champ_names array
        for champ_name in champ_names:
                # check if the user mentioned the current champion name. also checks for edge cases for certain champions
            if champ_name.lower() in message.lower() or \
                champ_name == 'Twisted Fate' and 'tf' in message.lower() or \
                champ_name == 'Nunu & Willump' and ('nunu' in message.lower() or 'willump' in message.lower()) or \
                champ_name == 'Aurelion Sol' and ('a sol' in message.lower() or 'asol' in message.lower()) or \
                champ_name == 'Ultimate Ezreal' and ('ultimate ez' in message.lower() or 'ultimate ezreal' in message.lower()) or \
                champ_name == 'Mordekaiser' and 'morde' in message.lower() or \
                champ_name == 'Lee Sin' and ('lee' in message.lower() or 'lee sin' in message.lower()):
                    # If so, set the user's favorite champion to the current champion name
                user_favorite_champ = champ_name
                user.favchamp = user_favorite_champ
                break  # Exit the loop once a match is found
            # Check if the user mentioned a champion name
        
            if user_favorite_champ is not None:
                # check if the user's favorite champion is Syndra
                    if user_favorite_champ == 'Syndra':
                        # Return a custom message for Syndra
                        return "Syndra is an awesome champion! She's a Star Guardian Legendary who throws units onto your board."
                    elif user_favorite_champ == 'Nunu & Willump':
                        # Return a custom message for Nunu & Willump
                        return "Nunu & Willump is so cool! I like how he keeps the ball rolling, literally. He is a legendary unit that is a Gadgeteen, and is the trait breakpoint that you need to hit 5."
                    elif user_favorite_champ == 'Janna':
                        # Return a custom message for Janna
                        return "Janna is a great support champion! She is a legendary unit that is a Spellslinger, and a Forecaster. She provides unique effects, and blows away your enemies!"
                    elif user_favorite_champ == 'Fiddlesticks':
                        # Return a custom message for Fiddlesticks
                        return "Fiddlesticks is a fearsome threat unit. He fears the enemy team, and provides great utility. Spooky!"
                    elif user_favorite_champ == 'Urgot':
                        # Return a custom message for Urgot
                        return "Urgot is fearsome threat unit that can dig up treasure! He provides lots of Crowd Control due to his waves."
                    elif user_favorite_champ == 'Mordekaiser':
                        # Return a custom message for Mordekaiser
                        return "Mordekaiser is a strong champion! That can blow up teams and provide utility to everyone"
                    elif user_favorite_champ == 'Leona':
                        # Return a custom message for Leona
                        return "Leona is a great tank champion that is the legendary unit for Mecha:Prime's. She can blow up hyper tank carries by calling a sunbeam from the sky!"
                    elif user_favorite_champ == 'Ultimate Ezreal':
                        # Return a custom message for Ultimate Ezreal
                        return "Ultimate Ezreal is such a cool champion introduced in the mid-set! He is an Infiteam unit that can blow up any boards."
                    elif user_favorite_champ == 'Gnar':
                        # Return a custom message for Gnar
                        return "Gnar is a Gadgeteen unit that you can pair with hacker to the backline. I think he's cool too!"
                    elif user_favorite_champ == 'Miss Fortune':
                        # Return a custom message for Miss Fortune
                        return "Miss Fortune is amazing! Glad she's your favorite champion, she can blow up backlines as a staple in the Anima Squad tree"
                    elif user_favorite_champ == "Kai'Sa" or user_favorite_champ == 'Kaisa' or user_favorite_champ == "Kai'sa":
                        # Return a custom message
                        return "Kai'sa is amazing, I agree too! She is a star guardian unit that works well as a carry and is good single target."
                    elif user_favorite_champ == 'Poppy':
                    # Return a custom message for Poppy
                        return "Poppy is a great tank champion one cost early game. Her carry augment makes her blow up the back unit scaling of armor"
                    elif user_favorite_champ == 'Garen':
                    # Return a custom message for Garen
                        return "Garen is a great tank champion introduced in the midset! I love him too. His utility and stun is simply amazing, he's a cool defender unit"
                    elif user_favorite_champ == 'Ekko':
                    # Return a custom message for Ekko
                        return "Ekko is such a cool tankchampion! He can tank so much damage in the star guardian comp."
                    elif user_favorite_champ == 'Viego':
                    # Return a custom message for Viego
                        return "Viego is a great champion! Although he's more utility based now since he is a heart and Ox-Force is more utility, he is still cool."
                    elif user_favorite_champ == 'Pantheon':
                    # Return a custom message for Pantheon
                        return "Pantheon is so good for being a one cost. He can stun enemy champs and works well as an Infiniteam unit."
                    elif user_favorite_champ == 'Twisted Fate' or user_favorite_champ == 'TF':
                    # Return a custom message for Twisted Fate
                        return "Twisted Fate is such a cool champion! He can have a lot of builds and items as a Spellslinger and Infiniteam unit."
                    elif user_favorite_champ == 'Ezreal':
                    # Return a custom message for Ezreal
                        return "Ezreal is a cool champion, I totally agree! He can be used as an underground unit for amazing cashouts, or an early game item holder."
                    elif user_favorite_champ == 'Lucian':
                    # Return a custom message for Lucian
                        return "Lucian is a great one cost carry! I agree he's very amazing, he can blow up backlines with his projectile."
                    elif user_favorite_champ == 'Sivir':
                    # Return a custom message for Sivir
                        return "Sivir is a cool champion that's very utility based. She can definitely hold her own early game, and is a great Infiteam support!"
                    elif user_favorite_champ == 'Neeko':
                    # Return a custom message for Neeko
                        return "Neeko is such a cool champion! She synergizes well with Shojin, and as a star guardian her damage can be amazing as her frog leaps in the enemies backline."
                    elif user_favorite_champ == 'Lulu':
                    # Return a custom message for Lulu
                        return "Lulu is a great champion! As an early gadgeteen, she can definitely do a lot of work."
                    elif user_favorite_champ == 'Shen':
                    # Return a custom message for Shen
                        return "Shen is such a cool tank (although pretty overloaded). I love him too."
                    elif user_favorite_champ == 'Annie':
                    # Return a custom message for Annie
                        return "Annie is such a cool champion! She can tank so much as an Ox-Force and Spellslinger due to her traits. I love her too."
                    elif user_favorite_champ == 'Alistar':
                    # Return a custom message for Alistar
                        return "Alistar is known for his traits, but his utility and value makes me agree that he is a cool champion! "
                    elif user_favorite_champ == 'Rell':
                    # Return a custom message for Rell
                        return "Rell is such a cool champion as a star guardian! She can be really tanky and provide a lot of utility"
                    elif user_favorite_champ == 'Pyke':
                    # Return a custom message for Pyke
                        return "Pyke is a great support champion! I love how he can stun the backline and be a great unit in the Hacker Trait."
                    elif user_favorite_champ == 'Morgana':
                    # Return a custom message for Morgana
                        return "Morgana is a great support champion! I like how she can substitute as shred, and how she stuns the closest enemies!"
                    elif user_favorite_champ == 'Samira':
                    # Return a custom message for Samira
                        return "Samira is a great ADC! I like how she has the Ace trait to execute enemies, I love her too!"
                    elif user_favorite_champ == 'Nilah':
                    # Return a custom message for Nilah
                        return "Nilah is an amazing tank! She is so cool, how she can heal her team and provide insane survivability for your front line."
                    # Return a custom message for Nilah
                    elif user_favorite_champ == 'Warwick':
                        return "Warwick is such a great champion! As an Admin and Brawler, he is good at shredding backliner carries with hacker, or you can evenuse him as a tanky hybrid!"
                    # Return a custom message for Warwick
                    elif user_favorite_champ == 'Sylas':
                        # Return a custom message for Sylas
                        return "Sylas is an interesting early game unit, he can mana reave but is usually dropped later"
                    elif user_favorite_champ == 'LeBlanc':
                        # Return a custom message for LeBlanc
                        return "Wow, LeBlanc? Just kidding. She is very good at blowing up backlines when sent to the back, and is very annoying to deal with. She is very cool though"
                    elif user_favorite_champ == 'Aurelion Sol':
                        # Return a custom message for Aurelion Sol
                        return "Aurelion Sol is such an amazing unit, with his backline access and heal cut he provides a lot for your team. He can be your carry, or support!"
                    elif user_favorite_champ == 'Ashe':
                        # Return a custom message for Ashe
                        return "Ashe is a cool early game unit! She is a good item holder until Samira."
                    elif user_favorite_champ == 'Blitzcrank':
                        # Return a custom message for Blitzcrank
                        return "Blitzcrank is a really cool champion, I agree! He can tank the whole enemy team!"
                    elif user_favorite_champ == 'Camille':
                        # Return a custom message for Camille
                        return "Camille is very good support! Although she isn't carried as much nowadays, she provides important traits to various teams."
                    elif user_favorite_champ == 'Yasuo':
                        # Return a custom message for Yasuo
                        return "Yasuo is a powerful champion that is used in the duelist tree"
                    elif user_favorite_champ == 'Fiora':
                        # Return a custom message for Fiora
                        return "Fiora is such a great duelist! I love how she can be very tanky with Ox Force."
                    elif user_favorite_champ == 'Zac':
                        # Return a custom message for Zac
                        return "Zac? He's not in this set, although he is a Riftwalker summon. I guess he is cool."
                    elif user_favorite_champ == 'Renekton':
                        # Return a custom message for Renekton
                        return "Renekton is so good considering he is a one cost. His tankiness and damage makes him very amazing!"
                    elif user_favorite_champ == 'Jinx':
                        # Return a custom message for Jinx
                        return "Jinx is a fun early game champion that can surprisingly do a lot of damage, I agree she is pretty amazing!"
                    elif user_favorite_champ == 'Lux':
                        # Return a custom message for Lux
                        return "Lux is a cool early game mage that is usually the item holder for lots of AP champions. But hey, her traits are really good!"
                    elif user_favorite_champ == 'Sona':
                        # Return a custom message for Sona
                        return "Sona does so much for ones team, with the heal, stun, and shields. She is very cool!"
                    elif user_favorite_champ == 'Riven':
                        # Return a custom message for Riven
                        return "Riven is such a cool champion for how much shields and utility she pvodes in Anima Squad."
                    elif user_favorite_champ == 'Jhin':
                        # Return a custom message for Jhin
                        return "Jhin is such a fun ADC that can do massive damage with his fourth shot!"
                    elif user_favorite_champ == 'Vayne':
                        # Return a custom message for Vayne
                        return "Vayne is such a cool duelist that can ramp up and delete teams! I agree she's amazing"
                    elif user_favorite_champ == 'Aatrox':
                        # Return a custom message for Aatrox
                        return "Aatrox is such a cool tank this set! He scales of maximium AP and can excel in many scenarios."
                    elif user_favorite_champ == "Bel'Veth":
                        # Return a custom message for Bel'Veth
                        return "Bel'Veth is a cool threat unit, although she is not that good now."
                    elif user_favorite_champ == "Vex":
                        # Return a custom message for Vex
                        return "Vex is a cool mascot unit introduced in Set 8.5. She can scale up, and blow up whole boards!"
                    elif user_favorite_champ == "Nasus":
                        # Return a custom message for Nasus
                        return "Nasus is a good early game champion, although weak right now he has seen better days."
                    elif user_favorite_champ == "Wukong":
                        # Return a custom message for Wukong
                        return "Wukong is an interesting early game champion as a mech. He can do well!"
                    elif user_favorite_champ == "Gangplank" or user_favorite_champ == "GP":
                        # Return a custom message for Gangplank
                        return "Gangplank is a cool early game unit that can do well in duelist lines in stages 1-3."
                    elif user_favorite_champ == "Jax":
                        # Return a custom message for Jax
                        return "Jax is a cool Mecha:Prime champion! I agree."
                    elif user_favorite_champ == "Lee Sin" or user_favorite_champ == "Lee":
                        # Return a custom message for Lee Sin
                        return "Lee Sin is an okay unit that provides shields and is used in the Supers trait. He has seen better days"
                    elif user_favorite_champ == "Malphite":
                        # Return a custom message for Malphite
                        return "Malphite is a cool mascot unit that can do a lot of work. He is really cool!"
                    elif user_favorite_champ == "Vi":
                        # Return a custom message for Vi
                        return "Vi is an interesting underground unit that provides shred and utility."
                    elif user_favorite_champ == "Rammus":
                        # Return a custom message for Rammus
                        return "Rammus is such a funny champion! He is a cool tank, but has seen better days."
                    elif user_favorite_champ == "Draven":
                        # Return a custom message for Draven
                        return "Draven is an amazing hyper carry that needs certain items to work. However, once he works he is crazy!"
                    elif user_favorite_champ == "Kayle":
                        # Return a custom message for Kayle
                        return "Kayle is a great early game unit that can be an item holder for AD. She's alright."
            else:
                # return a message indicating that no champion name was found in the user's message
                return "Sorry, I couldn't find a champion name in your message."
            
    elif 'what tier is' in message.lower() or 'how good is' in message.lower() or 'tier' in message.lower() or 'frequency' in message.lower() or 'win rate' in message.lower() or 'win-rate' in message.lower() or 'how often' in message.lower() or 'stats' in message.lower() or 'frequency' in message.lower() or 'average placement' in message.lower() or 'placement' in message.lower():
            selected_champ = None     
            for champ_name in champ_names:
            # check if the user mentioned the current champion name. also checks for edge cases for certain champions
                if champ_name.lower() in message.lower() or \
                    champ_name == 'Twisted Fate' and 'tf' in message.lower() or \
                    champ_name == 'Nunu & Willump' and ('nunu' in message.lower() or 'willump' in message.lower()) or \
                    champ_name == 'Aurelion Sol' and ('a sol' in message.lower() or 'asol' in message.lower()) or \
                    champ_name == 'Ultimate Ezreal' and ('ultimate ez' in message.lower() or 'ultimate ezreal' in message.lower()) or \
                    champ_name == 'Mordekaiser' and 'morde' in message.lower() or \
                    champ_name == 'Lee Sin' and ('lee' in message.lower() or 'lee sin' in message.lower()):
                    # If so, set the user's favorite champion to the current champion name
                    selected_champ = champ_name
                    user.favchamp = selected_champ
                   
                    print("The tier of " + selected_champ + " is " + champ_dict.get(selected_champ)[0] + " and the average placement of this champion is " + champ_dict.get(selected_champ)[1])
                    print("The winrate of this champion is " + champ_dict.get(selected_champ)[2] + " and the frequency of usage is " + champ_dict.get(selected_champ)[3])
                    break  # Exit the loop once a match is found
    
    elif 'my rank is' in message.lower() or 'i am' in message.lower() or 'i\'m' in message.lower():
        parts = message.split()
        rank = parts[-1]
        # print(rank)
        if rank.lower() in ['iron', 'bronze', 'silver', 'gold', 'platinum', 'diamond', 'grandmaster', 'challenger']:
                user.rank = rank
                return get_rank_response(rank.lower()) 
        else:
            return random.choice(error_messages)
        
    elif message.lower() == 'help':
        return "You can ask me about your rank, your favorite champion, or my favorite champion. What do you want to know?"

    else:
        return random.choice(error_messages)

def get_rank_response(rank):
    if rank == 'iron':
        return "Everyone starts somewhere! Keep grinding and you can climb the ranks!"
    elif rank == 'bronze':
        return "Some of my friends are made of bronze, but that’s not a bad rank to have!"
    elif rank == 'silver':
        return "Looks like you are silver! A few tips and studying, and you can climb in no time!"
    elif rank == 'gold':
        return "Looks like you are Gold! Most players are here, a few tricks and cleaner gameplay will have you climb in no time! I’m here to help!"
    elif rank == 'platinum':
        return "Congratulations on reaching Platinum! With more strategic play, you’ll soon reach Diamond!"
    elif rank == 'diamond':
        return "Diamond is where the best players shine! A little more practice and you'll be ready for the toughest challenges."
    elif rank == 'grandmaster':
        return "You are among the best players in the world! Keep it up!"
    elif rank == 'challenger':
        return "You are a true legend of TFT! Keep crushing your opponents!"
    
    
users = []
user = None
while True:
    if user is None:
        user = set_user_data()
        users.append(user)
        print("Nice to meet you " + user.name)
    elif response == "Goodbye!":
        user = input("Log in with another account, or type exit to exit.")
        if user == "exit":
            quit()
        else:
            user = set_user_data()
            users.append(user)
            print("Nice to meet you " + user.name)
        
        
    message = input("You: ")
    response = respond_to_message(message, user)
    
    print("Chatbot:", response)
    

