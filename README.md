# backend_exercise
IRobot_django_exercise

Backed for https://github.com/danilobassi8/backend-interview-exercise

backendPets is a backend in Django to use with Pets-app frontend application:

You can:
 - Create new Users. 
 - Create new pets.
 - list all pets created by users.
 - Delete pets (only if you are admin).


## available endpoints

<table>
<tr>
<td> Endpoint </td> <td> HTTP Verb </td> <td> Params / Body </td> <td> Expected response example </td>
</tr>
<tr>
<td> Pets </td>
<td> POST </td>
<td>
body:

```javascript
{
    name: (string)
    birth_date: (string - yyyy-mm-dd format)
    is_birth_approximate: (boolean)

}
```
</td>
<td>

```javascript
{
   birth_date: '2020-06-20',
   id: 25,
   is_birth_approximate: false,
   name: ’Puppy’,
}

```
 </td>
</tr>

<tr>
<td> pets </td>
<td> GET </td>
<td>
body:

```javascript
page: (number)
name: (string)
max_birth_date: (string - yyyy-mm-dd format)

```
</td>
<td>

```javascript
{
   count: 23,
   next: 'http://localhost:8000/api/pets/?page=3',
   previous: ’next: 'http://localhost:8000/api/pets/?page=1',
   results: [
      { id: 1, name: 'perro 1', age: '6 years', is_birth_approximate: false },
      { id: 2, name: 'perro 2', age: '4 months', is_birth_approximate: true },
      { id: 3, name: 'perro 3', age: '3 years and 1 month', is_birth_approximate: false },
      ]
}

```
 </td>
</tr>

</tr>
<tr>
<td> pets/:id </td>
<td> DELETE </td>
<td></td>
<td> status 200 if deleted </td>
</tr>

<tr>
<td> users/login </td>
<td> POST </td>
<td>
body:

```javascript
{
   email: (string)
   password: (string)
}
```

</td>
<td>

```javascript
{
   user: {
      email: 'guest@guest.com',
      first_name: 'guest',
      is_admin: false,
      last_name: 'guest_lastname',
      username: 'guest',
   },
}
```
</td>
</tr>

<tr>
<td> users/signin </td>
<td> POST </td>
<td>
body:

```javascript
{
   username: (string) 
   email: (string)
   password: (string)
}
```

</td>
<td>

```javascript
{
   user: {
      email: 'guest@guest.com',
      first_name: 'guest',
      is_admin: false,
      last_name: 'guest_lastname',
      username: 'guest',
   },
}
```
</td>
</tr>
</table>


## Requirements
 * Ubuntu Linux 18.04 or higher version.
 * Python 3
 * virtualenv


## Run app locally:

```sh
 $ git clone https://github.com/DanielAbt/backendPets.git
 $ python3 -m venv backendPets
 $ cd backendPets/
 $ source bin/activate
 $ pip3 install -r backendpets/requirements.txt
 $ python3 backendpets/manage.py makemigrations
 $ python3 backendpets/manage.py migrate
 $ python3 backendpets/manage.py runserver 0:8000
 ```

 ### you can populate DB whit test data

 ```sh
 $ python3 backendpets/manage.py initdata
 ```

