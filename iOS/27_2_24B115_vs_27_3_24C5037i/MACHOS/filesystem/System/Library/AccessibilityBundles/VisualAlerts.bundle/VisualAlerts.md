## VisualAlerts

> `/System/Library/AccessibilityBundles/VisualAlerts.bundle/VisualAlerts`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-3245.8.9.0.0
-  __TEXT.__text: 0x814
+3245.8.14.0.0
+  __TEXT.__text: 0x98c
   __TEXT.__auth_stubs: 0x160
   __TEXT.__objc_stubs: 0x140
   __TEXT.__objc_methlist: 0x19c
   __TEXT.__const: 0x8
-  __TEXT.__gcc_except_tab: 0xdc
-  __TEXT.__cstring: 0x271
+  __TEXT.__gcc_except_tab: 0xf4
+  __TEXT.__ustring: 0xfa
   __TEXT.__oslogstring: 0xb
+  __TEXT.__cstring: 0x271
   __TEXT.__objc_classname: 0x53
   __TEXT.__objc_methname: 0x276
   __TEXT.__objc_methtype: 0xc8
   __TEXT.__unwind_info: 0x88
-  __DATA_CONST.__cfstring: 0x100
+  __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libobjc.A.dylib
   Functions: 6
   Symbols:   39
-  CStrings:  73
+  CStrings:  75
 
Functions:
~ sub_c68 -> sub_cb8 : 892 -> 1080
~ sub_fe4 -> sub_10f0 : 892 -> 1080
CStrings:
+ "ERROR: turnTorchOff called with nil capture device — skipping."
+ "ERROR: turnTorchOn called with nil capture device — skipping."
```
