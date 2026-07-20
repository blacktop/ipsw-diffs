## libate.dylib

> `/usr/lib/libate.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

   __AUTH_CONST.__weak_auth_got: 0x8
   __AUTH_CONST.__auth_got: 0x148
   __DATA.__data: 0xc0
-  __DATA.__bss: 0xa0
+  __DATA.__bss: 0x148
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__common: 0x8
-  __DATA_DIRTY.__bss: 0x3d0
+  __DATA_DIRTY.__bss: 0x328
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
```
