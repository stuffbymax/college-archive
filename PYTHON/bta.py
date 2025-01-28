import os
import random
import time
import sys
import platform
import glob
import signal

# --- 0. Global Variables ---
player_name = ""
location = ""
cash = 0
health = 0
guns = []
items = []
drugs = {}
body_armor_equipped = False

# --- 1. Plugin Loading ---
plugin_dir = "plugins"

def load_plugins():
    if os.path.isdir(plugin_dir):
        for plugin_file in glob.glob(os.path.join(plugin_dir, "*.py")):
          try:
            with open(plugin_file, 'r') as file:
              exec(file.read(), globals())
          except Exception as e:
            print(f"Warning: Could not load plugin '{plugin_file}'. Error: {e}")
    else:
        print(f"Warning: Plugin directory '{plugin_dir}' not found.")
load_plugins()



# --- 2. Loading Animation ---
def start_loading_animation():
  print("Loading...")
  for i in range(3):
      sys.stdout.write('.')
      sys.stdout.flush()
      time.sleep(0.5)
  print("\n")

start_loading_animation()

# --- 3. Functions ---

# Function to clear the screen and display game info
def clear_screen():
    if platform.system() == "Windows":
      os.system("cls")
    else:
      os.system("clear")
    
    print("\033[1;34m-----------------------------------------\033[0m")
    print("\033[1;43m|        Bash theaft auto               |\033[0m")
    print("\033[1;34m-----------------------------------------\033[0m")
    print(f"Player: {player_name}   Location: {location}")
    print(f"Cash: {cash} dollars      Health: {health}%")
    print("\033[1;34m-----------------------------------------\033[0m")
    print("\033[1;44m|        made by stuffbymax             |\033[0m")
    print("\033[1;34m-----------------------------------------\033[0m")

# Function to check if the player is alive
def check_health():
    global health
    if health <= 0:
        print("You have no health left! Transporting to hospital...")
        input("Press Enter to continue...")
        hospitalize_player()

# Function for traveling to a new location
def travel_to(travel_cost, new_location):
    global cash, location
    if cash >= travel_cost:
        print(f"Traveling to {new_location}...")
        cash -= travel_cost
        input("Press Enter to continue...")
        location = new_location
        clear_screen()
        print(f"You have arrived at {location}.")
    else:
        print(f"Not enough cash to travel to {new_location}.")
        input("Press Enter to continue...")
        clear_screen()

# Function for buying guns
def buy_guns():
    clear_screen()
    print("Gun Store - Choose a gun to buy:")
    print("1. Pistol (100$)")
    print("2. Shotgun (250$)")
    print("3. SMG (500$)")
    print("4. Rifle (750$)")
    print("5. Back to main menu")
    
    while True:
      gun_choice = input("Enter your choice (number): ")
      if not gun_choice.isdigit():
        print("Invalid input. Please enter a number from the menu.")
        input("Press Enter to continue...")
        continue
      gun_choice = int(gun_choice)
      if gun_choice == 1:
          buy_item("Pistol", 100)
          break
      elif gun_choice == 2:
          buy_item("Shotgun", 250)
          break
      elif gun_choice == 3:
          buy_item("SMG", 500)
          break
      elif gun_choice == 4:
          buy_item("Rifle", 750)
          break
      elif gun_choice == 5:
          clear_screen()
          break
      else:
        print("Invalid choice.")

# Helper function for buying items
def buy_item(item_name, item_cost):
    global cash, guns
    if cash >= item_cost:
        cash -= item_cost
        guns.append(item_name)
        print(f"You bought a {item_name}.")
        input("Press Enter to continue...")
    else:
        print(f"Not enough cash to buy a {item_name}.")
        input("Press Enter to continue...")

# Function to show inventory
def show_inventory():
    clear_screen()
    print("Your Inventory:")
    print(f"Cash: {cash} dollars")
    print(f"Health: {health}%")
    print(f"Guns: {', '.join(guns)}")
    print(f"Items: {', '.join(items)}")
    print("Drugs: ")
    for drug, amount in drugs.items():
        print(f"  - {drug}: {amount}")
    input("Press Enter to return to main menu.")

