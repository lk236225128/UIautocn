class Element(object):

    # selenium关键字
    find_element_by_id = "id"
    find_elements_by_id = "ids"
    INDEX = "index"
    find_elements_by_xpath = "xpaths"
    find_element_by_xpath = "xpath"
    find_element_by_css_selector = "css"
    find_element_by_class_name = "class_name"
    find_element_by_link_text = "link_text"
    CLICK = "click"
    GET_TEXT = "get_text"
    SEND_KEYS = "send_keys"
    GET_VALUE = "get_value"
    WAIT_TIME = 20  # 查找元素等待时间
    MOVE_TO_ELEMENT = "move_to_element" # 鼠标悬停
    DEFAULT_OPERATE= "default_operate" # 默认值
    SELECT_BY_INDEX="select_by_index"
    JS_EXCUTE="js_excute"
    SELECT_BY_VALUE="select_by_value"
    SWITCH_TO_NEWWINDOW="switch_to_newwindow"
    SWITCH_TO_FRAME="switch_to_frame"
    SWITCH_TO_DEFAULTFRAME="switch_to_defaultframe"
    CONFIRM_ALERT="confirm_alert"
    CANCEL_ALERT="cancel_alert"
    ADD_COOKIE="add_cookie"
    DOUBLE_CLICK="double_click"
    OPEN_URL="open_url"
    BACK_PAGE="back_page"
    FORWARD_PAGE="forward_page"
    REFRESH_PAGE="refresh_page"
    MAXIMIZI_WINDOW="maximize_window"
    ASSERT_RESULT="assert_result"



    # 错误日志
    TIME_OUT = "timeout"
    NO_SUCH = "noSuch"
    WEB_DROVER_EXCEPTION = "WebDriverException"
    INDEX_ERROR = "index_error"
    STALE_ELEMENT_REFERENCE_EXCEPTION = "StaleElementReferenceException"
    DEFAULT_ERROR = "default_error"

    # 检查点
    CONTRARY = "contrary" # 相反检查点，表示如果检查元素存在就说明失败，如删除后，此元素依然存在
    CONTRARY_GETVAL = "contrary_getval" # 检查点关键字contrary_getval: 相反值检查点，如果对比成功，说明失败
    DEFAULT_CHECK = "default_check" # 默认检查点，就是查找页面元素
    COMPARE = "compare" # 历史数据和实际数据对比

    RE_CONNECT = 1  # 是否打开失败后再次运行一次用例

    # 文件名字
    INFO_FILE = "Webinfo.pickle"
    SUM_FILE = "Websum.pickle"
    DEVICES_FILE = "Webdevices.pickle"
    REPORT_FILE = "WebReport.xlsx"