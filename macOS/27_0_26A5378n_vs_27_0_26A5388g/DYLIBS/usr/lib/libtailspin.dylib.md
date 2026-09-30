## libtailspin.dylib

> `/usr/lib/libtailspin.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__DATA.__data`

```diff

   __AUTH_CONST.__objc_const: 0x3c0
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__auth_got: 0x7a0
-  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x44
   __DATA.__data: 0x10
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x6f0
+  __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x21a8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
```
