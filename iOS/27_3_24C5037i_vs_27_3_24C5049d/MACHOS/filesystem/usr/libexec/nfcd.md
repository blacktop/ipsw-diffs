## nfcd

> `/usr/libexec/nfcd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-372.4.1.0.0
+372.5.0.0.0
   __TEXT.__text: 0x1eab94
   __TEXT.__auth_stubs: 0x1930
   __TEXT.__delay_stubs: 0x540

   __TEXT.__objc_stubs: 0xe3a0
   __TEXT.__objc_methlist: 0x9fcc
   __TEXT.__const: 0x143c
-  __TEXT.__cstring: 0x230f7
+  __TEXT.__cstring: 0x230f5
   __TEXT.__oslogstring: 0x20c6a
   __TEXT.__objc_classname: 0x1d7c
   __TEXT.__objc_methname: 0x15fb1
CStrings:
+ "NFCD built from (B&I) Stockholm_Base-372.5"
- "NFCD built from (B&I) Stockholm_Base-372.4.1"
```
