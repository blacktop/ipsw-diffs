## libsystem_platform.dylib

> `/usr/lib/system/libsystem_platform.dylib`

### Sections with Same Size but Changed Content

- `__AUTH_CONST.__const`
- `__DATA_DIRTY.__la_resolver`

```diff

-402.0.0.0.0
-  __TEXT.__text: 0x6fdc
+402.0.1.0.0
+  __TEXT.__text: 0x6eec
   __TEXT.__resolver_help: 0x288
-  __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x872
-  __TEXT.__unwind_info: 0x318
+  __TEXT.__const: 0xb0
+  __TEXT.__cstring: 0x815
+  __TEXT.__unwind_info: 0x310
   __TEXT.__stubs: 0x48
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x108
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__script_config: 0x8000
+  __DATA.__script_config: 0x4000
   __DATA.__crash_info: 0x148
   __DATA_DIRTY.__la_resolver: 0x30
   __DATA_DIRTY.__common: 0x18
   __TPRO_CONST.__data: 0x8
   - /usr/lib/system/libdyld.dylib
   - /usr/lib/system/libsystem_kernel.dylib
-  Functions: 290
-  Symbols:   325
-  CStrings:  69
+  Functions: 287
+  Symbols:   322
+  CStrings:  67
 
Symbols:
- ___restrictions_config
- __freeze_restrictions_config
- _mach_vm_protect
CStrings:
- "BUG IN LIBPLATFORM: Failed to freeze config."
- "BUG IN LIBPLATFORM: Failed to reprotect config."
```
