## SpotlightDiagnostic

> `/System/Library/PrivateFrameworks/Search.framework/PlugIns/SpotlightDiagnostic.appex/SpotlightDiagnostic`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2459.105.0.0.0
-  __TEXT.__text: 0x1ea4
-  __TEXT.__auth_stubs: 0x3f0
+2465.1.2.0.0
+  __TEXT.__text: 0x1fe0
+  __TEXT.__auth_stubs: 0x3e0
   __TEXT.__objc_stubs: 0x8c0
   __TEXT.__objc_methlist: 0x5c
   __TEXT.__const: 0x88
-  __TEXT.__gcc_except_tab: 0x204
-  __TEXT.__cstring: 0x476
+  __TEXT.__gcc_except_tab: 0x21c
+  __TEXT.__cstring: 0x4d3
   __TEXT.__oslogstring: 0x598
   __TEXT.__objc_classname: 0x56
   __TEXT.__objc_methname: 0x649
   __TEXT.__objc_methtype: 0x73
   __TEXT.__unwind_info: 0xf8
   __DATA_CONST.__const: 0xf0
-  __DATA_CONST.__cfstring: 0x420
+  __DATA_CONST.__cfstring: 0x440
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0x208
+  __DATA_CONST.__auth_got: 0x200
   __DATA_CONST.__got: 0xb0
   __DATA.__objc_const: 0xb8
   __DATA.__objc_selrefs: 0x248

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 33
-  Symbols:   99
-  CStrings:  148
+  Symbols:   98
+  CStrings:  149
 
Symbols:
- _objc_retain_x26
Functions:
~ sub_100000d70 : 696 -> 728
~ sub_100001028 -> sub_100001048 : 4220 -> 4504
CStrings:
+ "^(build-history|CoreSpotlight-heartbeat|Spotlight_\\d{4}-\\d{2}-\\d{2}-\\d{2}-\\d{2}-\\d{2})\\.log$"
```
