**********
Change Log
**********

1.0.0rc2 (2022-10-30)
=====================
* Fix escaping in XML serialization.

  Notably, ``&`` was mistakenly escaped to ``&amp`` instead of ``&amp;``.
* Fix issues in verification of dates and other XML data types:

    * We checked ``matches_*(value) is not None``, while ``matches_*`` returns a boolean.
      Therefore, the checks against the patterns were outright ignored in the code.

    * We fix the verification of ``xs:float`` for infinity.
      This means that overflows are now correctly detected if the value is not a proper ``INF``.

    * We disallow floating-point numbers in exponents in ``xs:float`` and ``xs:double``,
      see also: `aas-core-meta b2d1230`.

    * We disallow ``+INF`` as plus sign is not allowed in XML, see also `aas-core-meta a8e6621`

.. _aas-core-meta b2d1230: https://github.com/aas-core-works/aas-core-meta/commit/b2d1230
.. _aas-core-meta a8e6621: https://github.com/aas-core-works/aas-core-meta/commit/a8e6621

1.0.0rc1 (2022-10-29)
=======================
* Initial version, ready for the very first review
