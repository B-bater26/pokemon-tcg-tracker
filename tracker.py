# ===============================================
# TCG Pokemon Card Finder
# Author: Bailey Baxter
# Date: April 5, 2026
# Description: A CLI Tool that calls on the
#              tcgdexsdk API and allows the user
#              to find out information about
#              their card.
# ===============================================


from colorama import Fore, Style, init
from tcgdexsdk import TCGdex, Query

init(autoreset=True)

tcgdex = TCGdex("en") # English deck

class Pokemon:
    def __init__(self, cardID):
        self.cardID = cardID
        self.allData = tcgdex.card.getSync(cardID) # grabs the card's entire data set
        self.name = self.allData.name
        self.hp = self.allData.hp
        self.types = self.allData.types
        self.rarity = self.allData.rarity
        self.stage = self.allData.stage
        self.evolvedFrom = self.allData.evolveFrom
        self.setName = self.allData.set.name
        self.abilities = self.allData.abilities
        self.retreat = self.allData.retreat
        self.legal = self.allData.legal
        self.symbols = {
            "Common": "●",
            "Uncommon": "◆",
            "Rare": "★",
            "Rare Holo": "★",
            "Ultra Rare": "✦"
        }
        self.symbol = self.symbols.get(self.rarity, "")

    def displayCard(self):
        print(f"{Style.NORMAL}{Fore.YELLOW}{"Item":<14}{Style.BRIGHT}{Fore.CYAN}{self.cardID}\n")
        print(f"{Style.NORMAL}{Fore.YELLOW}{"Name:":<14} {Style.BRIGHT}{Fore.CYAN}{self.name}")
        print(f"{Style.NORMAL}{Fore.YELLOW}{"HP:":<14} {Style.BRIGHT}{Fore.CYAN}{self.hp}")
        if self.types:
            print(f"{Style.NORMAL}{Fore.YELLOW}Types:")
            for i, type in enumerate(self.types, start=1):
                print(f"{Style.NORMAL}{Fore.WHITE}{"Type #"}{(i):<8} {Style.BRIGHT}{Fore.CYAN}{type}")
        else:
            print(f"{Style.NORMAL}{Fore.YELLOW}{"Types:":<14}{Style.BRIGHT}{Fore.CYAN} None")    
        print(f"{Style.NORMAL}{Fore.YELLOW}{"Rarity:":<14} {Style.BRIGHT}{Fore.CYAN}{self.rarity} {self.symbol}")
        print(f"{Style.NORMAL}{Fore.YELLOW}{"Stage:":<14} {Style.BRIGHT}{Fore.CYAN}{self.stage}")
        print(f"{Style.NORMAL}{Fore.YELLOW}{"Evolved From:":<14} {Style.BRIGHT}{Fore.CYAN}{self.evolvedFrom}")
        print(f"{Style.NORMAL}{Fore.YELLOW}{"Set Name:":<14} {Style.BRIGHT}{Fore.CYAN}{self.setName}")
        if self.abilities:
            print(f"{Style.NORMAL}{Fore.YELLOW}Abilities:")
            for i, ability in enumerate(self.abilities, start=1):
                print(f"{Style.NORMAL}{Fore.WHITE}{"Ability #"}{(i):<5} {Style.BRIGHT}{Fore.CYAN}{ability.name} - {ability.effect}")
        else:
            print(f"{Style.NORMAL}{Fore.YELLOW}{"Abilities:":<14}{Style.BRIGHT}{Fore.CYAN} None")
        print(f"{Style.NORMAL}{Fore.YELLOW}{"Retreat Cost:":<14} {Style.BRIGHT}{Fore.CYAN}{self.retreat}")   
        print(f"{Style.NORMAL}{Fore.YELLOW}       Legal")
        print(f"{Style.NORMAL}{Fore.YELLOW}{"Standard:":<14} {Style.BRIGHT}{Fore.CYAN}{self.legal.standard}")
        print(f"{Style.NORMAL}{Fore.YELLOW}{"Expanded:":<14} {Style.BRIGHT}{Fore.CYAN}{self.legal.expanded}")


def search_card(name):
    cards = tcgdex.card.listSync(Query().equal("name", name)) # locate the cards with that name
    return cards

def displayOptions(data):
    for i, card in enumerate(data, start=1):
        print(f"{Fore.YELLOW}{i}. {Fore.GREEN}{card.name} | {Fore.WHITE}{card.id}")
    
def selection(data):
    while True:
        try:
            selectedItem = (int(input(f"{Fore.YELLOW} Chose the card that matches your ID (1 to {len(data)}) -> ")))-1
            if selectedItem < 0 or selectedItem > len(data)-1:
                print(f"{Fore.RED}Error! {selectedItem+1} is not a valid entry. Please try again.\n")
            else:
                return data[selectedItem]


        except ValueError:
            print(f"{Fore.RED}Error! Input is not a valid entry. Please try again.\n")

def createItem(selectedId):
    newPokemon = Pokemon(selectedId)
    return newPokemon

def anotherCard():
    while True:
        restart = input("Y/N would you like to search for another card? -> ").upper()
        if restart != "N" and restart != "Y":
            continue
        if restart == "Y":
            return True
        else:
            return False


def main():
    print(f"{Fore.CYAN}{"="*10}{Fore.RED}{Style.BRIGHT}POKEMON TCG CARD LOCATOR{Fore.CYAN}{Style.NORMAL}{"="*10}")
    while True:
        searchItem = input("Enter the name of your card -> ")
        searchItem = searchItem.title()
        data = search_card(searchItem)
        if not data:
            print(f"{Fore.RED}Error! {searchItem} is not in the TCGdex!")
            continue
        displayOptions(data)
        selectedItem = selection(data)
        newPokemon = createItem(selectedItem.id)
        newPokemon.displayCard()
        restart = anotherCard()
        if not restart:
            break
    print(f"{Fore.BLUE}{"="*10}{Fore.RED}{Style.BRIGHT}POKEMON TCG CARD LOCATOR{Fore.BLUE}{Style.NORMAL}{"="*10}")



if __name__ == "__main__":
    main()