# Function for working (simplified logic)
def work_job(job_type):
  global cash
  min_earnings = 0
  max_earnings = 0
  
  if location == "Los Santos":
    min_earnings = 20
    max_earnings = 60
  elif location == "San Fierro":
    min_earnings = 25
    max_earnings = 70
  elif location == "Las Venturas":
    min_earnings = 30
    max_earnings = 90
  elif location == "Vice City":
    min_earnings = 15
    max_earnings = 50
  elif location == "Liberty City":
    min_earnings = 35
    max_earnings = 100
  else:
    min_earnings = 10
    max_earnings = 40
    
  if job_type == "taxi":
    earnings = random.randint(min_earnings,max_earnings)
  elif job_type == "delivery":
    earnings = random.randint(min_earnings,max_earnings + 10)
  elif job_type == "mechanic":
     earnings = random.randint(min_earnings,max_earnings + 20)
  elif job_type == "security":
    earnings = random.randint(min_earnings,max_earnings + 30)
  elif job_type == "performer":
      earnings = random.randint(min_earnings,max_earnings - 20)
  elif job_type == "race":
    work_race()
    return
  else:
    print("Invalid Job")
    return
    
  print(f"You are working as a {job_type} driver in {location}...")
  input("Press Enter to continue...")
    
  cash += earnings
  clear_screen()
  print(f"You earned {earnings} dollars. You now have {cash} dollars.")
  input("Press Enter to continue...")

# Function for street racing (separate function)
def work_race():
    global cash, health, body_armor_equipped
    print(f"You are participating in a street race in {location}...")
    input("Press Enter to continue...")
    
    if random.randint(0, 1) == 0:
      winnings = random.randint(100, 300)
      cash += winnings
      damage = random.randint(10, 30)
      if body_armor_equipped:
        damage = int(damage / 2)
        print("Your body armor reduced the damage!")
        body_armor_equipped = False
      health -= damage
      check_health()
      clear_screen()
      print(f"You won the street race and got {winnings} dollars, but lost {damage}% health. You now have {cash} dollars and {health}% health.")
      input("Press Enter to continue...")
    else:
      damage = random.randint(20, 60)
      if body_armor_equipped:
        damage = int(damage / 2)
        print("Your body armor reduced the damage!")
        body_armor_equipped = False
      health -= damage
      check_health()
      clear_screen()
      print(f"You lost the street race and took {damage}% damage. You now have {health}% health.")
      input("Press Enter to continue...")


# Function to use guns for jobs
def use_guns(gun_name):
    if gun_name in guns:
        print(f"You used your {gun_name} for this job.")
        input("Press Enter to continue...")
    else:
        print(f"You don't have a {gun_name}. Job failed.")
        input("Press Enter to continue...")

# Function for visiting the hospital
def visit_hospital():
    global health, cash, items, body_armor_equipped
    clear_screen()
    print("Hospital Services:")
    print("1. Basic Treatment (50$) - Full heal")
    print("2. Advanced Treatment (100$) - Full heal + 10% health boost")
    print("3. Buy Health Pack (30$) - Heal 25% health")
    print("4. Buy Body Armor (75$) - Reduce damage by 50% in next encounter")
    print("5. Back to main menu")
    
    while True:
      hospital_choice = input("Enter your choice (number): ")
      if not hospital_choice.isdigit():
        print("Invalid input. Please enter a number from the menu.")
        input("Press Enter to continue...")
        continue
      hospital_choice = int(hospital_choice)
      if hospital_choice == 1:
          buy_hospital_item(50, "basic_treatment")
          break
      elif hospital_choice == 2:
        buy_hospital_item(100, "advanced_treatment")
        break
      elif hospital_choice == 3:
        buy_hospital_item(30, "health_pack")
        break
      elif hospital_choice == 4:
        buy_hospital_item(75, "body_armor")
        break
      elif hospital_choice == 5:
        clear_screen()
        break
      else:
        print("Invalid choice.")
        

