## libsystem_sandbox.dylib

> `/usr/lib/system/libsystem_sandbox.dylib`

```diff

-2680.100.172.0.0
-  __TEXT.__text: 0x36d0
-  __TEXT.__auth_stubs: 0x360
+2680.100.174.0.0
+  __TEXT.__text: 0x38ac
+  __TEXT.__auth_stubs: 0x370
   __TEXT.__const: 0x178
-  __TEXT.__cstring: 0x747
-  __TEXT.__unwind_info: 0x1c0
+  __TEXT.__cstring: 0x77f
+  __TEXT.__unwind_info: 0x1d0
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0x60
-  __AUTH_CONST.__auth_got: 0x1b0
+  __AUTH_CONST.__auth_got: 0x1b8
   __AUTH_CONST.__const: 0x20
   __DATA.__data: 0x13
   __DATA.__bss: 0x10

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
-  UUID: BB8AED94-2B18-3ACA-85F8-AD8C309EA030
-  Functions: 131
-  Symbols:   251
-  CStrings:  67
+  UUID: C5B2C13A-5DC8-372D-BB92-4E244189A4FD
+  Functions: 135
+  Symbols:   256
+  CStrings:  70
 
Symbols:
+ _sandbox_check_network
+ _sandbox_checkattr_alloc
+ _sandbox_checkattr_disable_reporting
+ _sandbox_checkattr_free
+ _strncmp
CStrings:
+ "%s: failed to allocate"
+ "network-"
+ "sandbox_checkattr_alloc"

```
