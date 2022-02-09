# BreakFastApi 🍣 🍔 🍕

![Breakfastapi](images/BreakFastAPI.png)

**The most delicious API on the web.** Just send a request and you'll receive the most mouth watering dish recipe with estimated cooking time and all the necessary ingredients and instructions.

### **Problem:**

Humans are only capable of remembering a limited number of food recipes.

### **Solution:**

Break Fast Api solves this problem by memorizing more than 12.000 recipes and making them available at will.
The delicious meals are now only one GET request away from you.

---

### **Check it out!** 
[![BreakFastApi](https://img.shields.io/badge/BreakFastApi-0077B5?style=for-the-badge&logo=fastapi&logoColor=white)](https://breakfastapi.fun/)


### **How does it work?**

---

**Sample request:**


```python
import requests
r = requests.get(url='https://breakfastapi.fun/')
data = r.json()
```

**Sample response:**


```python
{
    'ID': 11574,
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
    'Directions': '''In a saucepan over high heat, 
                   blend raspberry jam, brown sugar, 
                   Worcestershire sauce, tomato sauce, 
                   malt vinegar, hot pepper sauce, salt, 
                   and pepper. Bring to a boil over high heat, 
                   reduce heat to low, and simmer 10 minutes,
                   or until thickened.'''
}
```

### Bon Appétit! │ Hyvää Ruokahalua! 😋


