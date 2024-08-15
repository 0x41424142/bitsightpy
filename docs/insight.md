# Insights Module

The insights module of ```bitsightpy``` gives details on rating changes for companies.

To get started, import the module and load your API key:

```py
from bitsightpy import insights

key = '<API_KEY>'
```

>**Head's Up!:** Some Bitsight API parameters contain a period in their name. Due to Python rules, these periods have been changed to underscores when a user defines them in a call. The underlying base API call function handles the conversion back to a period. For example, ```risk_vector.slug``` is defined by the user as ```risk_vector_slug```.

### Get Insights API

```get_insights``` lets you get a list of all insights in your subscription, filtering by kwargs.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```company``` | ```str``` as a company guid | ✅ |
| ```start``` | ```str``` in ```YYYY-MM-DD``` format | ❌ |
| ```end``` | ```str``` in ```YYYY-MM-DD``` format | ❌ |
| ```score_delta_lt``` | ```str/int``` | ❌ |


### Get Change Explanations API

```get_change_explanations``` gives the reasonings behind a company's score change.

>**Head's Up!:** Bitsight notes that usually, only negative changes have an event/explanation

 Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```company``` | ```str``` as a company guid | ✅ |
| ```limit``` | ```int``` = 100 | ❌ |
| ```date_gte``` | ```str``` in ```YYYY-MM-DD``` format | ❌ |
| ```date_lt``` | ```str``` in ```YYYY-MM-DD``` format | ❌ |
| ```score_delta_gte``` | ```int``` | ❌ |
| ```score_delta_lt``` | ```int``` | ❌ |
