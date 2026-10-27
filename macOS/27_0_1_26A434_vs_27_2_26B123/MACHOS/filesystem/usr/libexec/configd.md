## configd

> `/usr/libexec/configd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1446.0.0.0.0
-  __TEXT.__text: 0x6be88
-  __TEXT.__auth_stubs: 0x2450
+1453.40.1.0.0
+  __TEXT.__text: 0x6bf80
+  __TEXT.__auth_stubs: 0x2460
   __TEXT.__objc_stubs: 0x1600
   __TEXT.__objc_methlist: 0xb64
   __TEXT.__const: 0x248
   __TEXT.__cstring: 0x3261
-  __TEXT.__oslogstring: 0x59ea
+  __TEXT.__oslogstring: 0x5a2c
   __TEXT.__objc_methname: 0x1c8d
   __TEXT.__objc_classname: 0x73
   __TEXT.__objc_methtype: 0x672

   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
-  __DATA_CONST.__auth_got: 0x1238
+  __DATA_CONST.__auth_got: 0x1240
   __DATA_CONST.__got: 0x710
   __DATA_CONST.__auth_ptr: 0x108
   __DATA.__objc_const: 0xde8

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 999
-  Symbols:   819
-  CStrings:  1775
+  Symbols:   820
+  CStrings:  1776
 
Symbols:
+ _nw_resolver_config_set_interface_name
Functions:
~ sub_10004c590 : 1372 -> 1588
~ sub_1000517e8 -> sub_1000518c0 : 536 -> 568
CStrings:
+ "NetBIOS name: ptr query reply w/no hosts (query time = %ld.%3.3d)"
```
