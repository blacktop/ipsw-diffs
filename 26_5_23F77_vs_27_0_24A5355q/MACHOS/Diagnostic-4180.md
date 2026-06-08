## Diagnostic-4180

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4180.appex/Diagnostic-4180`

```diff

-1066.122.1.0.0
-  __TEXT.__text: 0x7e4
-  __TEXT.__auth_stubs: 0x130
+1351.0.0.0.0
+  __TEXT.__text: 0x6f8
+  __TEXT.__auth_stubs: 0x120
   __TEXT.__objc_stubs: 0x3e0
   __TEXT.__objc_methlist: 0x1e4
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x29
+  __TEXT.__cstring: 0x2b
   __TEXT.__oslogstring: 0x3e
-  __TEXT.__objc_classname: 0x79
+  __TEXT.__objc_classname: 0x77
   __TEXT.__objc_methtype: 0x13a
   __TEXT.__objc_methname: 0x4b9
-  __TEXT.__unwind_info: 0x98
-  __DATA_CONST.__auth_got: 0xa0
-  __DATA_CONST.__got: 0x20
+  __TEXT.__unwind_info: 0x88
   __DATA_CONST.__const: 0x10
   __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x90
+  __DATA_CONST.__auth_got: 0x98
+  __DATA_CONST.__got: 0x20
   __DATA.__objc_const: 0x3a0
   __DATA.__objc_selrefs: 0x1c8
   __DATA.__objc_ivar: 0x8

   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BBFEC33A-3968-33BD-8390-DFC15FBEF6A8
+  UUID: F6E32580-F993-3E7C-81E1-C1C56FDF72D0
   Functions: 13
-  Symbols:   41
+  Symbols:   40
   CStrings:  103
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_release_x19
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x21
- _objc_retain_x22
Functions:
~ sub_100000d40 : 468 -> 452
~ sub_100000f14 -> sub_100000f04 : 396 -> 384
~ sub_1000010a0 -> sub_100001084 : 300 -> 280
~ sub_1000011d0 -> sub_1000011a0 : 332 -> 304
~ sub_10000131c -> sub_1000012d0 : 16 -> 20
~ sub_10000132c -> sub_1000012e4 : 80 -> 20
~ sub_100001390 -> sub_10000130c : 200 -> 192
~ sub_100001460 -> sub_1000013d4 : 64 -> 12
~ sub_1000014ac -> sub_1000013ec : 120 -> 76

```
