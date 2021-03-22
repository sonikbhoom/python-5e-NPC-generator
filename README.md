# python-5e-NPC-generator
5e NPC stats generator in python

This is the secret sauce: 

stats = sorted(([sum(sorted([random.randint(1,6) for _ in range (4)])[1:]) for _ in range(6)]),reverse=True)

I made this tool to quickly whip up an NPC block as a quick fix in case your players tend to latch on to throwaway NPCs... :)


![image](https://user-images.githubusercontent.com/21292601/111931549-cb432b80-8a91-11eb-812e-54eb088cc567.png)



TODO: add stats limiter (weak, medium, strong, epic) option

10000 Iterations:


![image](https://user-images.githubusercontent.com/21292601/111924601-cffce500-8a7b-11eb-973a-7d1bdf91fad8.png)


Standard Deviation


![image](https://user-images.githubusercontent.com/21292601/111924472-24539500-8a7b-11eb-8779-6a9a3b71dd87.png)