# Helper function for buying hospital items
def buy_hospital_item(item_cost, item_type):
    global cash, health, items, body_armor_equipped
    if cash >= item_cost:
        cash -= item_cost
        if item_type == "basic_treatment":
            health = 100
            print("You received basic treatment and are fully healed.")
            input("Press Enter to continue...")
        elif item_type == "advanced_treatment":
            health += 10
            if health > 100:
                health = 100
            print("You received advanced treatment and are fully healed with a health boost.")
            input("Press Enter to continue...")
        elif item_type == "health_pack":
            items.append("Health Pack")
            print("You bought a Health Pack.")
            input("Press Enter to continue...")
        elif item_type == "body_armor":
          body_armor_equipped = True
          print("You bought Body Armor.")
          input("Press Enter to continue...")
    else:
        print(f"Not enough cash for {item_type}.")
        input("Press Enter to continue...")

# Function for robbing a store
def rob_store():
    global cash, health, body_armor_equipped
    print(f"Attempting to rob a store in {location}...")
    input("Press Enter to continue...")
    if random.randint(0, 1) == 0:
        loot = random.randint(100, 300)
        cash += loot
        damage = random.randint(10, 40)
        if body_armor_equipped:
          damage = int(damage / 2)
          print("Your body armor reduced the damage!")
          body_armor_equipped = False
        health -= damage
        check_health()
        clear_screen()
        print(f"You successfully robbed the store and got {loot} dollars, but lost {damage}% health. You now have {cash} dollars and {health}% health.")
        input("Press Enter to continue...")
    else:
        fine = random.randint(25, 75)
        cash -= fine
        clear_screen()
        print(f"You got caught and fined {fine} dollars. You now have {cash} dollars.")
        input("Press Enter to continue...")

# Function for participating in a heist
def heist():
    global cash, health, body_armor_equipped
    print(f"Planning a heist in {location}...")
    input("Press Enter to continue...")
    if random.randint(0, 2) == 0:
        loot = random.randint(200, 700)
        cash += loot
        damage = random.randint(20, 70)
        if body_armor_equipped:
          damage = int(damage / 2)
          print("Your body armor reduced the damage!")
          body_armor_equipped = False
        health -= damage
        check_health()
        clear_screen()
        print(f"The heist was successful! You got {loot} dollars, but lost {damage}% health. You now have {cash} dollars and {health}% health.")
        input("Press Enter to continue...")
    else:
        fine = random.randint(50, 150)
        cash -= fine
        clear_screen()
        print(f"The heist failed and you got caught, losing {fine} dollars. You now have {cash} dollars.")
        input("Press Enter to continue...")


# Function for gang wars
def gang_war():
  global cash, health, body_armor_equipped
  print(f"Starting a gang war in {location}...")
  input("Press Enter to continue...")
  
  if random.randint(0, 2) == 0:
      loot = random.randint(100, 400)
      cash += loot
      damage = random.randint(30, 80)
      if body_armor_equipped:
        damage = int(damage / 2)
        print("Your body armor reduced the damage!")
        body_armor_equipped = False
      health -= damage
      check_health()
      clear_screen()
      print(f"You won the gang war and got {loot} dollars, but lost {damage}% health. You now have {cash} dollars and {health}% health.")
      input("Press Enter to continue...")
  else:
    fine = random.randint(50, 200)
    cash -= fine
    damage = random.randint(20, 60)
    if body_armor_equipped:
          damage = int(damage / 2)
          print("Your body armor reduced the damage!")
          body_armor_equipped = False
    health -= damage
    check_health()
    clear_screen()
    print(f"You lost the gang war, got fined {fine} dollars, and lost {damage}% health. You now have {cash} dollars and {health}% health.")
    input("Press Enter to continue...")

# Function for carjacking
def carjack():
    global cash, health, body_armor_equipped
    print(f"Attempting to carjack a vehicle in {location}...")
    input("Press Enter to continue...")
    if random.randint(0, 1) == 0:
        loot = random.randint(50, 250)
        cash += loot
        damage = random.randint(10, 30)
        if body_armor_equipped:
          damage = int(damage / 2)
          print("Your body armor reduced the damage!")
          body_armor_equipped = False
        health -= damage
        check_health()
        clear_screen()
        print(f"You successfully carjacked a vehicle and got {loot} dollars, but lost {damage}% health. You now have {cash} dollars and {health}% health.")
        input("Press Enter to continue...")
    else:
      fine = random.randint(25, 100)
      cash -= fine
      clear_screen()
      print(f"You got caught and fined {fine} dollars. You now have {cash} dollars.")
      input("Press Enter to continue...")

