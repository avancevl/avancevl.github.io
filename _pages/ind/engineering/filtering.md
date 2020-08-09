---
layout: default
title: Indexing, Filtering, and Querying
lang: ind
description: How we build indexing, filtering, and querying.
---



## Cloud Firestore

```javascript

// Create a reference to the cities collection
var citiesRef = db.collection("cities");

// Create a query against the collection.
var query = citiesRef.where("state", "==", "CA");

// Returns all the capital cities:
var query = citiesRef.where("capital", "==", true);
```

### Online Resources

* [Querying and filtering data](https://cloud.google.com/firestore/docs/query-data/queries){:target="_blank"}
* [Perform simple and compound queries in Cloud Firestore](https://firebase.google.com/docs/firestore/query-data/queries){:target="_blank"}
* [Query limitations](https://firebase.google.com/docs/firestore/query-data/queries#query_limitations){:target="_blank"}
* [SO: Can I filter Multiple Fields in a Firestore search?](https://stackoverflow.com/questions/52277456/can-i-filter-multiple-fields-in-a-firestore-search){:target="_blank"}
* [Order and limit data with Cloud Firestore](https://firebase.google.com/docs/firestore/query-data/order-limit-data){:target="_blank"}
* [Paginate data with query custors](https://firebase.google.com/docs/firestore/query-data/query-cursors){:target="_blank"}