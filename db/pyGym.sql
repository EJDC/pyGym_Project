DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS sessions;
DROP TABLE IF EXISTS staff;
DROP TABLE IF EXISTS rooms;
DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS session_types;
DROP TABLE IF EXISTS rooms_types
DROP TABLE IF EXISTS staff_session_types

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
    monthly_bill FLOAT,
);

CREATE TABLE session_types (
    id SERIAL PRIMARY KEY
    name VARCHAR(255)
);

CREATE TABLE rooms (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    name NAME,
    date_and_time DATETIME,
    duration INT,
    min_age INT,
    max_age INT,
    p_member_price FLOAT,
    s_member_price FLOAT,
    max_capacity INT,
    instructor_id INT NOT NULL REFERENCES staff(id),
    instructor_payment FLOAT,
    room INT NOT NULL REFERENCES rooms(id)
    session_type INT NOT NULL REFERENCES session_types(id)
);

CREATE TABLE staff (
    id SERIAL PRIMARY KEY,
    first_name NAME,
    last_name NAME,
    email VARCHAR(255),
    monthly_invoice FLOAT
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
)