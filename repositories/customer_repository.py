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
        humans.append(human)
    return humans


def select(id):
    human = None 
    sql = "SELECT * FROM humans WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        human = Human(result["name"], result["id"])
    return human


def delete_all():
    sql = "DELETE FROM humans"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM humans WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(human):
    sql = "UPDATE humans SET name = %s WHERE id = %s"
    values = [human.name, human.id]
    run_sql(sql, values)
