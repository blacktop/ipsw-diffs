## MallocStackLogging

> `/System/Library/PrivateFrameworks/MallocStackLogging.framework/MallocStackLogging`

```diff

-64572.129.1.0.0
-  __TEXT.__text: 0x9140
+64572.134.1.0.0
+  __TEXT.__text: 0x9150
   __TEXT.__auth_stubs: 0x6c0
   __TEXT.__const: 0x138
-  __TEXT.__cstring: 0x1f73
+  __TEXT.__cstring: 0x1fb6
   __TEXT.__unwind_info: 0x288
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__const: 0x98

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_sandbox.dylib
-  UUID: 0645DC98-D25D-35EB-851F-FB9C8EC6B987
+  UUID: E8DE710C-A81C-3D80-A3E1-8F98EFA3E2CF
   Functions: 228
   Symbols:   582
-  CStrings:  207
+  CStrings:  208
 
Functions:
~ _create_lite_zone_if_has_default_zone0 : 140 -> 156
CStrings:
+ "malloc_msl_lite_hooks not initialized so can't turn on lite mode.\n"

```
