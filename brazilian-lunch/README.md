# Brazilian lunch application

This is a simple Brazilian lunch application written in Python. The application simulate restaurant, but the only sales feijoada, that is a typical Brazilian lunch. The application doesn't have a database, so the data is stored in memory and is cleaned when the app stop to run.

## Base for price calculation

The price is calculated using the following formula:

```python
price = (volume * option) + accompaniment
```

## Menu options

The application has the following menu options:

1. Chose the volume of feijoada

   | Volume (ml) | value (R$)     |
   | ----------- | -------------- |
   | < 300       | not acceptable |
   | 300 <= 5000 | volume \* 0.8  |
   | > 5000      | not acceptable |

1. Chose the option

   | Option      | Multiplier |
   | ----------- | ---------- |
   | 1 (basic)   | 1.00       |
   | 2 (premium) | 1.25       |
   | 3 (supreme) | 1.50       |

1. Chose the accompaniment

   | Accompaniment                             | value (R$) |
   | ----------------------------------------- | ---------- |
   | 0 (finish the order and stop application) | 0.00       |
   | 1 (200g of rice)                          | 5.00       |
   | 2 (150g of special farofa)                | 6.00       |
   | 3 (100g of boiled cabbage)                | 7.00       |
   | 4 (1 peeled orange)                       | 3.00       |
