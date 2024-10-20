## Appointment booking tool

This repo holds my student project for the University of Helsinki course Tietokannat ja web-ohjelmointi

I have created an appointment scheduling program where a business can provide services for their customers to book appointments for.
The owner/admin is able to:
- Create and manage different services with a custom description and duration
- WIP Set time windows within which services can be booked
- WIP Manage active bookings

A user/client is able to:
- Browse available services
- Book services and add messages to bookings
- WIP Review and edit their bookings

My plan is to implement this application as a bike shop service scheduler

### Testing the project

#### Starting the project

To test this project you need to have Python3 and Postgresql installed.

1. Clone the repo to your machine.
    ```bash
    git clone https://github.com/Reidforbus/booker.git
    ```
2. ```cd``` into the project folder
3. Create a python virtual environment
    ```bash
    python3 -m venv venv
    ```
4. Open the virtual environment.
    ```bash
    source venv/bin/activate
    ```
5. Install the required libraries using pip.
    ```bash
    pip install -r requirements.txt
    ```
6. Create ```.env``` file with ```SECRET_KEY``` and ```DATABASE_URL``` as per course instructions
7. Run ```start-pg.sh``` and in another terminal build database using ```psql < schema.sql``` 
    - You can also add sample services with ```psql < testdata.sql```
8. Run the flask server with ```flask run```

Now you can access the site at ```localhost:5000```

#### Testing the site

Currently (15.10.24) on the site you can try:
- Registering an account
- Logging in
- As a user:
    - Browse available services
    - Make bookings at available times
- As an admin:
    - Add new services
    - Edit existing services
    - View users
    - View bookings
