## AppInFocus

> `/System/Library/Trace/PassiveDataSources/AppInFocus.bundle/AppInFocus`

```diff

-134.120.2.0.0
-  __TEXT.__text: 0xc0c
-  __TEXT.__auth_stubs: 0x270
+188.0.0.0.0
+  __TEXT.__text: 0xb9c
+  __TEXT.__auth_stubs: 0x2a0
   __TEXT.__objc_stubs: 0x440
   __TEXT.__objc_methlist: 0xc8
   __TEXT.__const: 0x60
-  __TEXT.__gcc_except_tab: 0x6c
+  __TEXT.__gcc_except_tab: 0x74
   __TEXT.__cstring: 0x1a6
   __TEXT.__objc_classname: 0x3f
   __TEXT.__objc_methname: 0x2d3
   __TEXT.__objc_methtype: 0x141
   __TEXT.__oslogstring: 0x68
   __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__auth_got: 0x148
-  __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x90
   __DATA_CONST.__cfstring: 0x1c0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x160
+  __DATA_CONST.__got: 0x58
   __DATA.__objc_const: 0x150
   __DATA.__objc_selrefs: 0x138
   __DATA.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/ktrace.framework/ktrace
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EBD10470-5854-3934-84C6-B8925302BA4B
+  UUID: 915497E1-A4AA-3C22-AC6E-8B3AB290B1F5
   Functions: 13
-  Symbols:   63
+  Symbols:   66
   CStrings:  87
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x26
+ _objc_retain_x3
+ _objc_retain_x5
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x24
- _objc_retain_x27
Functions:
~ sub_cd0 : 152 -> 144
~ sub_d68 -> sub_d60 : 832 -> 760
~ sub_10b4 -> sub_1064 : 1192 -> 1204
~ sub_155c -> sub_1518 : 208 -> 200
~ sub_1650 -> sub_1604 : 216 -> 208
~ sub_1728 -> sub_16d4 : 84 -> 68
~ sub_177c -> sub_1718 : 264 -> 252

```
