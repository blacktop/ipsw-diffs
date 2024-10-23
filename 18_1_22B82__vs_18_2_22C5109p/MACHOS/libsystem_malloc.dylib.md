## libsystem_malloc.dylib

> `/System/ExclaveKit/usr/lib/system/libsystem_malloc.dylib`

```diff

-646.40.3.0.0
-  __TEXT.__text: 0xd278
+657.60.19.0.0
+  __TEXT.__text: 0xd21c
   __TEXT.__auth_stubs: 0x1d0
-  __TEXT.__cstring: 0x1043
+  __TEXT.__cstring: 0x1036
   __TEXT.__const: 0x230
   __TEXT.__unwind_info: 0x310
   __TEXT.__eh_frame: 0x48

   - /System/ExclaveKit/usr/lib/system/libsystem_platform.dylib
   Functions: 253
   Symbols:   304
-  CStrings:  98
+  CStrings:  97
 
CStrings:
+ "Failed to allocate memory at address 0x%!l(MISSING)x of size 0x%!l(MISSING)x with flags %!d(MISSING): %!d(MISSING)\n"
+ "Failed to deallocate at address %!p(MISSING) of size 0x%!l(MISSING)x: %!d(MISSING)\n"
+ "Unsupported deallocation address %!p(MISSING) or size %!l(MISSING)u: %!d(MISSING)\n"
- "Failed to allocate memory at address 0x%!l(MISSING)x of size 0x%!l(MISSING)x with flags %!d(MISSING)\n"
- "Failed to deallocate at address %!p(MISSING) of size 0x%!l(MISSING)x\n"
- "Unsupported deallocation address %!p(MISSING) or size %!l(MISSING)u\n"
- "populate of chunk failed"

```
