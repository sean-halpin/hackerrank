# MongoDB

Mongo is a document store. It is flexible and schema-less(polymorphic).
Fewer restrictions on data shape. 

Easier to maintain. 

Easy to scale via horizontal scaling. Distribute load across multiple servers. 

## Replication Set

- A replica set in MongoDB is a group of mongod instances that maintain the same data set, providing redundancy and high availability. 
  - It consists of a primary node, which receives all write operations, 
   - and multiple secondary nodes, which replicate the primary's data. 
  - If the primary node fails, an automatic election process selects a new primary from the secondaries, 
   - ensuring continuous availability of the database.

## Sharded Clusters

- Sharded clusters in MongoDB are used for horizontal scaling, allowing data to be distributed across multiple servers.
- Each shard in a sharded cluster is a separate MongoDB replica set, consisting of primary and secondary nodes.
- The data in a sharded cluster is divided into chunks, which are distributed across the shards based on a shard key.
  - The shard key determines how the data is partitioned and distributed among the shards.
- Sharded clusters provide high availability and fault tolerance, as data is replicated across multiple shards.
  - Queries in a sharded cluster are automatically routed to the appropriate shard based on the shard key.
  - Sharded clusters can handle large amounts of data and high write and read workloads.
- Managing a sharded cluster involves configuring and monitoring the shards, as well as managing the shard key and chunk distribution.
  - Sharded clusters can be scaled by adding more shards to distribute the data and workload further.
- MongoDB provides tools and features to manage and optimize sharded clusters, such as the balancer for redistributing chunks and the explain command for query optimization.

## MQL - Mongo Query Language

MQL is an imperitive language, used for simple queries across single collections. 

For complex queries across collections we use Mongo's Aggregation Pipeline. 
- Breaks operations into stages


## findOne & find

From mongosh;

```bash
show dbs
use sample
show collections
db.companies.findOne()
db.companies.find({"name": "Wetpaint"})
# Regex Filter, all companies with name starting with T
db.companies.find({"name": {"$regex": "^T", "$options": "i"}})
```

## $ in MQL

Dollar is used before operators, e.g. $lt, is equivalent of <

```bash
{ "founded_year": { "$gte": 2006 } }
```

## Operators

Here are some examples of MQL operators:

- **Comparison Operators:**
    - `$eq`: Matches values that are equal to a specified value.
        - Example: `db.companies.find({"founded_year": {"$eq": 2006}})`
    - `$ne`: Matches values that are not equal to a specified value.
        - Example: `db.companies.find({"founded_year": {"$ne": 2006}})`
    - `$gt`: Matches values that are greater than a specified value.
        - Example: `db.companies.find({"founded_year": {"$gt": 2006}})`
    - `$lt`: Matches values that are less than a specified value.
        - Example: `db.companies.find({"founded_year": {"$lt": 2006}})`
    - `$gte`: Matches values that are greater than or equal to a specified value.
        - Example: `db.companies.find({"founded_year": {"$gte": 2006}})`
    - `$lte`: Matches values that are less than or equal to a specified value.
        - Example: `db.companies.find({"founded_year": {"$lte": 2006}})`

- **Logical Operators:**
    - `$and`: Joins query clauses with a logical AND.
        - Example: `db.companies.find({"$and": [{"founded_year": {"$gte": 2006}}, {"category_code": "Technology"}]})`
    - `$or`: Joins query clauses with a logical OR.
        - Example: `db.companies.find({"$or": [{"founded_year": {"$gte": 2006}}, {"category_code": "Technology"}]})`
    - `$not`: Inverts the effect of a query expression.
        - Example: `db.companies.find({"founded_year": {"$not": {"$eq": 2006}}})`

- **Element Operators:**
    - `$exists`: Matches documents that have the specified field.
        - Example: `db.companies.find({"founded_year": {"$exists": true}})`
    - `$type`: Matches documents that have the specified field of a specific type.
        - Example: `db.companies.find({"founded_year": {"$type": "number"}})`

