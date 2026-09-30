## libremovefile.dylib

> `/usr/lib/system/libremovefile.dylib`

```diff

-75.80.1.0.0
-  __TEXT.__text: 0x1964
-  __TEXT.__auth_stubs: 0x2e0
-  __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x2f
-  __TEXT.__unwind_info: 0xa8
+81.0.0.0.0
+  __TEXT.__text: 0x2078
+  __TEXT.__auth_stubs: 0x300
+  __TEXT.__const: 0x50
+  __TEXT.__cstring: 0x2d
+  __TEXT.__unwind_info: 0xb8
   __DATA_CONST.__got: 0x10
-  __AUTH_CONST.__auth_got: 0x170
+  __AUTH_CONST.__auth_got: 0x180
   __AUTH_CONST.__auth_ptr: 0x10
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdyld.dylib

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
-  Functions: 20
-  Symbols:   66
-  CStrings:  6
+  Functions: 21
+  Symbols:   72
+  CStrings:  5
 
Symbols:
+ ___removefile_tree_walker_slim
+ _dirfd
+ _malloc_type_realloc
+ _memmove
- _strcmp
CStrings:
+ "%s"
- "."
- ".."

```
