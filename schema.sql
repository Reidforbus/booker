-- Clean up old tables
DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS service_items;
DROP TABLE IF EXISTS open_hours;
DROP TABLE IF EXISTS booking_info;
DROP TABLE IF EXISTS users;

-- Create tables
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    pwd TEXT,
    name TEXT,
    admin BOOLEAN DEFAULT FALSE,
    active BOOLEAN DEFAULT TRUE
);

CREATE TABLE service_items (
    service_id SERIAL PRIMARY KEY,
    name TEXT,
    description TEXT,
    dur INTERVAL,
    price NUMERIC,
    active BOOLEAN DEFAULT TRUE
);

CREATE TABLE open_hours (
    open TIME NOT NULL,
    close TIME NOT NULL,
    day DATE NOT NULL UNIQUE
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
    time TIME NOT NULL,
    day DATE NOT NULL,

    CONSTRAINT fk_booking
    FOREIGN KEY(booking_id)
    REFERENCES booking_info(booking_id),

    CONSTRAINT fk_service
    FOREIGN KEY(service_id)
    REFERENCES service_items(service_id)
);
