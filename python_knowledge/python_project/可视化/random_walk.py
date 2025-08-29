from random import choice

class RandomWalk:
    def __init__(self,num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points=num_points

        # 所有随机漫步都始于(0,0)
        self.x_values=[0]
        self.y_values=[0]
    
    def fill_walk(self):
        """计算漫步的所有点"""

        #不断漫步,知道列表达到指定长度
        while len(self.x_values)<self.num_points:
            # 决定前进方向以及行进距离
            x_step=self.get_step()
            y_step=self.get_step()

            #跳过原地踏步
            if x_step==0 and y_step==0:
                continue

            #计算下一个点的x和y
            x=self.x_values[-1]+int(x_step)
            y=self.y_values[-1]+int(y_step)

            #为了体现他们是走过去的
            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        direction=choice([-1,1])
        distance=choice([0,1,2,3,4,5])
        step=direction*distance
        return step