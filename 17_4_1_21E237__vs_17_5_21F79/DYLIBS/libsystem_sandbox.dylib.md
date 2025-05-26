## libsystem_sandbox.dylib

> `/usr/lib/system/libsystem_sandbox.dylib`

```diff

-2190.100.100.0.0
-  __TEXT.__text: 0x31e8
+2190.120.12.0.0
+  __TEXT.__text: 0x31ec
   __TEXT.__auth_stubs: 0x2f0
   __TEXT.__const: 0x138
   __TEXT.__cstring: 0x62e
-  __TEXT.__unwind_info: 0x1a4
+  __TEXT.__unwind_info: 0x1a0
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0x40
   __AUTH_CONST.__auth_got: 0x178

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
-  Functions: 130
-  Symbols:   224
+  Functions: 131
+  Symbols:   225
   CStrings:  57
 
Symbols:
+ __sandbox_enter_notify_libxpc

```
