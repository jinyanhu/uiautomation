import json
from utils.http_util import Http
from utils.datetime_util import DatetimeUtil


class DingMsgSend(object):
    """
    钉钉群消息推送类
    """
    def __init__(self, access_token="72584842502405be7d393ad130b8e86bb9a58e50ee1cd079934c844ba71f6702"):
        self._http = Http()
        self._url = "https://oapi.dingtalk.com/robot/send?access_token=" + access_token

    def send_msg(self, text, msg_type="text"):
        """
        发送钉钉群消息
        :param text:
        :param msg_type:
        :return:
        """
        body = {
            "msgtype": msg_type,
            "text": {
                "content": text
            }
        }
        try:
            self._http.post(self._url, body=body)
        except Exception as e:
            print(e)


class DingNotice(object):
    """
    钉钉公告推送类
    """
    def __init__(self):
        self._http = Http()
        pass

    def get_token(self):
        url = "https://oapi.dingtalk.com/gettoken?corpid=ding5872486cef57428335c2f4657eb6378" \
              "f &corpsecret=y5h-RU0i51ET_WbJmivzmFtg0u9eASAj61hhlGoTyPYu9NqBu-xt9uHltmScT080"
        res = self._http.get(url).text
        res_json = json.loads(res)
        token = res_json["access_token"]
        return token

    def notice(self, text):
        try:
            url = "https://eco.taobao.com/router/rest"
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            datetime_util = DatetimeUtil()
            user_str = "0264354281217479,136060036624190684"
            body = {"format": "json",
                    "method": "dingtalk.corp.message.corpconversation.asyncsend",
                    "session": self.get_token(),
                    "timestamp": datetime_util.str_now_date_time(),
                    "v": "2.0",
                    "msgtype": "text",
                    "agent_id": "48876744",
                    "userid_list": user_str,
                    "msgcontent": {"content": text}}
            self._http.post(url, headers, body)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    ding = DingMsgSend("72584842502405be7d393ad130b8e86bb9a58e50ee1cd079934c844ba71f6702")
    ding.send_msg("测试")
    # dingNotice = DingNotice()
    # dingNotice.notice("测试中")

