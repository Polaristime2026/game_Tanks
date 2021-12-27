'''
新增功能
    添加事件
    1.点击关闭 关闭窗口
    2.按下键盘时候，判断键盘按下的是什么键，分别对不同的键做处理
    3.左上角绘制文字
    4.加载我方坦克
    5.实现我方坦克转向移动
    6.优化移动我方坦克移动方式
    7.优化:按下方向键，坦克一直移动
         松开方向键，坦克停止
    8.优化:按下方向键，坦克一直移动
         松开方向键，坦克停止
    9.加载敌方坦克

'''
#导入pygame模块f
import pygame,time,random
SCREEN_WIDTH=700
SCREEN_HEIGHT=500
BG_COLOR=pygame.Color(0,0,0)
TEXT_COLOR=pygame.Color(255,0,0)
class MainGame():
    window=None
    my_tank=None
    #创建存储敌方坦克的列表
    enemyTanklist=[]
    #定义敌方坦克数量
    enemyTankCount=5
    def __init__(self):
        pass
    #开始游戏
    def startGame(self):
        #加载主窗口
        #初始化窗口
        pygame.display.init()
        #设置窗口的大小及显示
        MainGame.window=pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
        #初始化我方坦克
        MainGame.my_tank=Tank(350,250)
        #初始化敌方坦克
        self.createEnemyTank()      
        #设置窗口的标题
        pygame.display.set_caption('坦克大战1.03')
        while True:
            #使用坦克移动的速度慢一点
            time.sleep(0.02)
            #给窗口设置填充色
            MainGame.window.fill(BG_COLOR)
            #获取事件
            self.getEvent()
            #绘制文字
            MainGame.window.blit(self.getTextSuface('敌方坦克剩余数量%d'%6),(10,10))
            #调用坦克显示的方法
            MainGame.my_tank.displayTank()
            #调用移动方法
            #如果坦克的开关是开启，才可以移动
            if not MainGame.my_tank.stop:
                MainGame.my_tank.move()
            pygame.display.update()
    #初始化敌发坦克
    def createEnemyTank(self):
        top=100
        #循环生成敌方坦克
        for i range (MainGame.enemyTankCont):

        EnemyTank(left,top,speed)


    #结束游戏
    def endGame(self):
        print('你这个垃圾就不玩了？')
        exit()
    #左上角文字的绘制
    def getTextSuface(self,text):
        #初始化字体模块
        pygame.font.init()
        #查看所有的字体名称
        # print(pygame.font.get_fonts())
        #获取字体Font对象
        font=pygame.font.SysFont('kaiti',18)
        #绘制文字信息
        textSurface=font.render(text,True,TEXT_COLOR)
        return textSurface
    #获取事件
    def getEvent(self):
        #获取所有事件
        eventList= pygame.event.get()
        #遍历事件
        for event in eventList:
            #判断按下的键是关闭还是键盘按下
            #如果按的是退出，关闭窗口
            if event.type == pygame.QUIT:
                self.endGame()
            #如果是键盘的按下
            if event.type == pygame.KEYDOWN:
                #判断按下的是上、下、左、右
                if event.key == pygame.K_LEFT:
                    #切换方向
                    MainGame.my_tank.direction='L'
                    #修改坦克的开关状态
                    MainGame.my_tank.stop=False
                    # MainGame.my_tank.move()
                    print('按下左键，坦克向左移动')
                elif event.key == pygame.K_RIGHT:
                    #切换方向
                    MainGame.my_tank.direction='R'
                    #修改坦克的开关状态
                    MainGame.my_tank.stop=False
                    # MainGame.my_tank.move()
                    print('按下右键，坦克向右移动')
                elif event.key == pygame.K_UP:
                    #切换方向
                    MainGame.my_tank.direction='U'
                    #修改坦克的开关状态
                    MainGame.my_tank.stop=False
                    # MainGame.my_tank.move()
                    print('按下上键，坦克向上移动')
                elif event.key == pygame.K_DOWN:
                    #切换方向
                    MainGame.my_tank.direction='D'
                    #修改坦克的开关状态
                    MainGame.my_tank.stop=False
                    # MainGame.my_tank.move()
                    print('按下左键，坦克向下移动')
                elif event.key == pygame.K_SPACE:
                    print('发射子弹')

            #松开方向键，坦克停止移动，修改坦克的开关状态
            if event.type == pygame.KEYUP:
                #判断松开的键是上、下、左、右时候才停止坦克移动
                if event.key==pygame.K_UP or event.key==pygame.K_DOWN or event.key == pygame.K_LEFT or event.key ==pygame.K_RIGHT:
                    MainGame.my_tank.stop = True


