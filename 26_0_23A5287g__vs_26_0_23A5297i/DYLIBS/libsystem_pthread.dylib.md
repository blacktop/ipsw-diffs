## libsystem_pthread.dylib

> `/usr/lib/system/libsystem_pthread.dylib`

```diff

-538.0.0.0.0
-  __TEXT.__text: 0xa500
+539.0.0.0.0
+  __TEXT.__text: 0xa4e4
   __TEXT.__auth_stubs: 0x450
   __TEXT.__const: 0x120
-  __TEXT.__cstring: 0xd7a
+  __TEXT.__cstring: 0xdaa
   __TEXT.__unwind_info: 0x340
   __DATA_CONST.__got: 0x30
   __AUTH_CONST.__auth_got: 0x228

   - /usr/lib/system/libmacho.dylib
   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_platform.dylib
-  UUID: 1B889397-32B5-3C1B-B3CB-B3FB9A70A1B2
-  Functions: 310
-  Symbols:   598
-  CStrings:  65
+  UUID: A9A3DF7E-4736-378E-9851-0BD28321E760
+  Functions: 311
+  Symbols:   600
+  CStrings:  66
 
Symbols:
+ _pthread_atfork.cold.1
Functions:
~ _pthread_atfork : 488 -> 420
+ _pthread_dependency_wait_np.cold.2
CStrings:
+ "BUG IN LIBPTHREAD: expected atfork to be inline"

```
