class Head:
    def __init__(self):
        self.description= 'A head with brain and eyes'


class Hand:
    def __init__(self, side):
        self.side=side

class Feed:
    def __init__(self, side):
        self.side=side
        

class Arm:
    def __init__(self, hand):
        self.hand=hand

class Leg:
    def __init__(self, feed):
        self.feed=feed

class Torso:
    def __init__(self, head, left_arm, right_arm, left_leg, right_leg):
        self.head=head
        self.left_arm=left_arm
        self.right_arm=right_arm
        self.left_leg=left_leg
        self.right_leg=right_leg

class Human:
    def __init__(self, name, torso):
        self.name=name
        self.torso=torso

#1
left_hand=Hand('left')
right_hand=Hand('right')
left_feed=Feed('left')
right_feed=Feed('right')


#2

left_arm=Arm(left_hand)
right_arm=Arm(right_hand)
left_leg=Leg(left_feed)
right_leg=Leg(right_feed)
head=Head()

#3
my_torso=Torso(head,left_arm, right_arm, left_leg, right_leg)

#4
person_1=Human('Alex', my_torso)

#5
print(f'The human is called: {person_1.name}')
print(f'Side of right hand: {person_1.torso.right_arm.hand.side}')