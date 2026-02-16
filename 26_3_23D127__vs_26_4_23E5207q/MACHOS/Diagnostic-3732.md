## Diagnostic-3732

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3732.appex/Diagnostic-3732`

```diff

-1066.80.3.0.0
-  __TEXT.__text: 0x948
-  __TEXT.__auth_stubs: 0x170
+1066.100.26.0.0
+  __TEXT.__text: 0x9c4
+  __TEXT.__auth_stubs: 0x140
   __TEXT.__objc_stubs: 0x300
   __TEXT.__objc_methlist: 0x2c
   __TEXT.__const: 0x18

   __TEXT.__objc_methname: 0x175
   __TEXT.__objc_methtype: 0x1e
   __TEXT.__unwind_info: 0x80
-  __DATA_CONST.__auth_got: 0xc8
+  __DATA_CONST.__auth_got: 0xb0
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__cfstring: 0x1a0

   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C90B99D1-924F-3529-A7D7-6E6044FBD744
+  UUID: 233287F2-DA99-3EBC-A0A8-CFC65B3E8BBA
   Functions: 7
-  Symbols:   45
+  Symbols:   42
   CStrings:  57
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x22
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
- _objc_retain_x2
- _objc_storeStrong
Functions:
~ _stringOrNull : 92 -> 100
~ sub_100000d60 -> sub_100000d68 : 1528 -> 1604
~ sub_100001370 -> sub_1000013c4 : 428 -> 448
~ sub_10000151c -> sub_100001584 : 180 -> 200

```
