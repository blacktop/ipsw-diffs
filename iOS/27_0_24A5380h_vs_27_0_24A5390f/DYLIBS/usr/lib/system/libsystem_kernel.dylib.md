## libsystem_kernel.dylib

> `/usr/lib/system/libsystem_kernel.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__DATA.__data`
- `__DATA_DIRTY.__data`

```diff

-13432.0.50.502.2
-  __TEXT.__text: 0x34f00
+13432.0.94.502.2
+  __TEXT.__text: 0x34f30
   __TEXT.__const: 0xc90
   __TEXT.__cstring: 0x5cda
-  __TEXT.__unwind_info: 0x11f8
+  __TEXT.__unwind_info: 0x1200
   __DATA_CONST.__const: 0x28d8
   __AUTH_CONST.__const: 0x150
   __DATA.__crash_info: 0x148

   __DATA_DIRTY.__data: 0x18
   __DATA_DIRTY.__bss: 0x38
   __DATA_DIRTY.__common: 0x680
-  Functions: 1555
-  Symbols:   1725
+  Functions: 1556
+  Symbols:   1726
   CStrings:  915
 
Symbols:
+ _os_cross_arch_is_supported
Functions:
+ _os_cross_arch_is_supported
```
