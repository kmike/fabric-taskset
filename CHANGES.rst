
Changes
=======

0.2.1 (2012-09-21)
------------------

- private ``_expose_to`` method now returns list, not generator.

0.2 (2012-08-28)
----------------

- ``@task`` decorator is deprecated and replaced with ``@task_method``.
  This was a bad name because of ``@fabric.task`` decorator
  (thanks Denis Untevskiy);
- ``Taskset.expose_as_module`` method that allows to use TaskSet instances
  from command line without creating dummy modules on disk
  (thanks Denis Untevskiy).


0.1 (2012-03-03)
----------------

Initial release.
