# kloudkitchenman
KloudKitchenMan is a cloud kitchen management software backend implemented with django and django rest framework. This application provides apis to interact with various online food deliver functionalities.

#### The Architecture
I had plan a ERD for the full application which is now kind of partially obsolute.
![APP ERD](/resources/kloudkitchen.png "ERD")
> Note: This is modified on the go while developing the apis. This will be updated shortly.

As you can see I have used dbdiagram.io to version control the diagram. You can find the code in the `/resources/erd.sql`.

Please refer the `Functionalities` section to have a clear understanding on the working application.

#### Functionalities
We have 4 different types of `Users` and they are `SuperUser`(automatically created), Owner, Employee, Customer. We have permissions defined in the `stakeholders/permissions.py` file. I have extended the user creation rule a bit. How? With apis, The `Owner` can be created only by the `SuperUser`. And `Employee` can be only created by the `Owner`. Again, no one can create `Customer` but an `Anonymous` user which is strictly saying a non-signedup entity. Please have patience and skim through the codebase to have a better understanding as of now. I will be updating this very soon to give you more insight.

#### Prerequisites for Building and Running the Application
* Make sure docker is installed
* Patience to build the software

Actually I made the docker configuration use caching so the later requirement is not necessary but good to have.

#### Prerequisites for Building and Running the Application
* Clone the repository
* Change Directory to `kloudkitchenman`
* Do `cp .env.example .env` or just copy rename the `.env.example` to `.env`
* Run `docker compose up` or `docker compose up --build`

With this it should be up and running.

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


