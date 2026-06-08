## Diagnostic-3732

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3732.appex/Diagnostic-3732`

```diff

-1066.122.1.0.0
-  __TEXT.__text: 0x9c4
-  __TEXT.__auth_stubs: 0x140
+1351.0.0.0.0
+  __TEXT.__text: 0x94c
+  __TEXT.__auth_stubs: 0x170
   __TEXT.__objc_stubs: 0x300
   __TEXT.__objc_methlist: 0x2c
   __TEXT.__const: 0x18

   __TEXT.__objc_methname: 0x175
   __TEXT.__objc_methtype: 0x1e
   __TEXT.__unwind_info: 0x80
-  __DATA_CONST.__auth_got: 0xb0
-  __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__cfstring: 0x1a0
   __DATA_CONST.__objc_classlist: 0x8

   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x18
+  __DATA_CONST.__auth_got: 0xc8
+  __DATA_CONST.__got: 0x40
   __DATA.__objc_const: 0x90
   __DATA.__objc_selrefs: 0xc8
   __DATA.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 40A06A80-C3E3-3EF2-BBD2-A8219C63A8FD
+  UUID: 41B9994C-B262-365A-BF9D-96615DAF89D8
   Functions: 7
-  Symbols:   42
+  Symbols:   45
   CStrings:  57
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_storeStrong
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
Functions:
~ _stringOrNull : 100 -> 92
~ sub_100000d68 -> sub_100000d60 : 1604 -> 1528
~ sub_1000013c4 -> sub_100001370 : 448 -> 432
~ sub_100001584 -> sub_100001520 : 200 -> 180

```
