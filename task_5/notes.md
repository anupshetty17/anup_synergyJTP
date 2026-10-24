# Notes - Task 5

## How I cleaned the data

- **Duplicates:** S005 (Rohan) was there two times with the same values. I removed one. I remove exact same rows and also repeated student ids.
- **Domain:** the same domain was written in many ways (`ml`, `ML`, `MACHINE LEARNING`, `web`, `Web Dev`, `web development`, `electronics`). I made 4 names: ML, Web Dev, Electronics, Mechanical.
- **Submitted:** `yes`, `Yes`, `Y` -> Submitted. `no`, `N` -> Not Submitted.
- **Attendance:** removed the `%` sign and changed to number.
- **Score and study hours:** some were words (`nine`, `two`). I changed them to numbers (9 and 2).
- **Height:** some were in metres (`1.62 m`). I multiplied by 100 to get cm. The ones already in cm I just removed the text.
- **Weight:** all were in kg already so I just removed the `kg` text.

## Invalid values

- Dev (S007) has attendance `-10`. Attendance cannot be negative so I made it missing.
- Naina (S008) has attendance `105%`. Attendance cannot be more than 100 so I made it missing too. (I did not just change it to 100 because I dont know what the real value was.)

## Missing values

I used the **median** of the column to fill missing values. I chose median because mean can go up or down a lot if there is one weird value.

- Kabir (S003): attendance missing and weight missing -> filled with median.
- Omkar (S009): score missing -> filled with median.
- S007 and S008 attendance (the invalid ones above) -> also filled with median.

I did not treat all missing values the same way in the plots. The students with a filled score are left out of the score plots and the students with filled attendance are left out of the scatter plot, because filled values are not real data.

Kabir's score `0` and study hours `0` are real values (not missing) so I kept them as they are.

## Validation rules

1. Student ids are unique and not missing
2. Attendance between 0 and 100
3. Domain is one of the 4 allowed domains
4. Submitted is Submitted or Not Submitted
5. No missing values in the important columns
6. Numeric columns are really numbers
7. (extra) Score is between 0 and 10

The validation does not delete any rows. It only tells pass or fail.

## Problems I faced

- It was hard to decide what to do with attendance 105% and -10. I decided to treat them as invalid and not guess.
- Some values were words like `nine` so a normal number conversion gave errors. I made a small dictionary for words to numbers.
- Height had two units (cm and m) so I had to check the unit in the text first.
- The data is very small (10 students) so the plots and the correlation are not very strong proof.

## Observations

- After cleaning there are 10 rows and 9 columns.
- Read `output/plot_summary.md` for what the plots show. All numbers in it come from the code.
- Filling with the median is simple but it is a guess, so the real data would be better.