- **Array Operators:**
    - `$in`: Matches any of the values specified in an array.
        - Example: `db.companies.find({"category_code": {"$in": ["Technology", "Finance"]}})`
    - `$nin`: Matches none of the values specified in an array.
        - Example: `db.companies.find({"category_code": {"$nin": ["Technology", "Finance"]}})`
    - `$all`: Matches arrays that contain all elements specified in an array.
        - Example: `db.companies.find({"category_code": {"$all": ["Technology", "Finance"]}})`

- **Evaluation Operators:**
    - `$regex`: Matches documents that satisfy a specified regular expression.
        - Example: `db.companies.find({"name": {"$regex": "^T", "$options": "i"}})`
    - `$mod`: Performs a modulo operation on the value of a field and selects documents with a specified result.
        - Example: `db.companies.find({"founded_year": {"$mod": [2, 0]}})`

- **Array Update Operators:**
    - `$push`: Adds an element to an array field.
        - Example: `db.companies.updateOne({"name": "Wetpaint"}, {"$push": {"tags": "technology"}})`
    - `$pull`: Removes all array elements that match a specified query.
        - Example: `db.companies.updateOne({"name": "Wetpaint"}, {"$pull": {"tags": "technology"}})`

- **Other Operators:**
    - `$text`: Performs text search on the specified field(s).
        - Example: `db.companies.find({ "$text": { "$search": "technology" } })`
    - `$where`: Matches documents that satisfy a JavaScript expression.
        - Example: `db.companies.find({ "$where": "this.founded_year < 2006" })`

Please note that these are just a few examples of MQL operators. MongoDB provides a wide range of operators to perform various operations on your data.

## $expr Operator

The `$expr` operator allows you to use aggregation expressions within the query language. It enables you to perform complex comparisons and logical operations on fields in your documents.

Here's an example of using the `$expr` operator:
```bash
db.companies.find({
    $expr: {
        $and: [
            { $gt: ["$founded_year", "$last_funding_year"] },
            { $lte: ["$employee_count", 100] }
        ]
    }
})
```

In this example, the query retrieves documents where the `founded_year` field is greater than the `last_funding_year` field. The `$expr` operator allows you to compare the values of different fields within the same document.

You can use various aggregation expressions like `$gt`, `$lt`, `$eq`, etc., within the `$expr` operator to perform complex queries.

## Cursor Methods

MongoDB provides several cursor methods that allow you to iterate over query results and perform various operations on the returned documents. Here are some concise examples of cursor methods in the Mongo Query Language (MQL):

- `forEach`: Executes a JavaScript function for each document in the cursor.
    ```bash
    db.companies.find().forEach(function(doc) {
            print(doc.name);
    });
    ```

- `limit`: Limits the number of documents returned by the query.
    ```bash
    db.companies.find().limit(10);
    ```

- `sort`: Sorts the documents in the cursor based on a specified field.
    ```bash
    db.companies.find().sort({ name: 1 });
    ```

- `skip`: Skips a specified number of documents in the cursor.
    ```bash
    db.companies.find().skip(5);
    ```

- `count`: Returns the number of documents in the cursor.
    ```bash
    db.companies.find().count();
    ```

- `toArray`: Converts the cursor to an array of documents.
    ```bash
    db.companies.find().toArray();
    ```

These cursor methods provide flexibility and control over the query results, allowing you to manipulate and process the returned documents according to your needs.

## Projection in MongoDB

Projection in MongoDB allows you to specify which fields to include or exclude in the query results. It helps you retrieve only the necessary data, reducing network traffic and improving query performance.

### Including Fields

To include specific fields in the query results, you can use the projection parameter with a value of 1 for each field you want to include. For example:

```bash
db.companies.find({}, { name: 1, category_code: 1 })
```

In this example, the query will return only the `name` and `category_code` fields for each document in the `companies` collection.

