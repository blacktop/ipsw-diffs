## libremovefile.dylib

> `/usr/lib/system/libremovefile.dylib`

```diff

-75.80.1.0.0
-  __TEXT.__text: 0x1930
-  __TEXT.__auth_stubs: 0x2e0
-  __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x2f
-  __TEXT.__unwind_info: 0xa0
+81.0.0.0.0
+  __TEXT.__text: 0x2018
+  __TEXT.__auth_stubs: 0x300
+  __TEXT.__const: 0x50
+  __TEXT.__cstring: 0x2d
+  __TEXT.__unwind_info: 0xb0
   __DATA_CONST.__got: 0x10
-  __AUTH_CONST.__auth_got: 0x170
+  __AUTH_CONST.__auth_got: 0x180
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdyld.dylib
   - /usr/lib/system/libsystem_c.dylib
   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
-  UUID: D242539B-BA45-363C-8B08-83FBCE4EC1C2
-  Functions: 20
-  Symbols:   68
-  CStrings:  6
+  UUID: B0D1E2D8-62D3-38A3-AFA9-E44B4BAFF856
+  Functions: 21
+  Symbols:   74
+  CStrings:  5
 
Symbols:
+ ___removefile_tree_walker_slim
+ _check_error_cb
+ _dirfd
+ _iopolicy_materialization_on
+ _memmove
+ _move_to_parent_dir
+ _realloc
- _strcmp
CStrings:
+ "%s"
- "."
- ".."

```
