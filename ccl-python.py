from google.cloud import datastore

datastore_client = datastore.Client()

kind = 'Task'
name = 'sampleTask1'

task_key = datastore_client.key(kind, name)
task['description'] = 'Buy Milk'

datastore_client.put(task)

print('Saved {}:'.format(task.key.name), task['description']))