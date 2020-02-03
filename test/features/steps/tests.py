from behave import *
from application.app import app


@given( 'a {salary}')
def step_impl(context,salary):
    context.app = app.test_client()
    context.salary = float(salary)
    
@when('I calculate tax')
def step_impl(context):
    context.response = context.app.get('/tax/{}'.format(context.salary))

@then('it should get the tax as {tax}')
def step_impl(context, tax):
    assert float(context.response.data) == float(tax)
    