## logd

> `/usr/libexec/logd`

```diff

-1815.60.5.0.0
-  __TEXT.__text: 0x2699c
+1815.62.1.0.0
+  __TEXT.__text: 0x26b14
   __TEXT.__auth_stubs: 0x19d0
   __TEXT.__delay_helper: 0x110
   __TEXT.__objc_stubs: 0x760
   __TEXT.__objc_methlist: 0x44
   __TEXT.__const: 0x2d0
-  __TEXT.__cstring: 0x4681
+  __TEXT.__cstring: 0x477a
   __TEXT.__objc_methname: 0x4ee
   __TEXT.__objc_classname: 0x2c
   __TEXT.__objc_methtype: 0x10

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 8872F90A-B51C-360D-BA0B-8875A08E2B0A
+  UUID: B17531AA-2CE4-3D4F-AE09-57E6BA340F00
   Functions: 506
   Symbols:   471
-  CStrings:  647
+  CStrings:  653
 
Symbols:
+ _fdopen
- _fopen
Functions:
~ sub_10001358c : 1960 -> 2276
~ sub_1000143fc -> sub_100014538 : 1296 -> 1356
CStrings:
+ "Deleted legacy shutdown.log due to size (%lld bytes) exceeding threshold (%d bytes)"
+ "Failed to delete oversized legacy shutdown.log (size %lld bytes): %d"
+ "Failed to migrate shutdown.log: %d"
+ "Migrated legacy shutdown.log to %s"
+ "a"
+ "shutdown.0.log"
+ "shutdown.1.log"
+ "shutdown.log"
- "%s/shutdown.log"
- "w+"

```
