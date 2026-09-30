## libSEUpdater.dylib

> `/usr/lib/updaters/libSEUpdater.dylib`

```diff

-57.2.1.0.0
-  __TEXT.__text: 0x65f20
+57.4.1.0.0
+  __TEXT.__text: 0x660d4
   __TEXT.__auth_stubs: 0x1210
   __TEXT.__init_offsets: 0x1c
   __TEXT.__objc_methlist: 0x654
   __TEXT.__const: 0x7c78
   __TEXT.__oslogstring: 0x5e
-  __TEXT.__cstring: 0x8046
-  __TEXT.__gcc_except_tab: 0x7b00
+  __TEXT.__cstring: 0x8067
+  __TEXT.__gcc_except_tab: 0x7b48
   __TEXT.__unwind_info: 0x1a18
   __TEXT.__objc_classname: 0x9a
   __TEXT.__objc_methname: 0x1263

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libnfrestore.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 972EABBC-B26F-30E0-A026-BF2DA7EF78E9
+  UUID: 0C4BE8BF-C8C4-34DB-B201-9F57CF05749D
   Functions: 1337
   Symbols:   4370
-  CStrings:  1770
+  CStrings:  1771
 
Symbols:
+ ___block_descriptor_tmp.352
+ ___block_descriptor_tmp.354
- ___block_descriptor_tmp.351
- ___block_descriptor_tmp.353
Functions:
~ __ZN9SEUpdater23P73BaseUpdateController9doPerformEv : 50992 -> 51428
CStrings:
+ "Current Oasis Config ID: %s, Expected: %s\n"
+ "Oasis up to date.\n"
- "Current Oasis Config ID: %s\n"

```
