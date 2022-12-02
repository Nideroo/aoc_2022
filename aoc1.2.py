"""
--- Day 1: Calorie Counting ---
--- Part Two ---
By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.
To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories.
That way, even if one of those Elves runs out of snacks, they still have two backups.
In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories).
The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
"""


def main():
    calories_per_elf = {}
    with open("aoc1_input.txt") as input_file:
        i = 1  # Track elf number
        for line in input_file:
            line = line.strip()
            if line:
                if calories_per_elf.get(i):  # Add to entry for this elf
                    calories_per_elf[i] += int(line)  # Stripped line is a string representing number of calories
                else:
                    calories_per_elf[i] = int(line) # Make a new entry for this elf
            else:  # Blank line denotes end of current elf's inventory
                i += 1
    elves_top3_max_calories = sorted(calories_per_elf, key=calories_per_elf.get, reverse=True)[:3]
    print(f"Elves number {elves_top3_max_calories[0]}, {elves_top3_max_calories[1]} and {elves_top3_max_calories[2]} "
          f"carry the most food, altogether totaling "
          f"{sum([calories_per_elf[i] for i in elves_top3_max_calories])} calories.")


if __name__ == "__main__":
    main()