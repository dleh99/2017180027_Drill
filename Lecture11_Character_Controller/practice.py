class Star:

    type = 'Star'
    x = 100

    def change(self):
        x = 200
        print('x is ', x)

print('x IS ', Star.x)
Star.change(Star)
print('x IS ', Star.x)

star = Star()
print('x IS ', star.x)
star.change()
print('x IS ', star.x)