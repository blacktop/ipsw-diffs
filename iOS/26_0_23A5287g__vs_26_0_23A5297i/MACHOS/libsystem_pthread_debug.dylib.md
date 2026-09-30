## libsystem_pthread_debug.dylib

> `/System/DriverKit/usr/lib/system/libsystem_pthread_debug.dylib`

```diff

-538.0.0.0.0
-  __TEXT.__text: 0x1c030
+539.0.0.0.0
+  __TEXT.__text: 0x1bfc4
   __TEXT.__auth_stubs: 0x430
   __TEXT.__const: 0xcc
-  __TEXT.__cstring: 0xbcd
-  __TEXT.__unwind_info: 0x298
+  __TEXT.__cstring: 0xbfd
+  __TEXT.__unwind_info: 0x290
   __DATA_CONST.__got: 0x30
   __AUTH_CONST.__auth_got: 0x218
   __DATA.__data: 0x1c

   - /System/DriverKit/usr/lib/system/libdyld.dylib
   - /System/DriverKit/usr/lib/system/libsystem_kernel.dylib
   - /System/DriverKit/usr/lib/system/libsystem_platform.dylib
-  UUID: 233AD5EA-B9A7-30C4-B4A6-213C84A380C7
+  UUID: ADBF4546-8EDD-3E2A-8D7F-F0B0AB0288BF
   Functions: 306
   Symbols:   425
-  CStrings:  56
+  CStrings:  57
 
Functions:
~ _pthread_atfork : 828 -> 720
CStrings:
+ "BUG IN LIBPTHREAD: expected atfork to be inline"

```
