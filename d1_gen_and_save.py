from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://v4.ketangpai.com/User/login.html
    page.goto("https://v4.ketangpai.com/User/login.html")

    # Click [placeholder="邮箱/账号/手机号"]
    page.click("[placeholder=\"邮箱/账号/手机号\"]")

    # Fill [placeholder="邮箱/账号/手机号"]
    page.fill("[placeholder=\"邮箱/账号/手机号\"]", "your name")

    # Press Tab
    page.press("[placeholder=\"邮箱/账号/手机号\"]", "Tab")

    # Click [placeholder="密码"]
    page.click("[placeholder=\"密码\"]")

    # Fill [placeholder="密码"]
    page.fill("[placeholder=\"密码\"]", "your password")

    # Click text=账号： 密码： 下次自动登录 忘记密码？ 登录 还没有账号？去注册 >> :nth-match(a, 3)
    # with page.expect_navigation(url="https://v4.ketangpai.com/Main/index.html"):
    with page.expect_navigation():
        # page.click("text=账号： 密码： 下次自动登录 忘记密码？ 登录 还没有账号？去注册 >> :nth-match(a, 3)")
        page.click(".btn-btn")

    # Click text=+ 加入课程
    page.click("text=+ 加入课程")

    # Click [placeholder="请输入课程加课验证码"]
    page.click("[placeholder=\"请输入课程加课验证码\"]")

    # Fill [placeholder="请输入课程加课验证码"]
    page.fill("[placeholder=\"请输入课程加课验证码\"]", "sffs")

    # Click a:has-text("加入")
    page.click("a:has-text(\"加入\")")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
