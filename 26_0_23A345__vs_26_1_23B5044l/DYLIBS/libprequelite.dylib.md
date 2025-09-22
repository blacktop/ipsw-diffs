## libprequelite.dylib

> `/usr/lib/libprequelite.dylib`

```diff

-139.0.0.0.0
-  __TEXT.__text: 0xccd0
+141.0.0.0.0
+  __TEXT.__text: 0xccf4
   __TEXT.__auth_stubs: 0xa30
   __TEXT.__objc_methlist: 0xf98
-  __TEXT.__const: 0xb8
+  __TEXT.__const: 0xc0
   __TEXT.__cstring: 0xe8f
-  __TEXT.__oslogstring: 0x655
+  __TEXT.__oslogstring: 0x696
   __TEXT.__gcc_except_tab: 0xc4
   __TEXT.__unwind_info: 0x388
   __TEXT.__objc_classname: 0x14e

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 3E2A429F-EDEB-36A2-9B8C-DE994DF105B5
+  UUID: CE521489-A34A-33FA-B206-7D62E41A4B3E
   Functions: 331
   Symbols:   1440
-  CStrings:  876
+  CStrings:  877
 
Functions:
~ -[PQLStatement invalidate] : 68 -> 84
~ -[PQLStatement initWithFormat:arguments:db:cache:preparationTime:] : 1492 -> 1512
CStrings:
+ "%s:%d: PQLStatement [%p] sqlite stmt [%p] sql [%s] at depth [%d]"

```
