## keybagd

> `/usr/libexec/keybagd`

```diff

-674.0.0.0.0
-  __TEXT.__text: 0x21768
+674.0.1.0.0
+  __TEXT.__text: 0x217ec
   __TEXT.__auth_stubs: 0x14a0
   __TEXT.__objc_stubs: 0xfc0
   __TEXT.__objc_methlist: 0x814
-  __TEXT.__cstring: 0x97f2
+  __TEXT.__cstring: 0x9871
   __TEXT.__const: 0x198
   __TEXT.__gcc_except_tab: 0x468
   __TEXT.__objc_methname: 0x17d3

   __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__auth_ptr: 0x40
   __DATA_CONST.__const: 0xff0
-  __DATA_CONST.__cfstring: 0x4e60
+  __DATA_CONST.__cfstring: 0x4ea0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 0BE8AEC1-D2ED-3504-AA4B-B124BFB43985
-  Functions: 651
+  UUID: 8BC91368-6119-3E4E-8225-AC7A677ECF5D
+  Functions: 650
   Symbols:   399
-  CStrings:  2105
+  CStrings:  2109
 
CStrings:
+ "could not open db to drain %zu backup keys"
+ "db(%d) @ %s has a problem, rc=%d, version=%d, existed=%d, create=%d, readonly=%d"
+ "db(%d) @ %s has a problem, unlink rc=%d"
+ "unable to truncate (rc=%d)"
- "db(%d) @ %s has a problem, rc=%d, version=%d"
- "unable to truncate"

```
