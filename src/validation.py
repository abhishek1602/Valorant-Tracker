import pandas as pd

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("../data/raw/valorant_players.csv")

print("=" * 60)
print("VALORANT PLAYER DATA VALIDATION REPORT")
print("=" * 60)

# -----------------------------
# Dataset Information
# -----------------------------
print("\nDataset Shape")
print(df.shape)

print("\nColumns")
print(df.columns.tolist())

print("\nData Types")
print(df.dtypes)

# -----------------------------
# Missing Values
# -----------------------------
print("\nMissing Values")
missing = df.isnull().sum()
print(missing)

# -----------------------------
# Duplicate Records
# -----------------------------
duplicates = df.duplicated().sum()

print("\nDuplicate Rows")
print(duplicates)

# -----------------------------
# Duplicate Player IDs
# -----------------------------
duplicate_players = df["PlayerID"].duplicated().sum()

print("\nDuplicate Player IDs")
print(duplicate_players)

# -----------------------------
# Negative Session Length
# -----------------------------
negative_session = df[df["SessionLength"] < 0]

print("\nNegative Session Length Records")
print(len(negative_session))

# -----------------------------
# Invalid Rank
# -----------------------------
valid_ranks = [
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

invalid_rank = df[~df["Rank"].isin(valid_ranks)]

print("\nInvalid Rank Records")
print(len(invalid_rank))

# -----------------------------
# Invalid Queue Type
# -----------------------------
valid_queue = [
    "Competitive",
    "Unrated",
    "Swiftplay",
    "Spike Rush",
    "Deathmatch"
]

invalid_queue = df[~df["QueueType"].isin(valid_queue)]

print("\nInvalid Queue Types")
print(len(invalid_queue))

# -----------------------------
# Invalid Map
# -----------------------------
valid_maps = [
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

invalid_map = df[~df["Map"].isin(valid_maps)]

print("\nInvalid Maps")
print(len(invalid_map))

# -----------------------------
# Wins Greater Than Matches
# -----------------------------
invalid_wins = df[df["Wins"] > df["MatchesPlayed"]]

print("\nWins Greater Than Matches Played")
print(len(invalid_wins))

# -----------------------------
# Losses Check
# -----------------------------
invalid_losses = df[
    df["Losses"] != (df["MatchesPlayed"] - df["Wins"])
]

print("\nInvalid Loss Values")
print(len(invalid_losses))

# -----------------------------
# VP Spent
# -----------------------------
negative_spending = df[df["TotalVPSpent"] < 0]

print("\nNegative VP Spending")
print(len(negative_spending))

# -----------------------------
# Account Level
# -----------------------------
invalid_level = df[df["AccountLevel"] <= 0]

print("\nInvalid Account Level")
print(len(invalid_level))

# -----------------------------
# Days Since Last Login
# -----------------------------
negative_days = df[df["DaysSinceLastLogin"] < 0]

print("\nNegative Days Since Last Login")
print(len(negative_days))

# -----------------------------
# Summary Report
# -----------------------------
report = pd.DataFrame({
    "Validation Check": [
        "Missing Values",
        "Duplicate Rows",
        "Duplicate Player IDs",
        "Negative Session Length",
        "Invalid Rank",
        "Invalid Queue",
        "Invalid Map",
        "Wins > Matches",
        "Invalid Losses",
        "Negative Spending",
        "Invalid Account Level",
        "Negative Days Since Login"
    ],
    "Issues Found": [
        missing.sum(),
        duplicates,
        duplicate_players,
        len(negative_session),
        len(invalid_rank),
        len(invalid_queue),
        len(invalid_map),
        len(invalid_wins),
        len(invalid_losses),
        len(negative_spending),
        len(invalid_level),
        len(negative_days)
    ]
})

report.to_csv("../reports/validation_report.csv", index=False)

print("\nValidation report saved to reports/validation_report.csv")

print("\nValidation Completed Successfully.")