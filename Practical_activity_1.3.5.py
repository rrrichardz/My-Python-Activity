{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "082cbbab",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Time = 14:42:05.000566\n",
      "Hour = 14\n",
      "Minute = 42\n",
      "Second = 5\n",
      "Microsecond = 566\n"
     ]
    }
   ],
   "source": [
    "# 1\n",
    "from datetime import time\n",
    "\n",
    "t = time(14, 42, 5, 566)\n",
    "print(\"Time =\", t)\n",
    "print(\"Hour =\", t.hour)\n",
    "print(\"Minute =\", t.minute)\n",
    "print(\"Second =\", t.second)\n",
    "print(\"Microsecond =\", t.microsecond)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "73f6536c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Date and time = 2019-01-28 23:55:59.001023\n",
      "Year = 2019\n",
      "Month = 1\n",
      "Day = 28\n",
      "Hour = 23\n",
      "Minute = 55\n",
      "Second = 59\n",
      "Microsecond = 1023\n"
     ]
    }
   ],
   "source": [
    "# 2\n",
    "from datetime import datetime\n",
    "\n",
    "dt = datetime(2019, 1, 28, 23, 55, 59, 1023)\n",
    "print(\"Date and time =\", dt)\n",
    "print(\"Year =\", dt.year)\n",
    "print(\"Month =\", dt.month)\n",
    "print(\"Day =\", dt.day)\n",
    "print(\"Hour =\", dt.hour)\n",
    "print(\"Minute =\", dt.minute)\n",
    "print(\"Second =\", dt.second)\n",
    "print(\"Microsecond =\", dt.microsecond)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "7bdaa6c7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Today's date = 2022-03-28\n",
      "Current year = 2022\n",
      "Current month = 3\n",
      "Current day = 28\n"
     ]
    }
   ],
   "source": [
    "# 3\n",
    "from datetime import date\n",
    "\n",
    "today = date.today()\n",
    "\n",
    "print(\"Today's date =\", today)\n",
    "print(\"Current year =\", today.year)\n",
    "print(\"Current month =\", today.month)\n",
    "print(\"Current day =\", today.day)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "7aa91818",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Saturday'"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 4\n",
    "from datetime import datetime\n",
    "\n",
    "day = datetime(2017, 1, 28)\n",
    "day.strftime('%A')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "dbbd0161",
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
       "      <th>Date</th>\n",
       "      <th>Week_Day</th>\n",
       "      <th>Day_name</th>\n",
       "      <th>Month_name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2008-01-01</td>\n",
       "      <td>1</td>\n",
       "      <td>Tuesday</td>\n",
       "      <td>January</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2008-01-02</td>\n",
       "      <td>2</td>\n",
       "      <td>Wednesday</td>\n",
       "      <td>January</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2008-01-03</td>\n",
       "      <td>3</td>\n",
       "      <td>Thursday</td>\n",
       "      <td>January</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2008-01-04</td>\n",
       "      <td>4</td>\n",
       "      <td>Friday</td>\n",
       "      <td>January</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2008-01-05</td>\n",
       "      <td>5</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>January</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>56</th>\n",
       "      <td>2008-02-26</td>\n",
       "      <td>1</td>\n",
       "      <td>Tuesday</td>\n",
       "      <td>February</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>57</th>\n",
       "      <td>2008-02-27</td>\n",
       "      <td>2</td>\n",
       "      <td>Wednesday</td>\n",
       "      <td>February</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58</th>\n",
       "      <td>2008-02-28</td>\n",
       "      <td>3</td>\n",
       "      <td>Thursday</td>\n",
       "      <td>February</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>59</th>\n",
       "      <td>2008-02-29</td>\n",
       "      <td>4</td>\n",
       "      <td>Friday</td>\n",
       "      <td>February</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>60</th>\n",
       "      <td>2008-03-01</td>\n",
       "      <td>5</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>March</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>61 rows × 4 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date  Week_Day   Day_name Month_name\n",
       "0  2008-01-01         1    Tuesday    January\n",
       "1  2008-01-02         2  Wednesday    January\n",
       "2  2008-01-03         3   Thursday    January\n",
       "3  2008-01-04         4     Friday    January\n",
       "4  2008-01-05         5   Saturday    January\n",
       "..        ...       ...        ...        ...\n",
       "56 2008-02-26         1    Tuesday   February\n",
       "57 2008-02-27         2  Wednesday   February\n",
       "58 2008-02-28         3   Thursday   February\n",
       "59 2008-02-29         4     Friday   February\n",
       "60 2008-03-01         5   Saturday      March\n",
       "\n",
       "[61 rows x 4 columns]"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 5\n",
    "import pandas as pd\n",
    "\n",
    "dr = pd.date_range(start='2008-01-01', end='2008-03-01')\n",
    "df = pd.DataFrame()\n",
    "df['Date'] = dr\n",
    "df['Week_Day'] = pd.to_datetime(dr).weekday\n",
    "df['Day_name'] = pd.to_datetime(dr).strftime(\"%A\")\n",
    "df['Month_name'] = pd.to_datetime(dr).strftime(\"%B\")\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9b242b8c",
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
