## libmrc.dylib

> `/usr/lib/libmrc.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__DATA.__data`

```diff

-3089.0.0.0.1
+3109.0.0.0.0
   __TEXT.__text: 0x6424
   __TEXT.__objc_methlist: 0x14c
   __TEXT.__cstring: 0x70f

   __AUTH_CONST.__const: 0x788
   __AUTH_CONST.__objc_const: 0xf58
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x320
   __DATA.__data: 0x5a0
   __DATA.__bss: 0x28
-  __DATA_DIRTY.__objc_data: 0x140
+  __DATA_DIRTY.__objc_data: 0x460
   __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /usr/lib/libSystem.B.dylib
```
