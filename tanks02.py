#新增功能加载主程序
#主程序
#导入pygame模块
import pygame
#设置窗口宽度和高度
SCREEN_WIDTH=700
SCREEN_HEIGHT=500
BG_COLOR=pygame.Color(0,0,0)
class MainGame():
    Window=None
    def __init__(self):
        pass
     #开始游戏
    def startGame(self):
        #加载窗口
        #初始化窗口
        pygame.display.init()
        #设置窗口大小及显示
        MainGame.Window=pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
        #设置窗口标题
        pygame.display.set_caption("坦克大战1.0")
         #一直显示窗口
        while True:
            #给窗口设置颜色
            MainGame.Window.fill(BG_COLOR)
            pygame.display.update()


    #结束游戏
    def endGame(self):
        pass


#坦克类
class Tank():
    def __init__(self):
        pass
    #移动
    def move(self):
        pass
    #射击
    def shot(self):
        pass
    #显示坦克的方法
    def displayTank(self):
        pass
#我方坦克 
class MyTank(Tank):
    def __init__(self):
        pass
#敌方坦克
class EnemyTank(Tank):
    def __init__(self):
        pass

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

#墙壁类
class Wall():
    def __init__(self):
        pass
    #展示墙壁的方法
    def displayWall(self):
        pass
#射击类
class Explode():
    def __init__(self):
        pass
    #展示爆炸效果的方法
    def displayExplode(self):
        pass

#音乐类
class Music():

    def __init__(self):
        pass
    #播放音乐
    def play(self):

        pass
#显示窗口
if __name__=="__main__":
    MainGame().startGame()
   