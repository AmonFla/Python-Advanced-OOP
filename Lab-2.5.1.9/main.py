class LuxuryWatch:
    __watches_created = 0

    def __init__(self):
        LuxuryWatch.__watches_created += 1

    @classmethod
    def get_number_of_watches_created(cls):
        return cls.__watches_created
    
    @classmethod
    def dedicated_engraving_watch(cls, dedication):
        LuxuryWatch.validateEngrave(dedication)
        watch = cls()
        watch.__engrave = dedication
        return watch
    
    @staticmethod
    def validateEngrave(text):
        if len(text) > 40:
            raise TypeError("dedication must be under 40 character")
        if not text.isalnum():
            raise TypeError("invalid characters")

    

        
watch1 = LuxuryWatch()
print(LuxuryWatch.get_number_of_watches_created())
watch2 = LuxuryWatch.dedicated_engraving_watch("ToMee")
print(LuxuryWatch.get_number_of_watches_created())
watch3 = LuxuryWatch.dedicated_engraving_watch("to me")
print(LuxuryWatch.get_number_of_watches_created())
watch4 = LuxuryWatch.dedicated_engraving_watch("12345678901234567890123456789012345678901")
print(LuxuryWatch.get_number_of_watches_created())

