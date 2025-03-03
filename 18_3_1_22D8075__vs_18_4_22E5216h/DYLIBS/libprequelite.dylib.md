## libprequelite.dylib

> `/usr/lib/libprequelite.dylib`

```diff

-138.0.0.0.0
-  __TEXT.__text: 0xc9c4
-  __TEXT.__auth_stubs: 0xa40
-  __TEXT.__objc_methlist: 0xd7c
-  __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0xe16
-  __TEXT.__oslogstring: 0x5df
-  __TEXT.__gcc_except_tab: 0x98
-  __TEXT.__unwind_info: 0x368
+139.0.0.0.0
+  __TEXT.__text: 0xccd4
+  __TEXT.__auth_stubs: 0xa30
+  __TEXT.__objc_methlist: 0xf98
+  __TEXT.__const: 0xb8
+  __TEXT.__cstring: 0xe8f
+  __TEXT.__oslogstring: 0x655
+  __TEXT.__gcc_except_tab: 0xc4
+  __TEXT.__unwind_info: 0x398
   __TEXT.__objc_classname: 0x14e
   __TEXT.__objc_methname: 0x2021
   __TEXT.__objc_methtype: 0x7f2

   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x930
+  __DATA_CONST.__objc_selrefs: 0x9c8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x530
+  __AUTH_CONST.__auth_got: 0x528
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0xc40
-  __AUTH_CONST.__objc_const: 0x2a00
+  __AUTH_CONST.__objc_const: 0x2660
   __AUTH_CONST.__objc_intobj: 0x18
   __DATA.__objc_ivar: 0x124
   __DATA.__data: 0x360

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 313
-  Symbols:   529
-  CStrings:  780
+  Functions: 331
+  Symbols:   595
+  CStrings:  783
 
Symbols:
- _objc_retain_x27
CStrings:
+ "%s:%d: PQLStatement [%p] sqlite stmt [%p] sql [%s]"
+ "-[PQLStatement initWithFormat:arguments:db:cache:preparationTime:]"
+ "-[PQLStatement initWithStatement:forDB:preparationTime:]"
+ "cleaning - conn - cache - PQL - SQL: %p, %p, %p, %p"
+ "sqlite3_close(%p, %@) failed: %@"
+ "sqlite3_close(%p, %@) fails: [%s, %p] isn't finalized"
+ "uncaching: <%@:%p:%p>"
- "sp"
- "sqlite3_close(%@) failed: %@"
- "sqlite3_close(%@) fails: [%s] isn't finalized"
- "uncaching: <%@:%p>"

```
