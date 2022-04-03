{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d3b0f643",
   "metadata": {},
   "source": [
    "### 1. Import Pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "f19fddbd",
   "metadata": {},
   "outputs": [],
   "source": [
    "#import necessary packages\n",
    "import pandas as pd\n",
    "\n",
    "pd.options.mode.chained_assignment = None"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5baf6c09",
   "metadata": {},
   "source": [
    "### 2. Import data sets"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7bf409f0",
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
       "      <th>Title</th>\n",
       "      <th>Year</th>\n",
       "      <th>Age</th>\n",
       "      <th>IMDb</th>\n",
       "      <th>Rotten Tomatoes</th>\n",
       "      <th>Directors</th>\n",
       "      <th>Genres</th>\n",
       "      <th>Country</th>\n",
       "      <th>Language</th>\n",
       "      <th>Runtime</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Inception</td>\n",
       "      <td>2010</td>\n",
       "      <td>13+</td>\n",
       "      <td>8.8</td>\n",
       "      <td>0.87</td>\n",
       "      <td>Christopher Nolan</td>\n",
       "      <td>Action,Adventure,Sci-Fi,Thriller</td>\n",
       "      <td>United States,United Kingdom</td>\n",
       "      <td>English,Japanese,French</td>\n",
       "      <td>148.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>The Matrix</td>\n",
       "      <td>1999</td>\n",
       "      <td>18+</td>\n",
       "      <td>8.7</td>\n",
       "      <td>0.87</td>\n",
       "      <td>Lana Wachowski,Lilly Wachowski</td>\n",
       "      <td>Action,Sci-Fi</td>\n",
       "      <td>United States</td>\n",
       "      <td>English</td>\n",
       "      <td>136.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Avengers: Infinity War</td>\n",
       "      <td>2018</td>\n",
       "      <td>13+</td>\n",
       "      <td>8.5</td>\n",
       "      <td>0.84</td>\n",
       "      <td>Anthony Russo,Joe Russo</td>\n",
       "      <td>Action,Adventure,Sci-Fi</td>\n",
       "      <td>United States</td>\n",
       "      <td>English</td>\n",
       "      <td>149.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Back to the Future</td>\n",
       "      <td>1985</td>\n",
       "      <td>7+</td>\n",
       "      <td>8.5</td>\n",
       "      <td>0.96</td>\n",
       "      <td>Robert Zemeckis</td>\n",
       "      <td>Adventure,Comedy,Sci-Fi</td>\n",
       "      <td>United States</td>\n",
       "      <td>English</td>\n",
       "      <td>116.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>The Good, the Bad and the Ugly</td>\n",
       "      <td>1966</td>\n",
       "      <td>18+</td>\n",
       "      <td>8.8</td>\n",
       "      <td>0.97</td>\n",
       "      <td>Sergio Leone</td>\n",
       "      <td>Western</td>\n",
       "      <td>Italy,Spain,West Germany</td>\n",
       "      <td>Italian</td>\n",
       "      <td>161.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                            Title  Year  Age  IMDb  Rotten Tomatoes  \\\n",
       "0                       Inception  2010  13+   8.8             0.87   \n",
       "1                      The Matrix  1999  18+   8.7             0.87   \n",
       "2          Avengers: Infinity War  2018  13+   8.5             0.84   \n",
       "3              Back to the Future  1985   7+   8.5             0.96   \n",
       "4  The Good, the Bad and the Ugly  1966  18+   8.8             0.97   \n",
       "\n",
       "                        Directors                            Genres  \\\n",
       "0               Christopher Nolan  Action,Adventure,Sci-Fi,Thriller   \n",
       "1  Lana Wachowski,Lilly Wachowski                     Action,Sci-Fi   \n",
       "2         Anthony Russo,Joe Russo           Action,Adventure,Sci-Fi   \n",
       "3                 Robert Zemeckis           Adventure,Comedy,Sci-Fi   \n",
       "4                    Sergio Leone                           Western   \n",
       "\n",
       "                        Country                 Language  Runtime  \n",
       "0  United States,United Kingdom  English,Japanese,French    148.0  \n",
       "1                 United States                  English    136.0  \n",
       "2                 United States                  English    149.0  \n",
       "3                 United States                  English    116.0  \n",
       "4      Italy,Spain,West Germany                  Italian    161.0  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# import the movies data set\n",
    "movies = pd.read_excel('movies.xlsx')\n",
    "\n",
    "movies.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3b089426",
   "metadata": {},
   "source": [
    "### 3. Calculate sum of missing data in Age column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6c40f124",
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
       "      <th>ID</th>\n",
       "      <th>Netflix</th>\n",
       "      <th>Hulu</th>\n",
       "      <th>Prime Video</th>\n",
       "      <th>Disney+</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   ID  Netflix  Hulu  Prime Video  Disney+\n",
       "0   1        0     0            1        0\n",
       "1   2        0     1            0        0\n",
       "2   3        0     0            1        0\n",
       "3   4        1     0            0        0\n",
       "4   5        0     0            1        0"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# import the ott data set\n",
    "ott = pd.read_csv('ott.csv')\n",
    "\n",
    "ott.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "b68d0ecf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# sum of missing values\n",
    "movies['Age'].isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "16121602",
   "metadata": {},
   "source": [
    "### 4. Assign a specific value to missing data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "52319d38",
   "metadata": {},
   "outputs": [],
   "source": [
    "# replace the missing values in Age column with set value\n",
    "movies['Age'][movies['Age'].isna()] = \"Others\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "39539448",
   "metadata": {},
   "outputs": [],
   "source": [
    "# replace the missing values in the directors, genres, country and language with others\n",
    "movies['Directors'][movies['Directors'].isna()] = \"Others\"\n",
    "\n",
    "movies['Genres'][movies['Genres'].isna()] = \"Others\"\n",
    "\n",
    "movies['Country'][movies['Country'].isna()] = \"Others\"\n",
    "\n",
    "movies['Language'][movies['Language'].isna()] = \"Others\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2fadd110",
   "metadata": {},
   "source": [
    "### Advanced problem "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "78823eec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Title               object\n",
      "Year                 int64\n",
      "Age                 object\n",
      "IMDb               float64\n",
      "Rotten Tomatoes     object\n",
      "Directors           object\n",
      "Genres              object\n",
      "Country             object\n",
      "Language            object\n",
      "Runtime            float64\n",
      "dtype: object\n"
     ]
    }
   ],
   "source": [
    "# there are two options to convert an object to integer\n",
    "# 1) Pandas Series\n",
    "# determine the data type first\n",
    "print(movies.dtypes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "2709bdbe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Title               object\n",
      "Year                 int64\n",
      "Age                 object\n",
      "IMDb               float64\n",
      "Rotten Tomatoes    float64\n",
      "Directors           object\n",
      "Genres              object\n",
      "Country             object\n",
      "Language            object\n",
      "Runtime            float64\n",
      "dtype: object\n"
     ]
    }
   ],
   "source": [
    "# change Rotten Tomatoes from object to integer\n",
    "movies['Rotten Tomatoes'] = movies['Rotten Tomatoes'].astype(float)\n",
    "print(movies.dtypes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "ffad7dfa",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'float' object is not subscriptable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_28136/3590498923.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mnumpy\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mnp\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m \u001b[0mmovies\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'Rotten Tomatoes'\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mmovies\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'Rotten Tomatoes'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mapply\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;32mlambda\u001b[0m \u001b[0mx\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mif\u001b[0m \u001b[0mx\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mnan\u001b[0m \u001b[1;32melse\u001b[0m \u001b[0mx\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      6\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmovies\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdtypes\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\core\\series.py\u001b[0m in \u001b[0;36mapply\u001b[1;34m(self, func, convert_dtype, args, **kwargs)\u001b[0m\n\u001b[0;32m   4355\u001b[0m         \u001b[0mdtype\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mfloat64\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   4356\u001b[0m         \"\"\"\n\u001b[1;32m-> 4357\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mSeriesApply\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfunc\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mconvert_dtype\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mapply\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   4358\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   4359\u001b[0m     def _reduce(\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\core\\apply.py\u001b[0m in \u001b[0;36mapply\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m   1041\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mapply_str\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1042\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1043\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mapply_standard\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1044\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1045\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0magg\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\core\\apply.py\u001b[0m in \u001b[0;36mapply_standard\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m   1096\u001b[0m                 \u001b[1;31m# List[Union[Callable[..., Any], str]]]]]\"; expected\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1097\u001b[0m                 \u001b[1;31m# \"Callable[[Any], Any]\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1098\u001b[1;33m                 mapped = lib.map_infer(\n\u001b[0m\u001b[0;32m   1099\u001b[0m                     \u001b[0mvalues\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1100\u001b[0m                     \u001b[0mf\u001b[0m\u001b[1;33m,\u001b[0m  \u001b[1;31m# type: ignore[arg-type]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\_libs\\lib.pyx\u001b[0m in \u001b[0;36mpandas._libs.lib.map_infer\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_28136/3590498923.py\u001b[0m in \u001b[0;36m<lambda>\u001b[1;34m(x)\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mnumpy\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mnp\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m \u001b[0mmovies\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'Rotten Tomatoes'\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mmovies\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'Rotten Tomatoes'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mapply\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;32mlambda\u001b[0m \u001b[0mx\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mif\u001b[0m \u001b[0mx\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mnan\u001b[0m \u001b[1;32melse\u001b[0m \u001b[0mx\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      6\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmovies\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdtypes\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: 'float' object is not subscriptable"
     ]
    }
   ],
   "source": [
    "# 2) lambda function (you will learn more about lambda functions in week 3)\n",
    "# import numpy for the lambda function to work\n",
    "import numpy as np\n",
    "\n",
    "movies['Rotten Tomatoes'] = movies['Rotten Tomatoes'].apply(lambda x: int(x[:-1]) if x is not np.nan else x)\n",
    "print(movies.dtypes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "f3f8cc59",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "571\n",
      "11586\n"
     ]
    }
   ],
   "source": [
    "# missing values for IMDb and Rotten Tomatoes\n",
    "print(movies['IMDb'].isnull().sum())\n",
    "\n",
    "print(movies['Rotten Tomatoes'].isnull().sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "2d285b60",
   "metadata": {},
   "outputs": [],
   "source": [
    "# replace missing values with mean\n",
    "movies['IMDb'].fillna(movies['IMDb'].mean(), inplace = True)\n",
    "\n",
    "movies['Rotten Tomatoes'].fillna(movies['Rotten Tomatoes'].mean(), inplace = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "92dc9a4a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "0\n"
     ]
    }
   ],
   "source": [
    "# missing values for IMDb and Rotten Tomatoes\n",
    "print(movies['IMDb'].isnull().sum())\n",
    "\n",
    "print(movies['Rotten Tomatoes'].isnull().sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2c693006",
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
