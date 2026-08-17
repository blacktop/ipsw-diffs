## ReplayKitModule

> `/System/Library/ControlCenter/Bundles/ReplayKitModule.bundle/ReplayKitModule`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-740.63.1.1.0
-  __TEXT.__text: 0xbf6c
-  __TEXT.__auth_stubs: 0x530
-  __TEXT.__objc_stubs: 0x20e0
+740.63.1.2.0
+  __TEXT.__text: 0xbf94
+  __TEXT.__auth_stubs: 0x540
+  __TEXT.__objc_stubs: 0x2100
   __TEXT.__objc_methlist: 0xde0
   __TEXT.__const: 0xc0
   __TEXT.__cstring: 0x1fcf
-  __TEXT.__objc_methname: 0x307a
+  __TEXT.__objc_methname: 0x3089
   __TEXT.__oslogstring: 0x1049
   __TEXT.__objc_classname: 0x178
   __TEXT.__objc_methtype: 0x967

   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
-  __DATA_CONST.__auth_got: 0x2a8
+  __DATA_CONST.__auth_got: 0x2b0
   __DATA_CONST.__got: 0x170
   __DATA.__objc_const: 0x1ef8
-  __DATA.__objc_selrefs: 0xca8
+  __DATA.__objc_selrefs: 0xcb0
   __DATA.__objc_ivar: 0xd4
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x2a0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 244
-  Symbols:   153
+  Symbols:   154
   CStrings:  829
 
Symbols:
+ _objc_opt_respondsToSelector
Functions:
~ sub_b56c : 140 -> 116
~ sub_b5f8 -> sub_b5e0 : 416 -> 480
CStrings:
+ "presentationInterfaceOrientation"
- "_geometryProvider"
```