# Function to handle hospital visit after death
def hospitalize_player():
    global health, cash
    clear_screen()
    print("You have been hospitalized and are being treated...")
    input("Press Enter to continue...")
    health = 100
    clear_screen()
    print("You are fully healed but lost $200 for the treatment.")
    cash -= 200
    if cash < 0:
      cash = 0
    input("Press Enter to continue...")
    clear_screen()

# Function to hire a hooker
def hire_hooker():
    global cash, health
    print(f"You are looking for a hooker in {location}...")
    input("Press Enter to continue...")
    hooker_cost = random.randint(50, 150)
    health_gain = random.randint(10, 30)
    if cash >= hooker_cost:
        cash -= hooker_cost
        health += health_gain
        if health > 100:
            health = 100
        clear_screen()
        print(f"You hired a hooker for {hooker_cost} dollars and gained {health_gain}% health. You now have {cash} dollars and {health}% health.")
        input("Press Enter to continue...")
    else:
      clear_screen()
      print("Not enough cash to hire a hooker.")
      input("Press Enter to continue...")
    clear_screen()

# Function to buy drugs
def buy_drugs():
    global drugs, cash
    clear_screen()
    print("Drug Dealer - Choose a drug to buy:")
    print("1. Weed (10$/unit)")
    print("2. Cocaine (50$/unit)")
    print("3. Heroin (100$/unit)")
    print("4. Meth (75$/unit)")
    print("5. Back to main menu")

    while True:
      drug_choice = input("Enter your choice (number): ")
      if not drug_choice.isdigit():
        print("Invalid input. Please enter a number from the menu.")
        input("Press Enter to continue...")
        continue
      drug_choice = int(drug_choice)

      drug_amount = input("Enter the amount you want to buy: ")
      if not drug_amount.isdigit():
          print("Invalid input. Please enter a number.")
          input("Press Enter to continue...")
          continue
      drug_amount = int(drug_amount)


      if drug_choice == 1:
        buy_drug("Weed", 10, drug_amount)
        break
      elif drug_choice == 2:
        buy_drug("Cocaine", 50, drug_amount)
        break
      elif drug_choice == 3:
        buy_drug("Heroin", 100, drug_amount)
        break
      elif drug_choice == 4:
        buy_drug("Meth", 75, drug_amount)
        break
      elif drug_choice == 5:
        clear_screen()
        break
      else:
          print("Invalid choice.")
          
    clear_screen()

# Helper function for buying drugs
def buy_drug(drug_name, drug_price, drug_amount):
    global cash, drugs
    cost = drug_price * drug_amount
    if cash >= cost:
        cash -= cost
        drugs[drug_name] = drugs.get(drug_name, 0) + drug_amount
        print(f"You bought {drug_amount} units of {drug_name}.")
        input("Press Enter to continue...")
    else:
        print(f"Not enough cash to buy {drug_name}.")
        input("Press Enter to continue...")


# Function to sell drugs
def sell_drugs():
    global drugs, cash
    clear_screen()
    print("Drug Dealer - Choose a drug to sell:")
    print("1. Weed")
    print("2. Cocaine")
    print("3. Heroin")
    print("4. Meth")
    print("5. Back to main menu")

    while True:
      drug_choice = input("Enter your choice (number): ")
      if not drug_choice.isdigit():
        print("Invalid input. Please enter a number from the menu.")
        input("Press Enter to continue...")
        continue
      drug_choice = int(drug_choice)

      drug_amount = input("Enter the amount you want to sell: ")
      if not drug_amount.isdigit():
        print("Invalid input. Please enter a number.")
        input("Press Enter to continue...")
        continue
      drug_amount = int(drug_amount)
      
      if drug_choice == 1:
          sell_drug("Weed", 15, drug_amount)
          break
      elif drug_choice == 2:
        sell_drug("Cocaine", 75, drug_amount)
        break
      elif drug_choice == 3:
        sell_drug("Heroin", 150, drug_amount)
        break
      elif drug_choice == 4:
        sell_drug("Meth", 100, drug_amount)
        break
      elif drug_choice == 5:
          clear_screen()
          break
      else:
        print("Invalid choice.")
    clear_screen()
    
