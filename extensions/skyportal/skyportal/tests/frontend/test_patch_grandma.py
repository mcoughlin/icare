from playwright.sync_api import expect


def test_patch_icare(super_admin_user, page):
    page.goto(f"/become_user/{super_admin_user.id}")
    page.goto("/")
    expect(page.locator('//*[contains(.,"Icare")]').first).to_be_visible(timeout=20000)
