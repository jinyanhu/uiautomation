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
            var coloredErrorInfo = errorInfo.replace(/(AssertionError)/, "<br /><span style='color:#e74c3c'>出错断言信息<\/span>");
            coloredErrorInfo = coloredErrorInfo.replace(/ft/, "用例");
            coloredErrorInfo = coloredErrorInfo.replace(/Traceback/, "<br /><span style='color:#9b59b6'>堆栈跟踪</span>");
            coloredErrorInfo = coloredErrorInfo.replace(/File/, "<br />出错测试代码文件");
            coloredErrorInfo = coloredErrorInfo.replace(/line\s(\d+)?,\s/g, "<span style='color:green'>第$1行</span><br /><span style='color:#e74c3c'>出错位置</span>：");
            coloredErrorInfo = coloredErrorInfo.replace(/(\[.*?\])/g, "<br /><span style='color:blue'>$1</span>");
            coloredErrorInfo = coloredErrorInfo.replace(/(错误信息：)/g, "<br /><span style='color:#9b59b6'>$1</span>")
            coloredErrorInfo = coloredErrorInfo.replace(/(状态码：)/g, "<br /><span style='color:#9b59b6'>$1</span>")
            coloredErrorInfo = coloredErrorInfo.replace(/(请求为：)/g, "<br /><span style='color:#9b59b6'>$1</span>")
            coloredErrorInfo = coloredErrorInfo.replace(/(body=)/g, "<br /><span style='color:#9b59b6'>$1</span>")
            coloredErrorInfo = coloredErrorInfo.replace(/(Expected: )/g, "<br /><span style='color:#9b59b6'>期望值为：</span>")
            coloredErrorInfo = coloredErrorInfo.replace(/(but: was)/g, "<br /><span style='color:#9b59b6'>但是结果为：</span>")
            coloredErrorInfo = coloredErrorInfo.replace(/(POST)/g, "<br /><span style='color:#9b59b6'>POST</span>")
            coloredErrorInfo = coloredErrorInfo.replace(/(java )/g, "<br /><span style='color:#9b59b6'>调用java </span>")
            //$errorDiv[i].innerHtml = coloredErrorInfo;
            $errorDivNew.html(coloredErrorInfo);
            //console.log(coloredErrorInfo);
        }
    }
);