### Excluding Fields

To exclude specific fields from the query results, you can use the projection parameter with a value of 0 for each field you want to exclude. For example:

```bash
db.companies.find({}, { _id: 0, employee_count: 0 })
```

In this example, the query will return all fields except for the `_id` and `employee_count` fields for each document in the `companies` collection.

### Nested Fields

You can also project nested fields by using dot notation. For example:

```bash
db.companies.find({}, { "address.city": 1, "address.zip": 1 })
```

In this example, the query will return only the `city` and `zip` fields from the `address` subdocument for each document in the `companies` collection.

### Combination of Inclusion and Exclusion

You can combine inclusion and exclusion in the projection parameter to fine-tune the query results. For example:

```bash
db.companies.find({}, { name: 1, "address.city": 1, _id: 0 })
```

In this example, the query will return only the `name` and `city` fields, excluding the `_id` field for each document in the `companies` collection.

Projection in MongoDB provides flexibility in retrieving specific fields from documents, allowing you to optimize your queries and improve performance.

## Querying Arrays in MongoDB

MongoDB provides powerful querying capabilities for arrays. You can perform various operations to query and manipulate array fields in your documents.

Here are some key points to consider when querying arrays in MongoDB:

- **Equality Match**: You can use the `$elemMatch` operator to match documents that contain an array element that matches all specified conditions. For example:
    ```bash
    db.companies.find({ tags: { $elemMatch: { $eq: "technology" } } })
    ```
    This query will return documents where the `tags` array contains the element "technology".

- **Array Operators**: MongoDB provides several array operators to query and manipulate array fields. Some commonly used array operators include:
    - `$size`: Matches documents where the array field has a specific size.
    - `$all`: Matches documents where the array field contains all specified elements.
    - `$elemMatch`: Matches documents where at least one array element matches all specified conditions.
    - `$in`: Matches documents where the array field contains any of the specified values.
    - `$nin`: Matches documents where the array field does not contain any of the specified values.

- **Array Indexing**: MongoDB supports indexing on array fields, which can improve query performance. You can create indexes on array fields to speed up queries that involve array operations.

- **Array Projection**: You can use projection to control which array elements are included in the query results. For example, you can use the `$slice` operator to limit the number of array elements returned. Additionally, you can use the `$elemMatch` operator in projection to return only the first matching array element.

- **Array Aggregation**: If you need to perform complex operations on array fields, you can use the aggregation framework in MongoDB. The aggregation pipeline provides a set of stages that allow you to transform and manipulate array fields in your documents.

These are just some of the key points to consider when querying arrays in MongoDB. MongoDB's flexible querying capabilities and array operators provide powerful tools for working with array fields in your documents.

## Mongo Insert

To insert documents into a MongoDB collection, you can use the `insertOne()` or `insertMany()` methods.

- `insertOne()`: Inserts a single document into the collection.
    - Example: `db.collection.insertOne({ name: "John", age: 30 })`

- `insertMany()`: Inserts multiple documents into the collection.
    - Example: `db.collection.insertMany([{ name: "John", age: 30 }, { name: "Jane", age: 25 }])`

When inserting documents, MongoDB automatically generates a unique `_id` field for each document if one is not provided.

You can also specify the `_id` field manually if you want to control the document's unique identifier.

Inserting documents in MongoDB is a simple and straightforward process, allowing you to add data to your collections efficiently.

## deleteOne
The `deleteOne` method in MongoDB is used to delete a single document that matches the specified filter criteria. It removes the first document that satisfies the filter from the collection.

Syntax:
```bash
db.collection.deleteOne(filter)
```

- `filter`: Specifies the criteria to select the document to be deleted.

Example:
```bash
db.companies.deleteOne({ name: "Wetpaint" })
```

In this example, the `deleteOne` method deletes the first document in the `companies` collection that has the name "Wetpaint".

