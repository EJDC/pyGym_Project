DROP TABLE IF EXISTS customers CASCADE;
DROP TABLE IF EXISTS sessions CASCADE;
DROP TABLE IF EXISTS staff CASCADE;
DROP TABLE IF EXISTS rooms CASCADE;
DROP TABLE IF EXISTS bookings CASCADE;
DROP TABLE IF EXISTS session_types CASCADE;
DROP TABLE IF EXISTS room_session_types CASCADE;
DROP TABLE IF EXISTS staff_session_types CASCADE;

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    dob DATE,
    email VARCHAR(255),
    membership_level VARCHAR(255),
    membership_status VARCHAR(255),
    payment_method VARCHAR(255),
    extra_physio BOOLEAN,
    extra_pt BOOLEAN,
    extra_service_3 BOOLEAN,
    extra_service_4 BOOLEAN,
    missed_classes INT,
    monthly_bill FLOAT
);

CREATE TABLE session_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE rooms (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE staff (
    id SERIAL PRIMARY KEY,
    first_name NAME,
    last_name NAME,
    email VARCHAR(255),
    monthly_invoice FLOAT
);

CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date_and_time TIMESTAMP,
    duration INT,
    min_age INT,
    max_age INT,
    p_member_price FLOAT,
    s_member_price FLOAT,
    max_capacity INT,
    instructor_payment FLOAT,
    session_type INT NOT NULL REFERENCES session_types(id),
    instructor_id INT REFERENCES staff(id),
    room INT REFERENCES rooms(id)
);


CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    customer_id SERIAL NOT NULL REFERENCES customers(id),
    session_id SERIAL NOT NULL REFERENCES sessions(id)
);

CREATE TABLE room_session_types (
    id SERIAL PRIMARY KEY,
    room_id SERIAL NOT NULL REFERENCES rooms(id),
    session_type_id SERIAL NOT NULL REFERENCES session_types(id)
);

CREATE TABLE staff_session_types (
    id SERIAL PRIMARY KEY,
    staff_id SERIAL NOT NULL REFERENCES staff(id),
    session_type_id SERIAL NOT NULL REFERENCES session_types(id)
);