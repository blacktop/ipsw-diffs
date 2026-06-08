## Symbolication

> `/System/Library/Trace/Providers/Symbolication.bundle/Symbolication`

```diff

-134.120.2.0.0
-  __TEXT.__text: 0x5f4
-  __TEXT.__auth_stubs: 0x1a0
+188.0.0.0.0
+  __TEXT.__text: 0x5d0
+  __TEXT.__auth_stubs: 0x190
   __TEXT.__objc_stubs: 0x100
   __TEXT.__objc_methlist: 0x13c
   __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__cstring: 0x176
+  __TEXT.__cstring: 0x178
   __TEXT.__objc_methname: 0x29d
-  __TEXT.__objc_classname: 0x2a
+  __TEXT.__objc_classname: 0x28
   __TEXT.__objc_methtype: 0x1cd
-  __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__auth_got: 0xe0
-  __DATA_CONST.__got: 0x30
+  __TEXT.__unwind_info: 0x98
   __DATA_CONST.__const: 0x60
   __DATA_CONST.__cfstring: 0x180
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__auth_got: 0xd8
+  __DATA_CONST.__got: 0x30
   __DATA.__objc_const: 0x188
   __DATA.__objc_selrefs: 0xc8
   __DATA.__objc_ivar: 0xc

   - /System/Library/PrivateFrameworks/ktrace.framework/ktrace
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 63AA816A-6FF4-388C-8B84-E5B640D8776E
+  UUID: B3E16DC8-ACFE-35D5-A4A2-E3E519A4BAED
   Functions: 15
-  Symbols:   50
+  Symbols:   49
   CStrings:  73
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x2
+ _objc_retain_x21
- _objc_release_x19
- _objc_release_x9
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
Functions:
~ sub_d10 : 112 -> 108
~ sub_d80 -> sub_d7c : 472 -> 460
~ sub_f70 -> sub_f60 : 136 -> 128
~ sub_ff8 -> sub_fe0 : 260 -> 252
~ sub_10fc -> sub_10dc : 72 -> 68

```
