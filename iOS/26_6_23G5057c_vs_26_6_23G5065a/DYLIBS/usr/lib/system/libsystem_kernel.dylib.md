## libsystem_kernel.dylib

> `/usr/lib/system/libsystem_kernel.dylib`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__DATA.__data`
- `__DATA_DIRTY.__data`

```diff

-  __TEXT.__text: 0x33f4c
-  __TEXT.__const: 0xc60
+  __TEXT.__text: 0x33f7c
+  __TEXT.__const: 0xc50
   __TEXT.__cstring: 0x5ccf
-  __TEXT.__unwind_info: 0xb18
+  __TEXT.__unwind_info: 0xb20
   __DATA_CONST.__const: 0x28d0
   __AUTH_CONST.__const: 0x150
   __DATA.__crash_info: 0x148

   __DATA_DIRTY.__data: 0x18
   __DATA_DIRTY.__bss: 0x38
   __DATA_DIRTY.__common: 0x680
-  Functions: 1526
-  Symbols:   1695
+  Functions: 1527
+  Symbols:   1696
   CStrings:  914
 
Symbols:
+ _os_cross_arch_is_supported
Functions:
+ _os_cross_arch_is_supported
```
