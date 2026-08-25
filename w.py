import csv
import os

def write_csv(filename, fieldnames, rows):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print("Created {}".format(filename))

#beginn
def generate_all_csvs():
    # Only generate if files don't already. existhgggg
    if not os.path.exists("turnout_demographics.csv"):
        write_csv(
            "turnout_demographics.csv",
            [
                "province",
                "voter_turnout_2019",
                "voter_turnout_2021",
                "age_between_18_34_population",
                "age_between_35_54_population"
                "age_for_55_plus_population",
                "total_population"
            ],
            [
                {"province": "Ontario", "voter_turnout_2019": "57.3", "voter_turnout_2021": "62.1",
                 "age_between_18_34_population": "4500000", "age_between_35_54_population": "5200000",
                 "age_for_55_plus_population": "3900000", "total_population": "13600000"}
            ]
        )

    if not os.path.exists("cpi_vote_change.csv"):
        write_csv(
            "cpi_vote_change.csv",
            [
                "province",
                "cpi_category",
                "cpi_change",
                "incumbent_vote_change"
            ],
            [
                {"province": "Ontario", "cpi_category": "Food", "cpi_change": "4.2", "incumbent_vote_change": "-1.8"}
            ]
        )

    if not os.path.exists("jobs_votes.csv"):
        write_csv(
            "jobs_votes.csv",
            [
                "province",
                "party",
                "job_type",
                "avg_job_vacancy_rate",
                "vote_share_change"
            ],
            [
                {"province": "Ontario", "party": "Liberal", "job_type": "Healthcare",
                 "avg_job_vacancy_rate": "5.4", "vote_share_change": "-1.2"}
            ]
        )


# ============================================================
#  SHARED CSV LOADER
# ============================================================

def load_csv(filename):
    rows = []
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)
    return rows


# ============================================================
#  QUESTION 1 — TURNOUT & DEMOGRAPHICS
# ============================================================

def find_age_population(row, lower, upper):
    if lower == 18 and upper == 34:
        return int(row["age_between_18_34_population"])
    elif lower == 35 and upper == 54:
        return int(row["age_between_35_54_population"])
    elif lower >= 55:
        return int(row["age_for_55_plus_population"])
    else:
        raise ValueError("Age range not supported.")


def analyze_turnout(province, lower, upper):
    data = load_csv("turnout_demographics.csv")

    for row in data:
        if row["province"].lower() == province.lower():

            turnout_2019 = float(row["voter_turnout_2019"])
            turnout_2021 = float(row["voter_turnout_2021"])
            total_population = int(row["total_population"])

            age_population = find_age_population(row, lower, upper)

            turnout_change = turnout_2021 - turnout_2019
            age_share = age_population / total_population

            print("\n--- Voter Turnout Analysis ---")
            print("Province: {}".format(province))
            print("Age Range: {}-{}".format(lower, upper))
            print("Turnout 2019: {}%".format(turnout_2019))
            print("Turnout 2021: {}%".format(turnout_2021))
            print("Turnout Change: {:.2f}%".format(turnout_change))
            print("Population Share: {:.2%}".format(age_share))
            return

    print("Province not found.")


# ============================================================
#  QUESTION 2 — CPI & INCUMBENT VOTE SHARE
# ============================================================

def get_cpi_change(data, province, category):
    for row in data:
        if row["province"].lower() == province.lower() and row["cpi_category"].lower() == category.lower():
            return float(row["cpi_change"])
    raise ValueError("No CPI data found.")


def get_incumbent_vote_change(data, province):
    for row in data:
        if row["province"].lower() == province.lower():
            return float(row["incumbent_vote_change"])
    raise ValueError("No vote change data found.")


def analyze_cpi_vote(province, category):
    data = load_csv("cpi_vote_change.csv")

    cpi_change = get_cpi_change(data, province, category)
    vote_change = get_incumbent_vote_change(data, province)

    print("\n--- CPI & Vote Share Analysis ---")
    print("Province: {}".format(province))
    print("CPI Category: {}".format(category))
    print("CPI Change: {:.2f}%".format(cpi_change))
    print("Incumbent Vote Share Change: {:.2f}%".format(vote_change))


# ============================================================
#  QUESTION 3 — JOB VACANCY & PARTY VOTE SHARE
# ============================================================

def get_job_vacancy_rate(data, province, job_type):
    for row in data:
        if row["province"].lower() == province.lower() and row["job_type"].lower() == job_type.lower():
            return float(row["avg_job_vacancy_rate"])
    raise ValueError("No vacancy data found.")


def get_vote_share_change(data, province, party):
    for row in data:
        if row["province"].lower() == province.lower() and row["party"].lower() == party.lower():
            return float(row["vote_share_change"])
    raise ValueError("No vote share data found.")


def analyze_jobs_votes(province, party, job_type):
    data = load_csv("jobs_votes.csv")

    vacancy_rate = get_job_vacancy_rate(data, province, job_type)
    vote_change = get_vote_share_change(data, province, party)

    print("\n--- Job Vacancy & Vote Share Analysis ---")
    print("Province: {}".format(province))
    print("Party: {}".format(party))
    print("Job Type: {}".format(job_type))
    print("Avg Vacancy Rate: {:.2f}%".format(vacancy_rate))
    print("Vote Share Change: {:.2f}%".format(vote_change))


# ============================================================
#  MAIN MENU
# ============================================================

def main():
    generate_all_csvs()

    print("\n=== How Canada Votes — Analysis System ===")
    print("1. Voter Turnout & Demographics")
    print("2. CPI & Incumbent Vote Share")
    print("3. Job Vacancy Rates & Party Vote Share")
    print("4. Exit")

    choice = input("Select an option: ").strip()

    if choice == "1":
        province = input("Enter province: ").strip()
        lower = int(input("Enter lower age: ").strip())
        upper = int(input("Enter upper age: ").strip())
        analyze_turnout(province, lower, upper)

    elif choice == "2":
        province = input("Enter province: ").strip()
        category = input("Enter CPI category: ").strip()
        analyze_cpi_vote(province, category)

    elif choice == "3":
        province = input("Enter province: ").strip()
        party = input("Enter party: ").strip()
        job_type = input("Enter job type: ").strip()
        analyze_jobs_votes(province, party, job_type)

    elif choice == "4":
        print("Exiting.")
        return

    else:
        print("Invalid selection.")


if __name__ == "__main__":
    main()



