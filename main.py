import werobot
import baidu
import keyWords

robot = werobot.WeRoBot(token='123123')


@robot.text  # 对文本内容的处理
def echo(message):
    message = message.content
    print('----------------------  begin  -----------------------')
    val = keyWords.inn(message)
    if val is None:
        val = baidu.talk(message)
    print('val is:' + val)
    print('----------------------   end   -----------------------')
    return val


@robot.image  # 对图片内容的处理
def image(message):
    return message.img


# 配置信息


robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80

robot.run()
