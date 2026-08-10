## libdispatch_profile.dylib

> `/System/DriverKit/usr/lib/system/libdispatch_profile.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__dof_dispatch`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__auth_got`
- `__AUTH.__data`

```diff

-1605.0.1.0.0
-  __TEXT.__text: 0x496cc
+1605.0.2.0.0
+  __TEXT.__text: 0x496dc
   __TEXT.__const: 0x7a0
   __TEXT.__cstring: 0x6493
   __TEXT.__dof_dispatch: 0x4712
-  __TEXT.__dof_voucher: 0x2d6a
+  __TEXT.__dof_voucher: 0x2d71
   __TEXT.__unwind_info: 0xdb0
   __TEXT.__auth_stubs: 0xb60
   __DATA_CONST.__const: 0x738

   - /System/DriverKit/usr/lib/system/libsystem_malloc.dylib
   - /System/DriverKit/usr/lib/system/libsystem_platform.dylib
   - /System/DriverKit/usr/lib/system/libsystem_pthread.dylib
-  Functions: 1366
+  Functions: 1367
   Symbols:   1672
   CStrings:  517
 
Functions:
~ __dispatch_block_sync_invoke : 512 -> 372
~ _OUTLINED_FUNCTION_42 : 12 -> 20
~ _OUTLINED_FUNCTION_43 : 20 -> 12
+ _dispatch_block_sync_invoke.cold.3
```
