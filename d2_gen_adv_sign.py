from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://v4.ketangpai.com/User/login.html
    page.goto("https://v4.ketangpai.com/User/login.html")

    # Fill [placeholder="邮箱/账号/手机号"]
    page.fill("[placeholder=\"邮箱/账号/手机号\"]", "wagyu2017@163.com")

    # Press Tab
    page.press("[placeholder=\"邮箱/账号/手机号\"]", "Tab")

    # Fill [placeholder="密码"]
    page.fill("[placeholder=\"密码\"]", "admin123456")

    # Click text=账号： 密码： 下次自动登录 忘记密码？ 登录 还没有账号？去注册 >> :nth-match(a, 3)
    # with page.expect_navigation(url="https://v4.ketangpai.com/Main/index.html"):
    with page.expect_navigation():
        page.click(".btn-btn")

    # Click text=熟悉 课堂派
    page.click("text=熟悉 课堂派")
    # assert page.url == "https://v4.ketangpai.com/Interact/index/courseid/MDAwMDAwMDAwMLOGqZiIucmwhctyoQ.html"

    # Click a:has-text("考勤")
    page.click("a:has-text(\"考勤\")")

    # Click text=新建考勤
    # import time
    # time.sleep(2)
    # print(page.frames)
    # frame = page.frame(name="layui-layer-content1")

    # print(frame)
    frame = page.frames[-1]
    frame.click("text=新建考勤")

    # Click text=数字考勤 学生通过数字码签到，自动生成考勤状态 >> div div
    frame.click("text=数字考勤 学生通过数字码签到，自动生成考勤状态 >> div div")

    # Click text=开始考勤
    frame.click("text=开始考勤")

    # Click text=结束
    frame.click("text=结束")

    # Click #end-attend a:has-text("结束")
    frame.click("#end-attend a:has-text(\"结束\")")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
