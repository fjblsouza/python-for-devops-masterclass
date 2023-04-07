env="prd"
list_of_envs=["dev","prd","qa"]
print(type(list_of_envs))

print("I am in",list_of_envs[1])

list_of_envs.append("uat") #insert at the end

#dir what all methods are available

print(list_of_envs.count("dev"))