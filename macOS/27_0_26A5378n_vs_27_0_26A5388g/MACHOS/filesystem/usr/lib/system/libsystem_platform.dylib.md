## libsystem_platform.dylib

> `/usr/lib/system/libsystem_platform.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__AUTH_CONST.__const`
- `__DATA_DIRTY.__la_resolver`

```diff

-402.0.0.0.0
-  __TEXT.__text: 0x7e08
+402.0.1.0.0
+  __TEXT.__text: 0x7d44
   __TEXT.__resolver_help: 0x288
-  __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x8a1
+  __TEXT.__const: 0xb0
+  __TEXT.__cstring: 0x844
   __TEXT.__unwind_info: 0x2c8
   __TEXT.__stubs: 0x48
-  __TEXT.__auth_stubs: 0x250
+  __TEXT.__auth_stubs: 0x240
   __DATA_CONST.__got: 0x20
   __AUTH_CONST.__const: 0x108
-  __AUTH_CONST.__auth_got: 0x128
-  __DATA.__script_config: 0x8000
+  __AUTH_CONST.__auth_got: 0x120
+  __DATA.__script_config: 0x4000
   __DATA.__crash_info: 0x148
   __DATA_DIRTY.__la_resolver: 0x30
   __DATA_DIRTY.__common: 0x18
   __TPRO_CONST.__data: 0x8
   - /usr/lib/system/libdyld.dylib
   - /usr/lib/system/libsystem_kernel.dylib
-  Functions: 280
-  Symbols:   340
-  CStrings:  70
+  Functions: 278
+  Symbols:   338
+  CStrings:  68
 
Symbols:
- ___restrictions_config
- _mach_vm_protect
CStrings:
- "BUG IN LIBPLATFORM: Failed to freeze config."
- "BUG IN LIBPLATFORM: Failed to reprotect config."
```
