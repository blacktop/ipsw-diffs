## mtmergeprops

> `/usr/libexec/mtmergeprops`

```diff

-9130.2.0.0.0
-  __TEXT.__text: 0xb54
+9140.1.0.0.0
+  __TEXT.__text: 0xb84
   __TEXT.__auth_stubs: 0x3a0
   __TEXT.__objc_stubs: 0x1c0
   __TEXT.__const: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EAD1E984-10BD-3B9F-8A3C-4713413C9260
+  UUID: 9B005579-E868-33A4-929A-48CDBC5FB507
   Functions: 10
   Symbols:   109
   CStrings:  40
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x24
+ _objc_retain_x25
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
Functions:
~ _MergePersonalityDictionaryFromPathWithName : 644 -> 676
~ _recursiveMerge : 280 -> 276
~ _MergePropertiesForDriver : 400 -> 396
~ _MergePropertiesWithIterator : 284 -> 300
~ ___recursiveMerge_block_invoke : 272 -> 280

```
