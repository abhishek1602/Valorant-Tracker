import pandas as pd

# ----------------------------------------
# Load Dataset
# ----------------------------------------
df = pd.read_csv("../data/raw/valorant_players.csv")

print("=" * 60)
print("VALORANT DATA PREPROCESSING")
print("=" * 60)

print("\nOriginal Shape:")
print(df.shape)

# ----------------------------------------
# Remove Duplicate Rows
# ----------------------------------------
df = df.drop_duplicates()

# ----------------------------------------
# Convert LastLogin to Datetime
# ----------------------------------------
df["LastLogin"] = pd.to_datetime(df["LastLogin"])

# ----------------------------------------
# Win Rate
# ----------------------------------------
df["WinRate"] = (
    df["Wins"] / df["MatchesPlayed"]
).round(2)

# ----------------------------------------
# Spending Category
# ----------------------------------------
def spending_category(vp):

    if vp == 0:
        return "Free Player"

    elif vp <= 100:
        return "Low Spender"

    elif vp <= 300:
        return "Medium Spender"

    else:
        return "High Spender"

df["SpendingCategory"] = df["TotalVPSpent"].apply(spending_category)

# ----------------------------------------
# Player Segment
# ----------------------------------------
def player_segment(matches):

    if matches < 200:
        return "Casual"

    elif matches < 1000:
        return "Core"

    else:
        return "Hardcore"

df["PlayerSegment"] = df["MatchesPlayed"].apply(player_segment)

# ----------------------------------------
# Retention Bucket
# ----------------------------------------
def retention(days):

    if days <= 7:
        return "Active"

    elif days <= 30:
        return "At Risk"

    else:
        return "Churned"

df["RetentionBucket"] = df["DaysSinceLastLogin"].apply(retention)

# ----------------------------------------
# Average Hours Per Match
# ----------------------------------------
df["HoursPerMatch"] = (
    df["TotalHoursPlayed"] /
    df["MatchesPlayed"]
).round(2)

# ----------------------------------------
# Battle Pass Label
# ----------------------------------------
df["BattlePass"] = df["BattlePass"].replace({
    0: "No",
    1: "Yes"
})

# ----------------------------------------
# Save Clean Dataset
# ----------------------------------------
output_path = "../data/processed/valorant_players_cleaned.csv"

df.to_csv(
    output_path,
    index=False
)

print("\nCleaned Shape:")
print(df.shape)

print("\nNew Columns Added:")
print([
    "WinRate",
    "SpendingCategory",
    "PlayerSegment",
    "RetentionBucket",
    "HoursPerMatch"
])

print("\nDataset saved successfully!")

print(output_path)

print("\nFirst 5 Rows:\n")
print(df.head())