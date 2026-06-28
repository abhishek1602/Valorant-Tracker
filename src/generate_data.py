import random
import pandas as pd
from faker import Faker
from datetime import timedelta, date

fake = Faker()

NUM_PLAYERS = 500000

regions = [
    "APAC",
    "North America",
    "EU",
    "LATAM"
]

countries = [
    "India",
    "USA",
    "Canada",
    "Germany",
    "France",
    "Japan",
    "Brazil",
    "UK",
    "Australia"
]

ranks = [
    "Iron",
    "Bronze",
    "Silver",
    "Gold",
    "Platinum",
    "Diamond",
    "Ascendant",
    "Immortal",
    "Radiant"
]

agents = [
    "Jett",
    "Reyna",
    "Phoenix",
    "Sage",
    "Omen",
    "Brimstone",
    "Killjoy",
    "Cypher",
    "Skye",
    "Fade",
    "Sova",
    "Viper",
    "Yoru",
    "Neon",
    "Harbor",
    "Deadlock",
    "Clove",
    "Gekko"
]

maps = [
    "Ascent",
    "Bind",
    "Haven",
    "Split",
    "Lotus",
    "Sunset",
    "Pearl",
    "Icebox",
    "Abyss"
]

queue_types = [
    "Competitive",
    "Unrated",
    "Swiftplay",
    "Spike Rush",
    "Deathmatch"
]

rows = []

for player in range(1, NUM_PLAYERS + 1):

    account_level = random.randint(1, 500)

    matches_played = random.randint(10, 3000)

    wins = random.randint(0, matches_played)

    losses = matches_played - wins

    session_length = random.randint(10, 180)

    total_hours = round(matches_played * session_length / 60, 2)

    total_spent = random.randint(0, 500)

    skins = random.randint(0, 150)

    last_login = fake.date_between(
        start_date="-90d",
        end_date="today"
    )

    days_since = (date.today() - last_login).days

    churn = 1 if days_since > 20 else 0

    row = {

        "PlayerID": player,

        "Region": random.choice(regions),

        "Country": random.choice(countries),

        "Rank": random.choice(ranks),

        "AccountLevel": account_level,

        "MatchesPlayed": matches_played,

        "Wins": wins,

        "Losses": losses,

        "Agent": random.choice(agents),

        "Map": random.choice(maps),

        "QueueType": random.choice(queue_types),

        "SessionLength": session_length,

        "TotalHoursPlayed": total_hours,

        "TotalVPSpent": total_spent,

        "TotalSkinsOwned": skins,

        "BattlePass": random.choice([0,1]),

        "LastLogin": last_login,

        "DaysSinceLastLogin": days_since,

        "IsChurned": churn

    }

    rows.append(row)

df = pd.DataFrame(rows)

df.to_csv(
    "../data/raw/valorant_players.csv",
    index=False
)

print(df.head())

print()

print("Dataset Generated Successfully!")

print()

print(df.shape)