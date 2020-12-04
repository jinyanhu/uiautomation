$(document).ready(
    function() {
        var $errorDiv = $('.error-info');
        var $errorLen = $errorDiv.length;
        //console.log($errorDiv);
        var errorInfo = "";
        for (var i = 0; i < $errorLen; i++) {
            //errorInfo = $errorDiv[i].innerText;
            errorInfo = $($errorDiv[i]).text();
            //console.log(errorInfo);
            var $errorDivNew = $($errorDiv[i]);
            var coloredErrorInfo = errorInfo.replace(/(AssertionError)/, "<br /><span style='color:#e74c3c'>���������Ϣ<\/span>");
            coloredErrorInfo = coloredErrorInfo.replace(/ft/, "����");
            coloredErrorInfo = coloredErrorInfo.replace(/Traceback/, "<br /><span style='color:#9b59b6'>��ջ����</span>");
            coloredErrorInfo = coloredErrorInfo.replace(/File/, "<br />������Դ����ļ�");
            coloredErrorInfo = coloredErrorInfo.replace(/line\s(\d+)?,\s/g, "<span style='color:green'>��$1��</span><br /><span style='color:#e74c3c'>����λ��</span>��");
            coloredErrorInfo = coloredErrorInfo.replace(/(\[.*?\])/g, "<br /><span style='color:blue'>$1</span>");
            coloredErrorInfo = coloredErrorInfo.replace(/(������Ϣ��)/g, "<br /><span style='color:#9b59b6'>$1</span>")
            coloredErrorInfo = coloredErrorInfo.replace(/(״̬�룺)/g, "<br /><span style='color:#9b59b6'>$1</span>")
            coloredErrorInfo = coloredErrorInfo.replace(/(����Ϊ��)/g, "<br /><span style='color:#9b59b6'>$1</span>")
            coloredErrorInfo = coloredErrorInfo.replace(/(body=)/g, "<br /><span style='color:#9b59b6'>$1</span>")
            coloredErrorInfo = coloredErrorInfo.replace(/(Expected: )/g, "<br /><span style='color:#9b59b6'>����ֵΪ��</span>")
            coloredErrorInfo = coloredErrorInfo.replace(/(but: was)/g, "<br /><span style='color:#9b59b6'>���ǽ��Ϊ��</span>")
            coloredErrorInfo = coloredErrorInfo.replace(/(POST)/g, "<br /><span style='color:#9b59b6'>POST</span>")
            coloredErrorInfo = coloredErrorInfo.replace(/(java )/g, "<br /><span style='color:#9b59b6'>����java </span>")
            //$errorDiv[i].innerHtml = coloredErrorInfo;
            $errorDivNew.html(coloredErrorInfo);
            //console.log(coloredErrorInfo);
        }
    }
);