## deleteMany
The `deleteMany` method in MongoDB is used to delete multiple documents that match the specified filter criteria. It removes all documents that satisfy the filter from the collection.

Syntax:
```bash
db.collection.deleteMany(filter)
```

- `filter`: Specifies the criteria to select the documents to be deleted.

Example:
```bash
db.companies.deleteMany({ category_code: "technology" })
```

In this example, the `deleteMany` method deletes all documents in the `companies` collection that have the category code "technology".

Both `deleteOne` and `deleteMany` methods provide a convenient way to remove documents from a MongoDB collection based on specific criteria. They are useful for managing data and maintaining the integrity of your database.

## `updateOne` in MongoDB
The `updateOne` method in MongoDB is used to update a single document that matches the specified filter criteria. It modifies the first document that satisfies the filter in the collection.
Syntax:
```bash
db.collection.updateOne(filter, update, options)
```
- `filter`: Specifies the criteria to select the document to be updated.
- `update`: Specifies the modifications to be made to the selected document.
- `options`: Specifies additional options for the update operation (optional).
Example:
```bash
db.companies.updateOne({ name: "Wetpaint" }, { $set: { category_code: "technology" } })
```
In this example, the `updateOne` method updates the first document in the `companies` collection that has the name "Wetpaint" by setting its `category_code` field to "technology".

## `updateMany` in MongoDB
The `updateMany` method in MongoDB is used to update multiple documents that match the specified filter criteria. It modifies all documents that satisfy the filter in the collection.
Syntax:
```bash
db.collection.updateMany(filter, update, options)
```
- `filter`: Specifies the criteria to select the documents to be updated.
- `update`: Specifies the modifications to be made to the selected documents.
- `options`: Specifies additional options for the update operation (optional).
Example:
```bash
db.companies.updateMany({ category_code: "technology" }, { $set: { industry: "IT" } })
```
In this example, the `updateMany` method updates all documents in the `companies` collection that have the category code "technology" by setting their `industry` field to "IT".

Both `updateOne` and `updateMany` methods provide a convenient way to modify documents in a MongoDB collection based on specific criteria. They are useful for updating data and maintaining the accuracy of your database.


## Update Operators in MongoDB

MongoDB provides various update operators that allow you to modify specific fields in your documents. These operators provide flexibility and control over the update process. Here are some key update operators in MongoDB:

- `$set`: Sets the value of a field in the document. It can create a new field if it doesn't exist.

- `$unset`: Removes a field from the document.

- `$inc`: Increments the value of a numeric field by a specified amount.

- `$mul`: Multiplies the value of a numeric field by a specified amount.

- `$rename`: Renames a field in the document.

- `$min`: Updates the value of a field if the specified value is lower than the current value.

- `$max`: Updates the value of a field if the specified value is higher than the current value.

- `$currentDate`: Sets the value of a field to the current date or time.

These update operators can be used in conjunction with the `updateOne()` and `updateMany()` methods to modify documents in a MongoDB collection. They provide powerful tools for updating data and maintaining the integrity of your database.

## Upsert in MongoDB

Upsert is a combination of "update" and "insert" operations in MongoDB. It allows you to update a document if it exists, or insert a new document if it doesn't exist.

Syntax:
```bash
db.collection.updateOne(filter, update, { upsert: true })
```

- `filter`: Specifies the criteria to select the document to be updated.
- `update`: Specifies the modifications to be made to the selected document.
- `{ upsert: true }`: Enables the upsert operation.

Example:
```bash
db.companies.updateOne({ name: "Wetpaint" }, { $set: { category_code: "technology" } }, { upsert: true })
```

In this example, the `updateOne` method updates the document in the `companies` collection that has the name "Wetpaint" by setting its `category_code` field to "technology". If the document doesn't exist, it will be inserted as a new document.

Upsert operation is useful when you want to update a document if it exists, or insert a new document if it doesn't exist. It provides flexibility and convenience in managing your data in MongoDB.
