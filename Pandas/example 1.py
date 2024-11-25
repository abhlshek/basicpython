import pandas as pd

#
# data = {
#     'name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'age': [25, 30, 35, 40],
#     'city': ['New york', 'LosAngeles', 'Chicago', 'Houston'],
# }
# df = pd.DataFrame(data)
# print(df)
#

data = {
    'Title': ['Book1', 'Book2', "Book3", "Book4"],
    'Publication_Years': [1995, 1996, 1997, 1998],
    'Price': [10, 20, 30, 100]
}
book_df = pd.DataFrame(data)
# print(book_df)
recent_book = book_df[book_df['Publication_Years'] >= 1996]
# print(recent_book)

chip_recent_book = recent_book[book_df['Price'] >= 100]
# print(chip_recent_book)

great_book = book_df[book_df['Title'].str.contains('Book3')]
# print(great_book)
cheap_recent_book = book_df[book_df['Publication_Years'] > 1950 & (book_df['Price'] < 10)]
# print(cheap_recent_book)
recent_books = book_df[(book_df['Publication_Years'] > 1950) | (book_df['Price'] < 20)]
# print(recent_books)

# sort value

books_sorted_by_year = book_df.sort_values(by='Publication_Years' ,ascending=False)
# print(books_sorted_by_year)

# sort index
books_sorted_by_index=book_df.sort_index(axis=0)
# print(books_sorted_by_index)

top_expensive_books=book_df.nlargest(3,'Price')
# print(top_expensive_books)
old_expensive_books=book_df.nsmallest(3,'Publication_Years')
# print(old_expensive_books)

# Aggregate Queries
data={
    'category':['A','B','A','B','A','B'],
    'value':[10,20,15,30,10,25],
    'quanitity':[1,2,3,4,2,3]
}
df=pd.DataFrame(data)
print(df)
total=df['value'].sum()
print(total)

total=df['value'].mean()
print(total)
max=df['value'].max()
print(max)
min=df['value'].min()
print(min)
count=df['value'].count()
print(count)

# Grouping Data
grouping_sum=df.groupby('category')['value'].sum()
print(grouping_sum)
grouping_mean=df.groupby('category')['value'].mean()
print(grouping_mean)
multiple_aggregations = df.groupby('category')['value'].agg(['sum', 'mean', 'max', 'min'])
print(multiple_aggregations)





