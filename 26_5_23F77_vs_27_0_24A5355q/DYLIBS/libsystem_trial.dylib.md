## libsystem_trial.dylib

> `/usr/lib/system/libsystem_trial.dylib`

```diff

-474.2.18.2.0
-  __TEXT.__text: 0x2f4
-  __TEXT.__auth_stubs: 0x70
-  __TEXT.__const: 0x48
-  __TEXT.__cstring: 0xee
-  __TEXT.__unwind_info: 0x58
-  __AUTH_CONST.__auth_got: 0x38
+501.0.0.0.0
+  __TEXT.__text: 0x238
+  __TEXT.__const: 0x38
+  __TEXT.__cstring: 0x83
+  __TEXT.__unwind_info: 0x60
+  __TEXT.__auth_stubs: 0x0
+  __AUTH_CONST.__auth_got: 0x0
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdispatch.dylib
   - /usr/lib/system/libsystem_blocks.dylib

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: EC123CD7-F34A-3987-A6FF-931E44A7E84A
-  Functions: 3
-  Symbols:   13
-  CStrings:  11
+  UUID: B6FF2127-D8F3-3798-908C-D69046F79F52
+  Functions: 4
+  Symbols:   14
+  CStrings:  6
 
Symbols:
+ <redacted>
+ __os_trial_factor_get_long_long_impl
+ _after_strstr
+ _strlen
+ _strstr
- _MAX_FACTOR_STRING_LENGTH
- __os_trial_factor_get_long_impl
- _strnlen
- _strnstr
CStrings:
+ "_os_trial_factor_get_long_long_impl"
+ "trial_factor_private_impl.c"
- "_os_trial_factor_get_bool_impl"
- "_os_trial_factor_get_long_impl"
- "consumed_so_far <= MAX_FACTOR_STRING_LENGTH"
- "level >= factors"
- "search_false"
- "search_true"
- "trial_factor_private.c"

```
