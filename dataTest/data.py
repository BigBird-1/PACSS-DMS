import yaml


with open('dd.yaml') as f:
    docs = yaml.load_all(f, Loader=yaml.FullLoader)
    for doc in docs:
        for k, v in doc.items():
            print(k, v)

users = [{'name': 'John Doe', 'occupation': 'gardener'},
         {'name': 'Lucy Black', 'occupation': 'teacher'}]

print(yaml.dump(users))


with open('users.yaml', 'w') as f:
    data = yaml.dump(users, f)



