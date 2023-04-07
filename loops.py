for i in range(0,10,1):
    print(i)
    print("OK")

list_of_envs=["dev","prd","qa"]

for env in list_of_envs:
    if env == "dev":
        print("I am in dev")
