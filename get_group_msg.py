#coding=utf-8
import itchat

@itchat.msg_register('Text', isGroupChat=True)
def group_reply_text(msg):
    #目前微信群聊除了群聊名称并没有其它固定的唯一标识，所以暂时只能依据群昵称进行判断,如果这个还担心重复的话，还有别的办法哦~~大家发散一下思维.
    #在msg这个dict数据中，并不能直接获取到群昵称这个字段，所以这里用一个取巧的办法，将msg转换为字符串，然后判断指定的群昵称是否在字符串中^_^
    msg_to_str = str(msg)
    group_name = '我是指定的群昵称'
    if group_name in msg_to_str:
        #这里就不对数据进行存储和分析，仅将内容回复到自己的文件传输助手中
        itchat.send(msg['FromUserName'] + ' : ' + msg['ActualNickName']+ ' : ' +msg['Content'], 'filehelper')
        del msg_to_str
itchat.auto_login(True)
itchat.run()    