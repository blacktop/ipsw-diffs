## assetutil

> `/usr/bin/assetutil`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-1008.0.0.0.0
+1010.0.0.0.0
   __TEXT.__text: 0xe8250
   __TEXT.__auth_stubs: 0x2710
   __TEXT.__objc_stubs: 0xbb20
   __TEXT.__objc_methlist: 0x7290
   __TEXT.__const: 0x74e18
   __TEXT.__gcc_except_tab: 0x1338
-  __TEXT.__objc_methname: 0x11478
+  __TEXT.__objc_methname: 0x11482
   __TEXT.__objc_classname: 0x1071
   __TEXT.__objc_methtype: 0x41f1
   __TEXT.__cstring: 0x153cb

   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x20
-  __TEXT.__unwind_info: 0x29c8
+  __TEXT.__unwind_info: 0x29d0
   __TEXT.__eh_frame: 0x2fc
   __DATA_CONST.__const: 0x5350
   __DATA_CONST.__cfstring: 0x8140
Functions:
~ sub_10002af50 : 300 -> 320
~ sub_100086144 -> sub_100086158 : 124 -> 104
CStrings:
+ "themeNamed:forBundleIdentifier:error:"
- "themeNamed:forBundle:error:"
```