# Helper function for selling drugs
def sell_drug(drug_name, drug_price, drug_amount):
    global cash, drugs
    if drug_name in drugs and drugs[drug_name] >= drug_amount:
      cash += drug_price * drug_amount
      drugs[drug_name] -= drug_amount
      print(f"You sold {drug_amount} units of {drug_name}.")
      input("Press Enter to continue...")
    else:
      print(f"Not enough {drug_name} to sell.")
      input("Press Enter to continue...")


# Function to play music
def play_music():
  music_files = [
    "music/platforma.mp3",
    "music/the_loading_screen.mp3",
    "music/doom.mp3",
    "music/Jal.mp3"
    ]
  
  while True:
    clear_screen()
    print("Choose a song to play:")
    for i, track in enumerate(music_files):
        print(f"{i+1}. {os.path.basename(track)}")
    print("press q to Stop Music")
    print(f"{len(music_files)+1}. Back to Main menu")
    music_choice = input()
    if music_choice.lower() == 'q':
      os.system("pkill mpg123")
      continue
    if not music_choice.isdigit():
      print("Invalid input. Please enter a number.")
      time.sleep(2)
      continue # Go back to music player menu
    music_choice = int(music_choice)

    if 1 <= music_choice <= len(music_files):
      selected_track = music_files[music_choice - 1]
      if os.path.exists(selected_track):
        print(f"Playing: {os.path.basename(selected_track)}")
        os.system(f"mpg123 -q '{selected_track}'")
      else:
        print(f"Error: Music file '{selected_track}' not found.")
        time.sleep(2)
    elif music_choice == len(music_files) + 1:
        os.system("pkill mpg123")
        clear_screen()
        break # Exit the music player menu
    else:
      print("Invalid choice.")
      time.sleep(2)

# Save the game state to a file
def save_game():
    with open("saves/player_name.sav", "w") as f:
        f.write(player_name)
    with open("saves/location.sav", "w") as f:
      f.write(location)
    with open("saves/cash.sav", "w") as f:
      f.write(str(cash))
    with open("saves/health.sav", "w") as f:
      f.write(str(health))
    with open("saves/guns.sav", "w") as f:
      for gun in guns:
        f.write(gun + "\n")
    with open("saves/items.sav", "w") as f:
        for item in items:
          f.write(item + "\n")
    with open("saves/drugs.sav", "w") as f:
      for drug, amount in drugs.items():
        f.write(f"{drug} {amount}\n")
    with open("saves/body_armor_equipped.sav", "w") as f:
      f.write(str(body_armor_equipped))
      
    print("Game saved successfully.")
    input("Press Enter to continue...")

# Load the game state from a file
def load_game():
  global player_name, location, cash, health, guns, items, drugs, body_armor_equipped
  if (os.path.exists("saves/player_name.sav") and os.path.exists("saves/location.sav")
    and os.path.exists("saves/cash.sav") and os.path.exists("saves/health.sav")
    and os.path.exists("saves/guns.sav") and os.path.exists("saves/items.sav")
    and os.path.exists("saves/body_armor_equipped.sav")
    ):
    with open("saves/player_name.sav", "r") as f:
        player_name = f.readline().strip()
    with open("saves/location.sav", "r") as f:
        location = f.readline().strip()
    with open("saves/cash.sav", "r") as f:
        cash = int(f.readline().strip())
    with open("saves/health.sav", "r") as f:
        health = int(f.readline().strip())
    with open("saves/guns.sav", "r") as f:
        guns = [line.strip() for line in f]
    with open("saves/items.sav", "r") as f:
        items = [line.strip() for line in f]
    with open("saves/drugs.sav", "r") as f:
        drugs = {}
        for line in f:
          if line.strip():
            key, value = line.strip().split()
            drugs[key] = int(value)
    with open("saves/body_armor_equipped.sav", "r") as f:
      body_armor_equipped = f.readline().strip() == 'True'
          
    print("Game loaded successfully.")
    input("Press Enter to continue...")
  else:
        print("No saved game found.")
        input("Press Enter to continue...")

