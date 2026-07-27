## libsystem_kernel.dylib

> `/usr/lib/system/libsystem_kernel.dylib`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__DATA.__data`
- `__DATA_DIRTY.__data`

```diff

-12377.160.73.0.5
-  __TEXT.__text: 0x3495c
-  __TEXT.__const: 0xca8
+12377.161.13.0.0
+  __TEXT.__text: 0x3498c
+  __TEXT.__const: 0xc98
   __TEXT.__cstring: 0x69f8
-  __TEXT.__unwind_info: 0xb00
+  __TEXT.__unwind_info: 0xb08
   __DATA_CONST.__const: 0x2b88
   __AUTH_CONST.__const: 0x150
   __DATA.__crash_info: 0x148

   __DATA_DIRTY.__data: 0x18
   __DATA_DIRTY.__bss: 0x38
   __DATA_DIRTY.__common: 0x688
-  Functions: 1538
-  Symbols:   1716
+  Functions: 1539
+  Symbols:   1717
   CStrings:  994
 
Symbols:
+ _os_cross_arch_is_supported
Functions:
+ _os_cross_arch_is_supported
```
