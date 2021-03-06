from abstract_context import AbstractContext
from pages.admin_login_page import AdminLoginPage
from pages.home_admin_page import HomeAdminPage
from pages.wp_admin_page import WpAdminPage
from pages.new_user_page import NewUserPage
from pages.users_page import UsersPage
from pages.confirm_erase_page import ConfirmErasePage
from pages.membership_page import MembershipPage
from pages.add_membership_page import AddMembershipPage


class TestUsers(AbstractContext):
    def test_a_create_user(self):
        admin_page = AdminLoginPage(self.driver)
        admin_page.go()
        admin_page.wait(3)
        admin_page.login()
        admin_page.wait(10)
        home_adm_page = HomeAdminPage(self.driver)
        home_adm_page.click_site_name()
        wp_adm_page = WpAdminPage(self.driver)
        wp_adm_page.click_users()
        new_user_page = NewUserPage(self.driver)
        new_user_page.fill_form()
        users_page = UsersPage(self.driver)
        element = users_page.get_new_user_name()
        assert element.text == 'Orlando Sosa'

    def test_b_create_membership(self):
        admin_page = AdminLoginPage(self.driver)
        admin_page.go()
        admin_page.wait(3)
        admin_page.login()
        admin_page.wait(10)
        home_adm_page = HomeAdminPage(self.driver)
        home_adm_page.click_site_name()
        wp_adm_page = WpAdminPage(self.driver)
        wp_adm_page.click_membership()
        memb_page = MembershipPage(self.driver)
        memb_page.create_membership()
        add_membership = AddMembershipPage(self.driver)
        test_name = memb_page.set_membership_name()
        add_membership.add_test_membership(test_name)
        memb_page.click_pop_up_finish()
        membership_name = memb_page.get_new_membership_name()
        assert test_name == membership_name.text

    def test_c_erase_membership(self):
        admin_page = AdminLoginPage(self.driver)
        admin_page.go()
        admin_page.wait(3)
        admin_page.login()
        admin_page.wait(10)
        home_adm_page = HomeAdminPage(self.driver)
        home_adm_page.click_site_name()
        wp_adm_page = WpAdminPage(self.driver)
        wp_adm_page.click_membership()
        memb_page = MembershipPage(self.driver)
        count_memberships = memb_page.get_count_memberships()
        memb_page.erase_test_membership()
        new_count_memberships = memb_page.get_count_memberships()
        assert count_memberships != new_count_memberships


    def test_d_erase_user(self):
        admin_page = AdminLoginPage(self.driver)
        admin_page.go()
        admin_page.wait(3)
        admin_page.login()
        admin_page.wait(10)
        home_adm_page = HomeAdminPage(self.driver)
        home_adm_page.click_site_name()
        wp_adm_page = WpAdminPage(self.driver)
        wp_adm_page.click_all_users()
        users_page = UsersPage(self.driver)
        count_users = users_page.get_users()
        users_page.erase_created_user()
        confirm_erase_page = ConfirmErasePage(self.driver)
        confirm_erase_page.confirm_erase()
        actual_users = users_page.get_users()
        assert count_users != actual_users
