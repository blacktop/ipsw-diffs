## Symbolication

> `/System/Library/Trace/Providers/Symbolication.bundle/Symbolication`

```diff

-134.0.0.0.0
-  __TEXT.__text: 0x5d4
-  __TEXT.__auth_stubs: 0x190
+134.100.19.0.0
+  __TEXT.__text: 0x5f4
+  __TEXT.__auth_stubs: 0x1a0
   __TEXT.__objc_stubs: 0x100
-  __TEXT.__objc_methlist: 0x130
+  __TEXT.__objc_methlist: 0x13c
   __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0x28
   __TEXT.__cstring: 0x176
-  __TEXT.__objc_methname: 0x282
+  __TEXT.__objc_methname: 0x29d
   __TEXT.__objc_classname: 0x2a
-  __TEXT.__objc_methtype: 0x1a5
-  __TEXT.__unwind_info: 0x98
-  __DATA_CONST.__auth_got: 0xd8
+  __TEXT.__objc_methtype: 0x1cd
+  __TEXT.__unwind_info: 0xa0
+  __DATA_CONST.__auth_got: 0xe0
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x60
   __DATA_CONST.__cfstring: 0x180

   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x180
-  __DATA.__objc_selrefs: 0xc0
+  __DATA.__objc_const: 0x188
+  __DATA.__objc_selrefs: 0xc8
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x60

   - /System/Library/PrivateFrameworks/ktrace.framework/ktrace
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D8DB8751-0884-3E24-B3CD-1FFE13DCF510
+  UUID: 882B86C4-B3FC-36A5-83D3-5DE139483595
   Functions: 15
-  Symbols:   49
-  CStrings:  71
+  Symbols:   50
+  CStrings:  73
 
Symbols:
+ _objc_release_x19
+ _objc_release_x9
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x22
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x2
- _objc_retain_x21
Functions:
~ sub_d10 : 108 -> 112
~ sub_d7c -> sub_d80 : 464 -> 472
~ sub_f64 -> sub_f70 : 128 -> 136
~ sub_fe4 -> sub_ff8 : 252 -> 260
~ sub_10e0 -> sub_10fc : 68 -> 72
CStrings:
+ "B32@0:8^{ktrace_target_process=i}16^@24"
+ "shouldTargetProcess:error:"

```
