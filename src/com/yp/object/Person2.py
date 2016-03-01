# -*- coding: UTF-8 -*-
'''
Created on 2016年3月1日

@author: yupeng
'''
class Person2:
    '''Represents a person.'''
    population = 0

    def __init__(self, name):
        '''Initializes the person's data.'''
        self.name = name
        print '(Initializing %s)' % self.name

        # When this person is created, he/she
        # adds to the population
        Person2.population += 1

    def __del__(self):
        '''I am dying.'''
        print '%s says bye.' % self.name

        Person2.population -= 1

        if Person2.population == 0:
            print 'I am the last one.'
        else:
            print 'There are still %d people left.' % Person2.population

    def sayHi(self):
        '''Greeting by the person.

        Really, that's all it does.'''
        print 'Hi, my name is %s.' % self.name

    def howMany(self):
        '''Prints the current population.'''
        if Person2.population == 1:
            print 'I am the only person here.'
        else:
            print 'We have %d persons here.' % Person2.population

swaroop = Person2('Swaroop')
swaroop.sayHi()
swaroop.howMany()

kalam = Person2('Abdul Kalam')
kalam.sayHi()
kalam.howMany()

swaroop.sayHi()
swaroop.howMany()