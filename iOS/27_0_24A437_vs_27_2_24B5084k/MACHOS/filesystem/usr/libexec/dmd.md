## dmd

> `/usr/libexec/dmd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-261.2.5.0.0
+267.0.0.0.0
   __TEXT.__text: 0x7faac
   __TEXT.__auth_stubs: 0xf60
   __TEXT.__objc_stubs: 0xea00
   __TEXT.__objc_methlist: 0x7fdc
-  __TEXT.__const: 0x180
+  __TEXT.__const: 0x178
   __TEXT.__objc_classname: 0x1e43
   __TEXT.__objc_methname: 0x118ed
   __TEXT.__objc_methtype: 0x1d98
```
