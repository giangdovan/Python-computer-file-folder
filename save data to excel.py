import pandas as pd
file_path='./files/titanic.xlsx'
df = pd.DataFrame(
        {
            "Name": [
                "Braund, Mr. Owen Harris",
                "Allen, Mr. William Henry",
                "Bonnell, Miss. Elizabeth",
            ],
            "Age": [22, 35, 58],
            "Sex": ["male", "male", "female"],
        }
    )

#df.to_excel('titanic.xlsx', index=False, engine='openpyxl') # xlsxwriter , openpyxl

with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='passengers', index=False)
    df.to_excel(writer, sheet_name='Sheet2', index=False)

titanic = pd.read_excel(file_path, sheet_name='passengers', engine='openpyxl')
print(titanic)

# # Write the DataFrame to a CSV file
# df.to_csv('titanic.csv', index=False)  # index=False to avoid writing row indices

# titanic = pd.read_csv('titanic.csv')  # Adjust the filename as necessary
# print(titanic)
