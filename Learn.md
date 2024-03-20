# Pygame无人车环境

## 1. 整体框架

用户代码 -> 环境抽象层 -> 核心层

用户代码为强化学习算法，环境的创建、获取观测、输出动作等

环境抽象层从核心层抽象出状态空间、动作空间，以及对环境的操作

核心层实现环境运行的底层逻辑

## 2. 环境抽象层env.py

### 2.1 Env(agent_num, render = Ture)

抽象环境的类，agent_num为智能体数量，render为是否手动控制，默认手动控制。初始化会创建game对象为游戏核心的实例，创建g_map获取game的大小、区域及障碍。

#### 2.1.1 reset()方法

重置游戏，返回初始观测

#### 2.1.2 step(actions)方法

输入动作，环境运行一个时间步，并返回观测、奖励、是否结束和None（为了与低版本的gym中的Env.step()对应）

#### 2.1.3 get_observation(state)

观测的实现，输入当前状态，可以此方法内设计观测空间。

#### 2.1.4 get_reward(state)

奖励的实现，输入当前状态，可以在此方法内设计奖励规则

#### 2.1.5 play()

仅human模式可以开启，用于手动控制

#### 2.1.6 save_record(file)

保存回放

## 3. 核心层kernel.py

### 3.1 Kernel(car_num, render = False, record = True)

car_num指定车的数量，render指定是否为手动控制模式，record指定是否记录回放数据，其中self.areas, self.barriers为区域和障碍物的左右下上的边界范围，即[x1, x2, y1, y2]。修改对应的图片、坐标可以重新设计环境场地。

x1 是左边界的 x 坐标
x2 是右边界的 x 坐标
y1 是下边界的 y 坐标
y2 是上边界的 y 坐标

除此之外有一些可以自定义的参数：

| 参数名        | 含义                   | 目前值 |
| ------------- | ---------------------- | ------ |
| bullet_speed  | 子弹速度，单位是pixel  | 12.5   |
| motion        | 移动的惯性感           | 6      |
| rotate_motion | 底盘旋转的惯性感       | 4      |
| yaw_motion    | 云盘旋转的惯性感       | 1      |
| camera_angle  | 摄像头的视野范围       | 75/2   |
| lidar_angle   | 激光雷达的视野范围     | 120/2  |
| move_discount | 撞墙之后反弹的强度大小 | 0.6    |

#### 3.1.1 reset()

重置的内部实现，清空数据，返回初始状态

#### 3.1.2 play()

仅human模式可以调用，死循环执行时间步，且每10个时间步，获取一次指令。

#### 3.1.3 step(orders)

输入指令，连续运行10个时间步，返回状态

#### 3.1.4 one_epoch()

游戏进行一个时间步

#### 3.1.5 move_car(self, n)

实现运动的细节，包括底盘旋转运动、云台运动、自动瞄准、平移运动、射击

#### 3.1.6 move_bullet(self, n)

update_display(self)

dev_window(self)

get_order(self)

#### orders_to_acts(self, n)



## 注意事项

1. 掉血机制：并非击中或撞击任意部位都能掉血，仅限前后左右中间的装甲遭受击中或撞击才会掉血，且存在友军伤害。

## 疑问

1. 发射使能参数cars[n, 9] can_shoot使得子弹不能连续两次发射。

```
# fire or not
if self.acts[n, 4] and self.cars[n, 10]:  # 发射命令且存在剩余子弹
    if self.cars[n, 9]:  # can_shoot
        self.cars[n, 10] -= 1  # 剩余子弹数减1
        self.bullets.append(  # 添加子弹的坐标、角度、速度、发射者
            bullet(self.cars[n, 1:3], self.cars[n, 4] + self.cars[n, 3], self.bullet_speed, n))
        self.cars[n, 5] += self.bullet_speed  # 热量增加
        self.cars[n, 9] = 0
    else:
        self.cars[n, 9] = 1
else:
    self.cars[n, 9] = 1
```

2. 游戏没有控制时间与现实时间一致
