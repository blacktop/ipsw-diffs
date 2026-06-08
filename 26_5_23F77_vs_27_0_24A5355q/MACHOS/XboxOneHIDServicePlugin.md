## XboxOneHIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/XboxOneHIDServicePlugin.plugin/XboxOneHIDServicePlugin`

```diff

-13.5.1.0.0
-  __TEXT.__text: 0x15f0
-  __TEXT.__auth_stubs: 0x1f0
+14.0.14.0.0
+  __TEXT.__text: 0x1548
+  __TEXT.__auth_stubs: 0x200
   __TEXT.__objc_stubs: 0x3e0
   __TEXT.__objc_methlist: 0x284
   __TEXT.__const: 0x5c
   __TEXT.__gcc_except_tab: 0x28
   __TEXT.__cstring: 0xe2
-  __TEXT.__oslogstring: 0x1e5
   __TEXT.__objc_methname: 0x695
+  __TEXT.__oslogstring: 0x1e5
   __TEXT.__objc_classname: 0x32
   __TEXT.__objc_methtype: 0x2c5
-  __TEXT.__unwind_info: 0xb0
-  __DATA_CONST.__auth_got: 0x108
-  __DATA_CONST.__got: 0x30
+  __TEXT.__unwind_info: 0xa8
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__cfstring: 0x1a0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__objc_dictobj: 0xa0
+  __DATA_CONST.__auth_got: 0x110
+  __DATA_CONST.__got: 0x30
   __DATA.__objc_const: 0x358
   __DATA.__objc_selrefs: 0x240
   __DATA.__objc_ivar: 0x20

   - /System/Library/PrivateFrameworks/HID.framework/HID
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 89224331-6DC7-304F-8F02-A1EDDDE3F3CA
+  UUID: 4C53728F-9968-305D-8374-7203844D3733
   Functions: 20
-  Symbols:   50
+  Symbols:   51
   CStrings:  171
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x5
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x21
Functions:
~ sub_e20 : 84 -> 68
~ sub_eb8 -> sub_ea8 : 416 -> 464
~ sub_1058 -> sub_1078 : 1536 -> 1440
~ sub_1744 -> sub_1704 : 304 -> 296
~ sub_1874 -> sub_182c : 1492 -> 1472
~ sub_1e48 -> sub_1dec : 348 -> 304
~ sub_1fd4 -> sub_1f4c : 608 -> 576

```
