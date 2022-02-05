# breakfastapi 🍣 🍔 🍕

---

The most delicious API.

### **Problem:**
Humans are only capable of remembering a limited number of food recipes.

### **Solution:**
Break Fast Api solves this problem by memorizing more than 12.000 recipes and making them available at will.
The delicious meals are now only one GET request away from you.
---
### **Installation:**
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Sample request:**
```
import requests
r = requests.get(url='InsertApiUrl')
data = r.json()
```

**Sample response:**
```
{
    'ID':11574,
    'Recipe Name': 'Devils Steak Sauce Recipe',
    'Cook Time (minutes)': 15,
    'Ingredients': ['brown sugar',
                    'tomato sauce',
                    'raspberry',
                    'worcestershire sauce',
                    'hot pepper',
                    'black pepper',
                    'vinegar'
                    ],
    'Directions': 'In a saucepan over high heat, 
                   blend raspberry jam, brown sugar, 
                   Worcestershire sauce, tomato sauce, 
                   malt vinegar, hot pepper sauce, salt, 
                   and pepper. Bring to a boil over high heat, 
                   reduce heat to low, and simmer 10 minutes,
                   or until thickened.'
}
```
### Bon Appétit! │ Hyvää Ruokahalua!