# Information for the assessment

#Hypothesis (H1) - Reducing Screen time improves well-being
#Null Hypothesis (H0) - Reducing Screen time has no effect on well-being

# Use p-value to determine whether the Alternative Hypothesis or the Null hypothesis is correct

#Dataset info
# df 1 - basic demographic info (unnecessary as we the focus of the analysis is to test the relationship between screen time and well being)
# df 2 - daily digital screen time of respondents
# df 3 - self reported well-being


#imported libraries
import pandas as pd #used for data manipulation and analysis
import scipy.stats as st # t - test
import statsmodels.stats.weightstats as stm # for calculating confidence interval
import math #math functions

# Reading the CSV into Dataframe (df)

df_screen_time = pd.read_csv("dataset2.csv")
df_well_being = pd.read_csv("dataset3.csv")

#Display first few rows of each dataset / Ensures that the data is correct and is able to be viewed in terminal.

print("\nScreen Time Data: ")
print(df_screen_time.head())

print("\nWell-Being Data: ")
print(df_well_being.head())

#Check Column Names and basic statistics

print("\nScreen Time Data Columns:")
print(df_screen_time.columns)

print("\nWell-Being Data Columns:")
print(df_well_being.columns)

print("\nScreen Time Data Info:")
print(df_screen_time.info())

print("\nWell-Being Data Info:")
print(df_well_being.info())

# Merge Dataset 2 and Dataset 3 on 'ID' / As dataset 2 and 3 contain the information for the data analysis (screen time and well-being indicator scores)
merged_data = pd.merge(df_screen_time, df_well_being, on='ID')

#check for any inconsistencies with original source to ensure no errors.
print(merged_data.columns)

# Calculate total screen time (summing different types of screen usage)
merged_data['total_screen_time'] = (
    merged_data['C_we'] + merged_data['C_wk'] +
    merged_data['G_we'] + merged_data['G_wk'] +   #By summing the total screen time for each device for both weekdays and weekends we can account for all days of the week and gain a broader range of data for the analysis.
    merged_data['T_we'] + merged_data['T_wk']
)


# Split the data into two groups based on the median of total screen time
median_screen_time = merged_data['total_screen_time'].median()
high_screen_time = merged_data[merged_data['total_screen_time'] > median_screen_time]
low_screen_time = merged_data[merged_data['total_screen_time'] <= median_screen_time]

# List of well-being variables
well_being_indicators = ['Optm', 'Usef', 'Relx', 'Intp', 'Engs', 'Dealpr',  #List of well being indicators to loop through.
                   'Thcklr', 'Goodme', 'Clsep', 'Conf', 'Mkmind', 
                   'Loved', 'Intthg', 'Cheer']

#list to store the results gained from the testing
results = []

# Step 3: Solve - Loop through each well-being variable and perform the t-test
for var in well_being_indicators:
    # Get the mean of high and low screen time groups for the well-being variable
    mean_high_screen_time = high_screen_time[var].mean()
    mean_low_screen_time = low_screen_time[var].mean()

    # Perform the t-test
    t_stat, p_value = st.ttest_ind(high_screen_time[var], low_screen_time[var], equal_var=False)

    # Check if the p-value is less than 0.05 (our significance level)
    if p_value < 0.05:
        conclusion = "Reducing screen time likely improves " + var
    else:
        conclusion = "No significant effect of screen time on " + var

    # Save the results for each variable
    results.append({'Variable': var,  
                    'Mean_High': mean_high_screen_time, #Dataframe listings for the output of the code 
                    'Mean_Low': mean_low_screen_time,
                    'T-statistic': t_stat,
                    'P-Value': p_value,
                    'Conclusion': conclusion})

# Convert the results into a DataFrame for easier viewing
results_df = pd.DataFrame(results)

# Step 4: Conclude - Display the results
print(results_df)









