{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Homework 5, Part 1: Building a pandas cheat sheet\n",
    "\n",
    "**Use `animals.csv` to answer the following questions.** The data is small and the questions are pretty simple, so hopefully you can use this for pandas reference in the future."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## First: things we didn't cover in class\n",
    "\n",
    "### Counting things\n",
    "\n",
    "If during class we had wanted to know how many countries were on each continent, I would use `df.continent.value_counts()`.\n",
    "\n",
    "Lots of people like to try `groupby` when you're counting things, but in pandas there is only one rule: **every time you want to count things and think you should use groupby.... don't use `groupby`!** Instead use `value_counts()`.\n",
    "\n",
    "### Filtering your dataset\n",
    "\n",
    "We also spent the whole time working with the entire dataset! Oftentimes you only want a subset of it.\n",
    "\n",
    "We might have wanted to do something like \"I only want to see countries in Africa.\" In the same way we can do math to every single row at the same time, we can also do comparisons for every single row. We could have asked, \"is your `continent` column equal to `\"Africa\"`?\"\n",
    "\n",
    "```python\n",
    "df.continent == 'Africa'\n",
    "```\n",
    "\n",
    "This only gives me a list of Trues and Falses, which isn't very useful by itself (...technically it's a Series since it has an index). What *is* very useful is being able to say, **I want to see all of the rows where the continent is Africa:**\n",
    "\n",
    "```python\n",
    "df[df.continent == 'Africa']\n",
    "```\n",
    "\n",
    "There we have it! I could also save this as another variable if I wanted to spend time working with it later:\n",
    "\n",
    "```python\n",
    "df_africa = df[df.continent == 'Africa']\n",
    "df_africa.head()\n",
    "```\n",
    "\n",
    "Hope that's helpful.\n",
    "\n",
    "### Graphing things\n",
    "\n",
    "Just put `.plot()` on the end of whatever you're looking at. It works like 75% of the time!\n",
    "\n",
    "```python\n",
    "df.groupby('continent').population.sum().plot(kind='barh')\n",
    "```\n",
    "\n",
    "The code above will give me a horizontal bar graph of the sum of each continent's population. Technically speaking it works because it's a Series and it plots the index vs the values. \n",
    "\n",
    "If you have a full dataframe, though, you usually need to give it the `x` and `y`.\n",
    "\n",
    "```python\n",
    "df.plot(x='life_expectancy', y='per_capita_gdp', kind='scatter')\n",
    "```\n",
    "\n",
    "This will give you a scatterplot of each country's life expectancy vs. its per-capita GDP."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 0) Setup\n",
    "\n",
    "Import pandas **with the correct name**."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1) Reading in a csv file\n",
    "\n",
    "Use pandas to read in the animals CSV file, saving it as a variable with the normal name for a dataframe"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv(\"animals.csv\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2) Checking your data\n",
    "\n",
    "Display the number of rows and columns in your data. Also display the names and data types of each column."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>animal</th>\n",
       "      <th>name</th>\n",
       "      <th>length</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>cat</td>\n",
       "      <td>Anne</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>cat</td>\n",
       "      <td>Bob</td>\n",
       "      <td>45</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>dog</td>\n",
       "      <td>Egglesburg</td>\n",
       "      <td>65</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>dog</td>\n",
       "      <td>Devon</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>cat</td>\n",
       "      <td>Charlie</td>\n",
       "      <td>32</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>dog</td>\n",
       "      <td>Fontaine</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>cat</td>\n",
       "      <td>Xypher</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  animal        name  length\n",
       "0    cat        Anne      35\n",
       "1    cat         Bob      45\n",
       "2    dog  Egglesburg      65\n",
       "3    dog       Devon      50\n",
       "4    cat     Charlie      32\n",
       "5    dog    Fontaine      35\n",
       "6    cat      Xypher      10"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "animal    object\n",
       "name      object\n",
       "length     int64\n",
       "dtype: object"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 7 entries, 0 to 6\n",
      "Data columns (total 3 columns):\n",
      " #   Column  Non-Null Count  Dtype \n",
      "---  ------  --------------  ----- \n",
      " 0   animal  7 non-null      object\n",
      " 1   name    7 non-null      object\n",
      " 2   length  7 non-null      int64 \n",
      "dtypes: int64(1), object(2)\n",
      "memory usage: 296.0+ bytes\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3) Display the first 3 animals\n",
    "\n",
    "Hmmm, we know how to take the first 5, but maybe the first 3. Maybe there is an option to change how many you get? Use `?` to check the documentation on the command."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>animal</th>\n",
       "      <th>name</th>\n",
       "      <th>length</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>cat</td>\n",
       "      <td>Anne</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>cat</td>\n",
       "      <td>Bob</td>\n",
       "      <td>45</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>dog</td>\n",
       "      <td>Egglesburg</td>\n",
       "      <td>65</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  animal        name  length\n",
       "0    cat        Anne      35\n",
       "1    cat         Bob      45\n",
       "2    dog  Egglesburg      65"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4) Sort the animals to show me the 3 longest animals\n",
    "\n",
    "> **TIP:** You can use `.head()` after you sort things!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>animal</th>\n",
       "      <th>name</th>\n",
       "      <th>length</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>dog</td>\n",
       "      <td>Egglesburg</td>\n",
       "      <td>65</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>dog</td>\n",
       "      <td>Devon</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>cat</td>\n",
       "      <td>Bob</td>\n",
       "      <td>45</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  animal        name  length\n",
       "2    dog  Egglesburg      65\n",
       "3    dog       Devon      50\n",
       "1    cat         Bob      45"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = df.sort_values(by=\"length\", ascending=False)\n",
    "df.head(3)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 5) Get the mean and standard deviation of animal lengths\n",
    "\n",
    "You can do this with separate commands or with a single command.\n",
    "\n",
    "> **Tip:** You don't know how to do standard deviation, but remember when we did `df.so` and hit tab and it suggested some options for sorting? I'm assuming the standard deviation method starts with `s`...."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "length    17.101935\n",
       "dtype: float64"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.std(numeric_only=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 6) How many cats do we have and how many dogs?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "cat    4\n",
       "dog    3\n",
       "Name: animal, dtype: int64"
      ]
     },
     "execution_count": 133,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.animal.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "animal    3\n",
       "name      3\n",
       "length    3\n",
       "dtype: int64"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 7) Only display the dogs\n",
    "\n",
    "> **TIP:** It's probably easiest to make it display the list of `True`/`False` first, then wrap the `df[]` around it."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>animal</th>\n",
       "      <th>name</th>\n",
       "      <th>length</th>\n",
       "      <th>length_inches</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>dog</td>\n",
       "      <td>Egglesburg</td>\n",
       "      <td>65</td>\n",
       "      <td>25.590551</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>dog</td>\n",
       "      <td>Devon</td>\n",
       "      <td>50</td>\n",
       "      <td>19.685039</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>dog</td>\n",
       "      <td>Fontaine</td>\n",
       "      <td>35</td>\n",
       "      <td>13.779528</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  animal        name  length  length_inches\n",
       "2    dog  Egglesburg      65      25.590551\n",
       "3    dog       Devon      50      19.685039\n",
       "5    dog    Fontaine      35      13.779528"
      ]
     },
     "execution_count": 134,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df.animal == 'dog']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 8) Only display the animals that are longer than 40cm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>animal</th>\n",
       "      <th>name</th>\n",
       "      <th>length</th>\n",
       "      <th>length_inches</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>dog</td>\n",
       "      <td>Egglesburg</td>\n",
       "      <td>65</td>\n",
       "      <td>25.590551</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>dog</td>\n",
       "      <td>Devon</td>\n",
       "      <td>50</td>\n",
       "      <td>19.685039</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>cat</td>\n",
       "      <td>Bob</td>\n",
       "      <td>45</td>\n",
       "      <td>17.716535</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  animal        name  length  length_inches\n",
       "2    dog  Egglesburg      65      25.590551\n",
       "3    dog       Devon      50      19.685039\n",
       "1    cat         Bob      45      17.716535"
      ]
     },
     "execution_count": 135,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df.length > 40]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 9) `length` is the animal's length in centimeters. Create a new column called `inches` that is the length in inches."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>animal</th>\n",
       "      <th>name</th>\n",
       "      <th>length</th>\n",
       "      <th>length_inches</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>dog</td>\n",
       "      <td>Egglesburg</td>\n",
       "      <td>65</td>\n",
       "      <td>25.590551</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>dog</td>\n",
       "      <td>Devon</td>\n",
       "      <td>50</td>\n",
       "      <td>19.685039</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>cat</td>\n",
       "      <td>Bob</td>\n",
       "      <td>45</td>\n",
       "      <td>17.716535</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>cat</td>\n",
       "      <td>Anne</td>\n",
       "      <td>35</td>\n",
       "      <td>13.779528</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>dog</td>\n",
       "      <td>Fontaine</td>\n",
       "      <td>35</td>\n",
       "      <td>13.779528</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>cat</td>\n",
       "      <td>Charlie</td>\n",
       "      <td>32</td>\n",
       "      <td>12.598425</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>cat</td>\n",
       "      <td>Xypher</td>\n",
       "      <td>10</td>\n",
       "      <td>3.937008</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  animal        name  length  length_inches\n",
       "2    dog  Egglesburg      65      25.590551\n",
       "3    dog       Devon      50      19.685039\n",
       "1    cat         Bob      45      17.716535\n",
       "0    cat        Anne      35      13.779528\n",
       "5    dog    Fontaine      35      13.779528\n",
       "4    cat     Charlie      32      12.598425\n",
       "6    cat      Xypher      10       3.937008"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"length_inches\"] = df[\"length\"] / 2.54\n",
    "df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 10) Save the cats to a separate variable called `cats`. Save the dogs to a separate variable called `dogs`.\n",
    "\n",
    "This is the same as listing them, but you just save the result to a variable instead of looking at it. Be sure to use `.head()` to make sure your data looks right.\n",
    "\n",
    "Once you do this, every time you use `cats` you'll only be talking about the cats, and same for the dogs."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [],
   "source": [
    "dogs = df[df.animal == 'dog']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [],
   "source": [
    "cats = df[df.animal == 'cat']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>animal</th>\n",
       "      <th>name</th>\n",
       "      <th>length</th>\n",
       "      <th>length_inches</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>dog</td>\n",
       "      <td>Egglesburg</td>\n",
       "      <td>65</td>\n",
       "      <td>25.590551</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>dog</td>\n",
       "      <td>Devon</td>\n",
       "      <td>50</td>\n",
       "      <td>19.685039</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>dog</td>\n",
       "      <td>Fontaine</td>\n",
       "      <td>35</td>\n",
       "      <td>13.779528</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  animal        name  length  length_inches\n",
       "2    dog  Egglesburg      65      25.590551\n",
       "3    dog       Devon      50      19.685039\n",
       "5    dog    Fontaine      35      13.779528"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dogs.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 11) Display all of the animals that are cats and above 12 inches long.\n",
    "\n",
    "First do it using the `cats` variable, then also do it using your `df` dataframe.\n",
    "\n",
    "> **TIP:** For multiple conditions, you use `df[(one condition) & (another condition)]`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>animal</th>\n",
       "      <th>name</th>\n",
       "      <th>length</th>\n",
       "      <th>length_inches</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>cat</td>\n",
       "      <td>Bob</td>\n",
       "      <td>45</td>\n",
       "      <td>17.716535</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>cat</td>\n",
       "      <td>Anne</td>\n",
       "      <td>35</td>\n",
       "      <td>13.779528</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>cat</td>\n",
       "      <td>Charlie</td>\n",
       "      <td>32</td>\n",
       "      <td>12.598425</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  animal     name  length  length_inches\n",
       "1    cat      Bob      45      17.716535\n",
       "0    cat     Anne      35      13.779528\n",
       "4    cat  Charlie      32      12.598425"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cats[cats.length_inches > 12]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>animal</th>\n",
       "      <th>name</th>\n",
       "      <th>length</th>\n",
       "      <th>length_inches</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>cat</td>\n",
       "      <td>Bob</td>\n",
       "      <td>45</td>\n",
       "      <td>17.716535</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>cat</td>\n",
       "      <td>Anne</td>\n",
       "      <td>35</td>\n",
       "      <td>13.779528</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>cat</td>\n",
       "      <td>Charlie</td>\n",
       "      <td>32</td>\n",
       "      <td>12.598425</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  animal     name  length  length_inches\n",
       "1    cat      Bob      45      17.716535\n",
       "0    cat     Anne      35      13.779528\n",
       "4    cat  Charlie      32      12.598425"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[(df.animal == \"cat\") & (df.length_inches > 12)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 12) What's the mean length of a cat? What's the mean length of a dog?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "30.5"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cats.length.mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "50.0"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dogs.length.mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 13) If you didn't already, use `groupby` to do #12 all at once"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "animal\n",
       "cat    30.5\n",
       "dog    50.0\n",
       "Name: length, dtype: float64"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby(by='animal').length.mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 14) Make a histogram of the length of dogs.\n",
    "\n",
    "We didn't talk about how to make a histogram in class! It **does not** use `plot()`. Imagine you're a programmer who doesn't want to type out `histogram` - what do you think you'd type instead?\n",
    "\n",
    "> **TIP:** The method is four letters long\n",
    ">\n",
    "> **TIP:** First you'll say \"I want the length column,\" then you'll say \"make a histogram\"\n",
    ">\n",
    "> **TIP:** This is the worst histogram ever"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXQAAAD4CAYAAAD8Zh1EAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAAsTAAALEwEAmpwYAAAQkElEQVR4nO3df2xdd3nH8fdDQmCKWQqEWVXSkWgLY1E7Suu1ICaw+TG5bEo2UaFWpSOIkk0iExIbI4ip2zomrZsyGF3HljEIYwUvq8QatREFlVpo09olUUtDWrpZIYx4JQFSLLl0lI5nf9yT7WKufY+vj3vv/er9kqzcc8/3fv08/p58cn3scxKZiSRp+D2r3wVIkpphoEtSIQx0SSqEgS5JhTDQJakQa/v1iTdu3Jhbtmzp6bVPPPEE69evb7agPrGXwVNKH2Avg2olvRw7duxbmfmiTvv6Fuhbtmzh6NGjPb12enqa8fHxZgvqE3sZPKX0AfYyqFbSS0R8bbF9nnKRpEIY6JJUCANdkgphoEtSIQx0SSqEgS5Jhega6BHxsYg4GxFfXmR/RMSHI2ImIh6KiMuaL1OS1E2dd+gHgMkl9l8FbKs+dgMfWXlZkqTl6hromflF4NwSQ3YCf5ct9wEXRMSFTRUoSaon6vwHFxGxBbgzMy/usO9O4I8z85+r7XuA92bmj1wGGhG7ab2LZ3R09PKpqameij57bo4zT/b00hW7ZNOGRuebn59nZGSk0Tn7pZRePL4GU9O9HJ+da2yu5dq6YU3PvUxMTBzLzLFO+57RS/8zcz+wH2BsbCx7vfT1ltvuYN/x/ty14NR1443O5+XMg8fjazA13cuuvXc1NtdyHZhcvyrr0sRvucwCF7Vtb66ekyQ9g5oI9EPAr1W/7fIKYC4zH2tgXknSMnT9vjIiPg2MAxsj4jTwe8CzATLzr4DDwBuBGeC7wNtWq1hJ0uK6BnpmXttlfwLvbKwiSVJPvFJUkgphoEtSIQx0SSqEgS5JhTDQJakQBrokFcJAl6RCGOiSVAgDXZIKYaBLUiEMdEkqhIEuSYUw0CWpEAa6JBXCQJekQhjoklQIA12SCmGgS1IhDHRJKoSBLkmFMNAlqRAGuiQVwkCXpEIY6JJUCANdkgphoEtSIQx0SSqEgS5JhTDQJakQBrokFcJAl6RCGOiSVIhagR4RkxHxaETMRMTeDvt/MiLujYgHIuKhiHhj86VKkpbSNdAjYg1wK3AVsB24NiK2Lxj2u8DBzHw5cA3wl00XKklaWp136FcAM5l5MjOfAqaAnQvGJPDj1eMNwH81V6IkqY7IzKUHRFwNTGbmDdX29cCVmbmnbcyFwOeA5wPrgddn5rEOc+0GdgOMjo5ePjU11VPRZ8/NcebJnl66Ypds2tDofPPz84yMjDQ6Z7+U0ovH12Bqupfjs3ONzbVcWzes6bmXiYmJY5k51mnf2hVV9f+uBQ5k5r6IeCXwyYi4ODN/0D4oM/cD+wHGxsZyfHy8p092y213sO94U6Uvz6nrxhudb3p6ml6/DoOmlF48vgZT073s2ntXY3Mt14HJ9auyLnVOucwCF7Vtb66ea/d24CBAZv4r8FxgYxMFSpLqqRPoR4BtEbE1ItbR+qHnoQVj/hN4HUBE/CytQP9mk4VKkpbWNdAz82lgD3A38Ait32Y5ERE3RcSOathvAe+IiC8BnwZ2ZbeT85KkRtU6UZiZh4HDC567se3xw8Crmi1NkrQcXikqSYUw0CWpEAa6JBXCQJekQhjoklQIA12SCmGgS1IhDHRJKoSBLkmFMNAlqRAGuiQVwkCXpEIY6JJUCANdkgphoEtSIQx0SSqEgS5JhTDQJakQBrokFcJAl6RCGOiSVAgDXZIKYaBLUiEMdEkqhIEuSYUw0CWpEAa6JBXCQJekQhjoklQIA12SCmGgS1IhDHRJKkStQI+IyYh4NCJmImLvImPeHBEPR8SJiPhUs2VKkrpZ221ARKwBbgXeAJwGjkTEocx8uG3MNuB9wKsy8/GI+InVKliS1Fmdd+hXADOZeTIznwKmgJ0LxrwDuDUzHwfIzLPNlilJ6qZOoG8Cvt62fbp6rt1LgJdExL9ExH0RMdlUgZKkeiIzlx4QcTUwmZk3VNvXA1dm5p62MXcC3wfeDGwGvghckpnfWTDXbmA3wOjo6OVTU1M9FX323BxnnuzppSt2yaYNjc43Pz/PyMhIo3P2Sym9eHwNpqZ7OT4719hcy7V1w5qee5mYmDiWmWOd9nU9hw7MAhe1bW+unmt3Grg/M78PfDUi/h3YBhxpH5SZ+4H9AGNjYzk+Pl6rgYVuue0O9h2vU3rzTl033uh809PT9Pp1GDSl9OLxNZia7mXX3rsam2u5DkyuX5V1qXPK5QiwLSK2RsQ64Brg0IIx/wSMA0TERlqnYE42V6YkqZuugZ6ZTwN7gLuBR4CDmXkiIm6KiB3VsLuBb0fEw8C9wHsy89urVbQk6UfV+r4yMw8Dhxc8d2Pb4wTeXX1IkvrAK0UlqRAGuiQVwkCXpEIY6JJUCANdkgphoEtSIQx0SSqEgS5JhTDQJakQBrokFcJAl6RCGOiSVAgDXZIKYaBLUiEMdEkqhIEuSYUw0CWpEAa6JBXCQJekQhjoklQIA12SCmGgS1IhDHRJKoSBLkmFMNAlqRAGuiQVwkCXpEIY6JJUCANdkgphoEtSIQx0SSqEgS5JhTDQJakQtQI9IiYj4tGImImIvUuMe1NEZESMNVeiJKmOroEeEWuAW4GrgO3AtRGxvcO45wHvAu5vukhJUnd13qFfAcxk5snMfAqYAnZ2GPeHwM3AfzdYnySppsjMpQdEXA1MZuYN1fb1wJWZuadtzGXA+zPzTRExDfx2Zh7tMNduYDfA6Ojo5VNTUz0VffbcHGee7OmlK3bJpg2Nzjc/P8/IyEijc/ZLKb14fA2mpns5PjvX2FzLtXXDmp57mZiYOJaZHU9rr11RVUBEPAv4M2BXt7GZuR/YDzA2Npbj4+M9fc5bbruDfcdXXHpPTl033uh809PT9Pp1GDSl9OLxNZia7mXX3rsam2u5DkyuX5V1qXPKZRa4qG17c/Xcec8DLgamI+IU8ArgkD8YlaRnVp1APwJsi4itEbEOuAY4dH5nZs5l5sbM3JKZW4D7gB2dTrlIklZP10DPzKeBPcDdwCPAwcw8ERE3RcSO1S5QklRPrROFmXkYOLzguRsXGTu+8rIkScvllaKSVAgDXZIKYaBLUiEMdEkqhIEuSYUw0CWpEAa6JBXCQJekQhjoklQIA12SCmGgS1IhDHRJKoSBLkmFMNAlqRAGuiQVwkCXpEIY6JJUCANdkgphoEtSIQx0SSqEgS5JhTDQJakQBrokFcJAl6RCGOiSVAgDXZIKYaBLUiEMdEkqhIEuSYUw0CWpEAa6JBXCQJekQtQK9IiYjIhHI2ImIvZ22P/uiHg4Ih6KiHsi4sXNlypJWkrXQI+INcCtwFXAduDaiNi+YNgDwFhm/hxwO/AnTRcqSVpanXfoVwAzmXkyM58CpoCd7QMy897M/G61eR+wudkyJUndRGYuPSDiamAyM2+otq8HrszMPYuM/wvgG5n5gQ77dgO7AUZHRy+fmprqqeiz5+Y482RPL12xSzZtaHS++fl5RkZGGp2zX0rpxeNrMDXdy/HZucbmWq6tG9b03MvExMSxzBzrtG/tiqpaICLeAowBr+m0PzP3A/sBxsbGcnx8vKfPc8ttd7DveKOl13bquvFG55uenqbXr8OgKaUXj6/B1HQvu/be1dhcy3Vgcv2qrEudo3YWuKhte3P13A+JiNcD7wdek5nfa6Y8SVJddc6hHwG2RcTWiFgHXAMcah8QES8H/hrYkZlnmy9TktRN10DPzKeBPcDdwCPAwcw8ERE3RcSOatifAiPAP0bEgxFxaJHpJEmrpNaJwsw8DBxe8NyNbY9f33BdkqRl8kpRSSqEgS5JhTDQJakQBrokFcJAl6RCGOiSVAgDXZIKYaBLUiEMdEkqhIEuSYUw0CWpEAa6JBXCQJekQhjoklQIA12SCmGgS1IhDHRJKoSBLkmFMNAlqRAGuiQVwkCXpEIY6JJUCANdkgphoEtSIQx0SSqEgS5JhTDQJakQBrokFcJAl6RCGOiSVAgDXZIKYaBLUiEMdEkqRK1Aj4jJiHg0ImYiYm+H/c+JiH+o9t8fEVsar1SStKSugR4Ra4BbgauA7cC1EbF9wbC3A49n5k8DHwRubrpQSdLS6rxDvwKYycyTmfkUMAXsXDBmJ/CJ6vHtwOsiIporU5LUzdoaYzYBX2/bPg1cudiYzHw6IuaAFwLfah8UEbuB3dXmfEQ82kvRwMaFcz9TovnvPfrWyyoopRePr8FUTC8TN6+olxcvtqNOoDcmM/cD+1c6T0QczcyxBkrqO3sZPKX0AfYyqFarlzqnXGaBi9q2N1fPdRwTEWuBDcC3myhQklRPnUA/AmyLiK0RsQ64Bji0YMwh4K3V46uBL2RmNlemJKmbrqdcqnPie4C7gTXAxzLzRETcBBzNzEPA3wKfjIgZ4Byt0F9NKz5tM0DsZfCU0gfYy6BalV7CN9KSVAavFJWkQhjoklSIgQ/0iHhuRPxbRHwpIk5ExB9Uzx+IiK9GxIPVx6V9LrWWiFgTEQ9ExJ3V9tbqdgkz1e0T1vW7xro69DKsa3IqIo5XNR+tnntBRHw+Iv6j+vP5/a6zjkV6+f2ImG1blzf2u85uIuKCiLg9Ir4SEY9ExCuHeE069bIqazLwgQ58D3htZr4MuBSYjIhXVPvek5mXVh8P9qvAZXoX8Ejb9s3AB6vbJjxO6zYKw2JhLzCcawIwUdV8/neD9wL3ZOY24J5qe1gs7AVax9j5dTnct8rq+3Pgs5n5UuBltI6zYV2TTr3AKqzJwAd6tsxXm8+uPobyJ7kRsRn4JeCj1XYAr6V1uwRo3T7hV/pS3DIt7KVA7bezGJp1KUFEbABeTeu358jMpzLzOwzhmizRy6oY+ECH//vW/kHgLPD5zLy/2vVHEfFQRHwwIp7Tvwpr+xDwO8APqu0XAt/JzKer7dO0bqMwDD7ED/dy3rCtCbTeIHwuIo5Vt6cAGM3Mx6rH3wBG+1PasnXqBWBPtS4fG4JTFVuBbwIfr07pfTQi1jOca7JYL7AKazIUgZ6Z/5OZl9K6SvWKiLgYeB/wUuDngRcA7+1fhd1FxC8DZzPzWL9rWaklehmqNWnzC5l5Ga07ir4zIl7dvrO6SG5Yvivs1MtHgJ+idcryMWBf/8qrZS1wGfCRzHw58AQLTq8M0Zos1suqrMlQBPp51bcq9wKTmflYdTrme8DHad0VcpC9CtgREado3bHytbTOrV1Q3S4BOt9WYRD9SC8R8fdDuCYAZOZs9edZ4DO06j4TERcCVH+e7V+F9XXqJTPPVG+KfgD8DYO/LqeB023fid9OKxSHcU069rJaazLwgR4RL4qIC6rHPwa8AfhK28IGrXNpX+5XjXVk5vsyc3NmbqF1Je0XMvM6Wv9AXV0NeytwR59KrG2RXt4ybGsCEBHrI+J55x8Dv0ir7vbbWQzFuizWy/l1qfwqA74umfkN4OsR8TPVU68DHmYI12SxXlZrTZ7Ruy326ELgE9H6jzaeBRzMzDsj4gsR8SIggAeB3+hjjSvxXmAqIj4APED1w5MhddsQrsko8JnWv0GsBT6VmZ+NiCPAwYh4O/A14M19rLGuxXr5ZPUrpAmcAn69bxXW95u0jqd1wEngbVR//4dsTaBzLx9ejTXx0n9JKsTAn3KRJNVjoEtSIQx0SSqEgS5JhTDQJakQBrokFcJAl6RC/C/x92sNirnv4gAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "dogs.length.hist()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 15) Make a horizontal bar graph of the length of the animals, with the animal's name as the label\n",
    "\n",
    "> **TIP:** It isn't `df['length'].plot()`, because it needs *both* columns. Think about how we did the scatterplot in class.\n",
    ">\n",
    "> **TIP:** Which is the `x` axis and which is the `y` axis? You'll notice pandas is kind of weird and wrong.\n",
    ">\n",
    "> **TIP:** Make sure you specify the `kind` of graph or else it will be a weird line thing\n",
    ">\n",
    "> **TIP:** If you want, you can set a custom size for your plot by sending it something like `figsize=(15,2)`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>animal</th>\n",
       "      <th>name</th>\n",
       "      <th>length</th>\n",
       "      <th>length_inches</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>dog</td>\n",
       "      <td>Egglesburg</td>\n",
       "      <td>65</td>\n",
       "      <td>25.590551</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>dog</td>\n",
       "      <td>Devon</td>\n",
       "      <td>50</td>\n",
       "      <td>19.685039</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>cat</td>\n",
       "      <td>Bob</td>\n",
       "      <td>45</td>\n",
       "      <td>17.716535</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>cat</td>\n",
       "      <td>Anne</td>\n",
       "      <td>35</td>\n",
       "      <td>13.779528</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>dog</td>\n",
       "      <td>Fontaine</td>\n",
       "      <td>35</td>\n",
       "      <td>13.779528</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>cat</td>\n",
       "      <td>Charlie</td>\n",
       "      <td>32</td>\n",
       "      <td>12.598425</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>cat</td>\n",
       "      <td>Xypher</td>\n",
       "      <td>10</td>\n",
       "      <td>3.937008</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  animal        name  length  length_inches\n",
       "2    dog  Egglesburg      65      25.590551\n",
       "3    dog       Devon      50      19.685039\n",
       "1    cat         Bob      45      17.716535\n",
       "0    cat        Anne      35      13.779528\n",
       "5    dog    Fontaine      35      13.779528\n",
       "4    cat     Charlie      32      12.598425\n",
       "6    cat      Xypher      10       3.937008"
      ]
     },
     "execution_count": 122,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:ylabel='name'>"
      ]
     },
     "execution_count": 130,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.plot(x='name', y='length', kind='barh')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 16) Make a sorted horizontal bar graph of the cats, with the larger cats on top\n",
    "\n",
    "> **TIP:** Think in steps, even though it's all on one line - first make sure you can sort it, then try to graph it."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:ylabel='name'>"
      ]
     },
     "execution_count": 138,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAdEAAAEJCAYAAADLrh3ZAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAAsTAAALEwEAmpwYAAAgb0lEQVR4nO3deVRV9f7/8ddBFBW1o4iIhBGKCohDmXOaUSZ2DcdLowN1RRxStKupJWreqHDCUq85iy7LMa28erOQK5Zjt1LjIl0MSUv9qkcFwQH4/eGv8+18KfVswHOA52Mt1uLs/dmf896fxfLlnj7bZLFYCgUAAOzm4ugCAAAoqwhRAAAMIkQBADCIEAUAwCBCFAAAgwhRAAAMIkQBADCIEAUAwCBCFE4hPT3d0SWUaYyfcYxd8VT08SNEAQAwiBAFAMAgQhQAAIMIUQAADCJEAQAwiBAFAMAgQhQAAIMIUQAADCJEAQAwiBAFAMAgQhQAAIMIUQAADDJZLJZCRxdR3piXn3R0CQAASZYhPqXaP0eiAAAYRIgCAGAQIQoAgEGEKAAABhGiAAAYRIgCAGAQIQoAgEGEKAAABhGitxAdHa2IiAhHlwEAcFLlNkSjo6NlNputP/7+/oqIiNCxY8ccXRoAoJwotyEqSY888ojS0tKUlpamTZs2KTc3V88//7yjywIAlBPlOkTd3Nzk5eUlLy8vtWrVSsOHD9exY8eUm5srSTp69KjCw8NVv359+fn5KTo6WhcvXizST3x8vAICAuTj46Phw4dbtwcAVGzlOkR/6/Lly9q0aZOCgoJUrVo15eTkqF+/fnJ3d9fnn3+u1atXa//+/Ro5cqTNdnv27NGRI0e0ZcsWrVq1SklJSYqNjXXQXgAAnImrowsoTTt37pSPz80Z/HNycnTvvfdq3bp1kqQNGzboypUrWrRokWrWrClJmjt3rnr16qWMjAz5+/tLklxcXDR//nzVqFFDQUFBmjp1qkaNGqXY2Fi5u7s7ZscAAHckPT292H0EBAT84bpyHaIdO3ZUQkKCJMlisWjJkiXq27evdu7cqbS0NAUHB1sDVJLatWsnFxcX/ec//7GGaHBwsGrUqGFt07ZtW127dk3Hjx9X8+bN7+4OAQDscqsALAnlOkSrV69uDUNJevfdd9WwYUOtWLHiltuZTKZSrgwAUB5UmGui0s1wdHFxUW5urpo2baqjR4/q8uXL1vX79u1TQUGBmjZtal32/fffKycnx/r5wIEDqlKliu6///67WjsAwPmU6xC9evWqTp8+rdOnTystLU3jx49Xdna2evTooQEDBqh69eoaNmyYjh49qj179igmJka9evWyOXrNz8/XyJEjlZqaqqSkJE2bNk2DBg3ieigAoHyfzt21a5f1qLJmzZoKCAjQihUr9PDDD0uSNm7cqIkTJyo0NFRubm7q2bOn3nrrLZs+OnXqpGbNmqlXr17Kzc1Vr169NG3atLu+LwAA52OyWCyFji6ivDEvP+noEgAAkixDfEq1/3J9OhcAgNJEiAIAYBAhCgCAQYQoAAAGEaIAABhEiAIAYBAhCgCAQYQoAAAGMdkCnEJ6enqpv22hPGP8jGPsiqeijx9HogAAGESIAgBgECEKAIBBhCgAAAYRogAAGESIAgBgECEKAIBBhCgAAAYRogAAGESIAgBgECEKAIBBhCgAAAYRogAAGESIAgBgECEKAIBBhCgAAAYRogAAGESIAgBgECEKAIBBhCgAAAYRogAAGESIAgBgECEKAIBBhCgAAAYRogAAGESIAgBgECEKAIBBhCgAAAaZLBZLoaOLKG/My086ugQA5YRliI+jS7il9PR0BQQEOLoMh+FIFAAAgwhRAAAMIkQBADCIEAUAwCBCFAAAgwhRAAAMIkQBADCIEAUAwCBCFAAAg8psiH7zzTeqU6eOnnjiCUeXAgCooMpsiCYmJurFF19Uamqq0tLSHF0OAKACKpMhmpubq/Xr12vw4MF66qmnlJiYaF2XmZkps9msLVu2qHfv3vL29la7du2UlJRkbbN7926ZzWYlJycrNDRU3t7eeuSRR/TNN9/YfM++ffvUs2dPeXt7KzAwUGPHjtWlS5fu1m4CAJxcmQzRLVu2yNfXV8HBwYqIiNAHH3yg69ev27SZMWOGoqKilJKSotatWysyMlLZ2dk2baZNm6bY2FglJyerTp06Gjp0qAoLb87Hf/ToUfXt21dhYWFKSUlRYmKiDh8+rJEjR961/QQAODdXRxdgRGJiop5++mlJUufOnVWtWjVt27ZN4eHh1jbDhw9XWFiYJGnKlCn64IMPdPjwYXXo0MHaZvLkyerSpYskafz48erRo4dOnTolHx8fzZs3T3369NGoUaOs7WfNmqUuXbro7Nmz8vT0vBu7CqCCS09Pd3QJt1UWaiyOW72lpsyFaEZGhvbu3aslS5ZIkkwmk/785z8rMTHRJkSDg4Otv3t7e0uSzp49a9PXb9vUr1/f2sbHx0fffvutMjIytHnzZmubX49Sjx8/TogCuCuc/TVjFf1VaGUuRFetWqX8/Hw1b97cuuzXcPvpp5+syypXrmz93WQy2bS7kzYFBQUaOHCghg8fXqSGX0MZAFCxlakQvXHjhtauXavY2Ngij7ZERUVpzZo11tO8xdWyZUulpqbK39+/RPoDAJQ/ZerGoh07dujcuXMaNGiQgoKCbH769eunNWvWFDnaNGr06NH6+uuvFRMTYz21u337do0ZM6ZE+gcAlH1lKkQTExP18MMPq06dOkXW9e7dWydOnNCuXbtK5LuaN2+ubdu26cSJE/rTn/6kzp07a/r06VwLBQBYmSwWS8kcusHKvPyko0sAUE5Yhvg4uoRbqug3FpWpI1EAAJwJIQoAgEGG7869dOmSDh06pLNnz+qRRx5RvXr1SrIuAACcnqEj0VmzZikwMFB9+/bVsGHDlJqaKkk6d+6cvL29tWzZshItEgAAZ2R3iC5btkwzZsxQ//79tXz5cptHSjw8PNSzZ0999NFHJVkjAABOye4QXbRokXr37q2EhATrvLO/1aJFCx07dqxEigMAwJnZHaI//vijunbt+ofrzWazLly4UKyiAAAoC+wOUbPZXGQi999KTU2Vl5dXsYoCAKAssPvu3O7du2vlypV66aWXiqw7cuSIVq1apYEDB5ZIcWWVsz8c7Ywq+gPbxcX4GcfYoTjsPhJ97bXXJEkdOnTQ1KlTZTKZtGbNGkVGRio0NFReXl4aP358iRcKAICzsTtEvby8tGvXLj3xxBP6+OOPVVhYqPXr12vnzp0aMGCAPvvss9+d2xYAgPLG0GQLdevWVUJCghISEvQ///M/KigoUN26deXiwgRIAICKo9jvE61bt25J1AEAQJljKEQvX76sjz76SJmZmbJYLEXe4WkymTRz5swSKRAAAGdld4h+8cUXGjx4sC5fvvyHbQhRAEBFYHeITpgwQbVq1dLKlSv14IMPqlatWqVRFwAATs/uO4F++uknjRo1St26dSNAAQAVmt0h2rx5c128eLE0agEAoEyxO0SnT5+upUuX6sCBA6VRDwAAZYbd10Q7dOiguLg49ejRQ40bN5aPj48qVapk08ZkMmndunUlViQAAM7I7hDdvHmzoqKiVFBQoNOnTys3N7dIG5PJVCLFAQDgzOwO0WnTpikgIECrVq1S48aNS6MmAADKBLuviZ45c0aRkZEEKACgwrM7RFu3bq0TJ06URi0AAJQpdodofHy8Nm/erPXr15dGPQAAlBl2XxMdMmSIrl+/rqioKI0ZM0be3t6/e3fu3r17S6xIAACckd0hWrduXXl6enJNFABQ4dkdop9++mlp1AEAQJnDW7QBADDI8Eu5r1+/rmPHjunSpUsqKCgosr5Tp07FKgwAAGdnd4gWFhbqjTfe0OLFi5WTk/OH7c6fP1+swgAAcHZ2n86dO3eu5syZo379+unvf/+7CgsLNXXqVM2ZM0eBgYEKCQnR5s2bS6NWAACcit0hunr1aj311FOaO3euHnvsMUlSy5YtNWjQIH3xxRfKz89XSkpKiRcKAICzMfRS7q5du97c2OXm5levXpUkubm5KSIiQmvXri3BEgEAcE52h6jZbFZeXp4kqVatWqpSpYpOnjxpXe/m5sb1UABAhWB3iAYGBurw4cM3N3Zx0QMPPKClS5fq5MmTysrK0ooVKxQQEFDihQIA4GzsDtEBAwYoLS3NejQ6ZcoU/fDDDwoJCVHLli313//+V1OmTCnxQgEAcDYmi8VSWNxOfvzxR23btk2urq4KDQ1Vo0aNSqK2Msu8/OTtGwEoFyxDfBxdgkOlp6dX6LOPhidbkKTs7GxZLBZVqlRJvXr1si7PysqSr69vsYsDAMCZ2R2ieXl5evvtt5WYmHjLG4i4uQgAUN7ZHaLjxo3T2rVr9eSTT6pDhw4ym82lUBYAAM7P7hD9+OOPNXDgQM2dO7cUygEAoOyw++5ck8mkli1blkYtAACUKXaHaM+ePbVr165SKAUAgLLF7hAdN26cjh8/rpdfflkHDx7UL7/8orNnzxb5AQCgvLP7muhDDz0kSTp8+LBWr179h+24OxcAUN7ZHaLjx4+XyWQqjVp+l9ls1sqVKxUeHl7ifUdHR+v8+fP68MMPf/czAAC3YneITpw4sUQLOHPmjGbNmqUdO3bo1KlT8vDwUHBwsIYOHaru3buX6HfdzltvvaXCwmJP4AQAqCCKNWNRcWVmZqpHjx6qUaOGYmNj1bx5cxUUFCg5OVljx47VkSNHSuV7b9y4oUqVKhVZfs8995TK9wEAyie7bywqSa+88ookKSkpSX369FFAQICaNm2qoUOH2rzY+8KFCxo0aJAaNGigli1bFjndOnXqVLVp00b169dXSEiIpkyZYp0gX5Li4uLUoUMHrVmzRq1atVK9evWUk5NTpJ7o6GhFRERYPxcWFiohIUGtWrVS/fr11bFjR071AgCsHBaiFy5c0M6dO/XSSy+pRo0aRdb/diakd955Rz179lRKSor69u2rkSNHKisry7q+evXqeu+997Rv3z7NmjVLmzZt0syZM236y8zM1IYNG7RixQqlpKSoatWqt61xxowZSkxM1MyZM7V3717FxMQoJiZGO3bsML7jAIByw2EhmpGRocLCQjVp0uS2bSMiIhQRESF/f39NnjxZrq6u+vLLL63rx48fr/bt2+u+++5T9+7dNXbsWG3cuNGmj2vXrmnRokVq1aqVgoKC5Op66zPZOTk5mj9/vubNm6fHHntMfn5+GjBggAYOHKglS5YY22kAQLnisGui9tzAExwcbP3d1dVVHh4eNs+ibtmyRQsXLlRGRoZycnKUn5+v/Px8mz4aNGigevXq3fF3/vrO1P79+9vcjXz9+nU1bNjwjvsBUL6lp6c7ugSHK+9jcKtXvTksRBs1aiSTyaRjx47dtm3lypVtPptMJmsIHzhwQJGRkZowYYLefPNN3XPPPdq2bZtef/11m23c3d3tqq+goECStHbt2iKvdbvdUSyAiqMiv0tT4n2iDkuD2rVrKzQ0VIsXL1ZUVFSR66IWi+WO3hCzd+9eeXt7a/z48dZlv71ealTTpk3l5uamrKwsde3atdj9AQDKH4ceUs2cOVNPPPGEunXrpsmTJys4OFiFhYXavXu35syZc0ePuDRu3Fg///yz1q1bp7Zt2+rzzz8vcj3UiJo1a2rUqFF6/fXXVVhYqE6dOik7O1sHDx6Ui4uLBg8eXOzvAACUbQ4NUT8/PyUnJ2vWrFmKjY3Vzz//rDp16qh58+Z3/Kq1sLAwvfzyy5o4caLy8vLUrVs3TZo0SePGjSt2fZMnT5anp6fee+89jRs3TjVr1lRISIhGjx5d7L4BAGWfyWKxMEVPCTMvP+noEgDcJZYhPo4uwaEq+jVRh062AABAWUaIAgBgECEKAIBBhCgAAAYRogAAGESIAgBgECEKAIBBhCgAAAYxk3opqOgPXxtR0R/YLi7GzzjGDsXBkSgAAAYRogAAGESIAgBgECEKAIBBhCgAAAYRogAAGESIAgBgECEKAIBBhCgAAAYRogAAGESIAgBgECEKAIBBhCgAAAYRogAAGESIAgBgECEKAIBBhCgAAAYRogAAGESIAgBgECEKAIBBhCgAAAYRogAAGESIAgBgECEKAIBBhCgAAAYRogAAGESIAgBgECEKAIBBhCgAAAa5OrqA8si8/KSjSyhzDnR2dAUAYD+ORAEAMIgQBQDAIEIUAACDCFEAAAwiRAEAMIgQBQDAIEIUAACDCFEAAAyqECFqNpu1ZcsWR5cBAChnHBaiBQUFCgsLU0REhM3yK1euqE2bNoqJiXFQZQAA3BmHTfvn4uKihQsXqlOnTkpMTNQLL7wgSYqNjVV+fr5mzJjhqNLuyI0bN1SpUiWZTCZHlwKgHLlx44ZycnIcXcYdq1q1qi5evOjoMorN3d1drq72R6JD58718/PTG2+8ocmTJ6tr1646fvy4li1bpk8++UTu7u7q1auXmjVrpvj4eOs2ly5dUtOmTbVo0SI99dRTCgkJ0bPPPqvjx4/r008/lbu7u0aNGqVRo0bZfNeFCxc0aNAgffbZZ/L09NSkSZNsjoJPnTql1157TZ9//rkkqV27doqLi1OjRo0kSXFxcdq6datGjhyp+Ph4nThxQidOnFCNGjXuwkgBqAhu3Lihy5cvy2w2l5n/oLu5ualq1aqOLqNYCgsLZbFYVLNmTbuD1OHXRCMjI9WmTRtFRUVpxIgRGjFihDp06CBJGjRokNavX6+rV69a22/cuFHu7u4KCwuzLluwYIGaNGmi5ORkTZw4UdOnT9fWrVttvuedd95Rz549lZKSor59+2rkyJHKysqSdPMUcq9eveTm5qZPP/1Un332mby8vBQeHq4rV65Y+8jMzNSGDRu0YsUKpaSklPk/HADOJScnp0wFaHlhMplkNpsNnQEwWSyWwlKoyS4//vijWrdurfvvv19fffWV3NzcJElXr15VYGCg4uPj1a9fP0lSaGioOnToYD3dGxISokaNGumjjz6y9jdq1Cilp6dr+/btkm7eWBQTE6PY2FhJN/+35+vrq7lz5yoiIkKJiYmaM2eODh06ZP3jzc/PV+PGjTV79mz16dNHcXFxmjVrlr7//nvVq1fvlvvDW1zsd6Dzlds3Asq5qlWrytPT09FlVFhnz55VXl5ekeUBAQF/uI1TvApt9erVqlatmk6dOqXMzEw1adJE0s3TBBEREVq9erX69eun1NRUHTp0SAsWLLDZ/qGHHiry+eOPP7ZZFhwcbP3d1dVVHh4eOnv2rCTp22+/VWZmpu69916bba5cuaLjx49bPzdo0OC2AQrjbvWHiltLT09n/AxyprG7ePFimTvDlZeXV+Zq/iO1atWSr6+vXds4PES//vprzZ07V2vXrtXSpUsVHR2tf/7zn6pUqZIkaeDAgerUqZOysrK0evVqtW3bVk2bNrX7eypXrmzz2WQyqbDw5kF4QUGBQkJCtGzZsiLb1a5d2/q7u7u73d8LACi/HHpNNC8vT8OGDdOzzz6rxx9/XAkJCcrIyFBCQoK1TWBgoNq0aaOVK1dq3bp1ev7554v0c/DgwSKf7Qnali1bKiMjQ3Xq1JG/v7/Nz29DFADw+6Kjo4s8sugoISEhevfdd+/Kdzn0SHTatGnKy8vT3/72N0mSl5eXZs6cqejoaIWFhSkwMFDSzaPRsWPHqnLlyurTp0+Rfg4ePKjZs2crPDxcKSkp+uCDD7R48eI7rmPAgAF699139eyzz2rSpEm69957dfLkSW3btk2RkZHWO3QBwBHu9n0WliE+d/X7jFqzZo3Gjx+vkycddx+Kw45E9+zZo/fff1/z589XzZo1rcv79eunsLAwRUdH68aNG5Kkvn37qkqVKurdu7dN218NHz5cR48eVZcuXTRjxgxNmjRJ4eHhd1xL9erVtW3bNvn5+Wnw4MFq27atoqOjZbFYZDabi72vAIDyyWEh2qlTJ507d04PP/xwkXUrV67Url27rM/rXLx4Ubm5udYJGf6vGjVqaOnSpTp58qTS09M1ZswYm/UWi6VIqB4+fNjmWdJ69eppwYIF+uGHH3TmzBl99913mj9/vjw8PCRJEydO1FdffVWcXQaACqGwsFAJCQlq1aqV6tevr44dO+rDDz+0rs/MzLROx9q7d295e3urXbt2SkpKsulnx44datOmjby8vBQWFqaNGzfKbDYrMzNTu3fv1ogRI6yPBZnNZsXFxVm3zcvL05gxY+Tr66ugoCDNmzevVPbV4c+J3sr169d1+vRpTZ8+XS1atFD79u0dXRIA4DZmzJihxMREzZw5U3v37lVMTIxiYmK0Y8eOIu2ioqKUkpKi1q1bKzIyUtnZ2ZKkrKwsvfDCC+revbtSUlI0bNgw62OK0v9OiFO9enWlpaUpLS3N5sBowYIFCgoKUnJyskaPHq0pU6Zo//79Jb6vTh2ie/fuVdOmTbV//36bm40AAM4pJydH8+fP17x58/TYY4/Jz89PAwYM0MCBA7VkyRKbtsOHD1dYWJgaNWqkKVOm6MKFCzp8+LAkadmyZfLz89Obb76pgIAAhYeHa8iQIdZtq1Spolq1aslkMsnLy0teXl42M8g9+uijGjp0qPz9/RUVFSV/f38lJyeX+P46/BGXW3n44YdlsVhu2ebXAQcAOF5aWpry8vLUv39/m5mXrl+/roYNG9q0/e3z+97e3pJkfX7/2LFjat26tU37Nm3a3HEdv+1bkurXr2/tuyQ5dYgCAMqWgoICSdLatWuLTFzwf+el/e3z+78G7q/P7xfXreYGKEmEKACgxDRt2lRubm7KyspS165dDffTpEkTbdu2zWbZoUOHbD5XqVJF+fn5hr+jJBCiAIASU7NmTY0aNUqvv/66CgsL1alTJ2VnZ+vgwYNycXHR4MGD76ifIUOGaP78+Xrttdc0aNAgpaamavny5ZL+96i1YcOGysvLU1JSklq0aKFq1aqpevXqpbVrv8upbywCAJQ9kydP1quvvqr33ntP7du3V58+fbR161bdd999d9xHw4YNtWrVKv3jH/9Q586dtXDhQk2YMEGSrHP1tmvXTpGRkXrxxRfVqFEjh9yA6hRvcSlveIuL/Q50vuI0k4CXRc40iXpZ40xjd/HiRd1zzz2OLsMud3MC+oULFyouLk6ZmZml8ro4I+PP6dxSUFamzHIm6enpji4BgJNZvHixHnjgAXl4eOjgwYOKj4/XM88841TvWyVEAQBOKSMjQ7Nnz9b58+fVoEEDRUZGavz48Y4uywYhCgBwSnFxcTZT+TkjbiwCAMAgQhQAAIMIUQAADCJEAcBJuLq6Kicnp1Smp8MfKywsVE5OTpFpCe8ENxYBgJNwd3fX1atXdenSJUeXcscuXbqkWrVqObqMYqtatarc3Nzs3o4QBQAn4ubmZugfc0c5c+ZMkYnmKxJO5wIAYBAhCgCAQYQoAAAGEaIAABjEW1wAADCII1EAAAwiRAEAMIgQBQDAIEIUAACDCFEAAAwiREvAkiVL1KJFC3l5ealr16768ssvHV2SU9qzZ4+efvppBQYGymw2a82aNTbrCwsLFRcXp2bNmql+/fp68sknlZqa6qBqncvs2bPVrVs3+fr6qlGjRoqIiND3339v04bx+2OLFy9Wx44d5evrK19fXz3++OPasWOHdT1jd+dmz54ts9msv/71r9ZlFXn8CNFi2rRpk1599VWNGzdO//rXv9S2bVsNGDBAWVlZji7N6eTk5CgoKEhvvfWWqlWrVmR9QkKC5s+fr7fffltffPGFPD091adPH12+fNkB1TqXlJQUvfjii9qxY4e2bt0qV1dX9e7dWxcuXLC2Yfz+WIMGDTRt2jQlJycrKSlJXbp00XPPPacjR45IYuzu1IEDB7RixQoFBwfbLK/I48dzosUUGhqq4OBgzZs3z7rsgQceUHh4uGJjYx1YmXPz8fHRO++8o+eee07Szf/JNmvWTH/5y1/0yiuvSJJyc3MVEBCgN954Q0OGDHFkuU4nOztbDRs21Jo1axQWFsb4GeDn56fY2FgNHjyYsbsDFy9eVNeuXTVv3jy9/fbbCgoKUnx8fIX/2+NItBiuXbumb775Ro8++qjN8kcffVT79u1zUFVlU2Zmpk6fPm0zltWqVVPHjh0Zy9+RnZ2tgoICmc1mSYyfPfLz87Vx40bl5OSobdu2jN0dGjNmjMLDw9WlSxeb5RV9/HgVWjGcO3dO+fn58vT0tFnu6empM2fOOKiqsun06dOS9Ltj+fPPPzuiJKf26quvKiQkRG3btpXE+N2Jo0ePqnv37srLy5O7u7tWr16t4OBg6z/0jN0fW7lypTIyMvT+++8XWVfR//YIUaCMmTRpkvbu3avt27erUqVKji6nzAgICNDu3bt16dIlbdmyRdHR0frkk08cXZbTS09P1/Tp07V9+3ZVrlzZ0eU4HU7nFoOHh4cqVaqks2fP2iw/e/as6tWr56CqyiYvLy9JYixvY+LEidq4caO2bt0qPz8/63LG7/aqVKkif39/tWrVSrGxsQoJCdGCBQsYu9vYv3+/zp07p/bt28vDw0MeHh7as2ePlixZIg8PD9WpU0dSxR0/QrQYqlSpolatWikpKclmeVJSktq1a+egqsqm++67T15eXjZjmZeXp6+++oqx/P8mTJhgDdAmTZrYrGP87FdQUKBr164xdrfx5JNP6ssvv9Tu3butP61bt1a/fv20e/duNW7cuEKPH6dzi2nEiBGKiorSgw8+qHbt2mnZsmX65Zdfyv0daUZkZ2crIyND0s1/wH766Sd99913ql27tnx9fRUdHa3Zs2crICBAjRs31syZM+Xu7q7+/fs7uHLHe+WVV/Thhx9q9erVMpvN1utQ7u7uqlGjhkwmE+N3C1OnTlX37t3l4+Oj7OxsbdiwQSkpKVq3bh1jdxtms9l6A9uvqlevrtq1aysoKEiSKvT4EaLF1LdvX50/f17x8fE6ffq0AgMDtW7dOjVs2NDRpTmdf//73+rVq5f1c1xcnOLi4vTMM89o4cKFGj16tHJzc/XXv/5VFotFDz74oDZt2qSaNWs6sGrnsGTJEklSeHi4zfIJEyZo4sSJksT43cLp06c1dOhQnTlzRrVq1VJwcLA2bNig0NBQSYxdcVXk8eM5UQAADOKaKAAABhGiAAAYRIgCAGAQIQoAgEGEKAAABhGiAAAYRIgCAGAQIQoAgEGEKAAABv0/53Nv+JZ2ZrUAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "cats.sort_values(by=\"length\").plot(x='name', y='length', kind='barh')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 17) As a reward for getting down here: run the following code, then plot the number of dogs vs. the number of cats\n",
    "\n",
    "> **TIP:** Counting the number of dogs and number of cats does NOT use `.groupby`! That's only for calculations.\n",
    ">\n",
    "> **TIP:** You can set a title with `title=\"Number of animals\"`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "plt.style.use('fivethirtyeight')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 149,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:title={'center':'Number of animals'}>"
      ]
     },
     "execution_count": 149,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAZIAAAEqCAYAAAA/G9biAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAAsTAAALEwEAmpwYAAAcG0lEQVR4nO3de1TUdf7H8ReJKODiaCIFQooiiehW5iVTrDREMSzNLFszT5nmJbLLAW+Z4iquZRfT0lV3dXVJUsvQBQslBAw0u7hqKolr3iUJDNJQ8fdHh/lFkKAfxmHw+Thnz+p3hu+8kW/znO9lBqf8/PxLAgDgKt1g7wEAAI6NkAAAjBASAIARQgIAMEJIAABGCAkAwAghgV2tXLlSFotFs2bNsvco1SolJUVhYWFq3ry5LBaLwsPD7T2SDh06JIvFomeffdbeo5Qxa9YsWSwWpaWl2XsUXCVnew8AcxaLRZLk7e2tL774Qm5ubuXu06tXL33xxRf65ptvdMstt1zjCa8vhw4d0mOPPSYXFxcNHjxYjRs3lp+fn73HAmyGkNQix44d07x58xQVFWXvUa5rqampOnfunKKiojR+/Hh7j2Pl7e2tbdu2ycPDw96joJbh0FYt4eHhoSZNmujtt9/WiRMn7D3Ode348eOSpKZNm9p5krLq1q2r1q1b66abbrL3KKhlCEktUb9+fU2YMEFFRUWaMWNGlb6msmPmzz77rCwWiw4dOlTua8LDw3Xq1CmNGTNGAQEB8vb2VmhoqLZu3SpJKioq0pQpUxQcHKymTZuqc+fO+uijjy47T2ZmpiIiIuTr6ytfX189/PDD+vrrryu8b0lJiZYvX67evXvLz89PXl5euuuuuzR37lwVFxeXu7/FYlG7du1UUFCg6OhoBQcH68Ybb9SCBQsq/Xe6dOmSli9frl69eqlZs2a6+eab1b17d82bN0/nz5+33i8tLa3M+Z4xY8bIYrFU6fh/QUGB3n77bT3wwAMKCgqSp6enWrZsqcGDBysrK6vCryn9nn7/b3377bfrzTff1KVLZT/96I9+3qU/57S0NK1evVo9evTQzTffrFtvvVUTJ07UL7/8IunXPa1+/frJ19dXfn5+euaZZ5SXl1duri1btigyMlKdO3eWr6+vbrrpJnXp0kUzZ87U2bNnK/33LrV161Y9+uijatu2rZo2bapWrVrpnnvu0aRJk8p9b7AvDm3VIsOGDdOiRYv073//W6NGjVJwcLDNHqugoEC9e/dWo0aNNGjQIB07dkzr1q3TwIED9emnnyoyMlKFhYXq27evfvrpJ61Zs0bDhw+Xj4+POnbsWG59O3bs0BtvvKF7771XI0aM0IEDB5SQkKCMjAx99NFH6ty5s/W+Fy5c0F/+8hclJSWpVatWGjhwoOrVq6eMjAxNnz5dqampWrNmjZydy27excXFioiIUEFBge6//365urrKx8en0u911KhRWrVqlby9vTVkyBDVrVtXSUlJmjJlilJSUhQfHy9nZ2f5+fkpKipK6enpysjIUN++fdWuXTtJqvQcyf79+xUTE6OuXbsqNDRUFotFR44cUWJiopKTkxUXF6fQ0NByX3fhwgUNHDhQx48fV69eveTs7KwNGzbo1Vdf1blz5xQdHV3p91dq0aJFSklJUd++fdW1a1clJSVpwYIFKigoUGhoqEaOHKmwsDA98cQTSk1NVXx8vPLy8rR69eoy63nrrbe0f/9+de7cWaGhoTp37pyysrL0t7/9TWlpaUpISCj3s/m95ORkPfLII2rQoIH69OkjHx8f5efn68CBA1q4cKGmTZtW6Tpw7fCTqEWcnZ01ffp0DR48WJMnT650D8DErl279Mwzz2j27NlycnKSJL3++uuKiYlRv3791L17dy1ZskQuLi6SpPvuu08jRozQm2++qZUrV5ZbX3JysubMmaMRI0ZYl61bt07Dhg3T2LFjtW3bNuvjvPHGG0pKStKIESMUGxurOnXqSPp1L2X8+PFatmyZlixZopEjR5Z5jJMnT6pNmzZKTEys8IKEiqxdu1arVq1S27ZtlZiYaD2/MHXqVD388MPavHmz3n33XY0bN0633HKLJkyYoFmzZikjI0Ph4eF6/PHHq/Q4rVu31t69e3XjjTeWWX706FH17NlTkyZNqjAkx48fV3BwsD788EO5urpKkqKiotShQwctWLBAL774ourWrVulGdLS0rRlyxb5+/tLkqKjo3XHHXcoLi5OiYmJSkhIsL4IKC4uVo8ePZScnKydO3eqffv21vW8/vrruuWWW6w/r1IzZszQa6+9Zn3BcTnLli1TSUmJ1q9fX2bdkpSXl0dEahgObdUyvXv31j333KPPPvtMGzdutNnjuLu765VXXinzZDF48GBJUn5+vmbMmGGNiCQNGDBAdevW1X//+98K1+fv76+nnnqqzLL+/furU6dOys7Oth7eKSkp0XvvvSdPT0/NmjXLGhFJuuGGGzRt2jQ5OTlp1apVFT5OTExMlSMiScuXL5f0azh+e5LaxcVFM2fOlPTrk56phg0blouIJPn4+CgiIkLZ2dk6fPhwhV87e/Zsa0QkydPTU3379tWZM2eUnZ1d5RlGjhxpjUjpTH369FFJSYl69+5dZk/SxcVFDz74oKRfX1T8VvPmzctFRPr1UJ8kbd68ucoz/fb7KtW4ceMqfz2uDbJeC8XExKhHjx565ZVX1KtXrzJPttXF399fDRo0KLOs9CRuw4YNy11iXKdOHXl6eurYsWMVru+uu+7SDTeUf11z9913a9u2bdq5c6e6dOmi7777TqdPn1aLFi00Z86cCtfl6uqq/fv3l1tev379Kz7c980330iSunfvXu624OBgeXp66rvvvlNhYWG5f48rlZmZqffee0/bt29Xbm5uuXM9x48fl6+vb5llHh4eZZ78SzVr1kzSr1Gvqt+/8pf+/2da0W0333yzJJX7mRYVFem9997T+vXrdeDAAf30009lzmmUXoxwOYMGDVJCQoJ69uyphx56SN27d1fHjh25dL2GIiS1ULt27TRkyBCtWLFC//jHP/T0009X+2NUdAlp6eGGP7q8tE6dOrpw4UKFt/3RFU6enp6SpDNnzkiS9eTuwYMHNXv27CuauUmTJhW+Ur6cM2fOyMPDo8JXxpLk5eWl3NxcnTlzxigkCQkJGjZsmOrXr6977rlHLVq0kJubm2644QbrOZfSk96/1bBhwwrXV/ri4eLFi1WeoaKfW+l6Lnfbby84OH/+vCIiIrRjxw4FBQXpoYceUpMmTazbxuzZsyv8Pn4vIiJC8fHxmj9/vuLi4qx7fUFBQYqKilL//v2r/H3B9ghJLTV58mR9+OGHio2N1SOPPFLhfUr3AP7oyaagoMBm8/3eqVOnKlyem5sr6f+fyEr/PywsTO+///4VPcaVRqT08X788UedPXu2wpicPHmyzFxXa+bMmXJxcVFKSooCAwPL3Pb8888rIyPDaP3Xyn/+8x/t2LFDQ4YMKXdF3IkTJ64o/qGhoQoNDdXZs2f15ZdfKjk5WYsXL9aTTz6phIQEdevWrbrHx1XiHEktddNNN+m5557TDz/8oLlz51Z4n9J3xB85cqTcbRcuXNDOnTttOWIZmZmZKikpKbe89Am09NBK69at1bBhQ3355ZcVXuZb3f785z9LktLT08vdtmfPHuXm5qpVq1bGh7VycnIUGBhYLiIlJSXKzMw0Wve1lJOTI0l64IEHyt12tTF0dXXV3XffralTpyomJkaXLl3Shg0bjOZE9SIktdi4cePk7e2td999t8I3Kf7pT39SYGCgsrKytHv3buvyS5cuKTY2tsLA2MqBAwe0ZMmSMsvWrVunbdu2KSAgwHr5r7Ozs0aNGqVTp07ppZde0s8//1xuXadPn662CA4dOlSSNH36dBUWFlqXnz9/XpMmTZIkPfHEE8aP4+fnp5ycnDLnDy5duqRZs2Zp7969xuu/Vkovc/59eP/3v/9p6tSpVV5Penp6hYdBS/cAr+SCCdgeh7ZqMTc3N02ePFmjR4/+wyhERkZq9OjR6tOnjx588EG5ubkpKytLR48eVbdu3Sp8JW4LpZe4Jicnq23bttb3kbi6umrevHllDku9/PLL2rNnj5YvX65PPvlEISEh8vHx0Q8//KCDBw8qMzNTTz/9dIUniK/UwIEDlZSUpA8++EBdunRReHi49X0k3333nXr06KHRo0cbP87o0aM1fvx4hYSEKCIiQs7OzsrKytK+ffsUFhampKQk48e4FsLCwuTv76/58+drz549at++vY4cOaKNGzcqNDS0yi9OoqOjdfToUXXp0kV+fn6qX7++du/erU2bNqlx48YaNmyYjb8TXAn2SGq5Rx999LJPqKXHsps1a6b3339f8fHxatmypTZv3lzuCiFbuvPOO/Xxxx/r559/1qJFi7Rp0ybde++9SkxMVJcuXcrc19nZWcuXL9fixYvVpk0bffrpp3rnnXf0ySef6Ny5c3rhhRfKvB/F1MKFC/XGG2+oadOm+te//qXFixerXr16mj59uj744INqeU/D8OHDNX/+fHl5eSkuLk4ffPCBfHx8lJycbD285gjc3d318ccfa9CgQdq7d68WLlyo3bt36+WXX9aiRYuqvJ4XX3xRPXv21P79+7Vy5UotWbJE33//vZ599llt2bKFD8GsYZzy8/P5rAEAwFVjjwQAYISQAACMEBIAgBFCAgAwQkgAAEYICQDACCEBABghJLXElfzeCcCRsa3XPIQEAGCEkAAAjBASAIARQgIAMHLFIZk7d64sFotefvllW8wDAHAwVxSS7du365///Kfatm1rq3kAAA6myiEpKCjQiBEj9M4771h/RSsAAFUOyfPPP6/+/fsrJCTElvMAABxMlX6127Jly5STk3NFv+HMEd801DHdkX8PtJuUftTeQ1yV7d3K/9514HIc8fnFkQUEBFz29kpDkp2drenTpyspKUl169attgeukRz0idjROeS2ArvJzs5mm6lhKg3Jtm3bdPr06TK/N/vixYvaunWrli5dqmPHjqlevXo2HRIAUHNVGpLw8HDdfvvtZZaNGTNGLVu21AsvvCAXFxebDQcAqPkqDYnFYil3lZabm5saNWqkoKAgW80FAHAQvLMdAGCkSldt/d6GDRuqew4AgINijwQAYISQAACMEBIAgBFCAgAwQkgAAEYICQDACCEBABghJAAAI4QEAGCEkAAAjBASAIARQgIAMEJIAABGCAkAwAghAQAYISQAACOEBABghJAAAIwQEgCAEUICADBCSAAARggJAMAIIQEAGCEkAAAjhAQAYISQAACMEBIAgBFCAgAwQkgAAEYICQDACCEBABghJAAAI4QEAGCEkAAAjBASAIARQgIAMEJIAABGCAkAwAghAQAYISQAACOEBABghJAAAIwQEgCAEUICADBSaUj+/ve/q2vXrvL19ZWvr6/uv/9+bdy48VrMBgBwAJWGxNvbW9OmTVNqaqpSUlIUEhKixx9/XLt27boW8wEAajjnyu4QHh5e5u9TpkzRkiVLtH37dgUHB9tsMACAY6g0JL918eJFffTRRyoqKlKnTp1sNRMAwIFUKSS7d+9WaGiozp07J3d3d61YsUJt27a97NdkZ2dXy4DXlpu9B7guOea24tg6pjvytu4mpR+19xBXZXu3n+09wlUJCAi47O1O+fn5lypbSXFxsY4cOaIzZ85o3bp1WrZsmdavX6+goKBqG7QmsPzDMTdOR5c/3MfeI1x32Nbto7Zu61XaI3FxcZG/v78k6bbbbtOXX36pBQsW6J133rHpcACAmu+q3kdSUlKi4uLi6p4FAOCAKt0jefXVVxUaGiofHx8VFhZq9erVSk9PV3x8/LWYDwBQw1UakpMnT+qZZ57RqVOn5OHhobZt22r16tXq2bPntZgPAFDDVRqSd99991rMAQBwUHzWFgDACCEBABghJAAAI4QEAGCEkAAAjBASAIARQgIAMEJIAABGCAkAwAgh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LCzksK4dERIHNGTIEHuPAFwzUVFRioyM1JYtW3THHXdIkr766itt3rxZb731liTps88+0913323PMa9rHNpyQMXFxXrttde0Zs0aHTlyROfPny9zO1dtobbZtm2bFi1apP3790uSWrdurZEjR6pjx452ngwSeyQO6a9//avWrl2rF154QRMnTtT06dP1/fffa+3atZo0aZK9xwOqXadOndSpUyd7j4E/wB6JA2rfvr3mzp2rXr16qVmzZkpLS1OLFi20ZMkSpaamavny5fYeEahWv/zyi+Lj47Vv3z45OTnp1ltv1cMPP1zuTbmwDz5G3gHl5uYqMDBQkuTu7q6CggJJUs+ePct9uCbg6Pbu3asOHTpo0qRJ2rFjh7744gtNmDBBHTp00L59++w9HkRIHFKzZs104sQJSZK/v782bdokSdq+fTtXcqHWiY6OVrt27bRr1y4lJiYqMTFRu3btUnBwsCZMmGDv8SDOkTikfv36KTU1VR07dtSoUaP01FNPadmyZTp+/Liee+45e48HVKusrCxt3ry5zOW9Hh4emjJlCm/ArSEIiQOaOnWq9c/9+/eXj4+PMjMz1apVK4WFhdlxMqD61atXz3r49rfOnDnDOZIagkNbDigmJkZLly61/v3OO+/U2LFjdezYMc2YMcOOkwHVLywsTJGRkcrMzNTFixd18eJFff755xo/frz69Olj7/EgQuKQVq1apfbt25dbftttt+n999+3w0SA7cTGxsrf3199+vSRl5eXvLy81LdvX7Vs2VIzZ86093gQh7YcUm5urpo0aVJueePGjZWbm2uHiQDbsVgsiouLU05OjvUqrcDAwHKfvQX7ISQOqFmzZtq6dauaN29eZnlGRoa8vb3tMxRQjcaMGXPZ29evX2/98/z58209DipBSBzQk08+qYkTJ+r8+fMKCQmRJKWmpmratGl6/vnn7TscUA1++OGHMn///PPP5eTkpKCgIEnSt99+q5KSEuuvVoB9ERIHNG7cOOXl5SkqKkrFxcWSfv0Y+VGjRikyMtLO0wHmVq1aZf3z3Llz5erqqvnz51t/dUJRUZHGjRtnDQvsi49IcWBFRUXWY8atW7dWgwYN7DwRUP0CAwO1bt063XrrrWWWf/vtt+rfv7/1gxxhP+yRODB3d3frx2oDtVVRUZFOnDhRLiQnT57U2bNn7TQVfovLfwHUaA888IDGjBmjNWvW6NChQzp06JDWrFmjsWPHql+/fvYeD+LQFoAa7uzZs5o8ebJWrFhh/d07zs7OGjp0qGJiYuTm5mbnCUFIADiEoqIiHTx4UJLUokUL64l32B8hAQAY4RwJAMAIIQEAGCEkAAAjhAQAYISQAACM/B+KotS5yxml5wAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.animal.value_counts().plot(kind=\"bar\", title=\"Number of animals\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
