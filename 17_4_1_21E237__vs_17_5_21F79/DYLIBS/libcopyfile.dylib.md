## libcopyfile.dylib

> `/usr/lib/system/libcopyfile.dylib`

```diff

-196.100.4.0.0
-  __TEXT.__text: 0x6910
+196.120.5.0.0
+  __TEXT.__text: 0x6b2c
   __TEXT.__auth_stubs: 0x640
   __TEXT.__const: 0x1c0
-  __TEXT.__cstring: 0x1751
+  __TEXT.__cstring: 0x17b2
   __TEXT.__unwind_info: 0xcc
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__const: 0x3b0
+  __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__auth_got: 0x320
   __DATA.__data: 0x8
-  __DATA_DIRTY.__const: 0xe0
+  __DATA_DIRTY.__const: 0x40
   __DATA_DIRTY.__bss: 0x10
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdispatch.dylib

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: A3D43030-37DB-3F4C-AF17-F4B162A16682
+  UUID: 6E04BBFD-BE21-3FD0-B14F-FA19AE565CD6
   Functions: 35
   Symbols:   180
-  CStrings:  175
+  CStrings:  177
 
CStrings:
+ "Cannot lstat destination %s: %m"
+ "Destination %s already exists as a symlink, refusing to copy: %m"

```
