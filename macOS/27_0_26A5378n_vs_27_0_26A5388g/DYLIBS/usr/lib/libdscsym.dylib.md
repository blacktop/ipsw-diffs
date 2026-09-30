## libdscsym.dylib

> `/usr/lib/libdscsym.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_selrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`

```diff

-436.0.0.0.0
+438.0.0.0.0
   __TEXT.__text: 0x4afc
   __TEXT.__const: 0xb0
   __TEXT.__gcc_except_tab: 0x1a4

   __AUTH_CONST.__const: 0x230
   __AUTH_CONST.__cfstring: 0x180
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__bss: 0x10
+  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
```
