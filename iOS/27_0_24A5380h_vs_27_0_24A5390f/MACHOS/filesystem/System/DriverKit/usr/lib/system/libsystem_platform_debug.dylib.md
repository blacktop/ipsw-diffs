## libsystem_platform_debug.dylib

> `/System/DriverKit/usr/lib/system/libsystem_platform_debug.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__AUTH_CONST.__const`
- `__DATA_DIRTY.__la_resolver`

```diff

-402.0.0.0.0
-  __TEXT.__text: 0xa7fc
+402.0.1.0.0
+  __TEXT.__text: 0xa72c
   __TEXT.__resolver_help: 0x288
-  __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x7f2
+  __TEXT.__const: 0xc0
+  __TEXT.__cstring: 0x795
   __TEXT.__unwind_info: 0x258
   __TEXT.__eh_frame: 0xd8
   __TEXT.__stubs: 0x48
-  __TEXT.__auth_stubs: 0x1c0
+  __TEXT.__auth_stubs: 0x1b0
   __DATA_CONST.__got: 0x10
   __AUTH_CONST.__const: 0x108
-  __AUTH_CONST.__auth_got: 0xe0
-  __DATA.__script_config: 0x8000
+  __AUTH_CONST.__auth_got: 0xd8
+  __DATA.__script_config: 0x4000
   __DATA.__crash_info: 0x148
   __DATA_DIRTY.__la_resolver: 0x30
   __DATA_DIRTY.__common: 0x14
   __TPRO_CONST.__data: 0x8
   - /System/DriverKit/usr/lib/system/libdyld.dylib
   - /System/DriverKit/usr/lib/system/libsystem_kernel.dylib
-  Functions: 265
-  Symbols:   312
-  CStrings:  56
+  Functions: 263
+  Symbols:   310
+  CStrings:  54
 
Symbols:
- ___restrictions_config
- _mach_vm_protect
CStrings:
- "BUG IN LIBPLATFORM: Failed to freeze config."
- "BUG IN LIBPLATFORM: Failed to reprotect config."
```
