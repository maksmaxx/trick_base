# Trick Base - https://trickbase.herokuapp.com

<!-- ABOUT THE PROJECT -->
### About The Project

The Trick Base is a simple web app providing access to the database with various sports discipline's tricks and tutorials to them.  

### App endpoints
* Get all disciplines
```sh
GET: https://trickbase.herokuapp.com/api/disciplines
```
* Get discipline identified by name
```sh
GET: https://trickbase.herokuapp.com/api/disciplines/<name>
```
* Get all tricks
```sh
https://trickbase.herokuapp.com/api/tricks
```
 * Get all tricks belonging to discipline identified by name
```sh
{
 discipline: <name>
}
```
```sh
POST: https://trickbase.herokuapp.com/api/tricks
```
* Get trick identified by uuid
```sh
GET: https://trickbase.herokuapp.com/api/tricks/<uuid>
```


<!-- GETTING STARTED -->
### Repository
#### db_manager
Contains GUI admin app(Python/Tkinter) allowing to change DB records.
#### front_end
Contains front end application written in React displaying the main page.
#### server_app
Contains full server application deployed to heroku.com. Handles REST API, rendering React and accessing MongoDB.
<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE` for more information.

