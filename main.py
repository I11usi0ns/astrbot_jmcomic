from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import jmcomic

import os

def get_image_paths(directory, image_extensions=None):

    if image_extensions is None:
        image_extensions = ('.jpg', '.jpeg', '.png', '.gif', 
                          '.bmp', '.tiff', '.webp', '.svg')
    
    image_paths = []
    
    # 遍历目录及其子目录
    for root, _, files in os.walk(directory):
        for file in files:
            # 检查文件扩展名是否在指定的图片扩展名中
            if file.lower().endswith(image_extensions):
                full_path = os.path.join(root, file)
                image_paths.append(full_path)
    
    # 将列表转换为元组返回
    return tuple(image_paths)

@register("jmcomic", "YourName", "一个简单的 Hello World 插件", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
    
    # 注册指令的装饰器。指令名为 helloworld。注册成功后，发送 `/helloworld` 就会触发这个指令，并回复 `你好, {user_name}!`
    @filter.command("jmcomic")
    async def jmcomic(self, event: AstrMessageEvent,x: int):
        '''这是一个 hello world 指令''' # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
        user_name = event.get_sender_name()
        message_str = event.message_str # 用户发的纯文本消息字符串
        message_chain = event.get_messages() # 用户所发的消息的消息链 # from astrbot.api.message_components import *
        logger.info(message_chain)
        option = jmcomic.create_option_by_file('C:/Users/gigggjjffd/Desktop/!/bot/jmbot/option.yml')
# 使用option对象来下载本子
        jmcomic.download_album(x,option)
#        yield event.plain_result(f"Hello, {user_name}, 你发了 {message_str}!") # 发送一条纯文本消息
        aa = get_image_paths("D:\download")
        for pat in aa:
            yield event.make_result().file_image("pat")

    async def terminate(self):
        '''可选择实现 terminate 函数，当插件被卸载/停用时会调用。'''
