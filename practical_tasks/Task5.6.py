class MySingleAttributedClass():

    __slots__ = ('single_permitted_attribute',)

    def __setattr__(self, attrname, value):
        if attrname == 'single_permitted_attribute':
            MySingleAttributedClass.__dict__[attrname].__set__(self, value)
        else:
            print("Forbidden attribute to set!")

    def __getattr__(self, attrname):
        if attrname != 'single_permitted_attribute':
            print("Forbidden attribute to get!")


if __name__ == '__main__':
    inst = MySingleAttributedClass()
    inst.single_permitted_attribute = 5
    print(inst.single_permitted_attribute)
    inst.any_other_attribute_1 = 7
    inst.any_other_attribute_2
