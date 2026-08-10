## misd

> `/usr/libexec/misd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-399.0.0.0.0
-  __TEXT.__text: 0x21e14
+401.0.0.0.0
+  __TEXT.__text: 0x21f14
   __TEXT.__auth_stubs: 0x1250
   __TEXT.__objc_stubs: 0x4e0
   __TEXT.__objc_methlist: 0x39c

   __TEXT.__objc_methname: 0x915
   __TEXT.__objc_classname: 0x74
   __TEXT.__objc_methtype: 0x6b7
-  __TEXT.__unwind_info: 0x500
+  __TEXT.__unwind_info: 0x508
   __DATA_CONST.__const: 0xa18
   __DATA_CONST.__cfstring: 0xba0
   __DATA_CONST.__objc_classlist: 0x10

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 456
+  Functions: 457
   Symbols:   393
   CStrings:  1758
 
```
