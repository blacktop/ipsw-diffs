## libchannel.dylib

> `/usr/lib/libchannel.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`

```diff

-59.0.0.0.0
+59.0.1.0.0
   __TEXT.__text: 0x3178
   __TEXT.__objc_methlist: 0x74
   __TEXT.__const: 0x28

   __AUTH_CONST.__objc_const: 0x240
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x140
+  __DATA_DIRTY.__objc_data: 0x140
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
```
