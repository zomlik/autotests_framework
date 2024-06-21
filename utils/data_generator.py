from mimesis import Generic, Locale


class DataGenerator:
    _LOCALE = Locale.EN

    @staticmethod
    def first_name(locale=_LOCALE):
        return Generic(locale).person.first_name()

    @staticmethod
    def last_name(locale=_LOCALE):
        return Generic(locale).person.last_name()

    @staticmethod
    def emal(locale=_LOCALE):
        return Generic(locale).person.email()
