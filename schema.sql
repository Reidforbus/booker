-- Clean up old tables
DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS service_items;
DROP TABLE IF EXISTS open_hours;
DROP TABLE IF EXISTS booking_info;
DROP TABLE IF EXISTS users;

-- Create tables
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username TEXT,
    pwd TEXT,
    name TEXT,
    admin BOOLEAN DEFAULT FALSE,
    active BOOLEAN DEFAULT TRUE
);

CREATE TABLE service_items (
    service_id SERIAL PRIMARY KEY,
    name TEXT,
    description TEXT,
    dur INT, --TODO: change to time interval later
    price NUMERIC,
    active BOOLEAN DEFAULT TRUE
);

CREATE TABLE open_hours (
    open INT, -- TODO: change to time later
    close INT, -- TODO: change to time later
    day INT --TODO: change to date later
);

CREATE TABLE booking_info (
    booking_id SERIAL PRIMARY KEY,
    msg TEXT,
    user_id INT NOT NULL,
    active BOOLEAN DEFAULT TRUE,

    CONSTRAINT fk_user
    FOREIGN KEY(user_id)
    REFERENCES users(user_id)
);

CREATE TABLE bookings (
    booking_id INT,
    service_id INT,
    time INT, --TODO: change to time later
    day INT, --TODO: change to date later

    CONSTRAINT fk_booking
    FOREIGN KEY(booking_id)
    REFERENCES booking_info(booking_id),

    CONSTRAINT fk_service
    FOREIGN KEY(service_id)
    REFERENCES service_items(service_id)
);
