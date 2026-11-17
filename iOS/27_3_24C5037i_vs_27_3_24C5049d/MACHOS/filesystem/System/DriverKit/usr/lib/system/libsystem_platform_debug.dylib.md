## libsystem_platform_debug.dylib

> `/System/DriverKit/usr/lib/system/libsystem_platform_debug.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__eh_frame`
- `__AUTH_CONST.__const`
- `__DATA_DIRTY.__la_resolver`

```diff

-402.40.3.0.0
-  __TEXT.__text: 0xa5dc
+402.60.2.0.0
+  __TEXT.__text: 0xa65c
   __TEXT.__resolver_help: 0x288
   __TEXT.__const: 0xc0
   __TEXT.__cstring: 0x795
-  __TEXT.__unwind_info: 0x320
+  __TEXT.__unwind_info: 0x328
   __TEXT.__eh_frame: 0xd8
   __TEXT.__stubs: 0x48
   __TEXT.__auth_stubs: 0x1b0

   __TPRO_CONST.__data: 0x8
   - /System/DriverKit/usr/lib/system/libdyld.dylib
   - /System/DriverKit/usr/lib/system/libsystem_kernel.dylib
-  Functions: 263
-  Symbols:   297
+  Functions: 267
+  Symbols:   301
   CStrings:  54
 
Symbols:
+ _os_unfair_recursive_lock_assert_not_owned_by_self
+ _os_unfair_recursive_lock_assert_owned_by_self
+ _os_unfair_recursive_lock_lock
+ _os_unfair_recursive_lock_lock_with_flags
```
