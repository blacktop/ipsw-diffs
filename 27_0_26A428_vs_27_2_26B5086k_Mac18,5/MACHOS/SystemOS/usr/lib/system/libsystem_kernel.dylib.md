## libsystem_kernel.dylib

> `/usr/lib/system/libsystem_kernel.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__DATA.__data`
- `__DATA_DIRTY.__data`

```diff

-13432.1.9.0.0
-  __TEXT.__text: 0x3502c
-  __TEXT.__const: 0xcc0
+13432.40.144.0.1
+  __TEXT.__text: 0x350e8
+  __TEXT.__const: 0xcd0
   __TEXT.__cstring: 0x6a03
   __TEXT.__unwind_info: 0x15b8
   __DATA_CONST.__const: 0x2b90

   __DATA_DIRTY.__data: 0x18
   __DATA_DIRTY.__bss: 0x40
   __DATA_DIRTY.__common: 0x690
-  Functions: 1568
-  Symbols:   1747
+  Functions: 1570
+  Symbols:   1749
   CStrings:  995
 
Symbols:
+ _os_sme_engine_attr_count
+ _os_sme_engine_attr_read
```
