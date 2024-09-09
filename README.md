# kloudkitchenman
KloudKitchenMan is a cloud kitchen management software backend implemented with django and django rest framework. This application provides apis to interact with various online food deliver functionalities.

#### The Architecture
I had plan a ERD for the full application which is now kind of partially obsolute.
![APP ERD](/resources/kloudkitchen.png "ERD")
> Note: This is modified on the go while developing the apis. This will be updated shortly.

As you can see I have used dbdiagram.io to version control the diagram. You can find the code in the `/resources/erd.sql`.

Please refer the `Functionalities` section to have a clear understanding on the working application.

#### Functionalities


#### Prerequisites for Building and Running the Application
* Make sure docker is installed
* Patience to build the software

Actually I made the docker configuration use caching so the later requirement is not necessary but good to have.

#### Prerequisites for Building and Running the Application
* Clone the repository
* Change Directory to `kloudkitchenman`
* Run `docker compose up` or `docker compose up --build`

> Note: You may need `sudo` if you have installed docker under root user. I have developed this in my windows machine.

#### Checking the Functionalities
I would highly encourage you to use the Browsable API with a request interceptor browser extension as the `Bruno` APIs in `kkm_bruno` are not fully implemented.

A snapshot showing how to use network interceptor:
![interceptor](/resources/interceptor.png)

Again, the Bruno (alike Postman) APIs will be updated shortly.

Visit browsable apis like here:
![browsable_apis](/resources/browsable_apis.png)

#### Techstack Utilized
* Django
* Djangorestframework
* Python 3.10
> No third-party django/drf plugins not used

#### Contributions
Contributions are allowed and welcomed with a harm heart.
Feel free to create issues.


