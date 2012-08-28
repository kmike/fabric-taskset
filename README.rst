==============
Fabric-taskset
==============

`Fabric <http://fabfile.org>`_ has class-based tasks but they are
limited: Task class represents a single task.

This module make it possible to have class-based Fabric task sets.

Installation
------------

::

    pip install fabric-taskset

Usage
-----

``TaskSet`` is a class that can expose its methods as Fabric tasks.

Example::


    # fabfile.py
    from fabric.api import local
    from taskset import TaskSet, task_method

    class SayBase(TaskSet):
        def say(self, what):
            raise NotImplementedError()

        @task_method(default=True, alias='hi')
        def hello(self):
            self.say('hello')

        @task_method
        def bye(self):
            self.say('goodbye')

    class EchoSay(SayBase):
        def say(self, what):
            local('echo ' + what)

    say = EchoSay().expose_as_module('say')


and then::

    $ fab -l
    Available commands:

        say
        say.bye
        say.hello
        say.hi

    $ fab say.hi
    hello


``taskset.task_method`` is a decorator declaring the wrapped method to be task.
It acceps the same arguments as ``fabric.decorators.task`` so
use it on methods just like fabric's decorator is used on functions.

You can also create an "on-disk" Python module and populate it with tasks::

    # my_lib/say.py
    from taskset import TaskSet, task_method

    class SayBase(TaskSet):
        def say(self, what):
            raise NotImplementedError()

        @task_method(default=True, alias='hi')
        def hello(self):
            self.say('hello')

    class EchoSay(SayBase):
        def say(self, what):
            local('echo ' + what)

    instance = EchoSay()
    instance.expose_to_current_module()

    # fabfile.py
    from mylib import say



Acknowledgements
----------------

https://github.com/ramusus/fabriclassed is a very similar app.
At the time of writing it is focused on old-style Fabric tasks
and has a small deployment framework included.

In order to feed my NIH syndrome I create Fabric-taskset which
exposes new-style Fabric tasks, provides slightly different API and doesn't
have extra goodies.

This library then evolved to support exposing tasks without creating dummy
on-disk modules (thanks to Denis Untevskiy).
