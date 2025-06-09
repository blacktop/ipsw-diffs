## SafetyServiceFilter

> `/System/Library/HIDPlugins/ServiceFilters/SafetyServiceFilter.plugin/SafetyServiceFilter`

```diff

-125.0.17.0.0
+143.0.0.0.0
   __TEXT.__text: 0xc34
   __TEXT.__auth_stubs: 0x250
   __TEXT.__objc_stubs: 0xe0
-  __TEXT.__objc_methlist: 0x25c
+  __TEXT.__objc_methlist: 0x274
   __TEXT.__const: 0x38
   __TEXT.__gcc_except_tab: 0x3c
   __TEXT.__oslogstring: 0x171
   __TEXT.__cstring: 0xbe
-  __TEXT.__objc_methname: 0x2ff
+  __TEXT.__objc_methname: 0x33a
   __TEXT.__objc_classname: 0x31
-  __TEXT.__objc_methtype: 0x2db
+  __TEXT.__objc_methtype: 0x349
   __TEXT.__unwind_info: 0x98
   __DATA_CONST.__auth_got: 0x138
   __DATA_CONST.__got: 0x38

   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x2f8
-  __DATA.__objc_selrefs: 0x148
+  __DATA.__objc_const: 0x308
+  __DATA.__objc_selrefs: 0x158
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x2e0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F238C8A8-2404-3534-82E7-E24ECF476E63
+  UUID: 5C2173DE-85CA-33A6-A736-4FB2C3B143E4
   Functions: 17
   Symbols:   54
-  CStrings:  116
+  CStrings:  121
 
Functions:
~ sub_b98 : 8 -> 228
~ sub_ba0 -> sub_c7c : 228 -> 200
~ sub_c84 -> sub_d44 : 200 -> 116
~ sub_d4c -> sub_db8 : 116 -> 12
~ sub_dc0 -> sub_dc4 : 12 -> 148
~ sub_dcc -> sub_e58 : 148 -> 8
CStrings:
+ "@\"HIDEvent\"32@0:8@\"HIDEvent\"16@\"HIDConnection\"24"
+ "filterEvent:forClient:"
+ "filterSetProperty:forKey:forClient:"
+ "v40@0:8^@16@\"NSString\"24@\"HIDConnection\"32"
+ "v40@0:8^@16@24@32"

```
