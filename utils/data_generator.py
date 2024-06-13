from mimesis import Generic, Locale


class DataGenerator:
    _LOCALE = Locale.EN

    @staticmethod
    def username(locale=_LOCALE):
        return Generic(locale).person.username()

    @staticmethod
    def emal(locale=_LOCALE):
        return Generic(locale).person.email()
