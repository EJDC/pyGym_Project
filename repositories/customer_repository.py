from db.run_sql import run_sql
from models.customer import Customer

def save(customer):
    sql = "INSERT INTO customers (name) VALUES (%s) RETURNING id"
    values = [customer.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    customer.id = id


def select_all():
    customers = []
    sql = "SELECT * FROM customers"
    results = run_sql(sql)
    for result in results:
        customer = Customer(result["name"], result["id"])
        customers.append(customer)
    return customers


def select(id):
    customer = None 
    sql = "SELECT * FROM customers WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        customer = customer(result["name"], result["id"])
    return customer


def delete_all():
    sql = "DELETE FROM customers"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM customers WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(customer):
    sql = "UPDATE customers SET name = %s WHERE id = %s"
    values = [customer.name, customer.id]
    run_sql(sql, values)
