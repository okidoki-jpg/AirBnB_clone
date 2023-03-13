# [0x00. AirBnB clone - The console](https://github.com/okidoki-jpg/AirBnB_clone)

This is a command interpreter for managing objects for an AirBnB clone. The interpreter allows the user to create, update, and delete objects of different types such as State, City, Amenity, Place, and Review. The data is stored in a file-based storage system.

## Starting the Console
To start the console, simply run the file `console.py` in your terminal or command prompt:

`$ python3 console.py` or `$ ./console.py`

## Using the Console
Once the console is started, you will see the prompt `(hbnb)` indicating that the console is ready to accept commands. You can use the following commands:

- `quit`: Exits the console.
- `help`: Displays a list of available commands.
- `create`: Creates a new object of the specified class. For example, `create BaseModel`.
- `show`: Shows an object of the specified class and id. For example, `show BaseModel 1234-1234-1234`.
- `destroy`: Deletes an object of the specified class and id. For example, `destroy BaseModel 1234-1234-1234`.
- `all`: Shows all objects based or not on the specified class. For example, `all BaseModel`.
- `update`: Updates an object of the specified class and id by adding or updating an attribute. For example, `update BaseModel 1234-1234-1234 attribute_name "attribute_value"`.

## Examples
Creating an object:

```
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
```


## Showing an object:

```
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at':
datetime.datetime(2022, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2022, 10, 2, 3, 10, 25, 903300)}
```


## Updating an object:

```
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 attribute_name "attribute_value"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at':
datetime.datetime(2022, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2022, 10, 2, 3, 11, 3, 49401),
'attribute_name': 'attribute_value'}
```
