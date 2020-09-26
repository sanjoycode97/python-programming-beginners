class Toy():
    def __init__(self,color,age):
        self.color=color
        self.age=age
        self.my_dict={
            "name":"john",
            "color":"white"
        }
    def __str__(self):
        return f'{self.color}'
    def __del__(self):
        return "deleted"
    def __len__(self):
        return 5
    def __call__(self):
        return "yess"
    def __getitem__(self, i):
        return self.my_dict[i]
action_figure=Toy("red",100)
print(action_figure.__str__())
print(action_figure.__len__())
print(action_figure.__getitem__("name"))
print(action_figure())