## libnetworkextension.dylib

> `/usr/lib/libnetworkextension.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-2322.0.0.0.1
-  __TEXT.__text: 0x3576c
+2331.0.0.0.1
+  __TEXT.__text: 0x3596c
   __TEXT.__objc_methlist: 0x2ac
   __TEXT.__const: 0x26c
   __TEXT.__cstring: 0x2f07

   __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0x60
-  __DATA.__bss: 0xd18
+  __DATA.__bss: 0xd20
   __DATA.__common: 0x3d
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x1b8
Functions:
~ _ne_url_filter_check : 1484 -> 1480
~ ___ne_url_filter_check_block_invoke : 1092 -> 1604
~ ___ne_filter_protocol_identifier_block_invoke : 408 -> 412
```
