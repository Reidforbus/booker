-- sample services
INSERT INTO service_items (name, description, dur, price) VALUES ('Tire change', 'Includes the changing of one tire and/or inner tube. Tubeless install for +10€', '20 minutes', 15);
INSERT INTO service_items (name, description, dur, price) VALUES ('First time service', 'Includes gear adjustment, wheel truing and brake adjustment. Wash for +10€', '60 minutes', 60);
INSERT INTO service_items (name, description, dur, price) VALUES ('Sample service 2', 'Description of service', '60 minutes', 100);
INSERT INTO service_items (name, description, dur, price) VALUES ('Sample service 3', 'Description of service', '40 minutes', 50);
INSERT INTO service_items (name, description, dur, price) VALUES ('Sample service 4', 'Description of service', '2 hours', 200);
INSERT INTO service_items (name, description, dur, price) VALUES ('Sample service 4', 'Description of service', '1 hour', 100);

--sample user
INSERT INTO users (user_id, name, username) VALUES (100, 'John Doe', 'testuserdonotuse');
-- sample bookings
INSERT INTO booking_info (user_id, msg) VALUES (100, 'Sample booking 1');
INSERT INTO bookings (booking_id, service_id, time, day) VALUES (1, 1, '12:00', '2024-09-30');
INSERT INTO bookings (booking_id, service_id, time, day) VALUES (1, 2, '13:00', '2024-09-30');
INSERT INTO bookings (booking_id, service_id, time, day) VALUES (1, 3, '15:00', '2024-09-30');
