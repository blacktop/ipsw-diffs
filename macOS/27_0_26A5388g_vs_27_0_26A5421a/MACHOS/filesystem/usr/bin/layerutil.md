## layerutil

> `/usr/bin/layerutil`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-1008.0.0.0.0
-  __TEXT.__text: 0xa61a8
+1010.0.0.0.0
+  __TEXT.__text: 0xa61bc
   __TEXT.__auth_stubs: 0x2440
   __TEXT.__objc_stubs: 0xbee0
   __TEXT.__objc_methlist: 0x7dc0
   __TEXT.__const: 0x2c68
   __TEXT.__gcc_except_tab: 0x1a80
-  __TEXT.__objc_methname: 0x12289
+  __TEXT.__objc_methname: 0x12293
   __TEXT.__objc_classname: 0x119f
   __TEXT.__objc_methtype: 0x4411
   __TEXT.__cstring: 0x1032e

   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x20
-  __TEXT.__unwind_info: 0x2e48
+  __TEXT.__unwind_info: 0x2e50
   __DATA_CONST.__const: 0x49b8
   __DATA_CONST.__cfstring: 0x4b00
   __DATA_CONST.__objc_classlist: 0x420
Functions:
~ sub_10004d5a4 : 300 -> 320
CStrings:
+ "themeNamed:forBundleIdentifier:error:"
- "themeNamed:forBundle:error:"
```
