{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "third-techno",
   "metadata": {},
   "outputs": [],
   "source": [
    "original_price = 198.87\n",
    "current_price = 254.32"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "intermediate-arrest",
   "metadata": {},
   "outputs": [],
   "source": [
    "Increase = current_price - original_price\n",
    "Percent_Increase = (Increase / original_price)*100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "fifteen-validation",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original Price = $198.87\n",
      "Current Price =  $254.32\n",
      "Percentage Increase = 27.88%\n"
     ]
    }
   ],
   "source": [
    "print(f'Original Price = ${original_price}')\n",
    "print(f'Current Price =  ${current_price}')\n",
    "print('Percentage Increase =', \"{:.2f}%\".format(Percent_Increase))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "green-explorer",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
