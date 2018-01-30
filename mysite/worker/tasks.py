import time
from celery import task


@task(name='add')
def add(x, y):
    print('Adding task called with {} and {}'.format(x, y))
    time.sleep(1)
    print('Finished task')
    return x + y
