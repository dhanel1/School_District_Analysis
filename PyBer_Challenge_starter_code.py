{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Pyber Challenge"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4.3 Loading and Reading CSV files"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Add Matplotlib inline magic command\n",
    "%matplotlib inline\n",
    "# Dependencies and Setup\n",
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd\n",
    "\n",
    "# File to Load (Remember to change these)\n",
    "city_data_to_load = \"Resources/city_data.csv\"\n",
    "ride_data_to_load = \"Resources/ride_data.csv\"\n",
    "\n",
    "# Read the City and Ride Data\n",
    "city_data_df = pd.read_csv(city_data_to_load)\n",
    "ride_data_df = pd.read_csv(ride_data_to_load)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Merge the DataFrames"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "scrolled": true
   },
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
       "      <th>city</th>\n",
       "      <th>date</th>\n",
       "      <th>fare</th>\n",
       "      <th>ride_id</th>\n",
       "      <th>driver_count</th>\n",
       "      <th>type</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Lake Jonathanshire</td>\n",
       "      <td>2019-01-14 10:14:22</td>\n",
       "      <td>13.83</td>\n",
       "      <td>5739410935873</td>\n",
       "      <td>5</td>\n",
       "      <td>Urban</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>South Michelleport</td>\n",
       "      <td>2019-03-04 18:24:09</td>\n",
       "      <td>30.24</td>\n",
       "      <td>2343912425577</td>\n",
       "      <td>72</td>\n",
       "      <td>Urban</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Port Samanthamouth</td>\n",
       "      <td>2019-02-24 04:29:00</td>\n",
       "      <td>33.44</td>\n",
       "      <td>2005065760003</td>\n",
       "      <td>57</td>\n",
       "      <td>Urban</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Rodneyfort</td>\n",
       "      <td>2019-02-10 23:22:03</td>\n",
       "      <td>23.44</td>\n",
       "      <td>5149245426178</td>\n",
       "      <td>34</td>\n",
       "      <td>Urban</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>South Jack</td>\n",
       "      <td>2019-03-06 04:28:35</td>\n",
       "      <td>34.58</td>\n",
       "      <td>3908451377344</td>\n",
       "      <td>46</td>\n",
       "      <td>Urban</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 city                 date   fare        ride_id  \\\n",
       "0  Lake Jonathanshire  2019-01-14 10:14:22  13.83  5739410935873   \n",
       "1  South Michelleport  2019-03-04 18:24:09  30.24  2343912425577   \n",
       "2  Port Samanthamouth  2019-02-24 04:29:00  33.44  2005065760003   \n",
       "3          Rodneyfort  2019-02-10 23:22:03  23.44  5149245426178   \n",
       "4          South Jack  2019-03-06 04:28:35  34.58  3908451377344   \n",
       "\n",
       "   driver_count   type  \n",
       "0             5  Urban  \n",
       "1            72  Urban  \n",
       "2            57  Urban  \n",
       "3            34  Urban  \n",
       "4            46  Urban  "
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Combine the data into a single dataset\n",
    "pyber_data_df = pd.merge(ride_data_df, city_data_df, how=\"left\", on=[\"city\", \"city\"])\n",
    "\n",
    "# Display the data table for preview\n",
    "pyber_data_df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Deliverable 1: Get a Summary DataFrame "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "#  1. Get the total rides for each city type\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2. Get the total drivers for each city type\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "#  3. Get the total amount of fares for each city type\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "#  4. Get the average fare per ride for each city type. \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 5. Get the average fare per driver for each city type. \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "#  6. Create a PyBer summary DataFrame. \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "#  7. Cleaning up the DataFrame. Delete the index name\n",
    "pyber_summary_df.index.name = None"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "#  8. Format the columns.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Deliverable 2.  Create a multiple line plot that shows the total weekly of the fares for each type of city."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. Read the merged DataFrame\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2. Using groupby() to create a new DataFrame showing the sum of the fares \n",
    "#  for each date where the indices are the city type and date.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 3. Reset the index on the DataFrame you created in #1. This is needed to use the 'pivot()' function.\n",
    "# df = df.reset_index()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 4. Create a pivot table with the 'date' as the index, the columns ='type', and values='fare' \n",
    "# to get the total fares for each type of city by the date. \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 5. Create a new DataFrame from the pivot table DataFrame using loc on the given dates, '2019-01-01':'2019-04-29'.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 6. Set the \"date\" index to datetime datatype. This is necessary to use the resample() method in Step 8.\n",
    "# df.index = pd.to_datetime(df.index)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 7. Check that the datatype for the index is datetime using df.info()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 8. Create a new DataFrame using the \"resample()\" function by week 'W' and get the sum of the fares for each week.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 8. Using the object-oriented interface method, plot the resample DataFrame using the df.plot() function. \n",
    "\n",
    "# Import the style from Matplotlib.\n",
    "from matplotlib import style\n",
    "# Use the graph style fivethirtyeight.\n",
    "style.use('fivethirtyeight')\n",
    "\n"
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
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
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
   "version": "3.6.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