class Tank():
    #添加距离左边left 距离上边top
    def __init__(self,left,top):
        #保存加载的图片
        self.images={
            'U':pygame.image.load('img/p1tankU.gif'),
            'D':pygame.image.load('img/p1tankD.gif'),
            'L':pygame.image.load('img/p1tankL.gif'),
            'R':pygame.image.load('img/p1tankR.gif'),
        }
        #方向
        self.direction='L'
        #根据当前图片的方向获取图片 surface
        self.image=self.images[self.direction]
        #根据图片获取区域
        self.rect=self.image.get_rect()
        #设置区域的left 和top
        self.rect.left=left
        self.rect.top=top
        #速度  决定移动的快慢
        self.speed=5
        #坦克移动的开关
        self.stop=True

    #移动
    def move(self):
        #判断坦克的方向进行移动
        if self.direction == 'L':
            if self.rect.left>0:
                self.rect.left -= self.speed
        elif self.direction == 'U':
            if self.rect.top>0:
                self.rect.top -= self.speed
        elif self.direction == 'D':
            if self.rect.top+self.rect.height<SCREEN_HEIGHT:
                self.rect.top += self.speed
        elif self.direction == 'R':
            if self.rect.left+self.rect.height<SCREEN_WIDTH:
                self.rect.left += self.speed

    #射击
    def shot(self):
        pass
    #展示坦克的方法
    def displayTank(self):
        #获取展示的对象
        self.image=self.images[self.direction]
        #调用blit方法展示
        MainGame.window.blit(self.image,self.rect)
#我方坦克
class MyTank(Tank):
    def __init__(self):
        pass

#敌方坦克
class EnemyTank(Tank):
    def __init__(self,left,top,speed):
         #加载敌方图片
         self.images={
              'U':pygame.image.load(img/enmylU.gif),
              'D':pygame.image.load(img/enmylD.gif),
              'L':pygame.image.load(img/enmylL.gif),
              'R':pygame.image.load(img/enmylR.gif)
         }
         #方向,
         self.direction=self.randDirection()
         #根据方向获取图片
         self.image=self.images[self.direction]
         #区域
         self.rect=self.image.get_rect()
         #对left和top进行赋值
         self.rect.left=left
         self.rect.top=top
         #速度
         self.speed=speed
         #移动开关键
         self.flag=True
         #随机生成坦克方向
         def randDirection(self):
             num=random.randint(1, 4)
             if num==1:
                 return 'U'
             elif num==2:
                 return 'D'
             elif num==3:
                 return 'L'
             elif num==4:
                 return 'R'
#子弹类
class Bullet():
    def __init__(self):
        pass
    #移动
    def move(self):
        pass
    #展示子弹的方法
    def displayBullet(self):
        pass
class Wall():
    def __init__(self):
        pass
    #展示墙壁的方法
    def displayWall(self):
        pass
class Explode():
    def __init__(self):
        pass
    #展示爆炸效果的方法
    def displayExplode(self):
        pass
class Music():
    def __init__(self):
        pass
    #播放音乐
    def play(self):
        pass
if __name__=='__main__':
    MainGame().startGame()
    # MainGame().getTextSuface()