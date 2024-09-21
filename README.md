### Appointment booking tool

This repo holds my student project for the University of Helsinki course Tietokannat ja web-ohjelmointi

My plan is to create a appointment scheduling program where a business can provide services for their customers to book appointments for.
The owner/admin is able to:
- WIP Create different services with custom description and duration
- WIP Set time windows within which services can be booked
- WIP Manage active bookings

A user/client is able to:
- WIP Browse available services
- WIP Book services and add messages to bookings
- WIP Review and edit their bookings

My plan is to implement this application as a bike shop service scheduler

## Testing the project

To test this project you need to have at least Python3 and Postgresql installed.
1. Clone the repo to your machine.
    ```bash
    git clone https://github.com/Reidforbus/booker.git
    ```
2. Create a pyhton virtual environment in the project folder.
    ```bash
    python3 -m venv venv
    ```
3. Open the virtual environment.
    ```bash
    source venv/bin/activate
    ```
4. Install the required libraries using pip.
    ´´´bash
    pip install -r requirements.txt
    ´´´
5. Create ``` .env``` file as per course instructions
6. Run ```start-pg.sh``` and build database using ```psql < schema.sql``` 

