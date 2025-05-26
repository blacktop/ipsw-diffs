## libsystem_notify.dylib

> `/usr/lib/system/libsystem_notify.dylib`

```diff

-317.100.2.0.0
-  __TEXT.__text: 0x8fe0
+317.120.2.0.0
+  __TEXT.__text: 0x90e4
   __TEXT.__auth_stubs: 0x550
   __TEXT.__const: 0x118
-  __TEXT.__cstring: 0x862
+  __TEXT.__cstring: 0x893
   __TEXT.__dof_notify: 0x5a6
   __TEXT.__unwind_info: 0x48
   __DATA_CONST.__got: 0x50

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libxpc.dylib
-  Functions: 77
+  Functions: 80
   Symbols:   118
   CStrings:  68
 
CStrings:
+ "strncmp(name, SELF_PREFIX, SELF_PREFIX_LEN) && !(client_opts(globals) & NOTIFY_OPT_LOOPBACK)"
- "strncmp(name, SELF_PREFIX, SELF_PREFIX_LEN)"

```
