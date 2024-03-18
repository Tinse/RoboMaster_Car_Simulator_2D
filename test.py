# -*- coding: utf-8 -*-
import sys         # 导入sys模块
import pygame       # 导入pygame模块


pygame.init()        # 初始化pygame
size = width, height = 800, 500      # 设置窗口尺寸
screen = pygame.display.set_mode(size)    # 显示窗口
pygame.display.set_caption('RM AI Challenge Simulator')

gray = (180, 180, 180)
red = (190, 20, 20)
blue = (10, 125, 181)
# 执行死循环，确保窗口一直显示
while True:
    # 检查事件
    for event in pygame.event.get():    # 遍历所有事件
        if event.type == pygame.QUIT:     # 如果单击关闭窗口，则退出
            sys.exit()
pygame.quit()       # 退出pygame
