-- sample services
INSERT INTO service_items (name, description, dur, price) VALUES ('Tire change', 'Includes the changing of one tire and/or inner tube. Tubeless install for +10€', '20 minutes', 15);
INSERT INTO service_items (name, description, dur, price) VALUES ('First time service', 'Includes gear adjustment, wheel truing and brake adjustment. Wash for +10€', '60 minutes', 60);
INSERT INTO service_items (name, description, dur, price) VALUES ('Brake bleed', 'Includes the bleeding of one (1) hydraulic disc brake', '20 minutes', 25);
INSERT INTO service_items (name, description, dur, price) VALUES ('Wheel truing', 'Tightening, truing and dishing of a single spoked wheel', '40 minutes', 60);
INSERT INTO service_items (name, description, dur, price) VALUES ('Seasonal service', 'This is what youll want if you ride a lot. Also known as the works', '2 hours', 200);
INSERT INTO service_items (name, description, dur, price) VALUES ('Bike fit', 'Get your measurements before or next bike purchase or get your current setup dialed', '1 hour', 100);

--sample user
INSERT INTO users (user_id, name, username) VALUES (100, 'John Doe', 'testuserdonotuse');
-- sample bookings
INSERT INTO booking_info (user_id, msg) VALUES (100, 'Sample booking 1');
INSERT INTO bookings (booking_id, service_id, time, day) VALUES (1, 1, '12:00', 'tomorrow');
INSERT INTO bookings (booking_id, service_id, time, day) VALUES (1, 2, '13:00', 'tomorrow');
INSERT INTO bookings (booking_id, service_id, time, day) VALUES (1, 3, '15:00', 'tomorrow');
--sample hours
INSERT INTO open_hours (open, close, day) VALUES ('10:00','18:00', 'tomorrow')