# --- 4. Game Initialization and Loop ---
# Function to initialize game variables
def Game_variables():
    global player_name, location, cash, health, guns, items, drugs
    clear_screen()
    player_name = input("Enter your player name: ")
    location = "Los Santos"
    cash = 500
    health = 100
    guns = []
    items = []
    drugs = {"Weed": 0, "Cocaine": 0, "Heroin": 0, "Meth": 0}
    clear_screen()

# Start game loop
Game_variables()  # Initialize the game
while True:
  clear_screen()
  print("Choose an action:")
  print("1. Travel to another city")
  print("2. Buy guns")
  print("3. Show inventory")
  print("4. Work (earn money)")
  print("5. Work (criminal activity)")
  print("6. Buy drugs")
  print("7. Sell drugs")
  print("8. Hire hooker")
  print("9. Visit hospital")
  print("10. Exit Game")
  print("11. Save Game")
  print("12. Load Game")
  print("13. Play music")

  choice = input("Enter your choice: ")
  if not choice.isdigit():
    print("Invalid input. Please enter a number.")
    time.sleep(2)
    continue
  choice = int(choice)
  
  if choice == 1:
    clear_screen()
    print("Choose a city to travel to:")
    print("1. Los Santos (50$)")
    print("2. San Fierro (75$)")
    print("3. Las Venturas (100$)")
    print("4. Vice City (150$)")
    print("5. Liberty City (200$)")
    print("6. Back to main menu")
    
    while True:
      city_choice = input("Enter your choice: ")
      if not city_choice.isdigit():
        print("Invalid input. Please enter a number.")
        time.sleep(2)
        continue
      city_choice = int(city_choice)
      
      if city_choice == 1:
        travel_to(50, "Los Santos")
        break
      elif city_choice == 2:
        travel_to(75, "San Fierro")
        break
      elif city_choice == 3:
        travel_to(100, "Las Venturas")
        break
      elif city_choice == 4:
        travel_to(150, "Vice City")
        break
      elif city_choice == 5:
        travel_to(200, "Liberty City")
        break
      elif city_choice == 6:
        clear_screen()
        break
      else:
        print("Invalid choice.")
    
  elif choice == 2:
    buy_guns()
  elif choice == 3:
    show_inventory()
  elif choice == 4:
    clear_screen()
    print("Choose a job:")
    print("1. Taxi Driver")
    print("2. Delivery Driver")
    print("3. Mechanic")
    print("4. Security Guard")
    print("5. Street Performer")
    print("6. Street Racing")
    print("7. Back to main menu")
    
    while True:
      job_choice = input("Enter your choice: ")
      if not job_choice.isdigit():
        print("Invalid input. Please enter a number.")
        time.sleep(2)
        continue
      job_choice = int(job_choice)
      
      if job_choice == 1:
        work_job("taxi")
        break
      elif job_choice == 2:
        work_job("delivery")
        break
      elif job_choice == 3:
        work_job("mechanic")
        break
      elif job_choice == 4:
        work_job("security")
        break
      elif job_choice == 5:
        work_job("performer")
        break
      elif job_choice == 6:
        work_job("race")
        break
      elif job_choice == 7:
        clear_screen()
        break
      else:
        print("Invalid choice.")
    
  elif choice == 5:
    clear_screen()
    print("Choose a criminal activity:")
    print("1. Heist")
    print("2. Gang war")
    print("3. Carjack")
    print("4. Back to main menu")
    
    while True:
      criminal_choice = input("Enter your choice: ")
      if not criminal_choice.isdigit():
          print("Invalid input. Please enter a number.")
          time.sleep(2)
          continue
      criminal_choice = int(criminal_choice)
      if criminal_choice == 1:
        heist()
        break
      elif criminal_choice == 2:
        gang_war()
        break
      elif criminal_choice == 3:
        carjack()
        break
      elif criminal_choice == 4:
        clear_screen()
        break
      else:
        print("Invalid choice.")

  elif choice == 6:
    buy_drugs()
  elif choice == 7:
    sell_drugs()
  elif choice == 8:
      hire_hooker()
  elif choice == 9:
    visit_hospital()
  elif choice == 10:
      break
  elif choice == 11:
    save_game()
  elif choice == 12:
    load_game()
  elif choice == 13:
    play_music()
  else:
    print("Invalid choice.")
