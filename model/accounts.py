import properties


class Accounts:
    def __init__(self, row):
        self.row = row
        self.id_no = row[properties.ID_NO].value
        self.user = row[properties.USER_AVISO].value
        self.password = row[properties.PASSWORD_AVISO].value
        self.agent = row[properties.USER_AGENT].value
        self.cookies = row[properties.COOKIES].value

    def get_row(self):
        return self.row

    def get_id_no(self):
        return self.id_no

    def get_user(self):
        return self.user

    def get_password(self):
        return self.password

    def get_agent(self):
        return self.agent

    def get_cookies(self):
        return self.cookies

    def set_cookies(self, value):
        self.cookies = value

    def get_user_mail(self):
        return self.row[properties.USER_MAIL].value

    def get_password_mail(self):
        return self.row[properties.PASSWORD_MAIL].value

    def get_recover_mail(self):
        return self.row[properties.RECOVER_MAIL].value

    def get_id_payeer(self):
        return self.row[properties.ID_PAYEER].value

    def get_password_payeer(self):
        return self.row[properties.PASSWORD_PAYEER].value

    def set_updated_cookie(self, value):
        self.row[properties.UPDATE_COOKIES].value = value

    def get_updated_cookie(self):
        return self.row[properties.UPDATE_COOKIES].value

    def get_start_coins(self):
        return self.row[properties.START_COIN].value

    def set_start_coins(self, value):
        self.row[properties.START_COIN].value = value

    def get_end_coins(self):
        return self.row[properties.END_COIN].value

    def set_end_coins(self, value):
        self.row[properties.END_COIN].value = value

    def get_total_coins_per_day(self):
        return self.row[properties.TOTAL_COIN_PER_DAY].value

    def set_total_coins_per_day(self, value):
        self.row[properties.TOTAL_COIN_PER_DAY].value = value

    def get_start_time(self):
        return self.row[properties.START_TIME].value

    def set_start_time(self, value):
        self.row[properties.START_TIME].value = value

    def get_end_time(self):
        return self.row[properties.END_TIME].value

    def set_end_time(self, value):
        self.row[properties.END_TIME].value = value

    def get_count_login(self):
        return self.row[properties.COUNT_LOGIN].value

    def set_count_login(self, value):
        self.row[properties.COUNT_LOGIN].value = value






