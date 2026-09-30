## libsystem_trial.dylib

> `/usr/lib/system/libsystem_trial.dylib`

```diff

-463.0.0.0.0
-  __TEXT.__text: 0x2b0
-  __TEXT.__auth_stubs: 0x60
+466.0.0.0.0
+  __TEXT.__text: 0x2f8
+  __TEXT.__auth_stubs: 0x70
   __TEXT.__const: 0x40
   __TEXT.__cstring: 0xee
-  __TEXT.__unwind_info: 0x60
-  __AUTH_CONST.__auth_got: 0x30
+  __TEXT.__unwind_info: 0x58
+  __AUTH_CONST.__auth_got: 0x38
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdispatch.dylib
   - /usr/lib/system/libsystem_blocks.dylib

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 054D48E6-D2FB-35DB-97A3-02B403256D8D
+  UUID: FCD28DB9-D40D-361B-9B0D-E06052EBF2E4
   Functions: 3
-  Symbols:   12
+  Symbols:   13
   CStrings:  11
 
Symbols:
+ _free
+ _getenv_copy_np
- _getenv
Functions:
~ __os_trial_factor_get_bool_impl : 192 -> 212
~ __os_trial_factor_get_long_impl : 352 -> 372
~ __os_trial_factor_has_impl : 144 -> 176

```
